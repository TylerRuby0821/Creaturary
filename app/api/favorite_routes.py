from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Creature, Tag, db, Userfavorite

favorite_routes = Blueprint('favorites', __name__)


@favorite_routes.route('/')
def get_favorites():
    favorites = Creature.query.join(Userfavorite, Userfavorite.creature_id == Creature.id).filter(current_user.id == Userfavorite.user_id).all()
    return {'favorites': [favorite.to_dict() for favorite in favorites]}


@favorite_routes.route('/add', methods=['POST'])
def add_favorite():
    creat_id = request.json['creature_id']
    favorite = Userfavorite(
        user_id=current_user.id,
        creature_id=creat_id)
    db.session.add(favorite)
    db.session.commit()
    return favorite.to_dict()

@favorite_routes.route('/<int:id>', methods=["DELETE"])
def remove_favorite(id):
  print('ID---------->', id)
  userCreatures = Userfavorite.query.filter(Userfavorite.user_id == current_user.id).all()
  print('USERCREATURES----------->>', userCreatures)
  testCreatures = [creature.id for creature in userCreatures]
  print('TEST CREATURES -------->>', testCreatures)
  deleteCreature = [creature for creature in userCreatures if creature.creature_id == id]
  print('DELETED CREATURE---------->>', deleteCreature)
  creature = deleteCreature[0]
  print('CREATURE---------->', creature)
  db.session.delete(creature)
  db.session.commit()
  return creature.to_dict()
