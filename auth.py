from flask import Blueprint, render_template, request, flash

auth = Blueprint('/auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route('/sign-up', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if len(first_name) < 1:
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
            flash('You have successfully registered', category='success')

    return render_template('sign-up.html')