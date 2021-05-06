from app.models import db, Userfavorite

def seed_userfavorites():
  pass


def undo_userfavorites():
    db.session.execute('TRUNCATE user_favorites CASCADE;')
    db.session.commit()
