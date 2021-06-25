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

  harpy = Creature(name='Harpy',
    description="""
       harpy is a semi-humanoid monster that originates from Greek and Roman mythology. This creature appears to have a human face and torso with clear feminine features, but possesses large feathered wings (either on its back or in place of its arms) and its legs end in the sharp talons found on birds of prey.

According to Greek legend, harpies were supposedly spirits of wind and served the Erinyes by bringing them evildoers to be punished for their crimes. The name "harpy" means "snatcher", an appropriate monniker as these creatures are said to steal food from their victims while eating.

Ancient Greek arts depict harpies as being creatures of remarkable beauty, whereas Byzantine and Roman writers have described harpies as being hideous beasts.

Like many monsters of legend, harpies have been romanticized somewhat in modern times and their likeness has been used in various media formats. They have appeared in a number of fantasy works, such as the roleplaying game Dungeons & Dragons.
    """,
    tag_id=lore.id)

  merfolk= Creature(name='Merfolk',
    description="""
      Merfolk are legendary aquatic creatures with humanoid upper bodies and fish-like tails comprising their lower bodies. These beings have appeared in myths, legends and fairy tales all over the world. Female merfolk are referred to as mermaids with males being called mermen.

      Traditionally the fish tail only replaces the legs, however many modern day depictions show the tail starting at the waist. Merfolk are associated with perilous events such as floods, storms, shipwrecks, and drownings. In other folklore traditions they can be benevolent or beneficent, bestowing boons or falling in love with humans. They are commonly depicted as being highly attractive with long flowing hair and are often associated with the Sirens.
    """,
    tag_id=lore.id)

  griffin= Creature(name='Griffin',
    description="""
      The griffin (also spelt griffon or gryphon) is a legendary creature said to have originated from Greek mythology, though there is evidence that the beast may have originated from ancient Egyptian or Persian artworks. The griffin, like the chimera, is an amalgamation of different parts of other animals. It has the body, tail and back legs of a lion and the head, wings and talons of an eagle.

According to the folklore of various cultures, griffins were noble and proud creatures. Just as the lion was regarded as the king of beasts and the eagle the king of birds, griffins were viewed in a particularly majestic light. They were said to be guardians of exquisite and priceless treasures and artifacts. In medieval folklore, griffins were mated for life. If either griffin partner died, then the remaining griffin would live the rest of its life alone.
    """,
    tag_id=lore.id)

  chimera= Creature(name='Chimera',
    description="""
      The Chimera (/kɪˈmɪərə/ or /kaɪˈmɪərə/, also Chimaera (Chimæra) (Ancient Greek: Χίμαιρα, Chímaira means 'she-goat'), according to Greek mythology, was a monstrous fire-breathing hybrid creature of Lycia in Asia Minor, composed of the parts of more than one animal. It is usually depicted as a lion, with the head of a goat protruding from its back, and a tail that might end with a snake's head. It was one of the offspring of Typhon and Echidna and a sibling of such monsters as Cerberus and the Lernaean Hydra.

The term "chimera" has come to describe any mythical or fictional creature with parts taken from various animals, to describe anything composed of very disparate parts, or perceived as wildly imaginative, implausible, or dazzling.
    """,
    tag_id=lore.id)

  centaur= Creature(name='Centaur',
    description="""
      A centaur is an intelligent magical being that originates from Greek mythology. It appears to have an equine body similar to a horse, but has a humanoid upper body extending from where a horse's neck and head would be. These legendary creatures have featured in numerous forms of modern fantasy literature and other media,  commonly being described as benevolent and living in harmony with nature, hiding away from humans.
    """,
    tag_id=lore.id)

  cerberus= Creature(name='Cerberus',
    description="""
      In Greco-Roman mythology, Cerberus was the guardian to the Gates of Hades. Should any souls try to flee across the Styx, this terrifying hellhound will pursue them and drag them back. This monster has been envisioned as having more than just three heads (and often less) and has also been said to have serpents for tails. This classic beast has been used in many forms of literature and in other media such as video games.
    """,
    tag_id=lore.id)

  hydra= Creature(name='Hydra',
    description="""
      The Hydra is a monstrous, multi-headed reptile from the myths of Ancient Greece. It made its lair in Lake Lerna. According to the myth, beneath the lake was an entrance to the Underworld, and the Hydra was it's guardian. Most of the time, it stayed in the spring of Amymone, a deep cave , only coming out to terrorize neighboring villages. Believed by some to be a type of dragon, the Hydra would meet its end at the hands of Heracles, as the second of his Twelve Labours.

      Most myths agree that the hydra is a sea monster with many heads (according to the poets, more heads than the vase-painters could paint), one of which was immortal. Common depictions of the hydra give the creature a thick, strong body, a serpentine tail and webbed feet.
    """,
    tag_id=lore.id)

  siren= Creature(name='Siren',
    description="""
      The Sirens are a group of magical creatures originating from Greek mythology. They are comparable to other mythical creatures such as mermaids and harpies in that they are demihuman beings possessing both avian and fish traits and reside on the ocean.

According to the legend of Odysseus, the Sirens resided on a small island and would sing whenever ships sailed near. So beautiful and captivating was their song that the sailors who heard it were drawn toward the jagged rocks surrounding the island. The ships would be wrecked and the sailors aboard would perish, either by drowning or slain by the Sirens themselves. Exactly what the Sirens did to their captives is unknown but it has been implied that they ate the unfortunate sailors.

When Odysseus sailed toward the Sirens' island, he ordered his crew to tie him to the mast so that he could hear the Sirens' song without being led astray. The crew were also ordered to plug their ears with beeswax so that they could not hear. Thus, Odysseus' ship safely sailed past the island and the Sirens, anguished that someone had escaped them, cast themselves into the sea and perished.
    """,
    tag_id=lore.id)

  phoenix= Creature(name='Phoenix',
    description="""
      The phoenix is a legendary magical bird originating from Greek mythology. It has long been associated with the sun and is viewed as a symbol of renewal and rebirth. This creature has become widely popular, featuring in countless sources of fantasy fiction.
    """,
    tag_id=lore.id)

  fairy= Creature(name='Fairy',
    description="""
      Fairies (also called fey, fae or faeries) are legendary spirit creatures that possess great magical powers. They are commonly depicted as tiny humanoid creatures with insect or butterfly wings on their backs; they are said to dwell primarily in woodland areas and dress in garments made from plants.

Folklore on fairies can differ greatly between regions. Many tales describe them as a timid race that went into hiding as mankind's presence expanded across the world. Others still have depicted fairies as demons or fallen angels that are not evil enough to warrant banishment to Hell.

Fairies have sometimes been regarded as wicked, fearsome creatures, but they are more often described as being good-natured, if somewhat mischievous. While they usually hide from humans, they have been known to aid them in certain instances. For example, a human might be lost in the forest and a fairy will help guide him to safety, or a fairy might happen upon an injured human and use its magic to heal them. Fairies do not like being thanked for their good deeds, at least not with words. Instead, they prefer to be given something significant to the person they have helped, something that will ensure that the good deed will always be remembered.
    """,
    tag_id=lore.id)

  pegasus= Creature(name='Pegasus',
    description="""
      Pegasus is a legendary winged horse in Greek mythology. Sired by the ocean god Poseidon, this noble beast was birthed by the gorgon Medusa when she was slain by the hero Perseus. Greco-Roman poets write about his ascent to heaven after his birth and his obeisance to Zeus, king of the gods, who instructed him to bring lightning and thunder from Olympus. Friend of the Muses, Pegasus is the creator of Hippocrene, the fountain on Mt. Helicon.

He was captured by the Greek hero Bellerophon near the fountain Peirene with the help of Athena and Poseidon. Pegasus allows the hero to ride him to defeat a monster, the Chimera, before realizing many other exploits. His rider, however, falls off his back trying to reach Mount Olympus. Zeus transformed him into the constellation Pegasus and placed him up in the sky.

In modern times, Pegasus has been popularised in many forms of media, many of which feature numerous winged horses referred to as pegasus (plural: pegasi).
    """,
    tag_id=lore.id)

  banshee= Creature(name='Banshee',
    description="""
      A banshee is a ghost or fairy that originates from Irish and Scottish folklore. Depicted as a messenger from the realm of the dead, it takes the form of a human woman when it enters the mortal plane. It emits a shrill cry of lamentation when a person is about to die, alerting the dying individual's family of their imminent passing.

'Banshee' comes from the Gaelic 'Bean Sidhe' (Bean Sí (Irish), Bean Shìth (Scottish), bean shith (Scottish). The Banshee is also known to wash the bloodstains from clothes, an omen of death. Banshees are seen in three forms. A young, beautiful woman, a matronly figure or a distressed hag. Banshees are frequently described as dressed in white or grey, often having long, pale hair which they brush with a silver comb.
    """,
    tag_id=lore.id)

  kraken= Creature(name='Kraken',
    description="""
      The kraken is a legendary sea-monster of enormous proportions. Described as a cephalopod resembling a giant octopus or squid, this beast is said to be capable of enveloping whole ships in the grasp of its tentacles and dragging them beneath the depths. Kraken have been spoken of in sailors' tales and featured in various works of fiction since the 13th century and remain a common theme in popular culture today. These monsters are said to dwell off the coasts of Norway and Greenland.
    """,
    tag_id=lore.id)

  demon= Creature(name='Demon',
    description="""
      Demons are servants of Lucifer who follow his agenda as both his emissaries as well as torturers of the souls in Hell. Created from the accumulated misery and darkness born of the destruction of human souls, demons are universally malign and immoral in their actions and dealings.

      Born of torment and anguish, demons are creatures of malice and sadistic glee. Literally incapable of love or compassion, these beasts seduce and manipulate humans to fulfill what they believe is Lucifer's grand agenda. In truth, most demons only serve the will of a demon prince.
    """,
    tag_id=lore.id)

  genie= Creature(name='Genie',
    description="""
      Genies (traditionally called Djinn) are mythical beings which are deeply rooted in Indian and Islamic religion. They sometimes looking similar to humans, though it is said that they most often appear as wisps of smoke. In many works of fiction, genies are found by mortals to be inhabiting inanimate objects such as bottles or oil lamps. If a human disturbs said object, they will release the genie within. The natures of genies can differ greatly, ranging between benevolent and subservient to vicious and deceiving.

A generalization of genies in many stories is that they become servants to humans that release them from their vessels, using their great magical powers to grant the wishes of whoever they recognize as their masters. However, according to Muslim beliefs, genies have free will, so it seems that it would be up to the genie to decide whether or not to serve a mortal. Many works of fiction do not take the full details of mythology into account, describing genies as only being partially capable of acting on their own, or not at all unless a master releases the genie from his service.
    """,
    tag_id=lore.id)

  wraith= Creature(name='Wraith',
    description="""
      A wraith is an undead creature whose name originated in Scottish folklore. A type of ghost or spirit, wraiths were traditionally said to be the embodiment of souls who are either on the verge of death, or who have recently passed on.

In modern times, the concept of a wraith is more likely to refer to an evil spirit, particularly one which has unfinished business in the mortal realm. They are typically depicted as skeletal figures draped in tattered rags, and are most commonly associated with graveyards or other haunted locales. The modern perception of a wraith is that of an entity which actively seeks harm to those that it encounters, no matter their motivation.
    """,
    tag_id=lore.id)

  kitsune= Creature(name='Kitsune',
    description="""
      Kitsune means fox in Japanese and they are commonly known as intelligent beings with mystical powers in Japanese folklore.

      The origin of the kitsune legend is still unknown but is most likely related to this japanese folktale. Ono, who lived in Mino, often spent his time longing for female beauty (a wife). He met her one night on a moor and decided to marry her. Although with the birth of their son, Ono's dog also gave birth. The pup's opinion toward Ono's wife harshened as it grew and one day she begged her husband to kill it (of course he refused). At last one day, the dog had enough and attacked the woman. She then lost all her courage, turned back into a fox, and left. Then Ono cried out to her, "Even though you are a fox, you are the mother of my son and I love you! Come back when you please; you are always welcome."

Every night, she snuck back to Ono's house and slept in his arms.

The reason why that story is the most believable one is because kitsune also means sleep if pronounced kitsu-ne, and always comes if pronounced ki-tsune.
    """,
    tag_id=lore.id)

  succubus= Creature(name='Succubus',
    description="""
      Succubi in traditional fantasy form may comprise of various sexually appealing forms. From long haired, to lithe and winged. Succubi appear in whatever form is most pleasing to its intended victim. Though they commonly appearing as scantily clad, shapely, winged demons. Previously, Succubi were noted as being horribly disfigured monsters, with monstrous of rows of teeth, 3 sets of breasts and talon-like nails. The descriptions vary from legend to legend.

The origins of Succubi lay steeped in occult mysteries and various sleep disturbances. Victims of 'Succubi' described their visits to the men as 'a feeling of someone sitting on my chest or pelvic area.' and when they awoke, they would feel drained, unable to move and petrified, though having had a wonderful and erotic dream the night before.
    """,
    tag_id=lore.id)

  hellhound= Creature(name='HellHound',
    description="""
      In Greek, English, and Native American folklore, the Hellhound is commonly seen as an omen of death. If you see it once, you will likely die within the next year, and if you see it three or more times, you're definitely going to die soon. You are more likely to see a Hellhound while traveling at night around a wooded area, as these creatures are nocturnal.

The Hellhound is generally depicted as a large dog—its sizes ranging from that of a mastiff at its smallest to the size of a horse or bear—with a coal black pelt and glowing red or green eyes. They are sometimes depicted as having multiple heads or as being headless. Though the Native American Hellhound, the Cadejo, is said to have a white or black pelt and goat hooves, occasionally including horns in their appearance.
    """,
    tag_id=lore.id)

  leviathan= Creature(name='Leviathan',
    description="""
      Leviathan is a sea serpent monster of immense size. The leviathan of the Middle Ages was used as an image of Satan, endangering both God's creatures - by attempting to eat them - and God's creation - by threatening it with upheaval in the waters of chaos. As the demon of envy, it's classified as one of the Seven Princes of Hell, corresponding to the seven deadly sins. Leviathan represents the element of water. The element of water in Satanism is associated with life and creation.
    """,
    tag_id=lore.id)

  wendigo= Creature(name='Wendigo',
    description="""
    The Wendigo—also know as the Windigo, Witigo, Witiko, and Wee-Tee-Go—is a creature from Algonquian myth. The common translation of its names means "the evil spirit that devours mankind," though in 1860 it was translated by a German explorer to mean "cannibal."

Wendigo are known to live in Canada and the United States and seem only to live in cold climates. They've been sighted around the city of Kenora in Ontario, Canada, but throughout the late 1800's and early 1920's, there were sightings of Wendigo around the time of a death in Roseau, Minnesota. Another Wendigo hotspot is supposedly the Cave of the Wendigo, which is near lake Mameigwess in Ontario, Canada.

While the looks of the Wendigo vary between the different Algonquian tribes, most versions of the Wendigo share these traits: glowing eyes, long yellowed fangs, and long tongues. Legends describe them as about 15 feet (or 4.6 meters) tall, and they are commonly described as being thin and emaciated, their skin stretched so tight over their body that you could see all of their bones clearly. In some cases, they are said to have a stag skull head, while in others they have sunken eyes, look skeletal with ashen skin, and have decaying skin.
    """,
    tag_id=lore.id)

  goomba= Creature(name='Goomba',
    description="""
      As enemies, Goombas are rather pathetic. They aren't very bright and tend to attack enemies simply by charging at them (Let's face it, what else are they going to do?). They are pretty hopeless in battle since they can be defeated with a single stomp on the head, but if there's one thing Goombas have going for them, it's perseverance. It seems that no matter how many of them get flattened by Mario, the Goombas continue marching onward for the glory of Bowser without fear or hesitation. But then again, this lack of self-preservation could simply be a result of the Goombas aforementioned stupidity.
    """,
    tag_id=custom.id)

  mimic= Creature(name='Mimic',
    description="""
      As a natural survival mechanism, Mimics have developed a unique form of defence: they are able to change the shape of their body in order to mimic that of another species or even an inanimate object, hence their name. The only drawback to this ability is that if they decide to copy something larger than themselves, the copy will be of a proportionally smaller size. However, Mimics are capable of becoming anything from clothing to weaponry to furniture, although they do not possess the ability to reproduce the effects of mechanical equipment.

Once the subject of their mimicry leaves the immediate vicinity, a Mimic will revert to its natural form.
    """,
    tag_id=custom.id)

  headcrab= Creature(name='HeadCrab',
    description="""
    A typical headcrab is small, about 1 foot in height and 2 feet long. The creature's body is composed of smooth skin with a sickly tan pigmentation. It walks on four segmented legs, though its hind legs are capable of supporting its whole body, allowing it to "tiptoe" as it raises its forelegs when it prepares to pounce at prey. Headcrabs appear to have no eyes (though in the first Half-Life game they apparently have six very tiny eyes) and their fronts end in a set of four mandibles with fangs that inject toxins into the body of a potential host. Whether these toxins merely paralyze a victim or contribute to the zombification process is unknown. The underbelly of a headcrab consists of a gaping mouth containing a small but sharp beak. When a headcrab latches on to a victim's head, this beak burrows into the skull and the creature initiates an as-yet unknown biological process through which it hijacks the victim's body, controlling its motor functions and altering its physiology, causing the victim's fingers to elongate into gangling claws and strengthening muscle tissue to withstand attacks.
    """,
    tag_id=custom.id)

  molded= Creature(name='Molded',
    description="""
    The Molded are tall, humanoid creatures whose bodies are covered in, if not totally comprised of, a slimy, black, moss-like substance. Beneath the "skin" of the Molded body are multiple reddish veins and ligaments; the arms of the creature end in long, sharp talons for grabbing prey or tearing them apart. The head is misshapen, lacking eyes or a nose and consists primarily of a large mouth filled with jagged fangs.

Molded may be either mutated humans that have been infected and transformed by the Mold, or are completely constructed out of the bacterium by the E-series creator that spawned it. In either case, Molded have flexible and resilient bodies, capable of fitting through tight spaces such as air ducts and can take numerous gunshots before succumbing to injury.
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


def undo_creatures():
    db.session.execute('TRUNCATE creatures CASCADE;')
    db.session.commit()
