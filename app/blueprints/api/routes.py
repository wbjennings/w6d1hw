from flask import request, jsonify
from app.models import User, Post, Dealership

from . import bp

#This will view all the inventory in the db
@bp.get('/inventory')
def api_posts():
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append({
            'id': post.id,
            'body': post.body,
            'timestamp': post.timestamp,
            'author': post.user_id
        })
    return jsonify(result), 200


#This will view all the inventory of a singular username added
@bp.get('/inventory/<username>')
def user_posts(username):
    user = User.query.filter_by(username=username).all()
    if user:
        return jsonify([{
                'id':post.id,
                'body':post.body,
                'timestamp':post.timestamp,
                'author':post.id
                } for post in user.posts]), 200 
    return jsonify([{'message': 'Invalid Username'}]), 404

#This gets all the dealerships added into the DB
@bp.get('/dealerships')
def api_dealers():
    result = []
    dealerships = Dealership.query.all()
    for dealer in dealerships:
        result.append({
            'id': dealer.id,
            'dealer_name': dealer.dealer_name,
            'dealer_location': dealer.dealer_location,
            'dealer_brand': dealer.dealer_brand,
            'timestamp': dealer.timestamp,
            'author': dealer.user_id
        })
    return jsonify(result), 200

