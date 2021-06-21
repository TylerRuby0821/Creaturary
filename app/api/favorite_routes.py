from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Creature, Tag, db, Userfavorite

favorite_routes = Blueprint('favorites', __name__)

@favorite_routes.route('/')
def get_favorites():
  favorites = Userfavorite.query(current_user.id == Userfavorite.user_id).all()
  return {'favorites': [favorite.to_dict() for favorite in favorites]}

@favorite_routes('/add', methods=['POST'])
def add_favorite():
  creat_id = request.json('creature_id')
  favorite = Userfavorite(
    user_id = current_user.id,
    creature_id = creat_id
  )
  db.session.add(favorite)
  db.session.commit()
  return favorite.to_dict()

# @favorite_routes('/remove', methods=["DELETE"])
# def remove_favorite():
#   creat_id = request.json('creature_id')
#   favorite = Userfavorite.query(current_user.id == Userfavorite.user_id and creat_id == Userfavorite.creature_id)
#   db.session.delete(favorite)
#   db.session.commit()
#   return
