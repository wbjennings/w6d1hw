from flask import render_template, flash, redirect, url_for
from app.models import User
from app import db
from . import bp
from app.forms import RegisterForm

@bp.route('/inventory', methods=['GET', 'POST'])
def inventory():
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
    return render_template('inventory.jinja', form=form)