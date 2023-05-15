from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(id)

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    dealerships = db.relationship('Dealership', backref='author', lazy=True)


    def __repr__(self):
        return f'User: {self.username}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def hash_password(self, password):
        return generate_password_hash(self.password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
        #What import do I need to use to get these to work? I know I need to make the check in routes.py but what import is this?

    def get_id(self):
        return self.user_id

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Inventory {self.body}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Dealership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dealer_name = db.Column(db.String(100))
    dealer_location = db.Column(db.String(50))
    dealer_brand = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __repr__(self):
        return f'Dealerships {self.dealer_name}'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()