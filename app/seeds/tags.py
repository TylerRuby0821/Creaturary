from app.models import db, Tag

def seed_tags():

  lore = Tag(type='Lore')
  custom = Tag(type='Custom')

  db.session.add(lore)
  db.session.add(custom)

  db.session.commit()


def undo_tags():
    db.session.execute('TRUNCATE tags CASCADE;')
    db.session.commit()
