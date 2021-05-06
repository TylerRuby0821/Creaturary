from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Creature, Tag

creature_routes = Blueprint('creatures', __name__)


@creature_routes.route('/')
@login_required
def get_creatures():
  creatures = Creature.query.all()
  return {'creatures': [creature.to_dict() for creature in creatures]}


@creature_routes.route('/', methods=['POST'])
@login_required
def create_creature():
  creature_name = request.json['name']
  creature_desc = request.json['description']
  creature_tag_id= request.json['tag_id']
  creature = Creature(
    name = creature_name,
    description = creature_desc,
    tag_id = creature_tag_id
  )
  db.session.add(creature)
  db.session.commit()

@creature_routes.route('/<int:id>')
@login_required
def get_creature(id):
  creature = Creature.query.get(id)
  return creature.to_dict()
