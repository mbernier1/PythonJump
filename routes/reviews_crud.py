from flask import Blueprint, request
from database import db
from misc.utilities import read_sql

reviews_crud_blueprint = Blueprint('reviews_crud', __name__)

# add Review to database
@reviews_crud_blueprint.route('/reviews', method=['POST'])
def add_review():
    email = request.form.get('email')
    card_name = request.form.get('card_name')
    rating = request.form.get('rating')
    review = request.form.get('review')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("add_new_review"), [email, card_name, rating, review])
    conn = db.connection
    conn.commit()

    return f"Review added", 201

# update Review from database
@reviews_crud_blueprint.route('/reviews/<review_id>', methods=["PUT"])
def update_card(review_id):

    email = request.form.get('email')
    card_name = request.form.get('card_name')
    rating = request.form.get('rating')
    review = request.form.get('review')

    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("update_review"), [email, card_name, rating, review, review_id])
    conn = db.connection
    conn.commit()

    return f"Review updated", 201

# delete Review from database
@reviews_crud_blueprint.route('/reviews/<id>', methods=["DELETE"])
def delete_review(id):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("delete_review"), [id])
    conn = db.connection
    conn.commit()

    return "Deletion complete", 200