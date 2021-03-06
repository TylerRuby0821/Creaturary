from .db import db
from datetime import datetime

class Creature(db.Model):
  __tablename__ = 'creatures'

  id = db.Column(db.Integer, primary_key= True)
  name = db.Column(db.String, nullable=False)
  description = db.Column(db.Text, nullable=False)
  tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "tag_id": self.tag_id,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
