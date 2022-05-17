from flask import Blueprint, render_template, request, flash, redirect, url_for
from db_models import User
from __init__ import my_database
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('/auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('You are now logged in', category='success')
                login_user(user, remember=True)
                return redirect(url_for('/views.home'))
            else:
                flash('Incorrect password', category='error')
        else: 
            flash('No user found', category='error')  
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('/auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists', category='error')
        elif len(first_name) < 1:
            flash('First name is required', category='error')
        elif len(last_name) < 1:
            flash('Last name is required', category='error')
        elif len(email) < 4:
            flash('Email must be at least 4 characters long', category='error')
        elif len(password) < 8:
            flash('Password must be at least 8 characters long', category='error')
        elif password != password2:
            flash('Passwords do not match', category='error')
        else:
            new_user = User(first_name=first_name, last_name=last_name, email=email, password=generate_password_hash(password, method='sha256'))
            my_database.session.add(new_user)
            my_database.session.commit()
            flash('You have successfully registered', category='success')
            login_user(user, remember=True)
            return redirect(url_for('/views.home'))

    return render_template('sign-up.html',user=current_user)    