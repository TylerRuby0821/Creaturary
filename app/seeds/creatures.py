from app.models import db, Creature, Tag


def seed_creatures():
  lore = Tag.query.filter(Tag.type == 'Lore').first()
  custom = Tag.query.filter(Tag.type == 'Custom').first()

  vampire = Creature(name='Vampire',
    description="""A vampire is a creature from folklore that subsists by feeding on the vital essence (generally in the form of blood) of the living. In European folklore, vampires are undead creatures that often visited loved ones and caused mischief or deaths in the neighbourhoods they inhabited while they were alive. They wore shrouds and were often described as bloated and of ruddy or dark countenance, markedly different from today's gaunt, pale vampire which dates from the early 19th century.
    Vampiric entities have been recorded in most cultures; the term vampire was popularized in Western Europe after reports of an 18th-century mass hysteria of a pre-existing folk belief in the Balkans and Eastern Europe that in some cases resulted in corpses being staked and people being accused of vampirism. Local variants in Eastern Europe were also known by different names, such as shtriga in Albania, vrykolakas in Greece and strigoi in Romania.
    In modern times, the vampire is generally held to be a fictitious entity, although belief in similar vampiric creatures such as the chupacabra still persists in some cultures. Early folk belief in vampires has sometimes been ascribed to the ignorance of the body's process of decomposition after death and how people in pre-industrial societies tried to rationalize this, creating the figure of the vampire to explain the mysteries of death. Porphyria was linked with legends of vampirism in 1985 and received much media exposure, but has since been largely discredited.
    The charismatic and sophisticated vampire of modern fiction was born in 1819 with the publication of "The Vampyre" by the English writer John Polidori; the story was highly successful and arguably the most influential vampire work of the early 19th century.[1] Bram Stoker's 1897 novel Dracula is remembered as the quintessential vampire novel and provided the basis of the modern vampire legend, even though it was published after fellow Irish author Joseph Sheridan Le Fanu's 1872 novel Carmilla. The success of this book spawned a distinctive vampire genre, still popular in the 21st century, with books, films, television shows, and video games. The vampire has since become a dominant figure in the horror genre.""",
    tag_id=lore.id)

  werewolf = Creature(name='Werewolf',
    description="""In folklore, a werewolf (Old English: werwulf, "man-wolf"), occasionally wolfwalker or lycanthrope /ˈlaɪkənˌθroʊp/ (Greek: λυκάνθρωπος lukánthrōpos, "wolf-person"), is a human with the ability to shapeshift into a wolf (or, especially in modern film, a therianthropic hybrid wolflike creature), either purposely or after being placed under a curse or affliction (often a bite or scratch from another werewolf) with the transformations occurring on the night of a full moon. Early sources for belief in this ability or affliction, called lycanthropy /laɪˈkænθrəpi/, are Petronius (27–66) and Gervase of Tilbury (1150–1228).

The werewolf is a widespread concept in European folklore, existing in many variants, which are related by a common development of a Christian interpretation of underlying European folklore developed during the medieval period. From the early modern period, werewolf beliefs also spread to the New World with colonialism. Belief in werewolves developed in parallel to the belief in witches, in the course of the Late Middle Ages and the Early Modern period. Like the witchcraft trials as a whole, the trial of supposed werewolves emerged in what is now Switzerland (especially the Valais and Vaud) in the early 15th century and spread throughout Europe in the 16th, peaking in the 17th and subsiding by the 18th century.

The persecution of werewolves and the associated folklore is an integral part of the "witch-hunt" phenomenon, albeit a marginal one, accusations of lycanthropy being involved in only a small fraction of witchcraft trials.[b] During the early period, accusations of lycanthropy (transformation into a wolf) were mixed with accusations of wolf-riding or wolf-charming. The case of Peter Stumpp (1589) led to a significant peak in both interest in and persecution of supposed werewolves, primarily in French-speaking and German-speaking Europe. The phenomenon persisted longest in Bavaria and Austria, with persecution of wolf-charmers recorded until well after 1650, the final cases taking place in the early 18th century in Carinthia and Styria.[c]

After the end of the witch-trials, the werewolf became of interest in folklore studies and in the emerging Gothic horror genre; werewolf fiction as a genre has pre-modern precedents in medieval romances (e.g. Bisclavret and Guillaume de Palerme) and developed in the 18th century out of the "semi-fictional" chap book tradition. The trappings of horror literature in the 20th century became part of the horror and fantasy genre of modern popular culture.""",
    tag_id=lore.id)

  ghoul = Creature(name='Ghoul',
    description="""
    Ghoul (Arabic: غول‎, ghūl) is a demon-like being or monstrous humanoid originating in pre-Islamic Arabian religion, associated with graveyards and consuming human flesh. In modern fiction, the term has often been used for a certain kind of undead monster.

    By extension, the word ghoul is also used in a derogatory sense to refer to a person who delights in the macabre or whose profession is linked directly to death, such as a gravedigger or graverobber.

    In the Arabic folklore, the ghul is said to dwell in cemeteries and other uninhabited places. A male ghoul is referred to as ghul while the female is called ghulah. A source identified the Arabic ghoul as a female creature who is sometimes called Mother Ghoul (ʾUmm Ghulah) or a relational term such as Aunt Ghoul. She is portrayed in many tales luring hapless characters, who are usually men, into her home where she can eat them.

    Some state[who?] that a ghoul is a desert-dwelling, shapeshifting demon that can assume the guise of an animal, especially a hyena. It lures unwary people into the desert wastes or abandoned places to slay and devour them. The creature also preys on young children, drinks blood, steals coins, and eats the dead, then taking the form of the person most recently eaten. One of the narratives identified a ghoul named Ghul-e Biyaban, a particularly monstrous character believed to be inhabiting the wilderness of Afghanistan and Iran.

    It was not until Antoine Galland translated One Thousand and One Nights into French that the western idea of ghoul was introduced into European society. Galland depicted the ghoul as a monstrous creature that dwelled in cemeteries, feasting upon corpses.

    Ghouls (Persian: غول‎) were also adopted into Iranian folklore.

    A ghoul is also a name for a female ghost.
""",
    tag_id=lore.id)

  lep = Creature(name='Leprechaun',
    description="""
    A leprechaun (Irish: leipreachán/luchorpán) is a diminutive supernatural being in Irish folklore, classed by some as a type of solitary fairy. They are usually depicted as little bearded men, wearing a coat and hat, who partake in mischief. In later times, they have been depicted as shoe-makers who have a hidden pot of gold at the end of the rainbow.

Leprechaun-like creatures rarely appear in Irish mythology and only became prominent in later folklore.

    """,
    tag_id=lore.id)

  dragon = Creature(name='Dragon',
    description="""
    A dragon is a large, serpentine, legendary creature that appears in the folklore of many cultures worldwide. Beliefs about dragons vary considerably through regions, but dragons in western cultures since the High Middle Ages have often been depicted as winged, horned, four-legged, and capable of breathing fire. Dragons in eastern cultures are usually depicted as wingless, four-legged, serpentine creatures with above-average intelligence.

The earliest attested reports of draconic creatures resemble giant snakes. Draconic creatures are first described in the mythologies of the ancient Near East and appear in ancient Mesopotamian art and literature. Stories about storm-gods slaying giant serpents occur throughout nearly all Indo-European and Near Eastern mythologies. Famous prototypical draconic creatures include the mušḫuššu of ancient Mesopotamia; Apep in Egyptian mythology; Vṛtra in the Rigveda; the Leviathan in the Hebrew Bible; Grand'Goule in the Poitou region in France, Python, Ladon, Wyvern, and the Lernaean Hydra in Greek mythology; Jörmungandr, Níðhöggr, and Fafnir in Norse mythology; and the dragon from Beowulf.

The popular western image of a dragon is based on a conflation of earlier dragons from different traditions, and of inaccurate scribal drawings of snakes. In western cultures, dragons are portrayed as monsters to be tamed or overcome, usually by saints or culture heroes, as in the popular legend of Saint George and the Dragon. They are often said to have ravenous appetites and to live in caves, where they hoard treasure. These dragons appear frequently in western fantasy literature, including The Hobbit by J. R. R. Tolkien, the Harry Potter series by J. K. Rowling, and A Song of Ice and Fire by George R. R. Martin.

The word "dragon" has also come to be applied to the Chinese lung (traditional 龍, simplified 龙, Japanese simplified 竜, Pinyin lóng), which are associated with good fortune and are thought to have power over rain. Dragons and their associations with rain are the source of the Chinese customs of dragon dancing and dragon boat racing. Many East Asian deities and demigods have dragons as their personal mounts or companions. Dragons were also identified with the Emperor of China, who, during later Chinese imperial history, was the only one permitted to have dragons on his house, clothing, or personal articles.

Commonalities between dragons' traits are often a hybridization of avian, feline, and reptilian features, and may include: snakelike features, reptilian scaly skin, four legs with three or four toes on each, spinal nodes running down the back, a tail, and a serrated jaw with rows of teeth. Several modern scholars believe huge extinct or migrating crocodiles bear the closest resemblance, especially when encountered in forested or swampy areas, and are most likely the template of modern dragon imagery.
    """,
    tag_id=lore.id)

  ghost = Creature(name='Ghost',
    description="""
    In folklore, a ghost is the soul or spirit of a dead person or animal that can appear to the living. In ghostlore, descriptions of ghosts vary widely from an invisible presence to translucent or barely visible wispy shapes, to realistic, lifelike forms. The deliberate attempt to contact the spirit of a deceased person is known as necromancy, or in spiritism as a séance. Other terms associated with it are apparition, haunt, phantom, poltergeist, shade, specter or spectre, spirit, spook, wraith, demons, and ghouls.

The belief in the existence of an afterlife, as well as manifestations of the spirits of the dead, is widespread, dating back to animism or ancestor worship in pre-literate cultures. Certain religious practices—funeral rites, exorcisms, and some practices of spiritualism and ritual magic—are specifically designed to rest the spirits of the dead. Ghosts are generally described as solitary, human-like essences, though stories of ghostly armies and the ghosts of animals rather than humans have also been recounted. They are believed to haunt particular locations, objects, or people they were associated with in life. According to a 2009 study by the Pew Research Center, 18% of Americans say they have seen a ghost.

The overwhelming consensus of science is that there is no proof that ghosts exist. Their existence is impossible to falsify, and ghost hunting has been classified as pseudoscience. Despite centuries of investigation, there is no scientific evidence that any location is inhabited by spirits of the dead. Historically, certain toxic and psychoactive plants (such as datura and hyoscyamus niger), whose use has long been associated with necromancy and the underworld, have been shown to contain anticholinergic compounds that are pharmacologically linked to dementia (specifically DLB) as well as histological patterns of neurodegeneration. Recent research has indicated that ghost sightings may be related to degenerative brain diseases such as Alzheimer's disease. Common prescription medication and over-the-counter drugs (such as sleep aids) may also, in rare instances, cause ghost-like hallucinations, particularly zolpidem and diphenhydramine. Older reports linked carbon monoxide poisoning to ghost-like hallucinations.

In folklore studies, ghosts fall within the motif index designation E200-E599 ("Ghosts and other revenants").
    """,
    tag_id=lore.id)

  spyro = Creature(name='Spyro',
    description="""
    Spyro the Dragon was released in North America on 9 September 1998 and Europe in October 1998 for the PlayStation. It is a platform game that placed the player as Spyro, a small purple dragon set with the task of freeing his fellow dragons from crystal prisons, which are scattered around their world. Each level is accessed through 'portals' from a main world. The game concludes with a fight between Spyro and the primary antagonist, Gnasty Gnorc. The game sold well, with a total of five million copies being sold worldwide. The game received favorable reviews from IGN giving Spyro the Dragon a 9 out of 10. It received acclaim for its musical score by Stewart Copeland.

Ripto's Rage!, known as Gateway to Glimmer in Europe and Australia, followed on from the success of the first title, making its release on 2 November 1999 in North America and 5 November 1999 in Europe for the PlayStation. The game introduced new characters including Hunter, a cheetah; Elora, a faun; The Professor, a mole; and Zoe, a fairy. The structure of the game is similar to the first, with levels being accessed from the three main home worlds: Summer Forest, Autumn Plains, and Winter Tundra. The game concludes with a fight between Spyro and the primary antagonist, Ripto. The game introduces some abilities for Spyro, including hovering after a glide, swimming underwater, climbing ladders, head-bashing, and the ability to use power-ups. Like its predecessor, it was critically acclaimed.

Year of the Dragon was released in North America on 24 October 2000 and Europe on 10 November 2000 for the PlayStation, and it was the last Spyro game to be created by Insomniac Games. In the game, the dragons are celebrating the Year of the Dragon, an event held every twelve years in which new dragon eggs arrive in the dragon worlds. Bianca, an anthropomorphic rabbit, steals the eggs, and Spyro follows her down a rabbit hole. The rabbit hole leads to the Forgotten Realms, which are under the rule of the game's primary antagonist, The Sorceress, to whom Bianca is apprenticed. As in the previous games, levels are accessed from a central home world, of which there are four: Sunrise Spring, Midday Gardens, Evening Lake, and Midnight Mountain. The game also features levels in which the player controls "Sparx", Spyro's companion dragonfly, in a bird's eye view shooting game as well as four new playable characters: Sheila the Kangaroo, Sgt. Byrd, Bentley the Yeti, and Agent 9 the Monkey.
    """,
    tag_id=custom.id)

  shrek = Creature(name='Shrek',
    description="""
    Shrek is a 2001 American computer-animated comedy film loosely based on the 1990 fairy tale picture book of the same name by William Steig. Directed by Andrew Adamson and Vicky Jenson in their directorial debuts, it stars Mike Myers, Eddie Murphy, Cameron Diaz, and John Lithgow as the voices of the lead characters. The film parodies other fairy tale adaptations, primarily aimed at animated Disney films. In the story, an ogre called Shrek (Myers) finds his swamp overrun by fairy tale creatures who have been banished by the corrupt Lord Farquaad (Lithgow) aspiring to be king. Shrek makes a deal with Farquaad to regain control of his swamp in return for rescuing Princess Fiona (Diaz), whom Farquaad intends to marry. With the help of Donkey (Murphy), Shrek embarks on his quest but soon falls in love with the princess, who is hiding a secret that will change his life forever.

After purchasing the rights to Steig's book in 1991, Steven Spielberg planned to produce a traditionally-animated film based on the book, but John H. Williams convinced him to bring the project to the newly-founded DreamWorks in 1994. Jeffrey Katzenberg began active development of the film in 1995 immediately following the studio's purchase of the rights from Spielberg. Chris Farley was originally cast as the voice for the title character, recording nearly all of the required dialogue. After Farley died in 1997 before his work on the film was finished, Mike Myers was hired to voice the character, eventually settling on giving Shrek a Scottish accent. The film was initally intended to be created using motion capture, but after poor test results, the studio hired Pacific Data Images to complete the final computer animation.

Shrek premiered at the 2001 Cannes Film Festival, where it competed for the Palme d'Or, making it the first animated film since Disney's Peter Pan (1953) to be chosen to do so. The film was widely praised by critics for its animation, voice performances, writing and humor, which critics noted simultaneously catered to both adults and children. The film was theatrically released in the United States on May 18, 2001, and grossed $484 million worldwide against a production budget of $60 million. Shrek won the first ever Academy Award for Best Animated Feature and was also nominated for Best Adapted Screenplay. It earned six award nominations from the British Academy of Film and Television Arts (BAFTA), ultimately winning Best Adapted Screenplay. The film's success helped establish DreamWorks Animation as a prime competitor to Pixar in feature film computer animation, and three sequels were released—Shrek 2 (2004), Shrek the Third (2007), and Shrek Forever After (2010)—along with two holiday specials, a spin-off film, and a stage musical that kickstarted the Shrek franchise. Although plans for a fifth film were canceled prior to the fourth film's release, the project was revived in 2016, but has since stalled, with production and a potential release date getting pushed back.

In 2020, the film was selected for preservation in the National Film Registry by the Library of Congress as being "culturally, historically, or aesthetically significant", making it the first DreamWorks Animation film and the first animated feature not produced or distributed by Disney to earn that honor.
    """,
    tag_id=custom.id)


  pumpking = Creature(name='Pumpking',
    description="""
    Pumpking is a Hardmode, post-Plantera mini-boss that spawns during the Pumpkin Moon event. It is the event's most difficult enemy, being one of the two whose main body consistently travels through blocks (the other being the Poltergeist) and is also immune to most debuffs. Up to seven of them (more in Multiplayer) can attack simultaneously during the event's final wave (wave 15).

Pumpking has two arms, each possessing a large scythe that periodically fires erratic projectiles. The hands otherwise act much like Skeletron's hands, swiping at the player to inflict melee damage. But unlike Skeletron, Pumpking's hands cannot take damage.

Like Mourning Wood, the later the wave Pumpking is killed in, the more likely it is to drop items. Pumpkings defeated during Wave 15 are guaranteed to produce one Pumpking Trophy along with one of its other items. Defeating the Pumpking will add 150 points during the Pumpkin Moon event, giving the most number of points for any enemy during the event.
    """,
    tag_id=custom.id)

  db.session.add(vampire)
  db.session.add(werewolf)
  db.session.add(ghoul)
  db.session.add(lep)
  db.session.add(dragon)
  db.session.add(spyro)
  db.session.add(shrek)
  db.session.add(ghost)
  db.session.add(pumpking)

  db.session.commit()


def undo_creatures():
    db.session.execute('TRUNCATE creatures CASCADE;')
    db.session.commit()
