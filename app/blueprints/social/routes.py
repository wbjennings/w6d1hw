from flask import render_template, g, flash
from flask_login import current_user, login_required
from . import bp 
from app.models import Post, User, Dealership
from app import db
from app.forms import PostForm
from app.forms import RegisterForm, SignInForm, AddDealerForm

@bp.route('/inventory', methods=['GET','POST'])
def inventory():
    form = PostForm()
    if form.validate_on_submit():
        p = Post(body=form.body.data)
        p.user_id = current_user.user_id
        p.commit()
        print(p)
    return render_template('inventory.jinja', form=form)

@bp.route('/userpage/<username>')
@login_required
def user_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template('user_page.jinja', title=username, user=user, user_search_form=g.user_search_form)

@bp.route('/dealership', methods=['GET', 'POST'])
def dealership():
    form = AddDealerForm()
    if form.validate_on_submit():
        d = Dealership(dealer_name=form.dealer_name.data, dealer_location=form.dealer_location.data, dealer_brand=form.dealer_brand.data)
        d.user_id = current_user.user_id
        d.commit()
    return render_template('dealerships.jinja', form=form)

@bp.route('/dealerships/<username>')
@login_required
def dealer_page(username):
    user = User.query.filter_by(username=username).first()
    return render_template('dealer_page.jinja', title=username, user=user, user_search_form=g.user_search_form)


