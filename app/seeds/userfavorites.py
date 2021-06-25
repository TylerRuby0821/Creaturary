from app.models import Creature, db, Userfavorite, User


def seed_userfavorites():
  demo = User.query.filter(User.name == 'Demo').first()
  creat1 = Creature.query.filter(Creature.name =='Wraith').first()
  creat2 = Creature.query.filter(Creature.name =='Ghost').first()
  creat3 = Creature.query.filter(Creature.name =='Banshee').first()
  creat4 = Creature.query.filter(Creature.name =='Pumpking').first()

  fav1=Userfavorite(
    user_id=demo.id,
    creature_id= creat1.id
  )
  fav2=Userfavorite(
    user_id=demo.id,
    creature_id= creat2.id
  )
  fav3=Userfavorite(
    user_id=demo.id,
    creature_id= creat3.id
  )
  fav4=Userfavorite(
    user_id=demo.id,
    creature_id= creat4.id
  )

  db.session.add(fav1)
  db.session.add(fav2)
  db.session.add(fav3)
  db.session.add(fav4)

  db.session.commit()

def undo_userfavorites():
    db.session.execute('TRUNCATE user_favorites CASCADE;')
    db.session.commit()
