from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .models import User, Task, PointIn, PointOut
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(APP_ROOT, 'static')
@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Strona główna')


@app.route('/tsp')
@login_required
def tsp():
    return render_template('tsp.html',
                           title='Algorytm TSP')

@app.route('/_active_task')
@login_required
def _active_task():
    tasks = Task.query.filter_by(user_id = g.user.id)
    user_tasks = 0
    for task in tasks:
            user_tasks += 1
    return jsonify(result = user_tasks)

@app.route('/_done_task')
@login_required
def _done_task():
    tasks = Task.query.filter_by(user_id = g.user.id).filter_by(state = "done")
    user_tasks = 0
    for task in tasks:
            user_tasks += 1
    return jsonify(result = user_tasks)

@app.route('/_working_task')
@login_required
def _working_task():
    tasks = Task.query.filter_by(user_id = g.user.id)
    user_tasks = 0
    for task in tasks:
        if(task.state == "working"):
            user_tasks += 1
    return jsonify(result = user_tasks)


@app.route('/_update_progress')
@login_required
def _update_progress():
    tasks = Task.query.filter_by(user_id = g.user.id)
    message = {}
    message['value'] = []
    for task in tasks:
        message['value'].append(task.progress)
    return jsonify(message)


@app.route('/_add_active_task')
@login_required
def _add_active_task():
    tasks = Task.query.filter_by(user_id = g.user.id)
    user_tasks = 0
    test = 0
    for x in tasks:
        user_tasks += 1
        if (x.state == "working" or x.state == "done"):
            test += 1

    # Sprawdzenie czy dodaje nowe zadanie przez rozpoczeciem/skonczeniem poprzedniego
    if ((user_tasks - test) == 0):
        task = Task()
        task.add_waiting_task(g.user)
        db.session.add(task)
        db.session.commit()
    else: user_tasks = 500

    return jsonify(result = user_tasks)

@app.route('/tsp/add_task', methods=['POST'])
@login_required
def add_task():
    if request.method == 'POST':
        file = request.files['fileToUpload']
        if not file:
            flash("Błąd wysyłania pliku", 'upload-error')
            return redirect(url_for('tsp'))

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        tasks = Task.query.filter_by(user_id = g.user.id)

        task = None

        for t in tasks:
            if (t.state == "waiting"):
                task = t;


        task.init_from_file(filepath, g.user)
        db.session.add(task)
        db.session.commit()

        flash("Dodano zadanie", 'add_task-msg')

    return redirect(url_for('tsp'))

@app.route('/_user_task_points')
@login_required
def _login_task_points():
    tasks = Task.query.filter_by(user_id = g.user.id).filter(or_(Task.state == "working",Task.state == "done"))
    user_tasks = 0
    message = {}
    i = 1
    for task in tasks:
        message[str(i)] = []
        points = PointIn.query.filter_by(task_id = task.id).order_by(PointIn.number)
        scale = 290/task.max_value
        for point in points:
            message[str(i)].append(scale*point.x)
            message[str(i)].append(scale*point.y)
        i += 1
    return jsonify(result = message)

@app.route('/_user_done_task_points')
@login_required
def _login__done_task_points():
    tasks = Task.query.filter_by(user_id = g.user.id).filter(Task.state == "done")
    user_tasks = 0
    message = {}
    i = 1
    for task in tasks:
        message[str(i)] = []
        points = PointOut.query.filter_by(task_id = task.id).order_by(PointOut.number)
        scale = 290/task.max_value
        message[str(i)].append(task.id)
        message[str(i)].append(task.id)
        for point in points:
            message[str(i)].append(scale*point.x)
            message[str(i)].append(scale*point.y)
        i += 1
    return jsonify(result = message)

@lm.user_loader
def load_user(id):
        return User.query.get(int(id))

@app.route('/login', methods=['POST'])
def login():

    input_email = request.form.get('inputEmail', None)
    input_password = request.form.get('inputPassword', None)
    input_remember_me = request.form.get('remember-me', False)

    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    user = User.query.filter_by(email=input_email).first()


    if (user is None) or not check_password_hash(user.password, input_password):
        flash('Niewłaściwy login lub hasło', 'login-error')
        return redirect(url_for('index'))

    login_user(user, remember=bool(input_remember_me))

    flash('Zalogowano', 'login-msg')
    return redirect(url_for('tsp'))

@app.route('/logout')
def logout():
    logout_user()
    flash('Wylogowano', 'logout-msg')
    return redirect(url_for('index'))

@app.route('/register', methods=['POST'])
def register():
     email = request.form.get('inputEmail', None)
     pass1 = request.form.get('inputPassword1', None)
     pass2 = request.form.get('inputPassword2', None)

     if email is None:
         flash('Nie podano adresu e-mail', 'regiter-error')
         return redirect(url_for('index'))

     user = User.query.filter_by(email=request.form['inputEmail']).first()

     if user is not None:
         flash('Użytkownik o podanym adresie e-mail już istnieje', 'register-error')
         return redirect(url_for('index'))

     if pass1 != pass2:
         flash('Podane hasła są różne', 'register-error')
         return redirect(url_for('index'))

     password = generate_password_hash(pass1)
     user = User(email=email, password=password)
     db.session.add(user)
     db.session.commit()

     flash('Rejestracja zakończona powodzeniem', 'register-msg')
     return redirect((url_for('index')))





















