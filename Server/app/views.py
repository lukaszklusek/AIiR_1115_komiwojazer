from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .models import User, Task
from werkzeug.security import generate_password_hash, check_password_hash

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tsp')
@login_required
def tsp():
    return render_template('tsp.html')

@lm.user_loader
def load_user(id):
        return User.query.get(int(id))

@app.route('/login', methods=['POST'])
def login():

    input_email = request.form.get('inputEmail', None)
    input_password = generate_password_hash(request.form.get('inputPassword', None))
    input_remember_me = request.form.get('remember-me', False)

    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    user = User.query.filter_by(email=input_email).first()

    if user is None or check_password_hash(user.password, input_password):
        flash('Niewłaściwy login lub hasło', 'login-error')
        return redirect(url_for('index'))

    login_user(user, remember=bool(input_remember_me))

    flash('Zalogowano', 'login-msg')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
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





















