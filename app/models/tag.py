from .db import db
from datetime import datetime


class Tag(db.Model):
  __tablename__ = 'tags'

  id = db.Column(db.Integer, primary_key= True)
  type = db.Column(db.String, nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


  def to_dict(self):
    return {
      "id": self.id,
      "type": self.type,
      'created_at': self.created_at,
      'updated_at': self.updated_at
    }
