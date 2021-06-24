from flask import Blueprint, request
from app.models import db, Image
from flask_login import current_user, login_required
from app.s3_helpers import (
    upload_file_to_s3, allowed_file, get_unique_filename)

image_routes = Blueprint("images", __name__)

@image_routes.route('/')
def getImages():
    images = Image.query.all()
    return {'images': [image.to_dict() for image in images]}


@image_routes.route("", methods=["POST"])
@login_required
def upload_image():
    url = request.json['url']
    creatureId = request.json['creature_id']
    new_image = Image(
        url = url,
        creature_id=creatureId
        )
    db.session.add(new_image)
    db.session.commit()
    return new_image.to_dict()
