from flask import Blueprint, render_template, redirect, flash, url_for
from app.auth.forms import LoginForm, RegisterForm
from app.models import User
from app.extensions import db
from flask_login import login_user, logout_user, login_required, current_user

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))

        return "Login Gagal"
        
    return render_template('auth/login.html', form=form)

@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        # existing_user = User.query.filter_by(
        #     email=form.email.data
        # ).first()

        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash("Registrasi berhasil!. silahkan login", "success")
        return redirect(url_for('main.login'))

    return render_template('auth/register.html', form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('auth/dashboard.html')