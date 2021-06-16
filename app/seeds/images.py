from app.models import db, Creature, Image


def seed_images():
  vamp= Creature.query.filter(Creature.name == 'Vampire').first()
  wolf= Creature.query.filter(Creature.name == 'Werewolf').first()
  ghoul= Creature.query.filter(Creature.name == 'Ghoul').first()
  lep= Creature.query.filter(Creature.name == 'Leprechaun').first()
  dragon= Creature.query.filter(Creature.name == 'Dragon').first()
  spyro= Creature.query.filter(Creature.name == 'Spyro').first()
  shrek= Creature.query.filter(Creature.name == 'Shrek').first()
  ghost= Creature.query.filter(Creature.name == 'Ghost').first()
  pump= Creature.query.filter(Creature.name == 'Pumpking').first()
  print("VAMP RESULT-----------", vamp)
  vampire = Image(url='https://creaturary.s3.amazonaws.com/vampire.png',
    creature_id=vamp.id
    )
  werewolf=Image(url='https://creaturary.s3.amazonaws.com/werewolf.jpg',
    creature_id=wolf.id
  )
  ghoul_creat=Image(url='https://creaturary.s3.amazonaws.com/ghoul.jpg',
    creature_id=ghoul.id
  )
  leprechaun=Image(url='https://creaturary.s3.amazonaws.com/leprechaun.jpg',
    creature_id=lep.id
  )
  dragon_creat=Image(url='https://creaturary.s3.amazonaws.com/dragon.jpg',
    creature_id=dragon.id
  )
  spyro_creat=Image(url='https://creaturary.s3.amazonaws.com/spyro.jpg',
    creature_id=spyro.id
  )
  shrek_creat=Image(url='https://creaturary.s3.amazonaws.com/shrek.jpg',
    creature_id=shrek.id
  )
  ghost_creat=Image(url='https://creaturary.s3.amazonaws.com/Ghost.png',
    creature_id=ghost.id
  )
  pumpking=Image(url='https://creaturary.s3.amazonaws.com/pumpking.jpg',
    creature_id=pump.id
  )

  db.session.add(vampire)
  db.session.add(werewolf)
  db.session.add(ghoul_creat)
  db.session.add(leprechaun)
  db.session.add(dragon_creat)
  db.session.add(spyro_creat)
  db.session.add(shrek_creat)
  db.session.add(ghost_creat)
  db.session.add(pumpking)

  db.session.commit()

def undo_images():
  db.session.execute('TRUNCATE images CASCADE;')
  db.session.commit()
