from flask import Blueprint
from database import db
from misc.utilities import read_sql

users_blueprint = Blueprint('users', __name__)

# Function to get all users
@users_blueprint.route('/users', methods=["GET"])
def get_all_users() -> list[dict]:
    cur = db.new_cursor(dictionary=True)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return users

# Function to get user by name
def get_user_by_name(name):
    cur = db.new_cursor(dictionary=True)
    cur.execute(read_sql("get_user_by_name"), [name])
    user = cur.fetchall()
    return user
# Function to get user cards