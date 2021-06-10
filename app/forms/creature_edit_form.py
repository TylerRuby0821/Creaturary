from app.models.tag import Tag
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Creature, Tag

def tag_exists(form, field):
    print("Checking if tag exists..", field.data)
    print('FORM DATA ----->', form.data)
    tag_id = field.data
    tag = Tag.query.filter(Tag.id == tag_id).first()
    if not tag:
        raise ValidationError("Please Select a Tag")

class CreatureEditForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    tag = IntegerField('tag', validators=[tag_exists, DataRequired()])
