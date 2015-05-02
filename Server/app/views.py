from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from .models import User, Task
from werkzeug.security import generate_password_hash

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

@app.route('/login', methods=['GET', 'POST'])
def login():

    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    user = User.query.filter_by(email=request.form['inputEmail'], password=request.form['inputPassword']).first() #to powinno działać, ale coś nie halo


    if user is None:
        flash('Niewłaściwy login lub hasło', 'error')
        return redirect(url_for('index'))

    login_user(user, rememeber=request.form['remember-me'])
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))













