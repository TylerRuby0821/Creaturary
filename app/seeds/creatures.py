from app.models import db, Creature, Tag


def seed_creatures():
  lore = Tag.query.filter(Tag.type == 'Lore').first()
  print('IM THE LORE QUERY', lore)

  vampire = Creature(name='Vampire',
    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac mauris tempor, varius lorem efficitur, molestie mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla ut condimentum libero, a tincidunt magna. Quisque tristique sagittis mollis. Duis cursus eu ex non bibendum. Praesent eu arcu hendrerit, bibendum elit eu, pretium felis. Morbi suscipit nibh orci, eget rutrum leo pellentesque ut. Aliquam in aliquam lorem. Donec posuere viverra enim, non fermentum nisi faucibus in. Maecenas consectetur mollis blandit. Quisque pulvinar sodales enim sed elementum. Sed nec consequat dui. Quisque euismod tincidunt neque non pharetra. Nam vel dapibus ante. Aliquam commodo consectetur sem, at interdum mi mattis sed. Etiam nec tellus ut felis venenatis mattis sed ut velit.',
    tag_id=lore.id)

  werewolf = Creature(name='Werewolf',
    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac mauris tempor, varius lorem efficitur, molestie mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla ut condimentum libero, a tincidunt magna. Quisque tristique sagittis mollis. Duis cursus eu ex non bibendum. Praesent eu arcu hendrerit, bibendum elit eu, pretium felis. Morbi suscipit nibh orci, eget rutrum leo pellentesque ut. Aliquam in aliquam lorem. Donec posuere viverra enim, non fermentum nisi faucibus in. Maecenas consectetur mollis blandit. Quisque pulvinar sodales enim sed elementum. Sed nec consequat dui. Quisque euismod tincidunt neque non pharetra. Nam vel dapibus ante. Aliquam commodo consectetur sem, at interdum mi mattis sed. Etiam nec tellus ut felis venenatis mattis sed ut velit.',
    tag_id=lore.id)

  ghoul = Creature(name='Ghoul',
    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac mauris tempor, varius lorem efficitur, molestie mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla ut condimentum libero, a tincidunt magna. Quisque tristique sagittis mollis. Duis cursus eu ex non bibendum. Praesent eu arcu hendrerit, bibendum elit eu, pretium felis. Morbi suscipit nibh orci, eget rutrum leo pellentesque ut. Aliquam in aliquam lorem. Donec posuere viverra enim, non fermentum nisi faucibus in. Maecenas consectetur mollis blandit. Quisque pulvinar sodales enim sed elementum. Sed nec consequat dui. Quisque euismod tincidunt neque non pharetra. Nam vel dapibus ante. Aliquam commodo consectetur sem, at interdum mi mattis sed. Etiam nec tellus ut felis venenatis mattis sed ut velit.',
    tag_id=lore.id)

  lep = Creature(name='Leprechaun',
    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac mauris tempor, varius lorem efficitur, molestie mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla ut condimentum libero, a tincidunt magna. Quisque tristique sagittis mollis. Duis cursus eu ex non bibendum. Praesent eu arcu hendrerit, bibendum elit eu, pretium felis. Morbi suscipit nibh orci, eget rutrum leo pellentesque ut. Aliquam in aliquam lorem. Donec posuere viverra enim, non fermentum nisi faucibus in. Maecenas consectetur mollis blandit. Quisque pulvinar sodales enim sed elementum. Sed nec consequat dui. Quisque euismod tincidunt neque non pharetra. Nam vel dapibus ante. Aliquam commodo consectetur sem, at interdum mi mattis sed. Etiam nec tellus ut felis venenatis mattis sed ut velit.',
    tag_id=lore.id)

  dragon = Creature(name='Dragon',
    description='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac mauris tempor, varius lorem efficitur, molestie mi. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nulla ut condimentum libero, a tincidunt magna. Quisque tristique sagittis mollis. Duis cursus eu ex non bibendum. Praesent eu arcu hendrerit, bibendum elit eu, pretium felis. Morbi suscipit nibh orci, eget rutrum leo pellentesque ut. Aliquam in aliquam lorem. Donec posuere viverra enim, non fermentum nisi faucibus in. Maecenas consectetur mollis blandit. Quisque pulvinar sodales enim sed elementum. Sed nec consequat dui. Quisque euismod tincidunt neque non pharetra. Nam vel dapibus ante. Aliquam commodo consectetur sem, at interdum mi mattis sed. Etiam nec tellus ut felis venenatis mattis sed ut velit.',
    tag_id=lore.id)

  db.session.add(vampire)
  db.session.add(werewolf)
  db.session.add(ghoul)
  db.session.add(lep)
  db.session.add(dragon)

  db.session.commit()


def undo_creatures():
    db.session.execute('TRUNCATE creatures CASCADE;')
    db.session.commit()
