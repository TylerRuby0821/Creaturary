from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Tag

tag_routes = Blueprint('tags', __name__)

@tag_routes.route('/')
@login_required
def get_tags():
  tags = Tag.query.all()
  return {'tags': [tag.to_dict() for tag in tags]}
