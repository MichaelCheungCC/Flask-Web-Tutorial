from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Here is some text.")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        password_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'

        if not re.fullmatch(email_regex, email):
            flash('Please enter a valid Email address.', category='error')
        elif len(firstname) < 3 or len(lastname) < 3:
            flash('First name and last name must be at least 3 characters long.', category='error')
        elif not re.fullmatch(password_regex, password1):
            flash('Password must be at least 8 characters long, at least one letter and one number', category='error')
        elif password1!=password2:
            flash('Password inconsistent!', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")