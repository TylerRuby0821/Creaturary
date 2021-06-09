from .db import db
from datetime import datetime

class Image(db.Model):
  __tablename__ = 'images'

  id = db.Column(db.Integer, primary_key= True)
  image_url = db.Column(db.String, nullable=False)
  creature_id = db.Column(db.Integer, db.ForeignKey('creatures.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


  def to_dict(self):
    return {
      "id": self.id,
      "image_url": self.image_url,
      "creature_id": self.creature_id,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
