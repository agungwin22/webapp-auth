from flask import Blueprint, render_template, redirect, flash, url_for
from app.forms import LoginForm

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # sebelum menggunakan database
        if form.email.data == 'agung@example.com' and form.password.data == 'password123':
            flash("Login Berhasil!!", "success")
        else:
            flash("Email & Password Salah", "danger")
    return render_template('login.html', form=form)