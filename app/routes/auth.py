from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user

from app.models.user import User
from app.forms.auth import LoginForm, RegisterForm, ResetPasswordRequestForm, ResetPasswordForm
from app.services.email import EmailService

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/')
@auth.route('/index')
def index():
    return redirect(url_for('auth.login'))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.index'))
        else:
            flash('Login Failed', 'danger')

    return render_template('views/auth/login.html', title='Login', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegisterForm()

    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.name = form.name.data
        user.generate_password_hash(form.password.data)
        user.save()

        login_user(user)

        return redirect(url_for('main.index'))

    return render_template('views/auth/register.html', title='Register', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('Logged Out', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            service = EmailService()
            service.send_password_reset_email(user)

        flash('Check your email for the instructions to reset your password', 'success')

        return redirect(url_for('auth.login'))

    return render_template('views/auth/reset_password_request.html',
                           title='Reset Password', form=form)


@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    user = User.verify_reset_password_token(token)

    if not user:
        return redirect(url_for('main.index'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.set_password(form.password.data)
        user.save()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('views/auth/reset_password.html', form=form)