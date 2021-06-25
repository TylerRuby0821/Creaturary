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
  harp= Creature.query.filter(Creature.name == 'Harpy').first()
  merf= Creature.query.filter(Creature.name == 'Merfolk').first()
  griff= Creature.query.filter(Creature.name == 'Griffin').first()
  chim= Creature.query.filter(Creature.name == 'Chimera').first()
  cent= Creature.query.filter(Creature.name == 'Centaur').first()
  cerb= Creature.query.filter(Creature.name == 'Cerberus').first()
  hyd= Creature.query.filter(Creature.name == 'Hydra').first()
  sir= Creature.query.filter(Creature.name == 'Siren').first()
  phoe= Creature.query.filter(Creature.name == 'Phoenix').first()
  fair= Creature.query.filter(Creature.name == 'Fairy').first()
  pega= Creature.query.filter(Creature.name == 'Pegasus').first()
  bans= Creature.query.filter(Creature.name == 'Banshee').first()
  krak= Creature.query.filter(Creature.name == 'Kraken').first()
  dem= Creature.query.filter(Creature.name == 'Demon').first()
  gen= Creature.query.filter(Creature.name == 'Genie').first()
  wrai= Creature.query.filter(Creature.name == 'Wraith').first()
  kit= Creature.query.filter(Creature.name == 'Kitsune').first()
  succ= Creature.query.filter(Creature.name == 'Succubus').first()
  hell= Creature.query.filter(Creature.name == 'HellHound').first()
  levi= Creature.query.filter(Creature.name == 'Leviathan').first()
  wend= Creature.query.filter(Creature.name == 'Wendigo').first()
  goom= Creature.query.filter(Creature.name == 'Goomba').first()
  mim= Creature.query.filter(Creature.name == 'Mimic').first()
  head= Creature.query.filter(Creature.name == 'HeadCrab').first()
  mold= Creature.query.filter(Creature.name == 'Molded').first()

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
  harpy=Image(url='https://creaturary.s3.amazonaws.com/harpy.jpg',
    creature_id=harp.id
  )
  merfolk=Image(url='https://creaturary.s3.amazonaws.com/merfolk.jpg',
    creature_id=merf.id
  )
  griffin=Image(url='https://creaturary.s3.amazonaws.com/griffin.jpg',
    creature_id=griff.id
  )
  chimera=Image(url='https://creaturary.s3.amazonaws.com/chimera.jpg',
    creature_id=chim.id
  )
  centaur=Image(url='https://creaturary.s3.amazonaws.com/centaur.jpg',
    creature_id=cent.id
  )
  cerberus=Image(url='https://creaturary.s3.amazonaws.com/cerberus.jpg',
    creature_id=cerb.id
  )
  hydra=Image(url='https://creaturary.s3.amazonaws.com/hydra.jpg',
    creature_id=hyd.id
  )
  siren=Image(url='https://creaturary.s3.amazonaws.com/siren.jpg',
    creature_id=sir.id
  )
  phoenix=Image(url='https://creaturary.s3.amazonaws.com/phoenix.jpg',
    creature_id=phoe.id
  )
  fairy=Image(url='https://creaturary.s3.amazonaws.com/fairy.jpg',
    creature_id=fair.id
  )
  pegasus=Image(url='https://creaturary.s3.amazonaws.com/pegasus.jpg',
    creature_id=pega.id
  )
  banshee=Image(url='https://creaturary.s3.amazonaws.com/banshee.jpg',
    creature_id=bans.id
  )
  kraken=Image(url='https://creaturary.s3.amazonaws.com/kraken.jpg',
    creature_id=krak.id
  )
  demon=Image(url='https://creaturary.s3.amazonaws.com/demon.jpg',
    creature_id=dem.id
  )
  genie=Image(url='https://creaturary.s3.amazonaws.com/genie.jpg',
    creature_id=gen.id
  )
  wraith=Image(url='https://creaturary.s3.amazonaws.com/wraith.jpg',
    creature_id=wrai.id
  )
  kitsune=Image(url='https://creaturary.s3.amazonaws.com/kitsune.jpg',
    creature_id=kit.id
  )
  succubus=Image(url='https://creaturary.s3.amazonaws.com/succubus.jpg',
    creature_id=succ.id
  )
  hellhound=Image(url='https://creaturary.s3.amazonaws.com/hellhound.jpg',
    creature_id=hell.id
  )
  leviathan=Image(url='https://creaturary.s3.amazonaws.com/Leviathan.png',
    creature_id=levi.id
  )
  wendigo=Image(url='https://creaturary.s3.amazonaws.com/wendigo.jpg',
    creature_id=wend.id
  )
  goomba=Image(url='https://creaturary.s3.amazonaws.com/Goomba.png',
    creature_id=goom.id
  )
  mimic=Image(url='https://creaturary.s3.amazonaws.com/mimic.jpeg',
    creature_id=mim.id
  )
  headcrab=Image(url='https://creaturary.s3.amazonaws.com/headcrab.jpg',
    creature_id=head.id
  )
  molded=Image(url='https://creaturary.s3.amazonaws.com/molded.jpg',
    creature_id=mold.id
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
  db.session.add(harpy)
  db.session.add(merfolk)
  db.session.add(griffin)
  db.session.add(chimera)
  db.session.add(centaur)
  db.session.add(cerberus)
  db.session.add(hydra)
  db.session.add(siren)
  db.session.add(phoenix)
  db.session.add(fairy)
  db.session.add(pegasus)
  db.session.add(banshee)
  db.session.add(kraken)
  db.session.add(demon)
  db.session.add(genie)
  db.session.add(wraith)
  db.session.add(kitsune)
  db.session.add(succubus)
  db.session.add(hellhound)
  db.session.add(leviathan)
  db.session.add(wendigo)
  db.session.add(goomba)
  db.session.add(mimic)
  db.session.add(headcrab)
  db.session.add(molded)


  db.session.commit()

def undo_images():
  db.session.execute('TRUNCATE images CASCADE;')
  db.session.commit()
