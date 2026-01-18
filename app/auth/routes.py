from flask import Blueprint, render_template, redirect, flash, url_for
from app.auth.forms import LoginForm, RegisterForm

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
    return render_template('auth/login.html', form=form)

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # simulasi simpan user (belum DB)
        flash("Registrasi berhasil!. silahkan login", "success")
        return redirect(url_for('main.login'))
    return render_template('auth/register.html', form=form)