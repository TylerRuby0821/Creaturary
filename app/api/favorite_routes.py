from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Creature, Tag, db, Userfavorite

favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route('/')
def get_favorites():
  favorites = Userfavorite.query(current_user.id == Userfavorite.user_id).all()
  return {'favorites': [favorite.to_dict() for favorite in favorites]}
