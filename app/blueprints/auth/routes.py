from flask import render_template, flash, redirect, url_for
from flask_login import login_user
from app.models import User
from app import db
from . import bp
from app.forms import RegisterForm, SignInForm

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if not email and not user:
            u = User(username=form.username.data, email=form.email.data, password=form.password.data)
            u.commit()
            flash(f'{form.username.data} registered')
            return redirect(url_for("main.home"))
        if user:
            flash(f'{form.username.data} already exists, try a different one.')
        else:
            flash(f'{form.email.data} is already in use, please request a password reset if you are unsure.')
    return render_template('register.jinja', form=form)

@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        print(form.username.data, form.password.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user: #this is where I can do that check I reffered to about the password hash stuff. Have some questions with that.
            flash(f'{form.username.data} signed in', 'success')
            login_user(id)
            return redirect(url_for('main.home'))
        else:
            flash('User doesnt exist or incorrect password', 'warning')

    return render_template('signin.jinja', form=form)

@bp.route('/inventory')
def inventory():
    return render_template('inventory.jinja')