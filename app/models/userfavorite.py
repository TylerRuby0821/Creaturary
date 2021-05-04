from .db import db
from datetime import datetime

class Userfavorite(db.model):
  __tablename__ = 'user_favorites'

  id = db.Column(db.Integer, primary_key= True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  creature_id = db.Column(db.Integer, db.ForeignKey('creatures.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


  def to_dict(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "creature_id": self.creature_id,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
