from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import Creature, Tag, db

creature_routes = Blueprint('creatures', __name__)


@creature_routes.route('/')
def get_creatures():
  creatures = Creature.query.all()
  return {'creatures': [creature.to_dict() for creature in creatures]}

@creature_routes.route('/lore')
@login_required
def get_creatures_lore():
  tag = Tag.query.filter(Tag.type == 'Lore').first().to_dict()
  creatures = Creature.query.filter(Creature.tag_id == tag['id']).all()
  return {'creatures': [creature.to_dict() for creature in creatures]}

@creature_routes.route('/custom')
@login_required
def get_creatures_custom():
  tag = Tag.query.filter(Tag.type == 'Custom').first().to_dict()
  creatures = Creature.query.filter(Creature.tag_id == tag['id']).all()
  return {'creatures': [creature.to_dict() for creature in creatures]}

@creature_routes.route('/<string:search>')
@login_required
def get_creatures_search(search):
  creatures = Creature.query.filter(Creature.name == search.capitalize()).all()
  return {'creatures': [creature.to_dict() for creature in creatures]}

@creature_routes.route('/create', methods=['POST'])
@login_required
def create_creature():
  creature_name = request.json['name']
  creature_desc = request.json['description']
  creature_tag_id= request.json['tag']
  creature = Creature(
    name = creature_name,
    description = creature_desc,
    tag_id = creature_tag_id
  )
  db.session.add(creature)
  db.session.commit()
  return creature.to_dict()

@creature_routes.route('/<int:id>')
@login_required
def get_creature(id):
  creature = Creature.query.get(id)
  return creature.to_dict()
