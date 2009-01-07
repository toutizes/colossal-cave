from classes import *
from adv import *
ROAD = mkPLACE("ROAD", ["""You're at end of road again.""",
"""You are standing at the end of a road before a small brick building.
Around you is a forest.  A small stream flows out of the building and
down a gully.""",
])
HILL = mkPLACE("HILL", ["""You're at hill in road.""",
"""You have walked up a hill, still in the forest. The road slopes back
down the other side of the hill.  There is a building in the distance.""",
])
BUILDING = mkPLACE("BUILDING", ["""You're inside building.""",
"""You are inside a building, a well house for a large spring.""",
])
mkSYNON(BUILDING, ['HOUSE'])
HOUSE = BUILDING
VALLEY = mkPLACE("VALLEY", ["""You're in valley.""",
"""You are in a valley in the forest beside a stream tumbling along a
rocky bed.""",
])
FOREST = mkPLACE("FOREST", ["""You're in forest.""",
"""You are in open forest, with a deep valley to one side.""",
])
FOREST2 = mkPLACE("FOREST2", ["""You're in forest.""",
"""You are in open forest near both a valley and a road.""",
])
SLIT = mkPLACE("SLIT", ["""You're at slit in streambed.""",
"""At your feet all the water of the stream splashes into a 2-inch slit
in the rock.  Downstream the streambed is bare rock.""",
])
DEPRESSION = mkPLACE("DEPRESSION", ["""You're outside grate.""",
"""You are in a 20-foot depression floored with bare dirt. Set into the
dirt is a strong steel grate mounted in concrete.  A dry streambed
leads into the depression.""",
])
INCAVE = mkPLACE("INCAVE", ["""You're below the grate.""",
"""You are in a small chamber beneath a 3x3 steel grate to the surface.
A low crawl over cobbles leads inward to the west.""",
])
COBBLES = mkPLACE("COBBLES", ["""You're in cobble crawl.""",
"""You are crawling over cobbles in a low passage. There is a dim light
at the east end of the passage.""",
])
DEBRIS = mkPLACE("DEBRIS", ["""You're in debris room.""",
"""You are in a debris room filled with stuff washed in from the surface.
A low wide passage with cobbles becomes plugged with mud and debris
here, but an awkward canyon leads upward and west.  A note on the wall
says \"Magic word XYZZY\".""",
])
CANYON = mkPLACE("CANYON", ["""You are in an awkward sloping east/west canyon.""",
""">*< ditto""",
])
BIRDCHAMBER = mkPLACE("BIRDCHAMBER", ["""You're in bird chamber.""",
"""You are in a splendid chamber thirty feet high. The walls are frozen
rivers of orange stone.  An awkward canyon and a good passage exit
from east and west sides of the chamber.""",
])
PIT = mkPLACE("PIT", ["""You're at top of small pit.""",
"""At your feet is a small pit breathing traces of white mist. An east
passage ends here except for a small crack leading on.  Rough stone
steps lead down the pit.""",
])
MISTS = mkPLACE("MISTS", ["""You're in Hall of Mists.""",
"""You are at one end of a vast hall stretching forward out of sight to
the west, filled with wisps of white mist that sway to and fro
almost as if alive.  Rough stone steps lead up to a passage at the
top of a dome above you.  A wide staircase runs downward into
the darkness;  a chill wind blows up from below.  There are small
passages to the north and south, and a small crack leads east.""",
])
EASTOFFISSURE = mkPLACE("EASTOFFISSURE", ["""You're on east bank of fissure.""",
"""You are on the east bank of a fissure slicing clear across the hall.
The mist is quite thick here, and the fissure is too wide to jump.""",
])
WESTOFFISSURE = mkPLACE("WESTOFFISSURE", ["""You are on the west side of the fissure in the Hall of Mists.""",
""">*< ditto""",
])
GOLDROOM = mkPLACE("GOLDROOM", ["""You're in nugget of gold room.""",
"""This is a low room with a crude note on the wall. The note says,
\"You won't get it up the steps\".""",
])
MTKING = mkPLACE("MTKING", ["""You're in Hall of Mt King.""",
"""You are in the Hall of the Mountain King, with passages off in all
directions.""",
])
WEND2PIT = mkPLACE("WEND2PIT", ["""You're at west end of Twopit room.""",
"""You are at the west end of the Twopit room. There is a large hole in
the wall above the pit at this end of the room.""",
])
EEND2PIT = mkPLACE("EEND2PIT", ["""You're at east end of Twopit room.""",
"""You are at the east end of the Twopit room. The floor here is
littered with thin rock slabs, which make it easy to descend the pits.
There is a path here bypassing the pits to connect passages from east
and west.  There are holes all over, but the only big one is on the
wall directly over the west pit where you can't get to it.""",
])
EASTPIT = mkPLACE("EASTPIT", ["""You're in east pit.""",
"""You are at the bottom of the eastern pit in the Twopit room. There is
a small pool of oil in one corner of the pit.""",
])
WESTPIT = mkPLACE("WESTPIT", ["""You're in west pit.""",
"""You are at the bottom of the western pit in the Twopit room. There is
a large hole in the wall about 25 feet above you.""",
])
LOWNSPASSAGE = mkPLACE("LOWNSPASSAGE", ["""You're in a low N/S passage.""",
"""You are in a low N/S passage at a hole in the floor. The hole goes
down to an E/W passage.""",
])
SOUTHSIDE = mkPLACE("SOUTHSIDE", ["""You are in the south side chamber.""",
""">*< ditto""",
])
WESTSIDE = mkPLACE("WESTSIDE", ["""You're in the west side chamber.""",
"""You are in the west side chamber of the Hall of the Mountain King.
A passage continues west and up here.""",
])
Y2 = mkPLACE("Y2", ["""You're at \"Y2\".""",
"""You are in a large room, with a passage to the south, a passage to the
west, and a wall of broken rock to the east.  There is a large \"Y2\" on
a rock in the room's center.""",
])
JUMBLE = mkPLACE("JUMBLE", ["""You are in a jumble of rock, with cracks everywhere.""",
""">*< ditto""",
])
mkSYNON(JUMBLE, ['WALL', 'BROKEN'])
WALL = JUMBLE
BROKEN = JUMBLE
WINDOW = mkPLACE("WINDOW", ["""You're at window on pit.""",
"""You're at a low window overlooking a huge pit, which extends up out of
sight.  A floor is indistinctly visible over 50 feet below.  Traces of
white mist cover the floor of the pit, becoming thicker to the right.
Marks in the dust around the window would seem to indicate that
someone has been here recently.  Directly across the pit from you and
25 feet away there is a similar window looking into a lighted room.  A
shadowy figure can be seen there peering back at you.""",
])
WINDOW2 = mkPLACE("WINDOW2", ["""You're at window on pit.""",
"""You're at a low window overlooking a huge pit, which extends up out of
sight.  A floor is indistinctly visible over 50 feet below.  Traces of
white mist cover the floor of the pit, becoming thicker to the left.
Marks in the dust around the window would seem to indicate that
someone has been here recently.  Directly across the pit from you and
25 feet away there is a similar window looking into a lighted room.  A
shadowy figure can be seen there peering back at you.""",
])
DIRTY = mkPLACE("DIRTY", ["""You're in dirty passage.""",
"""You are in a dirty broken passage. To the east is a crawl. To the
west is a large passage.  Above you is a hole to another passage.""",
])
BRINK = mkPLACE("BRINK", ["""You are on the brink of a small clean climbable pit.""",
"""You are on the brink of a small clean climbable pit. A crawl leads
west.""",
])
STREAMPIT = mkPLACE("STREAMPIT", ["""You are at the pit's bottom with a stream nearby.""",
"""You are in the bottom of a small pit with a little stream, which
enters and exits through tiny slits.""",
])
DUSTY = mkPLACE("DUSTY", ["""You're in dusty rock room.""",
"""You are in a large room full of dusty rocks. There is a big hole in
the floor.  There are cracks everywhere, and a passage leading east.""",
])
WENDMISTS = mkPLACE("WENDMISTS", ["""You're at west end of Hall of Mists.""",
"""You are at the west end of Hall of Mists. A low wide crawl continues
west and another goes north.  To the south is a little passage 6 feet
off the floor.""",
])
MAZEA_42 = mkPLACE("MAZEA_42", ["""You are in a maze of twisty little passages, all alike.""",
""">*< ditto""",
])
MAZEA_43 = mkPLACE("MAZEA_43", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_44 = mkPLACE("MAZEA_44", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_45 = mkPLACE("MAZEA_45", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_46 = mkPLACE("MAZEA_46", ["""Dead end.""",
""">*< ditto""",
])
MAZEA_47 = mkPLACE("MAZEA_47", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_48 = mkPLACE("MAZEA_48", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_49 = mkPLACE("MAZEA_49", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_50 = mkPLACE("MAZEA_50", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_51 = mkPLACE("MAZEA_51", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_52 = mkPLACE("MAZEA_52", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_53 = mkPLACE("MAZEA_53", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_54 = mkPLACE("MAZEA_54", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_55 = mkPLACE("MAZEA_55", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_56 = mkPLACE("MAZEA_56", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_57_PIT = mkPLACE("MAZEA_57_PIT", ["""You're at brink of pit.""",
"""You are on the brink of a thirty foot pit with a massive orange column
down one wall.  You could climb down here but you could not get back
up.  The maze continues at this level.""",
])
MAZEA_58 = mkPLACE("MAZEA_58", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
LONGHALLEAST = mkPLACE("LONGHALLEAST", ["""You're at east end of long hall.""",
"""You are at the east end of a very long hall apparently without side
chambers.  To the east a low wide crawl slants up.  To the north a
round two foot hole slants down.""",
])
LONGHALLWEST = mkPLACE("LONGHALLWEST", ["""You're at west end of long hall.""",
"""You are at the west end of a very long featureless hall. The hall
joins up with a narrow north/south passage.""",
])
CROSSOVER = mkPLACE("CROSSOVER", ["""You are at a crossover of a high N/S passage and a low E/W one.""",
""">*< ditto""",
])
DEADEND1 = mkPLACE("DEADEND1", ["""Dead end passage. Scratched on a rock is the message, \"Stand where
the statue gazes, and make use of the proper tool.\"""",
""">*< ditto""",
])
COMPLEX = mkPLACE("COMPLEX", ["""You're at complex junction.""",
"""You are at a complex junction. A low hands and knees passage from the
north joins a higher crawl from the east to make a walking passage
going west.  There is also a large room above.  The air is damp here.""",
])
BEDQUILT = mkPLACE("BEDQUILT", ["""You're back at Bedquilt.""",
"""You are in Bedquilt, a long east/west passage with holes everywhere.
To explore at random select NORTH, SOUTH, UP, or DOWN.""",
])
SWISS = mkPLACE("SWISS", ["""You're in Swiss cheese room.""",
"""You are in a room whose walls resemble Swiss cheese. Obvious passages
go west, east, NE, and NW.  Part of the room is occupied by a large
bedrock block.""",
])
SLAB = mkPLACE("SLAB", ["""You're in Slab room.""",
"""You are in a large low circular chamber whose floor is an immense slab
fallen from the ceiling (Slab room).  East and west there once were
large passages, but they are now filled with boulders.  Low small
passages go north and south, and the south one quickly bends west
around the boulders.""",
])
SECRETNSCYN = mkPLACE("SECRETNSCYN", ["""You are in a secret N/S canyon above a large room.""",
""">*< ditto""",
])
SECRETNSCPAS = mkPLACE("SECRETNSCPAS", ["""You are in a secret N/S canyon above a sizable passage.""",
""">*< ditto""",
])
SECRETJUNCTION = mkPLACE("SECRETJUNCTION", ["""You're at junction of three secret canyons.""",
"""You are in a secret canyon at a junction of three canyons, bearing
north, south, and SE.  The north one is as tall as the other two
combined.""",
])
LOW = mkPLACE("LOW", ["""You are in a large low room.  Crawls lead north, SE, and SW.""",
""">*< ditto""",
])
DEADEND2 = mkPLACE("DEADEND2", ["""Dead end crawl.""",
""">*< ditto""",
])
SECRETEW_TITE = mkPLACE("SECRETEW_TITE", ["""You're in secret E/W canyon above tight canyon.""",
"""You are in a secret canyon which here runs E/W. It crosses over a
very tight canyon 15 feet below.  If you go down you may not be able
to get back up.""",
])
NSCANYONWIDE = mkPLACE("NSCANYONWIDE", ["""You are at a wide place in a very tight N/S canyon.""",
""">*< ditto""",
])
TIGHTERSTILL = mkPLACE("TIGHTERSTILL", ["""The canyon here becomes too tight to go further south.""",
""">*< ditto""",
])
TALLEWCNYN = mkPLACE("TALLEWCNYN", ["""You are in a tall E/W canyon.""",
"""You are in a tall E/W canyon. A low tight crawl goes 3 feet north and
seems to open up.""",
])
DEADEND3 = mkPLACE("DEADEND3", ["""The canyon runs into a mass of boulders -- dead end.""",
"""The canyon runs into a mass of boulders -- dead end.  Scratched on
one of the boulders are the words, \"Jerry Cornelius was here.\"""",
])
MAZEA_80 = mkPLACE("MAZEA_80", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_81 = mkPLACE("MAZEA_81", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_82 = mkPLACE("MAZEA_82", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_83 = mkPLACE("MAZEA_83", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_84 = mkPLACE("MAZEA_84", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
MAZEA_85 = mkPLACE("MAZEA_85", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_86 = mkPLACE("MAZEA_86", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
MAZEA_87 = mkPLACE("MAZEA_87", [""">*< short MAZEA.42""",
""">*< short MAZEA.42""",
])
NARROWCORRIDOR = mkPLACE("NARROWCORRIDOR", ["""You're in narrow corridor.""",
"""You are in a long, narrow corridor stretching out of sight to the
west.  At the eastern end is a hole through which you can see a
profusion of leaves.""",
])
INCLINE = mkPLACE("INCLINE", ["""You're at steep incline above large room.""",
"""You are at the top of a steep incline above a large room. You could
climb down here, but you would not be able to climb up.  There is a
passage leading back to the north.""",
])
GIANT = mkPLACE("GIANT", ["""You're in Giant room.""",
"""You are in the Giant room. The ceiling here is too high up for your
lamp to show it.  Cavernous passages lead east, north, and south.  On
the west wall is scrawled the inscription, \"Fee Fie Foe Foo\" {sic}.""",
])
IMMENSENSPASS = mkPLACE("IMMENSENSPASS", ["""You are at one end of an immense north/south passage.""",
""">*< ditto""",
])
CAVERN = mkPLACE("CAVERN", ["""You're in cavern with waterfall.""",
"""You are in a magnificent cavern with a rushing stream, which cascades
over a sparkling waterfall into a roaring whirlpool which disappears
through a hole in the floor.  Passages exit to the south and west.""",
])
SOFT = mkPLACE("SOFT", ["""You're in soft room.""",
"""You are in the soft room. The walls are covered with heavy curtains,
the floor with a thick pile carpet.  Moss covers the ceiling.""",
])
ORIENTAL = mkPLACE("ORIENTAL", ["""You're in Oriental room.""",
"""This is the Oriental room. Ancient oriental cave drawings cover the
walls.  A gently sloping passage leads upward to the north, another
passage leads SE, and a hands and knees crawl leads west.""",
])
MISTY = mkPLACE("MISTY", ["""You're in misty cavern.""",
"""You are following a wide path around the outer edge of a large cavern.
Far below, through a heavy white mist, strange splashing noises can be
heard.  The mist rises up through a fissure in the ceiling.  The path
exits to the south and west.""",
])
ALCOVE = mkPLACE("ALCOVE", ["""You're in alcove.""",
"""You are in an alcove. A small NW path seems to widen after a short
distance.  An extremely tight tunnel leads east.  It looks like a very
tight squeeze.  An eerie light can be seen at the other end.""",
])
PLOVER = mkPLACE("PLOVER", ["""You're in Plover room.""",
"""You're in a small chamber lit by an eerie green light. An extremely
narrow tunnel exits to the west.  A dark corridor leads NE.""",
])
DARK = mkPLACE("DARK", ["""You're in Dark room.""",
"""You're in the Dark room. A corridor leading south is the only exit.""",
])
ARCHED = mkPLACE("ARCHED", ["""You're in arched hall.""",
"""You are in an arched hall. A coral passage continues up and east.
The air smells of sea water.""",
])
SHELL = mkPLACE("SHELL", ["""You're in Shell room.""",
"""You're in a large room carved out of sedimentary rock. The floor and
walls are littered with bits of shells imbedded in the stone.  A
shallow passage proceeds downward, and a somewhat steeper one leads
up.  A low hands and knees passage enters from the south.""",
])
RAGGEDCORRID = mkPLACE("RAGGEDCORRID", ["""You are in a long sloping corridor with ragged sharp walls.""",
""">*< ditto""",
])
CULDESAC = mkPLACE("CULDESAC", ["""You are in a cul-de-sac about eight feet across.""",
""">*< ditto""",
])
ANTEROOM = mkPLACE("ANTEROOM", ["""You're in anteroom.""",
"""You are in an anteroom leading to a large passage to the east. Small
passages go west and up.  The remnants of recent digging are evident.
A sign in midair here says \"Cave under construction beyond this point.
Proceed at own risk.  {Witt Construction Company}\"""",
])
MAZED_107 = mkPLACE("MAZED_107", ["""You are in a maze of twisty little passages, all different.""",
""">*< ditto""",
])
WITTSEND = mkPLACE("WITTSEND", ["""You're at Witt's End.""",
"""You are at Witt's End. Passages lead off in *all* directions.""",
])
MIRRORCNYN = mkPLACE("MIRRORCNYN", ["""You're in mirror canyon.""",
"""You are in a north/south canyon about 25 feet across. The floor is
covered by white mist seeping in from the north.  The walls extend
upward for well over 100 feet.  Suspended from some unseen point far
above you, an enormous two-sided mirror is hanging parallel to and
midway between the canyon walls.  (The mirror is obviously provided
for the use of the dwarves, who as you know, are extremely vain.)  A
small window can be seen in either wall, some fifty feet up.""",
])
STALACT = mkPLACE("STALACT", ["""You're at top of stalactite.""",
"""A large stalactite extends from the roof and almost reaches the floor
below.  You could climb down it, and jump from it to the floor, but
having done so you would be unable to reach it to climb back up.""",
])
MAZED_112 = mkPLACE("MAZED_112", ["""You are in a little maze of twisting passages, all different.""",
""">*< ditto""",
])
RESERVOIR = mkPLACE("RESERVOIR", ["""You're on southern edge of reservoir.""",
"""You are on the southern edge of a large underground reservoir.  A
thick cloud of white mist fills the room, rising from the surface
of the water and drifting rapidly upwards.  The lake is fed by a
stream, which tumbles out of a hole in the wall about 10 feet overhead
and splashes noisily into the water near the reservoir's northern wall.
A dimly-seen passage exits through the northern wall, but you can't get
across the water to get to it.  Another passage leads south from here.""",
])
RESERVOIR_N = mkPLACE("RESERVOIR_N", ["""You are at the northern end of the reservoir.""",
"""You are at the northern end of a large underground reservoir.  Across
the water to the south, a dark passage is visible.  Another passage
leads north from here.  Large, clawed tracks are visible in the damp
ground, leading from the passage into the water.""",
])
WARM = mkPLACE("WARM", ["""You're in small, warm chamber.""",
"""You are in a small chamber with warm walls.  Mist drifts into the
chamber from a passage entering from the south and evaporates in
the heat.  Another passage leads out to the northeast.""",
])
BALCONY = mkPLACE("BALCONY", ["""You're on balcony above treasure chamber.""",
"""You are in a high balcony carved out of solid rock overlooking a large,
bare chamber lit by dozens of flickering torches.  A rushing stream
pours into the chamber through a two-foot slit in the east wall and
drains into a large pool along the north side of the chamber.  A small
plaque riveted to the edge of the balcony reads, \"You are looking at
the Witt Company's main treasure room, constructed by the famous
architect Ralph Witt in 4004 B.C., and dedicated to the proposition
that all adventurers are created equal (although some are more equal
than others).  NO ADMITTANCE VIA THIS ENTRANCE!\"  A small, dark
tunnel leads out to the west.""",
])
FAKE_SLIT = mkPLACE("FAKE_SLIT", ["""You're at slit in streambed.""",
"""At your feet all the water of the stream splashes into a 2-foot slit
in the rock.  Downstream the streambed is bare rock.""",
])
CYLINDRICAL = mkPLACE("CYLINDRICAL", ["""You're in cylindrical chamber.""",
"""You are in a small cylindrical room with very smooth walls and a flat
floor and ceiling.  There are no exits visible anywhere.""",
])
TREASUREROOM = mkPLACE("TREASUREROOM", ["""""",
"""You plunge into the stream and are carried down into total blackness.

Deeper
and
deeper
you
go,
down
into
the
very
bowels
of
the
earth,
until
your
lungs
are
aching
with
the
need
for
fresh
air.
Suddenly,
with
a
violent
>splash!!<

you find yourself sitting on the edge of a pool of water in
a vast chamber lit by dozens of flaring torches.

The floor is covered with thick layers of precious Persian rugs!

Rare coins, bars of silver, and lumps of gold and platinum are
strewn carelessly about!

There are diamonds, rubies, sapphires, emeralds, opals, pearls, and
fabulous sculptures and ornaments carved out of jade and imperishable
crystal resting on display shelves, along with rare Ming vases and
ancient Indian turquoise beads!

A flotilla of ruby-encrusted toy boats is floating in the pool of
water beside you!

A network of golden chains supports a fantastic Iridium crown!

There is a display case on the wall filled with a fantastic selection
of magical swords, which are singing \"Hail to the Chief\" in perfect
pitch and rhythm!

There are a dozen friendly little dwarves in the room, displaying
their talents by deftly juggling hundreds of golden eggs!

A large troll, a gigantic ogre, and a bearded pirate are tossing
knives, axes, and clubs back and forth in a friendly demonstration
of martial skill!

A horde of cheerful little gooseberry goblins are performing
talented acrobatics to an appreciative audience composed of a dragon,
a large green snake, a cute little bird (which is sitting, unmolested,
on the snake's head), a peaceful basilisk, and a large Arabian Djinn.

Everyone turns and sees you, and lets out a heart-warming cheer
of welcome!
""",
])
MAZEA_114 = mkPLACE("MAZEA_114", [""">*< short MAZEA.46""",
""">*< short MAZEA.46""",
])
SWOFCHASM = mkPLACE("SWOFCHASM", ["""You're on SW side of chasm.""",
"""You are on one side of a large, deep chasm. A heavy white mist rising
up from below obscures all view of the far side.  A SW path leads away
from the chasm into a winding corridor.""",
])
NEOFCHASM = mkPLACE("NEOFCHASM", ["""You're on NE side of chasm.""",
"""You are on the far side of the chasm. A NE path leads away from the
chasm on this side.""",
])
SLOPING = mkPLACE("SLOPING", ["""You're in sloping corridor.""",
"""You are in a long winding corridor sloping out of sight in both
directions.""",
])
SECRETCYNNE1 = mkPLACE("SECRETCYNNE1", ["""You are in a secret canyon which exits to the north and east.""",
""">*< ditto""",
])
SECRETCYNNE2 = mkPLACE("SECRETCYNNE2", ["""You are in a secret canyon which exits to the north and east.""",
""">*< ditto""",
])
CORRIDOR = mkPLACE("CORRIDOR", ["""You're in corridor.""",
"""You're in a long east/west corridor. A faint rumbling noise can be
heard in the distance.""",
])
FORK = mkPLACE("FORK", ["""You're at fork in path.""",
"""The path forks here. The left fork leads northeast. A dull rumbling
seems to get louder in that direction.  The right fork leads southeast
down a gentle slope.  The main corridor enters from the west.""",
])
WARMJUNCTN = mkPLACE("WARMJUNCTN", ["""You're at junction with warm walls.""",
"""The walls are quite warm here. From the north can be heard a steady
roar, so loud that the entire cave seems to be trembling.  Another
passage leads south, and a low crawl goes east.""",
])
BREATHTAKER = mkPLACE("BREATHTAKER", ["""You're at breath-taking view.""",
"""You are on the edge of a breath-taking view. Far below you is an
active volcano, from which great gouts of molten lava come surging
out, cascading back down into the depths.  The glowing rock fills the
farthest reaches of the cavern with a blood-red glare, giving every-
thing an eerie, macabre appearance.  The air is filled with flickering
sparks of ash and a heavy smell of brimstone.  The walls are hot to
the touch, and the thundering of the volcano drowns out all other
sounds.  Embedded in the jagged roof far overhead are myriad twisted
formations composed of pure white alabaster, which scatter the murky
light into sinister apparitions upon the walls.  To one side is a deep
gorge, filled with a bizarre chaos of tortured rock which seems to
have been crafted by the devil himself.  An immense river of fire
crashes out from the depths of the volcano, burns its way through the
gorge, and plummets into a bottomless pit far off to your left.
Across the gorge, the entrance to a valley is dimly visible.  To
the right, an immense geyser of blistering steam erupts continuously
from a barren island in the center of a sulfurous lake, which bubbles
ominously.  The far right wall is aflame with an incandescence of its
own, which lends an additional infernal splendor to the already
hellish scene.  A dark, foreboding passage exits to the south.""",
])
FACES = mkPLACE("FACES", ["""You're at the south end of the Valley of the Stone Faces.""",
"""You are standing at the southern end of a long valley illuminated by
flickering red light from the volcanic gorge behind you.  Carved
into the walls of the valley is an incredible series of stone faces.
Some of them look down into the valley with expressions of
benevolence that would credit a saint;  others glare with a malice
that makes the heart grow faint.  All of them are imbued with a
fantastic seeming of life by the shifting and flickering light of
the volcano.  The entire far end of the valley is taken up by an
immense carving of a seated figure;  its exact form cannot be seen
from here due to the uncertainty of the light.""",
])
BY_FIGURE = mkPLACE("BY_FIGURE", ["""You're at north end of the Valley of the Stone Faces.""",
"""You are standing at the north end of the Valley of the Stone Faces.
Above you, an incredible bas-relief statue of an immense minotaur
has been carved out of the rock.  At least sixty feet high, it sits
gazing down at you with a faint but definite expression of amusement.
Between its feet and the floor is a rock wall about ten feet high
which extends across the entire north end of the valley.""",
])
PLAIN_1 = mkPLACE("PLAIN_1", ["""You're at south end of fog-filled room.""",
"""You are standing at the southern end of what appears to be a
large room filled with multicolored fog.  The sides and far end
of the room cannot be seen due to the thickness of the fog - it's
a real pea-souper (even to the color in places!).  A passage leads
back to the south;  a dull rumbling sound issues from the passage.""",
])
PLAIN_2 = mkPLACE("PLAIN_2", ["""""",
])
PLAIN_3 = mkPLACE("PLAIN_3", ["""You're in foggy room by cairn of rocks.""",
"""You are standing in a fog-filled room next to a tall cairn of glowing
rocks.  An opening in the cairn leads down to a dark passage.""",
])
NONDESCRIPT = mkPLACE("NONDESCRIPT", ["""You're in nondescript chamber.""",
"""You're in a small, nondescript chamber.  A dark passage leads up
and to the south, and a wide but low crawl leads north.""",
])
PENTAGRAM = mkPLACE("PENTAGRAM", ["""You're in room with pentagram.""",
"""You're in a small room with a very smooth rock floor, onto which
has been marked a pentagram.  A low crawl leads out to the west, and
a crack in the rock leads north.""",
])
CHIMNEY = mkPLACE("CHIMNEY", ["""You're at the end of the crack, at the bottom of the chimney.""",
"""The crack in the rock ends here, but a narrow chimney leads up.  You
should be able to climb it.""",
])
TUBE = mkPLACE("TUBE", ["""You're in lava tube at top of chimney.""",
"""You're at the top of a narrow chimney in the rock.  A cylindrical
tube composed of hardened lava leads south.""",
])
TUBE_SLIDE = mkPLACE("TUBE_SLIDE", ["""You're at steep slide in lava tube.""",
"""The lava tube continues down and to the south, but it becomes very
steep here - if you go down it you probably won't be able to get
back up.""",
])
BASQUE_1 = mkPLACE("BASQUE_1", ["""You're in rough and narrow passage.""",
"""You are in a narrow and rough passage running north and south.
A dull rumbling sound can be heard from the south.""",
])
BASQUE_2 = mkPLACE("BASQUE_2", ["""You're in rough passage to the north of the basilisk's den.""",
""">*< ditto""",
])
BASQUE_FORK = mkPLACE("BASQUE_FORK", ["""You're at fork in passage by steps.""",
"""The passage here enters from the south and divides, with a wide
tunnel exiting to the north and a set of steps leading downward.""",
])
ON_STEPS = mkPLACE("ON_STEPS", ["""You're on the steps.""",
"""You are on a long, spiral set of steps leading downwards into the
earth.""",
])
STEPS_EXIT = mkPLACE("STEPS_EXIT", ["""You're at exit on steps.""",
"""A small tunnel exits from the steps and leads north.  The steps
continue downwards.""",
])
STORAGE = mkPLACE("STORAGE", ["""You're in the storage room.""",
"""You're in what was once a storage room.  A set of steps lead up.""",
])
FAKE_Y2 = mkPLACE("FAKE_Y2", ["""You're at \"Y2\"?""",
"""You are in a large room, with a passage to the south, a passage to the
west, and a wall of broken rock to the east.  There is a large \"Y2\" on
a rock in the room's center.""",
])
FAKE_JUMBLE = mkPLACE("FAKE_JUMBLE", ["""You are in a jumble of rock, with cracks everywhere.""",
""">*< ditto""",
])
CATACOMBS_1 = mkPLACE("CATACOMBS_1", ["""You are in the catacombs.  Enchanted tunnels lead in all directions.""",
""">*< ditto""",
])
CATACOMBS_2 = mkPLACE("CATACOMBS_2", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_3 = mkPLACE("CATACOMBS_3", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_4 = mkPLACE("CATACOMBS_4", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_5 = mkPLACE("CATACOMBS_5", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_6 = mkPLACE("CATACOMBS_6", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_7 = mkPLACE("CATACOMBS_7", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_8 = mkPLACE("CATACOMBS_8", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_9 = mkPLACE("CATACOMBS_9", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_10 = mkPLACE("CATACOMBS_10", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_11 = mkPLACE("CATACOMBS_11", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_12 = mkPLACE("CATACOMBS_12", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_13 = mkPLACE("CATACOMBS_13", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_14 = mkPLACE("CATACOMBS_14", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_15 = mkPLACE("CATACOMBS_15", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_16 = mkPLACE("CATACOMBS_16", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_17 = mkPLACE("CATACOMBS_17", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_18 = mkPLACE("CATACOMBS_18", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
CATACOMBS_19 = mkPLACE("CATACOMBS_19", [""">*< short CATACOMBS.1""",
""">*< short CATACOMBS.1""",
])
AUDIENCE = mkPLACE("AUDIENCE", ["""You're at west end of Audience Hall.""",
"""You are standing at the west end of the royal Audience Hall.
The walls here are composed of the finest marble, and the floor is
built of slabs of rare onyx and bloodstone.  The ceiling is high and
vaulted, and is supported by pillars of rare Egyptian red granite;
it gives off a nacreous glow that fills the entire chamber with
a light like moon-light shining off of polished silver.""",
])
AUDIENCE_E = mkPLACE("AUDIENCE_E", ["""You're at east end of Audience Hall.""",
"""You are at the eastern end of the Audience Hall.  There is a large
dais rising out of the floor here;  resting upon the dais is a strange-
looking throne made out of interlocking bars and rods of metal.""",
])
BANSHEE_1 = mkPLACE("BANSHEE_1", ["""You're in winding passage.""",
"""You are in a winding passage which enters from the northwest,
loops around several times, and exits to the north.""",
])
GOLDEN = mkPLACE("GOLDEN", ["""You're in golden chamber.""",
"""You are in a chamber with golden walls and a high ceiling.  Passages
lead south, northeast, and northwest.""",
])
ARABESQUE = mkPLACE("ARABESQUE", ["""You're in Arabesque room.""",
"""You are in a small room whose walls are covered with an elaborate
pattern of arabesque figures and designs.""",
])
TRANSLUCENT = mkPLACE("TRANSLUCENT", ["""You're in room with translucent walls.""",
"""You are in a large room whose walls are composed of some translucent
whitish mineral.  The room is illuminated by a flickering reddish
glow shining through the southern wall.  A passage leads east.""",
])
BOULDERS = mkPLACE("BOULDERS", ["""You're in chamber of boulders.""",
"""You are in a small chamber filled with large boulders. The walls are
very warm, causing the air in the room to be almost stifling from the
heat.  The only exit is a crawl heading west, through which is coming
a low rumbling.""",
])
LIMESTONE = mkPLACE("LIMESTONE", ["""You're in limestone passage.""",
"""You are walking along a gently sloping north/south passage lined with
oddly shaped limestone formations.""",
])
BARREN = mkPLACE("BARREN", ["""You are at entrance of the barren room.""",
"""You are standing at the entrance to a large, barren room. A sign
posted above the entrance reads:  \"Caution!  Bear in room!\"""",
])
BEARHERE = mkPLACE("BEARHERE", ["""You are in the barren room.""",
"""You are inside a barren room. The center of the room is completely
empty except for some dust.  Marks in the dust lead away toward the
far end of the room.  The only exit is the way you came in.""",
])
MAZED_131 = mkPLACE("MAZED_131", ["""You are in a maze of twisting little passages, all different.""",
""">*< ditto""",
])
MAZED_132 = mkPLACE("MAZED_132", ["""You are in a little maze of twisty passages, all different.""",
""">*< ditto""",
])
MAZED_133 = mkPLACE("MAZED_133", ["""You are in a twisting maze of little passages, all different.""",
""">*< ditto""",
])
MAZED_134 = mkPLACE("MAZED_134", ["""You are in a twisting little maze of passages, all different.""",
""">*< ditto""",
])
MAZED_135 = mkPLACE("MAZED_135", ["""You are in a twisty little maze of passages, all different.""",
""">*< ditto""",
])
MAZED_136 = mkPLACE("MAZED_136", ["""You are in a twisty maze of little passages, all different.""",
""">*< ditto""",
])
MAZED_137 = mkPLACE("MAZED_137", ["""You are in a little twisty maze of passages, all different.""",
""">*< ditto""",
])
MAZED_138 = mkPLACE("MAZED_138", ["""You are in a maze of little twisting passages, all different.""",
""">*< ditto""",
])
MAZED_139 = mkPLACE("MAZED_139", ["""You are in a maze of little twisty passages, all different.""",
""">*< ditto""",
])
MAZED_140 = mkPLACE("MAZED_140", ["""Dead end.""",
""">*< ditto""",
])
SANDSTONE = mkPLACE("SANDSTONE", ["""You're in sandstone chamber.""",
"""You are in a small chamber to the east of the Hall of Mists.  The
walls are composed of rough red sandstone.  There is a large, cubical
chunk of rock in the center of the room.""",
])
MORION = mkPLACE("MORION", ["""You're in the Morion room.""",
"""You are in a small room.  The walls are composed of a dark, almost
black form of smoky quartz; they glisten like teeth in the lamp-light.
The only exit is the passage to the south through which you entered.""",
])
VAULT = mkPLACE("VAULT", ["""You're in room with vaulted ceiling.""",
"""You are in a room with a high, vaulted ceiling.  A tunnel leads
upwards and to the north.""",
])
PEELGRUNT = mkPLACE("PEELGRUNT", ["""You're in Peelgrunt room.""",
"""You are in the Peelgrunt room.""",
])
INSAFE = mkPLACE("INSAFE", ["""You are in the safe.""",
"""You are inside the safe.""",
])
CORRID_1 = mkPLACE("CORRID_1", ["""You are standing in a wide, north-and-south corridor.""",
""">*< ditto""",
])
CORRID_2 = mkPLACE("CORRID_2", ["""You're at bend in wide corridor.""",
"""You are standing at a bend in a wide corridor which runs to the east
and west.  To the east, the corridor turns left and continues north;
to the west, it turns left and continues south.""",
])
TOOL = mkPLACE("TOOL", ["""You're in Tool room.""",
"""You are in a small, low-ceilinged room with the words \"Witt Company
Tool Room - Melenkurion division\" carved into one of the walls.  A
wide corridor runs south from here.""",
])
CORRID_3 = mkPLACE("CORRID_3", ["""You're at division in passage.""",
"""You are at a division in a narrow passage.  Two spurs run east and
north;  the main passage exits to the south.""",
])
CUBICLE = mkPLACE("CUBICLE", ["""You're in dank cubicle.""",
"""You are in a small, dank cubicle of rock.  A small passage leads back
out to the south;  there is no other obvious exit.""",
])
SPHERICAL = mkPLACE("SPHERICAL", ["""You're in spherical room.""",
"""You're in a large, completely spherical room with polished walls.  A
narrow passage leads out to the north.""",
])
TUNNEL_1 = mkPLACE("TUNNEL_1", ["""You're in low tunnel with irregular ceiling.""",
"""You are in a low tunnel with an irregular ceiling.  To the north, the
tunnel is partially blocked by a recent cave-in, but you can probably
get past the blockage without too much trouble.""",
])
GLASSY = mkPLACE("GLASSY", ["""You're in large room with glassy walls.""",
"""You're standing in a very large room (which however is smaller than the
Giant room) which has smooth, glassy-looking walls.  A passage enters
from the south and exits to the north.""",
])
LAIR = mkPLACE("LAIR", ["""You're in the Sorcerer's Lair.""",
"""This is the Sorcerer's Lair.  The walls are covered with exotic runes
written in strange, indecipherable scripts;  the only readable phrase
reads \"noside samoht\".  Strange shadows flit about on the walls, but
there is nothing visible to cast them.  Iridescent blue light drips
from a stalactite far above, falls towards the floor, and evaporates
before touching the ground.  A deep, resonant chanting sound vibrates
from deep in the ground beneath your feet, and a whispering sound
composed of the echoes of long-forgotten spells and cantrips seeps
from the walls and fills the air.  Passages exit to the east and west.""",
])
BRINK_1 = mkPLACE("BRINK_1", ["""You're at brink of bottomless pit.""",
"""You are standing on the brink of what appears to be a bottomless pit
plunging down into the bowels of the earth.  Ledges run around the
pit to the east and west, and a passage leads back to the north.""",
])
BRINK_2 = mkPLACE("BRINK_2", ["""You're on southern edge of bottomless pit.""",
"""You are standing at the south end of a ledge running around the west
side of a bottomless pit.  The ledge once continued around to the east
side of the pit, but was apparently obliterated by a rock-slide
years ago.  A cold wind blows out of a tunnel leading to the southeast.""",
])
ICE = mkPLACE("ICE", ["""You're in Ice room.""",
"""You are in the Ice room.  The walls and ceiling here are composed of
clear blue glacial ice;  the floor is fortunately made of rock and
is easy to walk upon.  There is a passage leading to the northwest,
and a slide of polished ice leading downwards to the east - if you
were to slide down it you probably couldn't get back up.""",
])
SLIDE = mkPLACE("SLIDE", ["""You're at bottom of icy slide.""",
"""You're at the entrance to an extensive and intricate network of tunnels
carved out of solid ice.  A slippery slope leads upwards and north, but
you cannot possibly climb up it.""",
])
ICECAVE_1 = mkPLACE("ICECAVE_1", ["""You are in an intricate network of ice tunnels.""",
""">*< ditto""",
])
ICECAVE_1A = mkPLACE("ICECAVE_1A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_2 = mkPLACE("ICECAVE_2", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_2A = mkPLACE("ICECAVE_2A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_3 = mkPLACE("ICECAVE_3", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_3A = mkPLACE("ICECAVE_3A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_4 = mkPLACE("ICECAVE_4", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_5 = mkPLACE("ICECAVE_5", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_6 = mkPLACE("ICECAVE_6", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_7 = mkPLACE("ICECAVE_7", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_8 = mkPLACE("ICECAVE_8", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_9 = mkPLACE("ICECAVE_9", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_10 = mkPLACE("ICECAVE_10", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_11 = mkPLACE("ICECAVE_11", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_12 = mkPLACE("ICECAVE_12", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_12A = mkPLACE("ICECAVE_12A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_13 = mkPLACE("ICECAVE_13", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_14 = mkPLACE("ICECAVE_14", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_15 = mkPLACE("ICECAVE_15", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_15A = mkPLACE("ICECAVE_15A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_16 = mkPLACE("ICECAVE_16", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_17 = mkPLACE("ICECAVE_17", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_18 = mkPLACE("ICECAVE_18", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_19 = mkPLACE("ICECAVE_19", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_20 = mkPLACE("ICECAVE_20", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_21 = mkPLACE("ICECAVE_21", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_22 = mkPLACE("ICECAVE_22", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_23 = mkPLACE("ICECAVE_23", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_24 = mkPLACE("ICECAVE_24", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_25 = mkPLACE("ICECAVE_25", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_26 = mkPLACE("ICECAVE_26", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_27 = mkPLACE("ICECAVE_27", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_28 = mkPLACE("ICECAVE_28", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_28A = mkPLACE("ICECAVE_28A", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_29 = mkPLACE("ICECAVE_29", [""">*< short ICECAVE.1""",
""">*< short ICECAVE.1""",
])
ICECAVE_30 = mkPLACE("ICECAVE_30", ["""You're in small, icy chamber.""",
"""You are in a small chamber melted out of the ice.  Glowing letters
in midair spell out the words \"This way out\".""",
])
BRINK_3 = mkPLACE("BRINK_3", ["""You're on eastern side of bottomless pit.""",
"""You are standing on the eastern side of a bottomless pit.  A narrow
ledge runs north towards a dimly-visible passage;  the ledge once
continued south of this point but has been shattered by falling rock.
A narrow crack in the rock leads northeast.""",
])
CRACK_1 = mkPLACE("CRACK_1", ["""You're in narrow, twisting crack.""",
"""You are following a narrow crack in the rock which enters from the
southwest, turns and twists somewhat, and exits to the southeast.""",
])
CRACK_2 = mkPLACE("CRACK_2", ["""You're at north end of tight passage.""",
"""You are standing at the northern end of a rather tight passage.  A
narrow crack in the rock leads west.""",
])
CRACK_3 = mkPLACE("CRACK_3", ["""You're at south end of tight passage.""",
"""You are at the southern end of a tight passage.  A hands-and-knees
crawl continues to the south.""",
])
CRACK_4 = mkPLACE("CRACK_4", ["""You're in very small chamber.""",
"""You are in a very small chamber.  A narrow crawl leads north.""",
])
ARCH_COR_1 = mkPLACE("ARCH_COR_1", ["""You're in coral passage.""",
"""You are in an arched coral passage which enters from the west, splits,
and continues on to the east over a smooth and damp-looking patch of
sand.  The fork in the passage once led to the south, but it is now
completely blocked by debris.""",
])
ARCH_COR_2 = mkPLACE("ARCH_COR_2", ["""You're at bend in arched coral corridor.""",
"""You are at a bend in an arched corral passage;  the passage enters
from the west over a patch of damp sand, turns, and continues north.""",
])
ARCH_FORK = mkPLACE("ARCH_FORK", ["""You're at fork in arched corral passage.""",
"""You are at a fork in a high, arched coral passage.  The main portion
of the passage enters from the south;  two smaller passages lead
east and north.  The smell of salt water is very strong here.""",
])
JONAH = mkPLACE("JONAH", ["""You're at entrance to the Jonah room.""",
"""You are standing at the entrance of the Jonah room, a cavernous
hall with high ribbed walls.  The hall extends far to the south;
a coral passage leads west.""",
])
IN_JONAH = mkPLACE("IN_JONAH", ["""You're at south end of the Jonah room.""",
"""You are at the south end of the Jonah room.  Ahead of you, the way
is barred by a large set of immense stalactites and stalagmites
which intermesh like clenched teeth.  Nothing except blackness is
visible between the stone formations.""",
])
FOURIER = mkPLACE("FOURIER", ["""You're in the Fourier passage.""",
"""You are in the Fourier passage.  This is a long and highly convoluted
passage composed of coral, which twists and turns like the path of
an earthworm tripping on LSD.  The passage here enters from the
northwest, convulses, and exits to the southwest (from which
direction can be felt a cool and salty-smelling breeze).""",
])
SHELF = mkPLACE("SHELF", ["""You're on shelf of rock above beach.""",
"""You are standing on a large shelf of sedementary rock overlooking
a lava beach.  The shelf is an extension of an incredible cliff
which extends north, south, and upwards for as far as the eye can
see.  Crudely carved steps lead down from the shelf to the beach, and
a twisting coral passage exits to the west.""",
])
BEACH = mkPLACE("BEACH", ["""You're on beach.""",
"""You are standing on a short, barren beach composed of hardened lava.
Rugged and unclimbable volcanic hills block all view to the north
and south, and a seemingly infinite cliff fills the entire western
hemisphere.  To the east, a narrow inlet of ocean water laps gently
upon the beach.  The scene is illuminated by the light of three small
moons shining through the shimmering glow of an aurora that fills
the entire sky with golden splendor.  Steps lead up the cliff to a
shelf of rock.""",
])
PLATFORM = mkPLACE("PLATFORM", ["""You're on tiny platform above volcano.""",
"""You are precariously perched on a tiny platform suspended in midair.
Two thousand feet below you is the mouth of a very active volcano,
spewing out a river of hot lava.""",
])
LIMBO = mkPLACE("LIMBO", ["""You are in Limbo.""",
"""You are in Limbo (program bug!).  Say OUT to get out of here.""",
])
YLEM = mkPLACE("YLEM", ["""You are in Ylem.""",
"""You are in Ylem (circular file for objects).""",
])
GRATE = mkOBJECT("GRATE", [""">$< Grate""",
"""The grate is locked.""",
"""The grate is open.""",
])
STEPS = mkOBJECT("STEPS", [""">$< Steps""",
])
DOOR = mkOBJECT("DOOR", [""">$< Rusty door""",
"""The way north is barred by a massive, rusty, iron door.""",
"""The way north leads through a massive, rusty, iron door.""",
])
SNAKE = mkOBJECT("SNAKE", [""">$< Snake""",
"""A huge green fierce snake bars the way!""",
""">$< (chased away)""",
])
FISSURE = mkOBJECT("FISSURE", [""">$< Fissure""",
""">$<""",
"""A crystalline bridge now spans the fissure.""",
"""The crystalline bridge has vanished!""",
])
TABLET = mkOBJECT("TABLET", [""">$< Stone tablet""",
"""A massive stone tablet imbedded in the wall reads:
\"Congratulations on bringing light into the Dark room!\"""",
])
MIRROR = mkOBJECT("MIRROR", [""">$< Mirror""",
""">$<""",
])
PLANT = mkOBJECT("PLANT", [""">$< Plant""",
"""There is a tiny little plant in the pit, murmuring \"Water, water, ...\"""",
"""The plant spurts into furious growth for a few seconds.""",
"""There is a 12-foot-tall beanstalk stretching up out of the pit,
bellowing \"WATER!! WATER!!\"""",
"""The plant grows explosively, almost filling the bottom of the pit.""",
"""There is a gigantic beanstalk stretching all the way up to the hole.""",
"""You've over-watered the plant! It's shriveling up! It's, it's...""",
])
PLANT2 = mkOBJECT("PLANT2", [""">$< Phony plant (seen in Twopit room only when tall enough)""",
""">$< (not grown yet - invisible from above)""",
""">$< (transition - growing)""",
"""The top of a 12-foot-tall beanstalk is poking out of the west pit.""",
""">$< (growing still more)""",
"""There is a huge beanstalk growing out of the west pit up to the hole.""",
])
STALACTITE = mkOBJECT("STALACTITE", [""">$< Stalactite""",
""">$<""",
])
FOG = mkOBJECT("FOG", [""">$< Fog in the fog-filled room (where else?)""",
"""You are standing, badly befuddled, in a pale purple fog.""",
"""You are wandering around in the middle of a bright red fog.""",
"""You are lost in the midst of a thick, pea-green fog.""",
"""You are trying to find your way through a dense coal-black fog.""",
"""You are lost in the heart of a strange yellow fog.""",
"""You are standing, badly bedazzled, in a day-glow orange fog.""",
"""You are hunting your way through a shimmering magenta fog.""",
"""You are somewhere in the center of a weird, pearly pink fog.""",
])
GLOW = mkOBJECT("GLOW", [""">$< Glow of light in the midst of the fog""",
"""A faint glow of light is visible through the fog to the east.""",
"""A glimmer of light is visible through the fog in the west.""",
"""A glow of light is visible through the fog to the north.""",
"""A faint shimmer of light is visible to the south.""",
"""A flickering light is visible through the fog in the northeast.""",
"""A dim light is visible in the southeast.""",
"""A dim glow of light is visible in the southwest.""",
"""A dim flickering light is visible through the fog in the northwest.""",
])
SHADOW = mkOBJECT("SHADOW", [""">$< Shadowy figure""",
"""The shadowy figure seems to be trying to attract your attention.""",
])
BLOB = mkOBJECT("BLOB", [""">$< The cave \"bouncer\"""",
""">$<                     0""",
""">$<                     1""",
"""
From somewhere in the distance comes an ominous bubbling sound.
""",
"""
The bubbling sound grows louder.
""",
"""
The bubbling sound ends with a loud >splash<.
""",
"""
A hollow, echoing >ROAR< sounds in the distance.
""",
""">$<                     6""",
"""
A strange throbbing sound can be heard in the distance.
""",
""">$<                     8""",
"""
The throbbing sound is growing louder.
""",
""">$<                     10""",
"""
The source of the throbbing sound is approaching quickly.  Another
hollow >ROAR< echoes through the cave.
""",
""">$<                     12""",
"""
There is a loud >ROAR< only a short distance away!!
""",
""">$<                     14""",
"""
Into view there bounces a horrible creature!!  Six feet across, it
resembles a large blob of translucent white jelly;  although it looks
massive, it is bouncing lightly up and down as though it were as light
as a feather.  It is emitting a constant throbbing sound, and it
>ROAR<s loudly as it sees you.
""",
"""There is an immense and unfriendly-looking blob in the room with you!""",
"""
The blob >ROAR<s triumphantly and bounces straight at you with amazing
speed, crushing you to the ground and cutting off your air supply
with its body.  You quickly suffocate.""",
])
DRAWING = mkOBJECT("DRAWING", [""">$< Cave drawings""",
""">$<""",
])
PIRATE = mkOBJECT("PIRATE", [""">$< Pirate""",
""">$<  He never stays to visit, but runs away.""",
])
DRAGON = mkOBJECT("DRAGON", [""">$< Dragon""",
"""A huge green fierce dragon bars the way!
The dragon is sprawled out on a Persian rug!!""",
"""Congratulations! You have just vanquished a dragon with your bare
hands!  (Unbelievable, isn't it?)""",
"""The body of a huge green dead dragon is lying off to one side.""",
"""The rotting carcass of a dead dragon is lying off to one side.""",
])
CHASM = mkOBJECT("CHASM", [""">$< Chasm""",
"""A rickety wooden bridge extends across the chasm, vanishing into the
mist.  A sign posted on the bridge reads, \"STOP! Pay troll!\"""",
"""The wreckage of a bridge (and a dead bear) can be seen at the bottom
of the chasm.""",
"""The charred remains of a wooden bridge can be seen at the bottom
of the chasm.""",
])
TROLL = mkOBJECT("TROLL", [""">$< Troll""",
"""A burly troll stands by the bridge and insists you throw him a
treasure before you may cross.""",
""">$< (paid off, haven't crossed bridge yet)""",
""">$< (paid off, crossed bridge - he'll be back!)""",
"""The troll steps out from beneath the bridge and blocks your way.""",
""">$< (chased away)""",
"""From beneath the bridge there sounds a muffled bellow of frustrated
avarice.  The troll stomps out, resumes his position by the end of
the bridge, and glowers fiercely in your direction.  \"Very funny,\"
you hear him mutter, \"but not very smart - you'll pay for that!\"""",
"""The troll nimbly steps to one side and grins nastily as the nest of
golden eggs flies past him and plummets into the chasm.  \"Fool me
once, shame on you;  fool me twice, shame on me!\" he sneers.  \"I want
something a touch more substantial this time!\"""",
])
TROLL2 = mkOBJECT("TROLL2", [""">$< Phony troll""",
"""The troll is nowhere to be seen.""",
])
OGRE = mkOBJECT("OGRE", [""">$< Ogre""",
"""There is a large, nasty-looking ogre blocking your path!""",
])
BASILISK = mkOBJECT("BASILISK", [""">$< Basilisk""",
"""There is a basilisk lying in the corridor to the north, snoring
quietly.""",
"""There is a basilisk lying in the corridor to the south.  It is
asleep, but is twitching and grumbling as if restless.""",
"""There is a petrified basilisk in the corridor to the north.""",
"""There is a petrified basilisk in the corridor to the south.""",
])
GONG = mkOBJECT("GONG", [""">$< Gong""",
"""There is a large brass gong fastened to the wall here.""",
])
DJINN = mkOBJECT("DJINN", [""">$< Djinn""",
"""There is a twelve-foot djinn standing in the center of the pentagram,
glowering at you.""",
])
TURTLE = mkOBJECT("TURTLE", [""">$< Turtle""",
"""Darwin the tortoise is swimming in the reservoir nearby.""",
])
MESSAGE = mkOBJECT("MESSAGE", [""">$< Message in second maze""",
"""There is a message scrawled in the dust in a flowery script, reading:
\"This is not the maze where the pirate leaves his treasure chest.\"""",
])
VOLCANO = mkOBJECT("VOLCANO", [""">$< Volcanic gorge""",
""">$<      Nothing happening yet""",
"""The earth begins to shudder violently, and smoke flows up from the
gorge beneath your feet.  With a violent >glop<, the volcano
belches out an immense blast of molten lava which flies into the
air above the gorge and suddenly solidifies into a fragile-looking arch
of wheat-colored stone that bridges the gorge.""",
"""There is a wheat-colored stone bridge arching over the gorge.""",
"""The earth shudders violently, and steam blasts upwards from the geyser.
The wheat-stone bridge cracks and splits, and the fragments fall into
the gorge.""",
])
STATUE = mkOBJECT("STATUE", [""">$< Statue of minotaur""",
""">$<  Solid wall""",
"""Dark tunnels lead northeast, north, and northwest.""",
])
QUICKSAND = mkOBJECT("QUICKSAND", [""">$< Quicksand - state 0 = soft, state 1 = hardened by rod.""",
])
SLIME = mkOBJECT("SLIME", [""">$< Slime""",
"""The passage to the south is swathed with sheets of evil-looking
green slime, which twitches and flows as if aware of your presence.""",
])
MACHINE = mkOBJECT("MACHINE", [""">$< Vending machine""",
"""There is a massive vending machine here. The instructions on it read:
\"Drop coins here to receive fresh batteries.\"""",
])
SAFE = mkOBJECT("SAFE", [""">$< Safe""",
"""A massive walk-in safe takes up one entire wall.  It is tightly
closed, and has no handle, lock, nor keyhole.""",
"""A massive walk-in safe takes up one entire wall.  Its door has been
swung open and blocks the exit passage.""",
"""A massive walk-in safe takes up one entire wall.  It is closed, and
there are signs of melting around the edges of its door.""",
])
THRONE = mkOBJECT("THRONE", [""">$< Throne in audience hall""",
])
SKELETON = mkOBJECT("SKELETON", [""">$< Skeleton""",
"""Resting on the throne (\"sitting\" isn't really the right word) is an
incredible skeleton.  It is fairly humanoid from the waist up (except
for its incredible size and four extra arms);  below that, it resembles
the body of a giant python, and is wrapped in and around the bars and
rods of the throne.  Clutched in one bony hand is a long sceptre,
ornately encrusted with sapphires!!""",
])
BEAR = mkOBJECT("BEAR", ["""""",
"""There is a ferocious cave bear eying you from the far end of the room!""",
"""There is a gentle cave bear sitting placidly in one corner.""",
"""There is a contented-looking bear wandering about nearby.""",
])
BATTERIES = mkOBJECT("BATTERIES", ["""Batteries""",
"""There are fresh batteries here.""",
"""Some worn-out batteries have been discarded nearby.""",
])
CARPET = mkOBJECT("CARPET", [""">$< Carpet and/or moss""",
""">$<""",
])
DINGHY = mkOBJECT("DINGHY", [""">$< Dingy""",
"""Lying upon the beach are the shattered remains of what must once have
been a dinghy.  The remains consist of little more than a few broken
boards, upon one of which may be seen a crude sketch of a skull and two
crossed thighbones (perhaps this dinghy was once owned by a cook?)""",
"""The shattered remains of a dinghy lie forlornly on the beach.""",
])
BAG = mkOBJECT("BAG", ["""Bag filled with pieces of eight""",
"""There is a bag (obviously filled with pieces of eight) in the dinghy!""",
"""There is a bag filled with pieces of eight lying off to one side!""",
])
CROWN = mkOBJECT("CROWN", ["""Crown""",
"""There is a massive crown made of solid iridium floating in midair!""",
"""There is a massive iridium crown here!""",
])
GOLD = mkOBJECT("GOLD", ["""Large gold nugget""",
"""There is a large sparkling nugget of gold here!""",
])
DIAMONDS = mkOBJECT("DIAMONDS", ["""Several diamonds""",
"""There are diamonds here!""",
])
SILVER = mkOBJECT("SILVER", ["""Bars of silver""",
"""There are bars of silver here!""",
])
JEWELRY = mkOBJECT("JEWELRY", ["""Precious jewelry""",
"""There is precious jewelry here!""",
])
COINS = mkOBJECT("COINS", ["""Rare coins""",
"""There are many coins here!""",
])
CHEST = mkOBJECT("CHEST", ["""Treasure chest""",
"""The pirate's treasure chest is here, half-hidden behind a rock!""",
"""The pirate's treasure chest is here!""",
])
EGGS = mkOBJECT("EGGS", ["""Golden eggs""",
"""There is a large nest here, full of golden eggs!""",
"""The nest of golden eggs has vanished!""",
"""Done!""",
])
TRIDENT = mkOBJECT("TRIDENT", ["""Jeweled trident""",
"""There is a jewel-encrusted trident here!""",
])
HELMET = mkOBJECT("HELMET", ["""Helmet""",
"""There is a gem-encrusted visorless helmet sitting on the floor!""",
])
VASE = mkOBJECT("VASE", ["""Ming vase""",
"""There is a delicate, precious, Ming vase here!""",
"""The vase is now resting, delicately, on a velvet pillow.""",
"""The Ming vase drops with a delicate crash.""",
])
POTTERY = mkOBJECT("POTTERY", ["""Worthless shards of pottery""",
"""The floor is covered with worthless shards of pottery.""",
])
EMERALD = mkOBJECT("EMERALD", ["""Egg-sized emerald""",
"""There is an emerald here the size of a plover's egg!""",
])
SCEPTRE = mkOBJECT("SCEPTRE", ["""Sapphire sceptre""",
""">$<  Sceptre's 0-mode description is part of \"SKELETON\"""",
"""A sapphire-encrusted sceptre is lying on the ground!""",
])
YACHT = mkOBJECT("YACHT", ["""Ruby-covered toy yacht""",
"""There is a small toy yacht sitting on the floor. It is totally
covered with rubies, and has the words \"Omar Khayyam\" engraved
on the side!!""",
"""The ruby yacht of Omar Khayyam is sitting on the floor!""",
])
PYRAMID = mkOBJECT("PYRAMID", ["""Platinum pyramid""",
"""There is a platinum pyramid here, 8 inches on a side!""",
])
PEARL = mkOBJECT("PEARL", ["""Glistening pearl""",
"""Off to one side lies a glistening pearl!""",
])
RUG = mkOBJECT("RUG", ["""Persian rug""",
"""There is a Persian rug spread out on the floor!""",
])
SPICES = mkOBJECT("SPICES", ["""Rare spices""",
"""There are rare spices here!""",
])
BEADS = mkOBJECT("BEADS", ["""Ancient Indian turquoise beads.""",
"""There is a string of ancient Indian turquoise beads draped casually
over the edge of the balcony!""",
"""There is a string of ancient Indian turquoise beads here!""",
])
CHAIN = mkOBJECT("CHAIN", ["""Golden chain""",
"""There is a golden chain lying in a heap on the floor!""",
"""The bear is locked to the wall with a golden chain!""",
"""There is a golden chain locked to the wall!""",
])
RING = mkOBJECT("RING", ["""Mithril ring""",
"""There is a shiny ring (crafted of the finest mithril) lying here!""",
])
SPYGLASS = mkOBJECT("SPYGLASS", ["""Scrimshaw spyglass""",
"""There is a small spyglass carved out of whale baleen sitting here!""",
])
SCULPTURE = mkOBJECT("SCULPTURE", ["""Rock-crystal sculpture""",
"""A finely-carved crystalline sculpture of a pig is resting in a niche
melted out of the icy wall of the tunnel!""",
"""There is a fine crystalline sculpture of a pig here!""",
"""There is a fine crystalline sculpture of an eel here!""",
"""There is a fine crystalline sculpture of an emu here!""",
"""There is a fine crystalline sculpture of an elf here!""",
"""There is a fine crystalline sculpture of a mouse here!""",
"""There is a fine crystalline sculpture of a rabbit here!""",
"""There is a fine crystalline sculpture of an ibex here!""",
"""There is a fine crystalline sculpture of a frog here!""",
"""There is a fine crystalline sculpture of a tiger here!""",
"""There is a fine crystalline sculpture of a mule here!""",
"""There is a fine crystalline sculpture of a moose here!""",
])
BRACELET = mkOBJECT("BRACELET", ["""Jade bracelet""",
"""There is an ancient Chinese jade bracelet here!""",
])
CASKET = mkOBJECT("CASKET", ["""Casket of opals""",
"""There is a casket full of rare black opals sitting on a shelf!""",
"""There is a casket full of rare black opals here!""",
])
KEYS = mkOBJECT("KEYS", ["""Set of keys""",
"""There are some keys on the ground here.""",
])
LAMP = mkOBJECT("LAMP", ["""Brass lantern""",
"""There is a shiny brass lamp nearby.""",
"""There is a lamp shining nearby.""",
])
CAGE = mkOBJECT("CAGE", ["""Wicker cage""",
"""There is a small wicker cage discarded nearby.""",
"""There is a small wicker cage nearby.""",
])
BIRD = mkOBJECT("BIRD", ["""Little bird in cage""",
"""A cheerful little bird is sitting here singing.""",
"""There is a little bird in the cage.""",
])
ROD = mkOBJECT("ROD", ["""Black rod""",
"""A three foot black rod with a rusty star on an end lies nearby.""",
])
PLATE = mkOBJECT("PLATE", ["""Metal plate""",
"""A highly polished metal plate is leaning against the wall.""",
"""A polished metal plate lies nearby.""",
])
DYNAMITE = mkOBJECT("DYNAMITE", ["""Black rod""",
"""A three foot black rod with a rusty mark on an end lies nearby.""",
])
PILLOW = mkOBJECT("PILLOW", ["""Velvet pillow""",
"""A small velvet pillow lies on the floor.""",
])
CLAM = mkOBJECT("CLAM", ["""Giant clam  >grunt!<""",
"""There is an enormous clam here with its shell tightly closed.""",
])
OYSTER = mkOBJECT("OYSTER", ["""Giant oyster  >groan!<""",
"""There is an enormous oyster here with its shell tightly closed.""",
"""Interesting. There seems to be something written on the underside of
the oyster.""",
])
MAGAZINES = mkOBJECT("MAGAZINES", ["""\"Spelunker Today\"""",
"""There are a few recent issues of \"Spelunker Today\" magazine here.""",
])
DWARF = mkOBJECT("DWARF", ["""""",
])
KNIFE = mkOBJECT("KNIFE", ["""""",
])
FOOD = mkOBJECT("FOOD", ["""Tasty food""",
"""There is food here.""",
])
BOTTLE = mkOBJECT("BOTTLE", ["""Small bottle""",
"""There is a bottle of water here.""",
"""There is an empty bottle here.""",
"""There is a bottle of oil here.""",
])
FLASK = mkOBJECT("FLASK", ["""Earthenware flask""",
"""There is a sealed earthenware flask sitting in the center of the
pentagram.""",
"""There is a small, tightly-sealed earthenware flask on the ground here.
It has the words, \"London Dry\" written on the side.""",
"""There is a small, empty earthenware flask here.""",
])
WATER = mkOBJECT("WATER", ["""Water in the bottle""",
])
OIL = mkOBJECT("OIL", ["""Oil in the bottle""",
])
AXE = mkOBJECT("AXE", ["""Dwarf's axe""",
"""There is a little axe here.""",
"""There is a little axe lying beside the bear.""",
])
SWORD = mkOBJECT("SWORD", ["""Singing sword""",
"""There is a sword here with its blade plunged deep into the block
of stone.  The sword is singing quietly to itself.""",
"""There is a magic sword here, chiming out the bell-like tones of
\"Khumbu Ice-fall\" by ringing its blade against the ground.""",
"""There is a sword here, singing \"A Day in the Life\" in a quiet,
introspective voice.""",
"""There is a magic sword here, singing \"Cold Blue Steel and Sweet
Fire\" to itself in a plaintive, hopeless voice.""",
"""There is a sharp and obviously magical sword here. It is
quietly humming excerpts from Prokofiev's \"Romeo and Juliet\"
ballet to itself.""",
"""There is a sword lying on the ground, jauntily whistling the
March from Tchaikovsky's \"Nutcracker Suite\".""",
"""There is a sharp sword lying here. It is (somehow) singing
Tchaikovsky's \"1812 Overture\" in twelve parts, by itself!""",
"""The stirring strains of Rossini's \"William Tell\" overture fill
the room, coming from a singing sword lying on the ground.""",
"""There is a singing sword lying on the ground. From it resound the
massed voices of a two-hundred-singer choir, filling the air with
the stirring sound of the Hallelujah Chorus from Handel's \"Messiah\".""",
"""There is a sharp and shiny sword here. It is somehow managing to
sing Harry Partch's \"Daphne of the Dunes\" without destroying its
singing organs (whatever they happen to be...)""",
"""There is a sword here, singing \"Witchi-Tai-To\" in two-part harmony
with itself.""",
"""There is a very strange singing sword here - it is glowing and
vibrating, and the eerie electronic notes of Charles Wuorinen's
\"Time's Encomium\" issue from its blade and fill the air.""",
])
TEETH = mkOBJECT("TEETH", ["""Several dragon's teeth""",
"""There are several dragon's teeth scattered haphazardly about.""",
"""There are several dragon's teeth in a pile on the floor.""",
])
VIAL = mkOBJECT("VIAL", ["""Vial of oily liquid""",
"""On the ground lies a small glass vial filled with an oily liquid.""",
"""The dwarf catches a lungful of the cloud, gags audibly and stumbles
out of the room retching, sneezing, and cursing up a storm.""",
"""The dwarves blanche in horror and dash away as fast as their brief
and misshapen legs can carry them.""",
"""The troll calmly waves the vapor away.""",
"""The bear inhales some of the vapor and snarls angrily.""",
"""The bear inhales some of the vapor and moans appreciatively.""",
"""The snake completely ignores the vapor.""",
"""The bird breathes in a miniscule amount of the vapor and immediately
sings a twenty-second segment of Morton Subotnik's \"Sidewinder\".""",
"""The slime filling the passage to the south blackens and shrivels
away into nothingness.""",
"""The dragon sniffs the air, rumbles deep in his chest, and shoots out
a small puff of flame that ignites and incinerates the vapor.""",
"""The djinn takes a deep sniff of the vapor and comments, \"AH!  A TRUELY
FINE ARABIAN PERFUME!  I HAVEN'T SMELLED ANYTHING LIKE THAT FOR YEARS!\"""",
"""The basilisk doesn't wake up.""",
"""The gooseberry goblins sniff the vapor, screech in terror, and dash off
into the distance.""",
])
MUSHROOM = mkOBJECT("MUSHROOM", ["""Mushroom""",
"""There is a small mushroom growing on the wall.""",
"""There is a small mushroom lying on the floor.""",
"""As you swallow the mushroom your mouth becomes numb, and everything
seems to swirl around you.  The effect quickly passes, and you find
that your muscles have bulged unbelievably.""",
"""
A strange malaise suddenly afflicts you.  You shiver with chill,
and your muscles seem to turn to putty;  everything around you becomes
grey and unreal.  The fit quickly passes, and you find that your body
has degenerated back to what it was like before you ate the mushroom.
""",
])
GOBLINS = mkOBJECT("GOBLINS", [""">$< Gooseberry goblins""",
"""
Suddenly and without warning, there appears from within the very
cave walls around you a horde of vicious little goblins!  Each one
stands about eight inches high on a pair of spindly black legs, has
a globular, spine-covered body resembling a giant gooseberry, a
wide mouth filled with sharp teeth, and a pair of glittering little
green eyes!  They swarm around you and try to block your way.
""",
"""You are surrounded by a horde of silent little gooseberry goblins!""",
"""
One of the gooseberry goblins begins to giggle in a high-pitched
voice.  Another takes up the giggling, then another....  soon all
of them are giggling insanely and jumping up and down with glee!
""",
"""You are surrounded by a giggling horde of little gooseberry goblins!""",
"""
The goblins are jumping up and down frantically, and are working
themselves into a real slavering frenzy!!
""",
"""You are surrounded by a slavering horde of gooseberry goblins!""",
"""
With a shrill cry, the gooseberry goblins hurl themselves upon you,
tickling you mercilessly.  You crush and hurl away several of them,
but are soon borne down to the ground by the endless attack.  The
goblins then gleefully rip out your throat, and you sink into
unconsciousness.""",
])
mkSYNON(KEYS, ['KEY', 'SET'])
KEY = KEYS
SET = KEYS
mkSYNON(LAMP, ['HEADLAMP', 'LANTERN'])
HEADLAMP = LAMP
LANTERN = LAMP
mkSYNON(PILLOW, ['VELVET'])
VELVET = PILLOW
mkSYNON(MAGAZINES, ['ISSUES', 'SPELUNKER'])
ISSUES = MAGAZINES
SPELUNKER = MAGAZINES
mkSYNON(DWARF, ['DWARVES'])
DWARVES = DWARF
mkSYNON(KNIFE, ['KNIVES'])
KNIVES = KNIFE
mkSYNON(FOOD, ['RATIONS'])
RATIONS = FOOD
mkSYNON(BOTTLE, ['JAR'])
JAR = BOTTLE
mkSYNON(WATER, ['H2O'])
H2O = WATER
mkSYNON(PLANT, ['BEANSTALK'])
BEANSTALK = PLANT
mkSYNON(SHADOW, ['FIGURE'])
FIGURE = SHADOW
mkSYNON(VOLCANO, ['GEYSER', 'GORGE'])
GEYSER = VOLCANO
GORGE = VOLCANO
mkSYNON(MACHINE, ['VENDING'])
VENDING = MACHINE
mkSYNON(CARPET, ['MOSS', 'CURTAINS'])
MOSS = CARPET
CURTAINS = CARPET
mkSYNON(GOLD, ['NUGGET'])
NUGGET = GOLD
mkSYNON(SILVER, ['BARS'])
BARS = SILVER
mkSYNON(CHEST, ['BOX', 'TREASURE'])
BOX = CHEST
TREASURE = CHEST
mkSYNON(EGGS, ['EGG', 'NEST'])
EGG = EGGS
NEST = EGGS
mkSYNON(VASE, ['MING'])
MING = VASE
mkSYNON(POTTERY, ['SHARDS'])
SHARDS = POTTERY
mkSYNON(PYRAMID, ['PLATINUM'])
PLATINUM = PYRAMID
mkSYNON(RUG, ['PERSIAN'])
PERSIAN = RUG
mkSYNON(CAGE, ['WICKER'])
WICKER = CAGE
mkSYNON(JEWELRY, ['JEWELS'])
JEWELS = JEWELRY
mkSYNON(CASKET, ['OPALS'])
OPALS = CASKET
mkSYNON(BRACELET, ['JADE'])
JADE = BRACELET
mkSYNON(SCULPTURE, ['CRYSTAL'])
CRYSTAL = SCULPTURE
mkSYNON(RING, ['MITHRIL'])
MITHRIL = RING
mkSYNON(SPYGLASS, ['SCRIMSHAW'])
SCRIMSHAW = SPYGLASS
mkSYNON(BAG, ['PIECES', 'EIGHT'])
PIECES = BAG
EIGHT = BAG
mkSYNON(VIAL, ['PHIAL'])
PHIAL = VIAL
mkSYNON(STATUE, ['MINOTAUR'])
MINOTAUR = STATUE
mkSYNON(YACHT, ['RUBY', 'RUBAIYAT'])
RUBY = YACHT
RUBAIYAT = YACHT
mkSYNON(DJINN, ['DJANN', 'GENIE'])
DJANN = DJINN
GENIE = DJINN
mkSYNON(TURTLE, ['TORTOISE', 'DARWIN'])
TORTOISE = TURTLE
DARWIN = TURTLE
mkSYNON(BEADS, ['INDIAN', 'STRING', 'TURQUOISE'])
INDIAN = BEADS
STRING = BEADS
TURQUOISE = BEADS
SAY = mkVERB('SAY', ['CHANT', 'SING', 'UTTER', 'MUMBLE'])
CHANT = SAY
SING = SAY
UTTER = SAY
MUMBLE = SAY
SAVE = mkVERB('SAVE', ['SUSPEND', 'PAUSE'])
SUSPEND = SAVE
PAUSE = SAVE
RESTORE = mkVERB('RESTORE', [])
UPSTREAM = mkVERB('UPSTREAM', [])
DOWNSTREAM = mkVERB('DOWNSTREAM', [])
FORWARD = mkVERB('FORWARD', ['CONTINUE', 'ONWARD'])
CONTINUE = FORWARD
ONWARD = FORWARD
BACK = mkVERB('BACK', ['RETURN', 'RETREAT'])
RETURN = BACK
RETREAT = BACK
OUT = mkVERB('OUT', ['OUTSIDE', 'EXIT', 'LEAVE'])
OUTSIDE = OUT
EXIT = OUT
LEAVE = OUT
ENTRANCE = mkVERB('ENTRANCE', [])
GULLY = mkVERB('GULLY', [])
STREAM = mkVERB('STREAM', [])
ROCK = mkVERB('ROCK', ['ROCKS'])
ROCKS = ROCK
BED = mkVERB('BED', ['STREAMBED'])
STREAMBED = BED
CRAWL = mkVERB('CRAWL', ['CRAWLS'])
CRAWLS = CRAWL
IN = mkVERB('IN', ['INWARD', 'INSIDE', 'ENTER'])
INWARD = IN
INSIDE = IN
ENTER = IN
SURFACE = mkVERB('SURFACE', [])
NULL = mkVERB('NULL', ['NOWHERE'])
NOWHERE = NULL
PASSAGE = mkVERB('PASSAGE', ['TUNNEL'])
TUNNEL = PASSAGE
VIEW = mkVERB('VIEW', [])
HOLE = mkVERB('HOLE', [])
STAIRS = mkVERB('STAIRS', [])
UP = mkVERB('UP', ['UPWARD', 'U', 'ABOVE', 'ASCEND'])
UPWARD = UP
U = UP
ABOVE = UP
ASCEND = UP
DOWN = mkVERB('DOWN', ['D', 'DOWNWARDS', 'DESCEND'])
D = DOWN
DOWNWARDS = DOWN
DESCEND = DOWN
OUTDOORS = mkVERB('OUTDOORS', [])
CRACK = mkVERB('CRACK', [])
DOME = mkVERB('DOME', [])
LEFT = mkVERB('LEFT', [])
RIGHT = mkVERB('RIGHT', [])
HALL = mkVERB('HALL', [])
JUMP = mkVERB('JUMP', [])
CROSS = mkVERB('CROSS', ['ACROSS', 'OVER'])
ACROSS = CROSS
OVER = CROSS
EAST = mkVERB('EAST', ['E'])
E = EAST
WEST = mkVERB('WEST', ['W'])
W = WEST
NORTH = mkVERB('NORTH', ['N'])
N = NORTH
SOUTH = mkVERB('SOUTH', ['S'])
S = SOUTH
NE = mkVERB('NE', ['NORTHEAST'])
NORTHEAST = NE
SE = mkVERB('SE', ['SOUTHEAST'])
SOUTHEAST = SE
SW = mkVERB('SW', ['SOUTHWEST'])
SOUTHWEST = SW
NW = mkVERB('NW', ['NORTHWEST'])
NORTHWEST = NW
SECRET = mkVERB('SECRET', [])
CLIMB = mkVERB('CLIMB', [])
LOOK = mkVERB('LOOK', ['EXAMINE', 'TOUCH', 'DESCRIBE'])
EXAMINE = LOOK
TOUCH = LOOK
DESCRIBE = LOOK
GET = mkVERB('GET', ['CARRY', 'TAKE', 'KEEP', 'CATCH', 'STEAL', 'CAPTURE', 'TOTE'])
CARRY = GET
TAKE = GET
KEEP = GET
CATCH = GET
STEAL = GET
CAPTURE = GET
TOTE = GET
DROP = mkVERB('DROP', ['RELEASE', 'FREE', 'DISCARD', 'DUMP'])
RELEASE = DROP
FREE = DROP
DISCARD = DROP
DUMP = DROP
OPEN = mkVERB('OPEN', ['UNLOCK'])
UNLOCK = OPEN
CLOSE = mkVERB('CLOSE', ['LOCK'])
LOCK = CLOSE
ON = mkVERB('ON', ['LIGHT'])
LIGHT = ON
OFF = mkVERB('OFF', ['EXTINGUISH'])
EXTINGUISH = OFF
WAVE = mkVERB('WAVE', ['SHAKE', 'SWING'])
SHAKE = WAVE
SWING = WAVE
PLACATE = mkVERB('PLACATE', ['CALM', 'TAME'])
CALM = PLACATE
TAME = PLACATE
WALK = mkVERB('WALK', ['RUN', 'TRAVEL', 'GO', 'PROCEED', 'EXPLORE', 'GOTO', 'FOLLOW', 'TURN'])
RUN = WALK
TRAVEL = WALK
GO = WALK
PROCEED = WALK
EXPLORE = WALK
GOTO = WALK
FOLLOW = WALK
TURN = WALK
KILL = mkVERB('KILL', ['ATTACK', 'FIGHT', 'HIT', 'STRIKE', 'SLAY'])
ATTACK = KILL
FIGHT = KILL
HIT = KILL
STRIKE = KILL
SLAY = KILL
POUR = mkVERB('POUR', [])
EAT = mkVERB('EAT', ['DEVOUR'])
DEVOUR = EAT
DRINK = mkVERB('DRINK', [])
RUB = mkVERB('RUB', [])
THROW = mkVERB('THROW', ['TOSS'])
TOSS = THROW
QUIT = mkVERB('QUIT', ['STOP', 'Q'])
STOP = QUIT
Q = QUIT
FIND = mkVERB('FIND', ['WHERE'])
WHERE = FIND
INVENTORY = mkVERB('INVENTORY', [])
FEED = mkVERB('FEED', [])
FILL = mkVERB('FILL', [])
SCORE = mkVERB('SCORE', [])
BRIEF = mkVERB('BRIEF', [])
READ = mkVERB('READ', ['PERUSE'])
PERUSE = READ
BREAK = mkVERB('BREAK', ['SHATTER', 'SMASH'])
SHATTER = BREAK
SMASH = BREAK
RIDE = mkVERB('RIDE', [])
HOURS = mkVERB('HOURS', [])
FUM = mkVERB('FUM', [])
SESAME = mkVERB('SESAME', ['OPENSESAME', 'ABRA', 'ABRACADABRA', 'SHAZAM', 'HOCUS', 'POCUS', 'CADABRA'])
OPENSESAME = SESAME
ABRA = SESAME
ABRACADABRA = SESAME
SHAZAM = SESAME
HOCUS = SESAME
POCUS = SESAME
CADABRA = SESAME
HELP = mkVERB('HELP', ['_'])
_ = HELP
TREE = mkVERB('TREE', ['TREES'])
TREES = TREE
DIG = mkVERB('DIG', ['EXCAVATE'])
EXCAVATE = DIG
LOST = mkVERB('LOST', [])
MIST = mkVERB('MIST', [])
INFO = mkVERB('INFO', ['INFORMATION'])
INFORMATION = INFO
SWIM = mkVERB('SWIM', [])
LPSD = mkVERB('LPSD', [])
FAST = mkVERB('FAST', [])
FULL = mkVERB('FULL', [])
NEWS = mkVERB('NEWS', [])
CAVE = mkVERB('CAVE', [])
FIX = mkVERB('FIX', ['REPAIR'])
REPAIR = FIX
WIZARD = mkVERB('WIZARD', [])
ZORTON = mkVERB('ZORTON', [])
XYZZY = mkVERB('XYZZY', [])
THURB = mkVERB('THURB', [])
SNOEZE = mkVERB('SNOEZE', [])
SAMOHT = mkVERB('SAMOHT', [])
PLUGH = mkVERB('PLUGH', [])
PHUGGG = mkVERB('PHUGGG', [])
NOSIDE = mkVERB('NOSIDE', [])
MELENKURION = mkVERB('MELENKURION', [])
KNERL = mkVERB('KNERL', [])
KLAETU = mkVERB('KLAETU', [])
FOO = mkVERB('FOO', [])
FOE = mkVERB('FOE', [])
FIE = mkVERB('FIE', [])
FEE = mkVERB('FEE', [])
BLERBI = mkVERB('BLERBI', [])
SOK_ = mkTEXT("""""",
)
BLANK = mkTEXT("""""",
)
OK_ = mkTEXT("""""",
)
LOGON = mkTEXT("""Welcome to the *new* UNIX Adventure!  Say \"NEWS\" to get up-to-date
game details.
""",
)
NEWSDATA = mkTEXT("""
This is the brand-spanking-new version of UNIX Adventure.
The cave is essentially stable at this point except for bug
fixes being done as needed.  The cave is almost twice as big as
before, and has lots of new creatures in it - have fun!

Please contact the local game guru if anything weird happens (that
is, anything weird that looks like it shouldn't happen).  In
particular, if you ever see the message \"Glitch!\", please save
the printout for error analysis if that's possible. Credit goes
to David Platt for the design and development of this new version
of Adventure for the Xerox SIGMA-9 and other Honeywell systems.
Ken Wellsch designed and wrote the C version for running on UNIX
systems which uses the original database.
""",
)
INTRO = mkTEXT("""Somewhere nearby is Colossal Cave, where others have found fortunes in
treasure and gold, though it is rumored that some who enter are never
seen again.  Magic is said to work in the cave.  I will be your eyes
and hands.  Direct me with commands of 1 or 2 words.  I should warn
you that I look at only the first six letters of each word.
(Should you get stuck, type \"HELP\" for some general hints.  For infor-
mation on how to end your adventure, etc., type \"INFO\".)
- - -
If you have any problems, please contact the local game guru.
""",
)
DWARFBLOCK = mkTEXT("""A little dwarf with a big knife blocks your way.""",
)
FIRSTDWARF = mkTEXT("""
A little dwarf just walked around a corner, saw you, threw a little
axe at you which missed, cursed, and ran away.""",
)
DWARFHERE = mkTEXT("""
There is a threatening little dwarf in the room with you!""",
)
DWARVESHERE = mkTEXT("""
There are # threatening little dwarves in the room with you!""",
)
KNIFETHROWN = mkTEXT("""One sharp nasty knife is thrown at you!""",
)
KNIVESTHROWN = mkTEXT("""# nasty sharp knives are thrown at you!""",
)
KNIVESMISS = mkTEXT("""None of them hit you!""",
)
KNIFEGOTYOU = mkTEXT("""One of them gets you!""",
)
SAYSPLUGH = mkTEXT("""A hollow voice says \"Plugh\".""",
)
NOCANGO = mkTEXT("""There is no way to go that direction.""",
)
OOF_ = mkTEXT("""You have run into a wall of rock and can go no further in this
direction.""",
)
IAMUNSURE = mkTEXT("""I am unsure how you are facing.  Use compass points or nearby objects.""",
)
INFROMOUT = mkTEXT("""I don't know in from out here.  Use compass points or name something
in the general direction you want to go.""",
)
CANTAPPLY = mkTEXT("""I don't know how to apply that word here.""",
)
HUH__ = mkTEXT("""I don't understand that!""",
)
IAMGAME = mkTEXT("""I'm game.  Would you care to explain how?""",
)
NOCANLOOK = mkTEXT("""Sorry, but I am not allowed to give more detail.  I will repeat the
long description of your location.""",
)
ITISNOWDARK = mkTEXT("""It is now pitch dark.  If you proceed you will likely fall into a pit.""",
)
WMEANSWEST = mkTEXT("""If you prefer, simply type W rather than WEST.""",
)
BIRDHINT_ = mkTEXT("""Are you trying to catch the bird?""",
)
mkTEXT("""The bird is frightened right now and you cannot catch it no matter
what you try.  Perhaps you might try later.""",
)
GETPASTSNAKE = mkTEXT("""Are you trying to somehow deal with the snake?""",
)
mkTEXT("""You can't kill the snake, or drive it away, or avoid it, or anything
like that.  There is a way to get by, but you don't have the necessary
resources right now.""",
)
WANTTOQUIT = mkTEXT("""Do you really want to quit now?""",
)
CRUNCH = mkTEXT("""You fell into a pit and broke every bone in your body!""",
)
YOUHAVEIT = mkTEXT("""You are already carrying it!""",
)
BESERIOUS = mkTEXT("""You can't be serious!""",
)
BIRDISSCARED = mkTEXT("""The bird was unafraid when you entered, but as you approach it becomes
disturbed and you cannot catch it.""",
)
NEEDCAGE = mkTEXT("""You might be able to catch the bird, but you could not carry it.""",
)
NOTCARRYING = mkTEXT("""You aren't carrying it!""",
)
IDONTSEE = mkTEXT("""I see no # here.""",
)
BIRD__SNAKE = mkTEXT("""The little bird attacks the green snake, and in an astounding flurry
drives the snake away.""",
)
NEEDKEYS = mkTEXT("""You have no keys!""",
)
NOLOCK = mkTEXT("""It has no lock.""",
)
CANTLOCKIT = mkTEXT("""I don't know how to lock or unlock such a thing.""",
)
ITWASLOCKED = mkTEXT("""It was already locked.""",
)
GRATELOCKED = mkTEXT("""The grate is now locked.""",
)
GRATEUNLOCKED = mkTEXT("""The grate is now unlocked.""",
)
GRATE_STUCK = mkTEXT("""The lock seems to be stuck - the key refuses to turn!""",
)
WASUNLOCKED = mkTEXT("""It was already unlocked.""",
)
NOLIGHTHERE = mkTEXT("""You have no source of light.""",
)
LAMPNOWON = mkTEXT("""Your lamp is now on.""",
)
LAMPNOWOFF = mkTEXT("""Your lamp is now off.""",
)
BEAR__CHAIN = mkTEXT("""There is no way to get past the bear to unlock the chain, which is
probably just as well.""",
)
NOTHING = mkTEXT("""Nothing happens.""",
)
WHERE_ = mkTEXT("""Where?""",
)
PACIFIST = mkTEXT("""There is nothing here to attack.""",
)
BIRDISDEAD = mkTEXT("""The little bird is now dead.  Its body disappears.""",
)
CANTKILLSNAKE = mkTEXT("""Attacking the snake both doesn't work and is very dangerous.""",
)
KILLEDDWARF = mkTEXT("""You killed a little dwarf.""",
)
DWARFDODGES = mkTEXT("""You attack a little dwarf, but he dodges out of the way.""",
)
DWARFSTABS = mkTEXT("""You attack a little dwarf, but he dodges out of the way and stabs
you with his nasty sharp knife!""",
)
WITHWHAT_ = mkTEXT("""With your bare hands??""",
)
MAGICKWORD = mkTEXT("""Good try, but that is an old worn-out magic word.""",
)
HELPDATA = mkTEXT("""
I know of places, actions, and things.  Most of my vocabulary
describes places and is used to move you there.  To move, try words
like FOREST, BUILDING, DOWNSTREAM, ENTER, EAST, WEST, NORTH, SOUTH,
UP, or DOWN.  I know about a few special objects, like a black rod
hidden in the cave.  These objects can be manipulated using some of
the action words that I know.  Usually you will need to give both the
object and action words (in either order), but sometimes I can infer
the object from the verb alone.  Some objects also imply verbs; in
particular, \"INVENTORY\" implies \"TAKE INVENTORY\", which causes me to
give you a list of what you're carrying.  The objects have side
effects; for instance, the rod scares the bird.  Usually people having
trouble moving just need to try a few more words.  Usually people
trying unsuccessfully to manipulate an object are attempting something
beyond their (or my!) capabilities and should try a completely
different tack.  To speed the game you can sometimes move long
distances with a single word.  For example, \"BUILDING\" usually gets
you to the building from anywhere above ground except when lost in the
forest.  Also, note that cave passages turn a lot, and that leaving a
room to the north does not guarantee entering the next from the south.
Good luck!
""",
)
MISSES = mkTEXT("""It misses!""",
)
GETSYOU = mkTEXT("""It gets you!""",
)
UNLOCKKEYS = mkTEXT("""You can't unlock the keys.""",
)
YOUDIDNTMOVE = mkTEXT("""You have crawled around in some little holes and wound up back in the
main passage.""",
)
WHEREISCAVE = mkTEXT("""I don't know where the cave is, but hereabouts no stream can run on
the surface for long.  I would try the stream.""",
)
NEEDDETAIL = mkTEXT("""I need more detailed instructions to do that.""",
)
CANTFIND = mkTEXT("""I can only tell you what you see as you move about and manipulate
things.  I cannot tell you where remote things or places are.""",
)
NOCOMPRENDE = mkTEXT("""I don't know the word \"#\".""",
)
WHAT_ = mkTEXT("""Huh??""",
)
LOOKINGCAVE = mkTEXT("""Are you trying to get into the cave?""",
)
GRATENEEDSKEYS = mkTEXT("""The grate is very solid and has a hardened steel lock.  You cannot
enter without a key, and there are no keys nearby.  I would recommend
looking elsewhere for the keys.""",
)
INFOREST = mkTEXT("""The trees of the forest are large hardwood oak and maple, with an
occasional grove of pine or spruce.  There is quite a bit of under-
growth, largely birch and ash saplings plus nondescript bushes of
various sorts.  This time of year visibility is quite restricted by
all the leaves, but travel is quite easy if you detour around the
spruce and berry bushes.""",
)
NO_TREES_HERE = mkTEXT("""I can't see any trees around here.""",
)
HITHERE = mkTEXT("""Would you like instructions?""",
)
NEEDSHOVEL = mkTEXT("""Digging without a shovel is quite impractical.  Even with a shovel
progress is unlikely.""",
)
NEEDDYNAMITE = mkTEXT("""Blasting requires dynamite.""",
)
IMCONFUSED = mkTEXT("""I'm as confused as you are.""",
)
THISISMIST = mkTEXT("""Mist is a white vapor, usually water, seen from time to time in
caverns.  It can be found anywhere but is frequently a sign of a deep
pit leading down to water.""",
)
FEETAREWET = mkTEXT("""Your feet are now wet.""",
)
BLEAH = mkTEXT("""Yeetttch!  I think I just lost my appetite.""",
)
URRP = mkTEXT("""Thank you, it was delicious!""",
)
SLURP = mkTEXT("""You have taken a drink from the stream.  The water tastes strongly of
minerals, but is not unpleasant.  It is extremely cold.""",
)
SALT_H20_BAD = mkTEXT("""I'm afraid that all that's available here is salt water, which
isn't good for anything much... you'de better try elsewhere.""",
)
WATERGONE = mkTEXT("""The bottle of water is now empty.
You convulse and fall to the ground, screaming and writhing in pain.""",
)
RUBLAMP = mkTEXT("""Rubbing the electric # is not particularly rewarding.  Anyway,
nothing exciting happens.""",
)
PECULIAR = mkTEXT("""Peculiar.  Nothing unexpected happens.""",
)
REPULSIVE = mkTEXT("""That's a repulsive idea!""",
)
POURWATER = mkTEXT("""Your bottle is empty and the ground is wet.""",
)
CANTPOUR = mkTEXT("""You can't pour that.""",
)
WATCHIT = mkTEXT("""Watch it!""",
)
WHICHWAY = mkTEXT("""Which way should I #?""",
)
YOUAREDEAD = mkTEXT("""Oh dear, you seem to have gotten yourself killed.  I might be able to
help you out, but I've never really done this before.  Do you want me
to try to reincarnate you?""",
)
mkTEXT("""All right.  But don't blame me if something goes wr......
--- poof!! ---
You are engulfed in a cloud of orange smoke.  Coughing and gasping,
you emerge from the smoke and find....""",
)
mkTEXT("""Tsk, tsk - you did it again!  Remember - you're only human, and you
don't have as many lives as a cat!  (at least, I don't think so...)
That's twice you've ended up dead - want to try for three?""",
)
mkTEXT("""As you wish.  Hang on for just a second while I fire up my thurible...
>foof!<    An immense cloud of orange smoke fills the air.  As it
clears, you find that once again....""",
)
mkTEXT("""You clumsy oaf, you've done it again!  I don't know how long I can
keep this up.  Do you want me to try reincarnating you again?""",
)
mkTEXT("""Okay, now where did I put my orange smoke?....  >poof!<
Everything disappears in a dense cloud of orange smoke.""",
)
mkTEXT("""Now you've really done it!  I'm out of orange smoke!  You don't expect
me to do a decent reincarnation without any orange smoke, do you?""",
)
mkTEXT("""Yes....  well, that's the kind of blinkered, Philistine pig-ignorance
that I've come to expect from you mortals.  You sit there on your
loathsome, spotty behind, squeezing blackheads and not caring a
thinker's damn about the struggling cave-sprite, you simpering,
whining, mouldy-faced heap of parrot droppings!  If you're so
smart, then you can just reincarnate yourself, because quite
frankly I'm as mad as hell and I'm not going to take this
anymore - I'm leaving!!!!
""",
)
SNIDELEY = mkTEXT("""""",
)
CANTGOBACK = mkTEXT("""Sorry, but I no longer seem to remember how it was you got here.""",
)
ARMSAREFULL = mkTEXT("""You can't carry anything more.  You'll have to drop something first.""",
)
CANTPASSLOCK = mkTEXT("""You can't go through a locked steel grate!""",
)
ITISHERENOW = mkTEXT("""I believe what you want is right here with you.""",
)
DONTFITSLIT = mkTEXT("""You don't fit through a two-inch slit!""",
)
TRYTHEBRIDGE = mkTEXT("""I respectfully suggest you go across the bridge instead of jumping.""",
)
NOWAYACROSS = mkTEXT("""There is no way across the fissure.""",
)
ARMSAREEMPTY = mkTEXT("""You're not carrying anything.""",
)
YOUNOWHAVE = mkTEXT("""You are currently holding the following:""",
)
BIRDSEED = mkTEXT("""It's not hungry (it's merely pinin' for the fjords).  Besides, you
have no bird seed.""",
)
SNAKE__BIRD = mkTEXT("""The snake has now devoured your bird.""",
)
SNAKEWONTEAT = mkTEXT("""There's nothing here it wants to eat (except perhaps you).""",
)
FED__DWARF = mkTEXT("""You fool, dwarves eat only coal!  Now you've made him *really* mad!!""",
)
NOWAYTOCARRY = mkTEXT("""You have nothing in which to carry it.""",
)
BOTTLEWASFULL = mkTEXT("""Your bottle is already full.""",
)
NOTHING2FILL = mkTEXT("""There is nothing here with which to fill the bottle.""",
)
BOTTLE__H20 = mkTEXT("""Your bottle is now full of water.""",
)
BOTTLE__OIL = mkTEXT("""Your bottle is now full of oil.""",
)
CANTFILLTHAT = mkTEXT("""You can't fill that.""",
)
HAH_ = mkTEXT("""Don't be ridiculous!""",
)
DOORNEEDSOIL = mkTEXT("""The door is extremely rusty and refuses to open.""",
)
OIL__PLANT = mkTEXT("""The plant indignantly shakes the oil off its leaves and asks, \"Water?\"""",
)
HINGES__RUST = mkTEXT("""The hinges are quite thoroughly rusted now and won't budge.""",
)
OIL__DOOR = mkTEXT("""The oil has freed up the hinges so that the door will now move,
although it requires some effort.""",
)
GET__PLANT = mkTEXT("""The plant has exceptionally deep roots and cannot be pulled free.""",
)
NO__KNIVES = mkTEXT("""The dwarves' knives vanish as they strike the walls of the cave.""",
)
WONT__FIT = mkTEXT("""Something you're carrying won't fit through the tunnel with you.
You'd best take inventory and drop something.""",
)
CLAM_2_BIG = mkTEXT("""You can't fit this five-foot clam through that little passage!""",
)
OYSTER_2_BIG = mkTEXT("""You can't fit this five-foot oyster through that little passage!""",
)
DROP_THE_CLAM = mkTEXT("""I advise you to put down the clam before opening it.  >strain!<""",
)
DROP_THE_OYSTER = mkTEXT("""I advise you to put down the oyster before opening it.  >wrench!<""",
)
NEED_TRIDENT = mkTEXT("""You don't have anything strong enough to open the clam.""",
)
NEED_TRIDNT2 = mkTEXT("""You don't have anything strong enough to open the oyster.""",
)
CLAM__OPENED = mkTEXT("""A glistening pearl falls out of the clam and rolls away.  Goodness,
this must really be an oyster.  (I never was very good at identifying
bivalves.)  Whatever it is, it has now snapped shut again.""",
)
OYSTER__OPENED = mkTEXT("""The oyster creaks open, revealing nothing but oyster inside.  It
promptly snaps shut again.""",
)
CRAWL__CAVEIN = mkTEXT("""You have crawled around in some little holes and found your way
blocked by a recent cave-in.  You are now back in the main passage.""",
)
RUSTLING = mkTEXT("""There are faint rustling noises from the darkness behind you.""",
)
PIRATE__ZOTZ = mkTEXT("""
Out from the shadows behind you pounces a bearded pirate!  \"Har, har,\"
he chortles, \"I'll just take all this booty and hide it away with me
chest deep in the maze!\"  He snatches your treasure and vanishes into
the gloom.""",
)
CLOSING_NOW = mkTEXT("""
A sepulchral voice reverberating through the cave, says, \"Cave closing
soon.  All adventurers please report to the treasure room via the
alternate entrance to claim your treasure.\"
""",
)
GRATE_CLOSED = mkTEXT("""
A mysterious recorded voice groans into life and announces:
\"This exit is closed.  Please report to the treasure room via
the alternate entrance to claim your treasure.\"
""",
)
DEAD_CLOSED = mkTEXT("""
It looks as though you're dead.  Well, seeing as how it's so close to
closing time anyway, I think we'll just call it a day.""",
)
GO_REPOSIT = mkTEXT("""
The sepulchral voice entones, \"The cave is now closed.\"  As the echoes
fade, there is a blinding flash of light (and a small puff of orange
smoke). . . .    As your eyes refocus, you look around and find...
""",
)
LEAVE_BIRD = mkTEXT("""Oh, leave the poor unhappy bird alone.""",
)
HERESOMEWHERE = mkTEXT("""I daresay whatever you want is around here somewhere.""",
)
NO_CAN_GO = mkTEXT("""I don't know how to get there from here.""",
)
YOU_ARE_THERE = mkTEXT("""That's where you are now!""",
)
I_C_A_BEAR = mkTEXT("""You are being followed by a very large, tame bear.""",
)
INFO_2 = mkTEXT("""
If you want to end your adventure early, say \"QUIT\".
To suspend your adventure such that you can continue later, say
\"SUSPEND\" (or \"PAUSE\" or \"SAVE\").  To re-start your game at a later
time, start up a new adventure and after I say \"You are standing...\",
you must say \"RESTORE\".  You can also name your game by saying
\"SUSPEND mine\" (and \"RESTORE mine\") where \"mine\" is the name that
you wish your suspended game to be known by (1-4 characters).
To see what hours the cave is normally open, say \"HOURS\".
To see how well you're doing, say \"SCORE\".  To get full credit for a
treasure, you must have left it safely in the building, though you get
partial credit just for locating it.  You lose points for getting
killed, or for quitting, though the former costs you more.  There are
also points based on how much (if any) of the cave you've managed to
explore; in particular, there is a large bonus just for getting in (to
distinguish the beginners from the rest of the pack), and there are
other ways to determine whether you've been through some of the more
harrowing sections.  If you think you've found all the treasures, just
keep exploring for a while.  If nothing interesting happens, you
haven't found them all yet.  If something interesting *does* happen,
it means you're getting a bonus and have an opportunity to garner many
more points in the master's section.  I may occasionally offer hints
if you seem to be having trouble.  If I do, I'll warn you in advance
how much it will affect your score.  To save paper, you may specify
\"BRIEF\", which tells me never to repeat the full description of a
place unless you explicitly ask me to by saying \"LOOK\".  If you
are an experienced adventurer, you may wish to specify \"FAST\", which
is like \"BRIEF\" but more so;  in \"FAST\" mode I will *never* under
any circumstances give the full description of a place.  Finally, if
you are in \"BRIEF\" or \"FAST\" modes, you may return to the normal mode
of operation by saying \"FULL\".
""",
)
QUIT_NOW_ = mkTEXT("""Do you indeed wish to quit now?""",
)
NOTHING_VASE = mkTEXT("""There is nothing here with which to fill the vase.""",
)
SHATTER_VASE = mkTEXT("""The sudden change in temperature has delicately shattered the vase.""",
)
NO_CAN_FIX = mkTEXT("""It is beyond your power to do that.""",
)
DUNNO_HOW = mkTEXT("""I don't know how.""",
)
TOO_FAR_UP = mkTEXT("""It is too far up for you to reach.""",
)
DWARF_POOF = mkTEXT("""You killed a little dwarf.  The body vanishes in a cloud of greasy
black smoke.""",
)
KILL_OYSTER = mkTEXT("""The shell is very strong and is impervious to attack.""",
)
START_OVER = mkTEXT("""What's the matter, can't you read?  Now you'd best start over.""",
)
KILL_DRAGON = mkTEXT("""The # bounces harmlessly off the dragon's thick scales.""",
)
PAST_DRAGON = mkTEXT("""The dragon looks rather nasty.  You'd best not try to get by.""",
)
BIRD__DRAGON = mkTEXT("""The little bird attacks the green dragon, and in an astounding flurry
gets burnt to a cinder.  The ashes blow away.""",
)
ON_WHAT_ = mkTEXT("""On what?""",
)
BRIEF_OK = mkTEXT("""Okay, from now on I'll only describe a place in full the first time
you come to it.  To get the full description, say \"LOOK\".""",
)
TROLL_DATA = mkTEXT("""Trolls are close relatives with the rocks and have skin as tough as
that of a rhinoceros.  The troll fends off your blows effortlessly.""",
)
EL_CHEAPO = mkTEXT("""The troll deftly catches the #, examines it carefully, and tosses it
back, declaring, \"Good workmanship, but it's not valuable enough.\"""",
)
BOUGHTHIMOFF = mkTEXT("""The troll catches the # and scurries away out of sight.""",
)
TROLL_SEZ_NO = mkTEXT("""The troll refuses to let you cross.""",
)
NO_BRIDGE = mkTEXT("""There is no longer any way across the chasm.""",
)
BEAR__BRIDGE = mkTEXT("""Just as you reach the other side, the bridge buckles beneath the
weight of the bear, which was still following you around.  You
scrabble desperately for support, but as the bridge collapses you
stumble back and fall into the chasm.""",
)
BEAR__TROLL = mkTEXT("""The bear lumbers toward the troll, who lets out a startled shriek and
scurries away.  The bear soon gives up the pursuit and wanders back.""",
)
AXE__BEAR = mkTEXT("""The axe misses and lands near the bear where you can't get at it.""",
)
KILL__BEAR = mkTEXT("""With what?  Your bare hands??  Against *his* bear hands???  Don't be
ridiculous - he'd tear you to shreds!""",
)
BEAR_PUZZLED = mkTEXT("""The bear is confused; he only wants to be your friend.""",
)
IT_IS_DEAD = mkTEXT("""For crying out loud, the poor thing is already dead!""",
)
BEAR__URRP = mkTEXT("""The bear eagerly wolfs down your food, after which he seems to calm
down considerably and even becomes rather friendly.""",
)
BEAR_IS_CHAINED = mkTEXT("""The bear is still chained to the wall.""",
)
CHAIN_LOCKED = mkTEXT("""The chain is still locked.""",
)
CHAIN_UNLOCKED = mkTEXT("""The chain is now unlocked.""",
)
LOCK__CHAIN = mkTEXT("""The chain is now locked.""",
)
LOCK__CHAIN_ = mkTEXT("""There is nothing here to which the chain can be locked.""",
)
NO_FOOD = mkTEXT("""There is nothing here to eat.""",
)
ILL_GIVE_HINT = mkTEXT("""I can give you some advice that might help you solve your problem,
but I'll have to charge you # points for it.  TANSTAAFL, y'know!""",
)
WANT_HINT_ = mkTEXT("""Do you want the hint?""",
)
HINT_MAZE_ = mkTEXT("""Do you need help getting out of here?""",
)
mkTEXT("""You can make the passages look less alike by dropping things.  You
could then make a map that would let you find your way around.""",
)
HINT_PLOVER_ = mkTEXT("""Are you trying to explore beyond the Plover room?""",
)
mkTEXT("""There is a way to explore that region without having to worry about
falling into a pit.  None of the objects available is immediately
useful in discovering the secret.""",
)
HINT_WITTS_ = mkTEXT("""Do you need help getting out of here?""",
)
mkTEXT("""Don't go west.""",
)
FEED__TROLL = mkTEXT("""Gluttony is not one of the troll's vices.  Avarice, however, is.""",
)
LAMP_IS_DIM = mkTEXT("""Your lamp is getting dim.  You'd best start wrapping this up, unless
you can find some fresh batteries.  I seem to recall there's a vending
machine in the maze.  Bring some coins with you.""",
)
LAMP_IS_DEAD = mkTEXT("""Your lamp has run out of power.""",
)
LAMP_DEAD_ = mkTEXT("""
There's not much point in wandering around out here, and you can't
explore the cave without a lamp.  So let's just call it a day.""",
)
PIRATE_RUNS = mkTEXT("""
There are faint rustling noises from the darkness behind you.  As you
turn toward them, the beam of your lamp falls across a bearded pirate.
He is carrying a large chest.  \"Shiver me timbers!\" he cries, \"I've
been spotted!  I'd best hie meself off to the maze to hide me chest!\"
With that, he vanishes into the gloom.""",
)
LAMP_BATTERIES = mkTEXT("""Your lamp is getting dim.  You'd best go back for those batteries.""",
)
LAMP_REFUEL = mkTEXT("""Your lamp is getting dim.  I'm taking the liberty of replacing the
batteries.""",
)
LAMP_NOFUEL = mkTEXT("""Your lamp is getting dim, and you're out of spare batteries.  You'd
best start wrapping this up.""",
)
MAG_DWARVISH = mkTEXT("""I'm afraid the magazine is written in Dwarvish.""",
)
CHEST_ELSEWHERE = mkTEXT("""\"This is not the maze where the pirate leaves his treasure chest.\"""",
)
THIS_IS_A_CLUE = mkTEXT("""Hmmm, this looks like a clue, which means it'll cost you 10 points to
read it.  Should I go ahead and read it anyway?""",
)
NEW_EFFECT = mkTEXT("""It says, \"There is something strange about this place, such that one
of the words I've always known now has a new effect.\"""",
)
UNCHANGED = mkTEXT("""It says the same thing it did before.""",
)
MACHINE_SIGN = mkTEXT("""It reads, \"Drop coins here to receive fresh batteries.\"""",
)
I_DONT_UNDERSTAND = mkTEXT("""I'm afraid I don't understand.""",
)
DARK_ROOM = mkTEXT("""It says, \"Congratulations on bringing light into the Dark-room!\"""",
)
SHATTER_MIRROR = mkTEXT("""You strike the mirror a resounding blow, whereupon it shatters into a
myriad tiny fragments.""",
)
THROW_VASE = mkTEXT("""You have taken the vase and hurled it delicately to the ground.""",
)
IS_THIS_OK_ = mkTEXT("""Is this acceptable?""",
)
SUSP_DEMO = mkTEXT("""There's no point in suspending a demonstration game.""",
)
BROKENECK = mkTEXT("""You are at the bottom of the pit with a broken neck.""",
)
UNCLIMBABLE = mkTEXT("""The dome is unclimbable.""",
)
SNAKEBLOCKS = mkTEXT("""You can't get past the snake.""",
)
MISTCRAWL = mkTEXT("""You have crawled around in a little passage north of and parallel
to the Hall of Mists.""",
)
PLUMMET = mkTEXT("""Aaaaaaaaaiiiiiiiiiiieeeeeeeeee........               >splat<
Hmmmm - I never saw a red flapjack before!""",
)
PLUMMET1 = mkTEXT("""Aaaaaaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhh........        >squish<
Yetch - what a mess!""",
)
PLUMMET2 = mkTEXT("""Gaaaaaaaaaaaaaaaaaaaaaaaaaahhhhhh............         >crunch<""",
)
PLUMMET3 = mkTEXT("""Haaaaaaaaaaaaaalllllllllllllllllpppppp...........      >smash<""",
)
NOCANCLIMB = mkTEXT("""There's nothing climbable here.""",
)
WHAT_DO = mkTEXT("""What do you want me to do with the #?""",
)
MISTCRACK = mkTEXT("""The crack is far too small for you to enter.""",
)
PIPEFIT = mkTEXT("""The stream flows out through a pair of 1 foot diameter sewer pipes.
It would be advisable to leave via the exit.""",
)
YOUDONTHAVE = mkTEXT("""You have no #!""",
)
NOCLIMBUP = mkTEXT("""There's nothing to climb here.  Say \"UP\" or \"OUT\" to leave the pit.""",
)
SHORTPLANT = mkTEXT("""You have climbed up the plant and out of the pit.""",
)
LONGPLANT = mkTEXT("""You scurry up the plant and into the hole in the wall.""",
)
CANTGETAXE = mkTEXT("""As you approach the bear, it snarls threateningly;  you are forced
to retreat without the #.""",
)
DRAGON_RUG = mkTEXT("""You can't get by the dragon to get at the rug.""",
)
YOUSCORED = mkTEXT("""

You have scored a total of # points, out of a possible maximum of""",
)
TOPSCORE = mkTEXT("""# points.  During this game of Adventure, you have taken a total of""",
)
NMOVES = mkTEXT("""# turns.

""",
)
NOJUMPING = mkTEXT("""There is nowhere for me to jump to.""",
)
CLARIFY = mkTEXT("""I'm not sure what you want me to # - please be more specific.""",
)
DWARF_QUITS = mkTEXT("""The dwarf quickly scuttles off into the gloom.""",
)
SAID = mkTEXT("""Ok - \"#\".""",
)
IFYOUQUIT = mkTEXT("""If you were to quit now, you would score a total of # points, out""",
)
IFYOUQUIT2 = mkTEXT("""of a possible maximum of # points.""",
)
FISH = mkTEXT("""You are obviously a rank amateur.  Better luck next time.""",
)
NOVICE = mkTEXT("""Your score qualifies you as a novice-class adventurer.""",
)
EXPERIENCED = mkTEXT("""You have achieved the rating; \"Experienced Adventurer\".""",
)
SEASONED = mkTEXT("""You may now consider yourself a \"Seasoned Adventurer\".""",
)
JUNIORMASTER = mkTEXT("""You have reached \"Junior Master\" status.""",
)
MASTER_C = mkTEXT("""Your score puts you in Master Adventurer class C.""",
)
MASTER_B = mkTEXT("""Your score puts you in Master Adventurer class B.""",
)
MASTER_A = mkTEXT("""Your score puts you in Master Adventurer class A.""",
)
GRAND = mkTEXT("""All of Adventuredom gives tribute to you, Adventurer Grandmaster!""",
)
NEED1 = mkTEXT("""You only need one more point to reach the next level of expertise!""",
)
NEED = mkTEXT("""To reach the next qualification level you need # more points.""",
)
NEW_BATTERIES = mkTEXT("""The old batteries in your lamp were pretty well shot - I've taken the
the liberty of putting in the new ones.""",
)
DUNNO_HAO = mkTEXT("""I don't know how to # such a thing.""",
)
MUSTWAIT = mkTEXT("""I can save your Adventure for you, but if I do you'll have to wait
at least # minutes before continuing.""",
)
CANT_SAVE = mkTEXT("""I'm sorry, but I can't save your game at the moment;  something
seems to be wrong with the save file.""",
)
NO_IMAGE = mkTEXT("""I can't find any saved game for you to restore.""",
)
EXPLOSION = mkTEXT("""An explosion has destroyed the well-house during the time that your
game was suspended.  You're going to have to start over.""",
)
SAVE_THE_IMAGE = mkTEXT("""Do you want me to keep the save-image?""",
)
CONTINUE_NOW_ = mkTEXT("""Do you wish to continue with the game immediately?""",
)
TOO_SOON = mkTEXT("""I'm sorry - only a wizard can restart a game in less than # minutes.""",
)
DOUSED_DWARF = mkTEXT("""The # flies through the air and thoroughly drenches the dwarf.  He
shakes himself off and curses violently; he *REALLY* looks angry!""",
)
DOUSED_DWARVES = mkTEXT("""The # flies through the air and thoroughly drenches the dwarves. They
shake themselves off and curse violently; they *REALLY* look angry!""",
)
CANTDRINK = mkTEXT("""There is nothing here that I can drink!""",
)
CANT_READ_OYSTER = mkTEXT("""There's nothing written on the oyster.""",
)
OYSTER_IS_BARE = mkTEXT("""There is nothing written on the top of the oyster.""",
)
CAVE_NOT_OPEN = mkTEXT("""I'm terrible sorry - Colossal Cave is closed.  Our hours are:
""",
)
ETMF_TOO_HIGH = mkTEXT("""I'm afraid that I can't start up a real Adventure for you at the
moment; the system's ETMF is too high.""",
)
TOO_MANY_USERS = mkTEXT("""I'm afraid that there are too many people on the system at the moment;
I can't start up a real Adventure for you.""",
)
CAN_DEMO = mkTEXT("""We do allow visitors to make short explorations during our off hours.
""",
)
WANT_DEMO = mkTEXT("""Would you like to do that?""",
)
TA_TA = mkTEXT("""Ok, then - I suggest that you try again later.""",
)
WIZARD_ENDS = mkTEXT("""
A large cloud of green smoke appears in front of you.  It clears away
to reveal a tall wizard, clothed in grey.  He fixes you with a steely
glare and declares, \"This adventure has lasted too long.\"  With that
he makes a single pass over you with his hands, and everything around
you fades away into a grey nothingness.""",
)
RESTORE_PRIME = mkTEXT("""I'm afraid that I can't restore your saved game - it's prime time
at the moment, and only demonstration Adventures are permitted.""",
)
RESTORE_ETMF = mkTEXT("""I'm sorry, but I can't restore your Adventure - the ETMF is too
high.  You'll have to try again later.""",
)
RESTORE_USERS = mkTEXT("""I'm sorry, but there are too many users on the system at the moment;
please try again later when the system is less heavily in use, and
I'll restore your Adventure then.""",
)
HOURS_ARE = mkTEXT("""
Colossal Cave is open during the following hours:
""",
)
R_U_A_WIZARD_ = mkTEXT("""Are you actually a wizard?""",
)
PROVE_IT = mkTEXT("""Prove it - say the magic word!""",
)
OH_POOH = mkTEXT("""Oh, pooh - you are nothing but a charlatan!  That little piece of
deception is going to cost you 10 points!!""",
)
SO_YOU_ARE = mkTEXT("""Oh, dear, you really *are* a wizard!  Sorry to have bothered you....""",
)
NOTHING_OBVIOUS = mkTEXT("""Nothing obvious happens.""",
)
SCHLURP = mkTEXT("""Hmmmm..  This sand is rather soft, and you're sinking in a little...
In fact you're sinking in a lot!   Oh, no - it's QUICKSAND!!  HELP!!
HELP!!! HELP!! >glub<   >glub<    >glub<     >blurp<""",
)
SCHLURP2 = mkTEXT("""You know, I've heard of people who really fell in for the soft sell,
but  >glub<  this  >glub<  is  >glub<  ridiculous!         >blop!<""",
)
SLIMED = mkTEXT("""As you enter into the passage, you are forced to brush up against
some of the green slime.  Instantly it flows down and covers your
body, and rapidly digests away all of your flesh.""",
)
FZAP = mkTEXT("""With a sharp sizzling sound, a large spark of electricity jumps
out of thin air and strikes your lamp.  The immense electrical charge
flows to ground through your body and fries you to a crisp.""",
)
LAMP_GOES_POOF = mkTEXT("""With a loud \"zap\" a bolt of lightning springs out of midair and strikes
your lamp, which immediately and violently explodes.  You narrowly
miss being torn to shreds by the flying metal.
""",
)
LAMP_EXPLODES = mkTEXT("""In a loud crackle of electricity, a bolt of lightning jumps out of
nowhere and strikes your lamp.  The lamp instantly explodes like a
grenade, and you are mown down by a cloud of shrapnel.""",
)
LAMP_RECHARGED = mkTEXT("""The air fills with tension, and there is a subdued crackling sound.
A blue aura forms about your lantern, and small sparks jump from the
lantern to the ground.  The aura fades away after several seconds,
and your lamp is once again shining brightly.""",
)
GOT_THE_SWORD = mkTEXT("""The singing sword slides easily out of the rock.""",
)
SWORD_IS_STUCK = mkTEXT("""The sword is firmly embedded in the stone, and you aren't strong
enough to pull it out.""",
)
VIAL_EXPLODES = mkTEXT("""The vial strikes the ground and explodes with a violent >foom<,
neatly severing your foot.  You bleed to death quickly and messily.""",
)
VIAL_BANG = mkTEXT("""The vial explodes into splinters and disintegrates, releasing an
oily liquid which rapidly sublimes into a large mushroom-shaped cloud""",
)
FIRST_FUME = mkTEXT("""of pale puce vapor smelling like sequoia sap and ozone.""",
)
mkTEXT("""of bright green vapor smelling like pine needles and sea water.""",
)
mkTEXT("""of thick yellow vapor smelling like cheddar cheese and bananas.""",
)
mkTEXT("""of choking green vapor smelling like chlorine and apples.""",
)
mkTEXT("""of misty white vapor with no scent.""",
)
mkTEXT("""of nearly-invisible vapor with a strong odor of walnuts and onions.""",
)
LAST_FUME = mkTEXT("""of ominously glowing vapor smelling of hot iron.""",
)
REVENGE = mkTEXT("""As you reach the middle of the bridge, the troll appears from out
of the tunnel behind you, wearing a large backpack.  \"So, Mister
Magician,\" he shouts, \"you like to use magic to steal back my hard-
earned toll?  Let's see how you like a little of MY magic!!\"  With
that, he aims a tube running from the backpack directly at the bear
and pulls a trigger.  A spout of magical fire roars out and singes the
bear's fur;  the bear bellows in pain and dashes onto the bridge to
escape.  The bridge shudders, groans, and collapses under the weight,
and you and the bear plunge down into the chasm.""",
)
REVENGE_1 = mkTEXT("""As you reach the middle of the bridge, the troll appears from out
of the tunnel behind you, wearing a large backpack.  \"So, Mister
Magician,\" he shouts, \"you like to use magic to steal back my hard-
earned toll?  Let's see how you like a little of MY magic!!\"  With
that, he aims a tube running from the backpack directly at the bridge
and pulls a trigger.  A spout of magical fire roars out and incinerates
the bridge supports, causing the bridge to sway giddily and collapse
into the chasm.  You plunge down to your death.""",
)
SWORD_MISSES = mkTEXT("""The sword misses the bear, bounces off of the wall, and lands at
your feet.""",
)
BEAR_MISSES = mkTEXT("""The bear dodges away from your attack, growls, and swipes at you
with his claws.  Fortunately, he misses.""",
)
BEAR_GETS_YOU = mkTEXT("""The bear snarls, ducks away from your attack and slashes you to death
with his claws.""",
)
FOOF = mkTEXT("""
>>Foof!<<
""",
)
OOF = mkTEXT("""Wheeeeeeeeeeeeeeee.......     >oof<
""",
)
SLIDE_SLIPPERY = mkTEXT("""The icy slide is far too steep and slippery to climb.""",
)
OGRE_BLOCKS = mkTEXT("""The ogre growls at you and refuses to let you pass.""",
)
OGRE_REBUFF = mkTEXT("""The ogre contemptously catches the # in mid-swing, rips it out
of your hands, and uses it to chop off your head.""",
)
OGRE_CATCH = mkTEXT("""The ogre casually catches the # in mid-air, braces his feet, winds
up and throws the # straight back at you with incredible force.  You
are unable to dodge it and it chops you in half.""",
)
OGRE_KILLED = mkTEXT("""The sword halts in mid-air, twirls like a dervish, and chants several
bars of \"Dies Ire\" in a rough tenor voice.  It then begins to spin
like a rip-saw blade and flies directly at the ogre, who attempts to
catch it without success;  it strikes him full on the chest.  There is
a brilliant flash of light, a deafening roar and a cloud of oily grey
smoke;  when the smoke clears (and your eyes begin working properly
again) you see that the ogre has vanished.  The sword is lying on the
ground, sparking and flaming.  Before your eyes it softens and melts,
writhes as if in pain, and shrinks rapidly until all that is left is
a small silvery ring which cools rapidly.""",
)
OGRE_TOO_TOUGH = mkTEXT("""You attack the ogre, but he fends off your attack easily and comes
very close to crushing your skull with *his* bare (but extremely
strong) hands.  You are forced to retreat in disgrace.""",
)
OGRE_RIPS_HEAD_OFF = mkTEXT("""You attack the ogre - a brave but foolish action.  He quickly grabs
you and with a heave of his mighty arms rips your body limb from limb.""",
)
NO_ARCH = mkTEXT("""I'm afraid I can't go that way - walking on red-hot lava is contrary
to union regulations (and is bad for your health anyhow).""",
)
LEAVE_BEAR = mkTEXT("""That archway looks pretty fragile - you'd better leave the bear here.""",
)
FUMES_BURN = mkTEXT("""As you approach the center of the archway, hot vapors saturated with
brimstone drift up from the lava in the gorge beneath your feet.  You
are swiftly overcome by the foul gasses and, with your lungs burned
out, fall off of the bridge and into the gorge.""",
)
FUMES_MISS = mkTEXT("""As you approach the center of the archway, hot vapors saturated with
brimstone drift up from the lava in the gorge beneath your feet.  The
mithril ring in your hand quivers and glows, and the fumes eddy away
from the bridge without harming you.
""",
)
GHOST_BANG = mkTEXT("""As you reach the center of the bridge, a ghostly figure appears in
front of you.  He (?) stands at least eight feet tall, and has the
lower body of an enormous snake, six arms, and an angry expression on
his face.  \"You'll not have my sceptre that easily!\" he cries, and
makes a complex magical gesture with his lower right arm.  There is a
brilliant flash of light and a vicious >crack<, and the bridge cracks
and plummets into the gorge.""",
)
NO_KEYHOLE = mkTEXT("""The door to the safe has no keyhole, dial, or handle - I can't figure
out how to open it!""",
)
ALREADY_OPEN = mkTEXT("""The # is already open!""",
)
IT_IS_MELTED = mkTEXT("""The door to the safe seems to be fused shut - I can't open it.""",
)
ALREADY_SHUT = mkTEXT("""The # is already closed!""",
)
SAFE_SHUTS = mkTEXT(""">Creeeeeeeeeeeeeeeeeeeeeeeeeeeek<     >ker-CHUNK!<

The safe is now closed.""",
)
SAFE_OPENS = mkTEXT(""">ker-THUNK<
>screeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeech<

The (somewhat rusty) safe is now open.""",
)
WHISPER = mkTEXT("""You pluck the sceptre from the skeleton's bony hand.  As you do, the
skeleton raises its head and whispers \"Remember - #!\" in a
forboding tone; it then sags to the ground and crumbles into dust which
drifts away into the still air of the cave.""",
)
BLEW_SAFE = mkTEXT("""As you pluck the sceptre from the skeleton's grasp, it raises its head
and whispers, \"You blew it!\".  It then shivers and collapses into a
pile of fine dust which quickly vanishes.""",
)
SAFE_FUSES = mkTEXT("""
>bong<                 The very air quivers with sound as though
>bong<               someone, somewhere in the distance, has struck
>bong<             three powerful blows on an immense brass gong.

Smoke trickles out from around the edges of the safe's door, and the
door itself glows red with heat for a moment.

A hollow voice says,  \"This is a Class 1 security alarm.  All cave
security forces go to Orange Alert.  I repeat - Orange Alert.\"
""",
)
SAFE_BLOCKS = mkTEXT("""The safe's door is blocking the exit passage - you'll have to close
the safe to get out of here.""",
)
SIZZLE = mkTEXT("""EEEEEEEEEAAAAAAAAAAAaaaaaahhhhhhhhhhhhh..........

>sizzle<""",
)
SLICE_BLOB = mkTEXT("""The # cuts through the blob's body (?) without harming it.""",
)
BOUNCE_BLOB = mkTEXT("""You attack the strange blob, but bounce harmlessly off of its strong
but very rubbery skin.""",
)
CRUMBLE = mkTEXT("""Rock silently crumbles off of the wall in front of you, revealing
dark passages leading northwest, north, and northeast.""",
)
PLAIN_HINT = mkTEXT("""Having problems?""",
)
mkTEXT("""Ok - what you need to do is apply a little philosophy.  To wit:  there
is a question that you need to ask whenever you explore a new room
in this cave.  In most places, the answer to the question is \"yes\".
In some other places, it's \"no\" for an obvious reason.  Right here,
the answer is \"no\" but the reason isn't so obvious.  If you can figure
out what the question is, you can get out of here easily.  I can tell
you this - it's always a vital question if you wish to survive.""",
)
BAS_GRUMBLE = mkTEXT("""The basilisk stirs restlessly and grumbles in its sleep as you pass,
but it does not awaken.
""",
)
PETRIFY_SELF = mkTEXT("""The basilisk stirs grumpily and awakens, peering sleepily about.  It
sees its reflection in the metal plate that you are carrying,
shudders, and turns into solid granite.
""",
)
PETRIFY_ME = mkTEXT("""The basilisk stirs grumpily and awakens, peering sleepily about.  It
spies you, growls, and stares you straight in the eye.  Your body
is instantly petrified.""",
)
HIT_BASILISK = mkTEXT("""You attack the basilisk mightily.  It instantly awakens and looks you
dead in the eye, and your body turns to solid rock.""",
)
AXE_BASILISK = mkTEXT("""The # rebounds harmlessly from the basilisk's tough scales.  The
basilisk awakens, grunting in shock, and glares at you.  You are
instantly turned into a solid rock statue (and not a particularly
impressive one, at that).""",
)
REBOUND = mkTEXT("""The # rebounds harmlessly from the pentagram's magic force
field.  It's just as well - the djinn doesn't seem dangerous.""",
)
KILL_A_FEW = mkTEXT("""You kill several of the gooseberry goblins with your #, but
the others swarm at you, force you to the ground, and rip out
your throat.""",
)
TOUGH_DJINN = mkTEXT("""That's not a wise thing to try - djinni are essentially immortal
and thus are pretty hard to hurt.  Besides, this one seems rather
friendly - why don't you just try releasing him?""",
)
GOBL_EAT_YOU = mkTEXT("""Goblins live exclusively on human flesh, and you can't spare
any of your own to placate them.  On the other hand, I suspect
that they're going to eat you pretty soon whether you like it
or not - you'd better find some way of killing them or driving
them away!""",
)
WARRIORS = mkTEXT("""
As each of the dragon's teeth strikes the ground, a fully-armed human
skeleton springs up from where it struck and leaps to your defense!
The skeletal warriors attack the vicious gooseberry goblins and drive
them away in screaming panic;  they then salute you with their ancient
and rusty swords, and fade silently into nothingness.
""",
)
POLITE_DJINN = mkTEXT("""The wax seal breaks away easily.  A cloud of dark smoke pours up from
the mouth of the flask and condenses into the form of a twelve-foot
Djinn standing in the pentagram.  He pushes experimentally at the
magical wall of the pentagram (which holds), and nods politely to
you.  \"MY THANKS, OH MORTAL,\" he says in an incredibly deep bass
voice.  \"IT HAS BEEN THREE THOUSAND YEARS SINCE SOLOMON SEALED ME
INTO THAT BOTTLE, AND I AM GRATEFUL THAT YOU HAVE RELEASED ME.  IF
YOU WILL OPEN THIS PENTAGRAM AND LET ME GO FREE, I WILL GIVE YOU SOME
ADVICE THAT YOU MAY ONE DAY WISH TO POSSESS.\"""",
)
RUDE_DJINN = mkTEXT("""The flask's wax seal crumbles at your touch.  A large cloud of black
smoke pours out, solidifying into the form of a twelve-foot Djinn.
\"AT LAST!\" he says in an earth-shaking voice, \"I KNEW THAT SOMEDAY
SOMEONE WOULD RELEASE ME!  I WOULD REWARD YOU FOR THIS, MORTAL, BUT
IT HAS BEEN THREE THOUSAND YEARS SINCE I HAD A SOLID MEAL, AND I'M
NOT GOING TO STAND HERE CHATTERING WHEN I COULD BE OUT EATING A SIX-
INCH SIRLOIN STEAK.  FAREWELL.\"  With that, he somewhat rudely explodes
back into smoke and drifts quickly out of sight.""",
)
DJINN_ADVICE = mkTEXT("""The pentagram's magical barrier sparks fitfully and goes down.  The
Djinn stretches gratefully and smiles at you.  \"AGAIN, MY THANKS,\" he
says.  \"MY ADVICE TO YOU WILL TAKE THE FORM OF A HISTORY LESSON.
WHEN RALPH WITT, THE ARCHITECT AND CONSTRUCTOR OF THIS CAVE, WAS VERY
YOUNG, HE BECAME VERY INCENSED THAT HIS NAME WAS AT THE END OF THE
ALPHABET.  HE FELT (FOR SOME REASON) THAT THE LETTER W BELONGED NEAR
THE BEGINNING OF THE ALPHABET, AND THAT ALL OF THOSE \"UPSTART LETTERS
WHICH UNFAIRLY USURPED THE BEST PLACES\" SHOULD BE FORCED INTO EXILE
AT THE END OF THE ALPHABET.  HIS INSTINCT FOR MATTERS MAGICAL AND
MYSTICAL LED HIM TO APPLY THIS STRANGE BELIEF INTO THE CAVE'S
STRUCTURE WHEN HE EXCAVATED IT.  YOU HAVEN'T YET BEEN AFFECTED BY HIS
STRANGE HABITS, BUT YOU SHOULD REMEMBER THIS.  FAREWELL, AND GOOD
LUCK.\"  With that, the Djinn evaporates into a cloud of smoke and
drifts rapidly away.""",
)
KILL_GOBLINS = mkTEXT("""You attack the goblins and manage to squash a few, but the others
overwhelm you, forcing you to the ground and ripping out your throat.""",
)
EMPTY_PENTA = mkTEXT("""The pentagram is empty - there's nothing to let out!""",
)
GOBLIN_CHASE = mkTEXT("""You are being pursued by a vicious horde of little gooseberry goblins!
""",
)
FALL_STARVE = mkTEXT("""You have jumped into a bottomless pit.  You continue to fall for
a very long time.  First, your lamp runs out of power and goes
dead. Later, you die of hunger and thirst.""",
)
FALL_STARVED = mkTEXT("""You have jumped into a bottomless pit.  Eventually, you die of thirst.""",
)
CANTENTERSAFE = mkTEXT("""The safe's door is closed, and you can't get in!""",
)
NO_HANDLE = mkTEXT("""There is no handle on the inside of the safe door, nor any other way
to get a grip on it.  You'll have to leave the safe before shutting it.""",
)
CANT_SWIM = mkTEXT("""I can't swim, or walk on water.  You'll have to find some other way
to get across, or get someone to assist you.""",
)
TURTLE_BACK = mkTEXT("""You step gently on Darwin the Tortoise's back, and he carries you
smoothly over to the southern side of the reservoir.  He then blows
a couple of bubbles at you and sinks back out of sight.
""",
)
GONG_RINGS = mkTEXT("""
>BONNNNGGGGGGGGGG<

Darwin the Tortoise blinks in surprise at the noise, but does nothing.""",
)
GONG_FETCH = mkTEXT("""
>BONNNNNGGGGGGGGG<

A hollow voice says, \"The GallopingGhost Tortoise Express is now at
your service!\"

With a swoosh and a swirl of water, a large tortoise rises to the
surface of the reservoir and paddles over to the shore near you.
The message, \"I'm Darwin - ride me!\" is inscribed on his back in
ornate letters.
""",
)
WHIRLPOOL_ = mkTEXT("""Into the whirlpool??""",
)
FLOW_DOWN = mkTEXT("""You plunge into the water and are sucked down by the whirlpool.""",
)
FLOW_RIP = mkTEXT("""You plunge into the water and are sucked down by the whirlpool.  The
current is incredibly strong, and you barely manage to hold onto
your lamp;  everything else is pulled from your grasp and is lost in
the swirling waters.""",
)
FLOW_DARK = mkTEXT("""You plunge into the water and are sucked down by the whirlpool into
pitch darkness.""",
)
FLOW_D_RIP = mkTEXT("""You plunge into the water and are sucked down by the whirlpool into
pitch darkness.  The current is incredibly strong, and everything that
you are carrying is ripped from your grasp and is lost in the swirling
waters.""",
)
WHIRL_LAND = mkTEXT("""
The swirling waters deposit you, not ungently, on solid ground.
""",
)
PHUGGG_DATA = mkTEXT("""
A large phosphorescent cloud of smoke drifts into view, and a large
mouth and two dark eyes take shape on the side.  One of the eyes winks
at you, and the djinn's deep voice says \"GREETINGS AGAIN, MORTAL.  I
HAVE REMEMBERED A PIECE OF ANCIENT LORE THAT I LEARNED FROM MY AUNT,
AN AFREET OF GREAT KNOWLEDGE.  THERE IS ANOTHER MAGIC WORD THAT YOU
MIGHT FIND OF USE IF YOU SHOULD EVER FIND YOURSELF BEING ATTACKED BY
THOSE PESTIFEROUS DWARVES.  YOU SHOULD USE IT ONLY AS A LAST RESORT,
THOUGH, SINCE IT IS A MOST POTENT WORD AND IS PRONE TO BACKFIRE FOR
NO OBVIOUS REASON;  ALSO, IT SHOULD NEVER BE USED NEAR WATER OR NEAR
ANY SHARP WEAPON OR THE RESULTS MAY BE MOST UNFORTUNATE.  THE WORD
IS 'phuggg'\", whispers the djinn, \"AND IT MUST BE PRONOUNCED CAREFULLY
IF IT IS TO HAVE THE PROPER EFFECT.  FAREWELL AGAIN, AND GOOD LUCK!\"
With that, the djinn-cloud drifts away out of sight.
""",
)
JELLYFISH = mkTEXT("""
>splurch!<

Oh, no!  You've turned yourself into a jellyfish, and fallen to the
ground and been splattered far and wide!  Well, that certainly wasn't
very smart!!!  You were warned not to use that work near water!""",
)
CAVE_DESTROYED = mkTEXT("""
The ground begins to shudder ominously, and the very cave walls around
you begin to creak and groan!  A sulphurious stench fills the air!

With an incredible lurch, the ground begins to dance and ripple as
though it were liquid!  You are thrown off of your feet and tossed
violently up and down!  The cave walls begin to crumble and split from
the stress!

There is a terrible ROAR of rending rock!!  The cave ceiling splits,
and rocks plunge down and smash your lower body to a gooey paste!!

There is a violent blast in the distance!  Steam and smoke drift into
view through the rents in the walls, and furiously-bubbling red-hot
lava flows in and surrounds you.  The cave ceiling disintegrates in
an incredible orgy of grinding destruction, and the cave walls fall
and are pounded into fine dust.



You are lying, badly mangled, on a small rock island in a sea of
molten lava.  Above you, the sky is faintly visible through a thick
pall of smoke and steam.  A short distance to the north, the remains
of a well-house are sinking slowly into the bubbling ooze.


There is a distant, sourceless screech of incredible anguish!  With
a sharp >poof< and a small puff of orange smoke, a bent and bearded
elf appears.  He is dressed in working clothes, and has a name-tag
marked \"Ralph\" on his shirt.  \"You blithering idiot!\" he storms.
\"You were warned quite clearly not to use that work near water!!  I
hadn't gotten all of the bugs out of it yet, and now your incredible
incompetance has totally destroyed Colossal Cave!!  Do you have the
faintest scintilla of an iota of an understanding of how much work
I'm going to have to do to get the cave rebuilt?!?  I'll have to go
all the way to Peking for another dragon, and I'll have to convince
the Goblin's Union to send me another team of gooseberry goblins;
I'll have to sub-contract the building of the volcano out to the
local totrugs, and worst of all I'll have to go through eight months
of paperwork and red tape to file a new Environmental Impact
statement!!  All because you couldn't follow directions, you
purblind and meatbrained moron!  I'm rescinding all of your game
points and throwing you out!  Out!   OUT!   GET OUT!$!%#&'@%!!%%!\"
""",
)
ZOT_AXE = mkTEXT("""Your axe glows bright orange and fades into nothingness.""",
)
ZOT_SWORD = mkTEXT("""Your sword jumps into the air, chants several bars of the \"Volga
Boatman\", shoots off several fitful blue sparks, and disintegrates.""",
)
IT_WORKED = mkTEXT("""A clear, liquid chime sounds in midair.  A large, four-clawed hand
reaches out of the ground, grabs the dwarf, and pulls it down into
nothingness.""",
)
mkTEXT("""A clear, liquid chime sounds in midair.  A long green tentacle
covered with sucker disks reaches out from nowhere, grabs the
dwarves, and pulls them back to wherever it came from.""",
)
mkTEXT("""There is a sharp sizzling sound.  The dwarf explodes into flame
and vanishes.""",
)
mkTEXT("""There is a sharp sizzling sound.  The dwarves are engulfed in
a wave of fire that appears from nowhere, and are completely
incinerated;  the flames then vanish into nothingness again.""",
)
mkTEXT("""There is a sharp whistling sound from nowhere.  The dwarf shudders
and turns into a moth, which then flies away.""",
)
mkTEXT("""There is a sharp whistling sound from nowhere.  The dwarves stiffen,
shudder, and melt down into a large puddle of soggy goo that quickly
soaks into the ground and vanishes.""",
)
IT_DIDNT_WORK = mkTEXT("""A clear, liquid chime sounds in midair.  A large, four-clawed foot
appears in midair and stomps violently downward, missing the dwarf
but thoroughly squashing you.""",
)
mkTEXT("""A clear, liquid chime sounds in midair.  A large and very toothy
mouth appears in midair and chomps ferociously.  The dwarves manage
to evade it, but it bites you in half.""",
)
mkTEXT("""There is a sharp sizzling sound.  A ball of fire roars out of nowhere,
misses the dwarf, bounces off of a wall, and incinerates you.""",
)
mkTEXT("""There is a sharp sizzling sound.  A ball of fire appears from nowhere,
bounces off of the ground, and explodes violently, incinerating both
you and the dwarves.""",
)
mkTEXT("""There is a sharp crackling sound from the air above you.  The dwarf
shudders and turns into a sabre-toothed tiger, which attacks and
kills you in short order.""",
)
mkTEXT("""There is a sharp crackling sound from the air above you.  The dwarves
stiffen, fall to the ground, and melt into a large puddle of soggy
goo.  The goo twitches a few times and then flows at you with
incredible speed;  it attacks and strangles you with little
difficulty.""",
)
SET_FLASK_DOWN = mkTEXT("""You have set the flask down in the center of the pentagram.""",
)
CAMEO = mkTEXT("""From somewhere in the distance, there comes a musical skirl of
light, elvish laughter and the sounds of merriment.""",
)
mkTEXT("""From somewhere nearby, there suddenly comes a sound of something
mechanical in motion.  As you turn towards it, an incredible
figure rolls into the light of your lamp.  It stands about five
feet high on a wheeled metal pedestal, and has a globular light-
filled head, accordion-pleated metal arms, and a cylindrical body
the size of an oil drum with a plastic panel on the front.  It rolls
past without taking any notice of you, all the while waving its
arms, flashing a light behind its front panel and bellowing \"WARNING!
WARNING!  DANGER!\" at the top of its not inconsiderable voice.  It
rolls on out of sight, and moments later there is an immense flash
of light and a tremendous blast of sparks and smoke.  When the air
clears, you find that no trace remains of the strange apparition.""",
)
mkTEXT("""With a sudden gust of air, a large cave bat flutters into view,
flies around your head several times, squeaks with disgust, and
flutters on out of sight.""",
)
mkTEXT("""Suddenly, the ground quivers underfoot;  a dull rumbling sound
resounds from the rock around you, and in the distance you can
hear the crash of falling rock.  The earth tremor subsides after
a few seconds without causing any major damage.""",
)
mkTEXT("""From the darkness nearby comes the sound of shuffling feet.  As you
turn towards the sound, a nine-foot cyclops ambles into the light of
your lamp.  The cyclops is dressed in a three-piece suit of worsted
wool, and is wearing a black silk top-hat and cowboy boots and is
carrying an ebony walking-stick.  It catches sight of you and stops,
seeming frozen in its tracks, with its bloodshot eye bulging in
amazement and its fang-filled jaw drooping with shock.  After staring
at you in incredulous disbelief for a few moments, it reaches into
the pocket of its vest and pulls out a small plastic bag filled with
a leafy green substance, and examines it carefully.  \"It must be
worth eighty pazools an ounce after all\" mumbles the cyclops, who
casts one final look at you, shudders, and staggers away out of
sight.""",
)
mkTEXT("""From somewhere in the distance comes a heart-wrenching scream of
mortal terror!  \"NO!  DON'T!  NO!  NO!  HELP!!!!\" cries the voice,
and then lets out a wail of agony that is cut off abruptly.  Subdued
crunching and slurping sounds can be heard for a minute or so, and
then silence falls.""",
)
LAST_CAMEO = mkTEXT("""From somewhere nearby come the sounds of sliding, stumbling feet.
As you turn towards them, the beam of your lamp falls upon a tall,
shambling figure approaching you out of the darkness.  Standing no
more than five feet tall, it cannot possibly weigh more than fifty
pounds including the shroud and bandages in which it is wrapped;
a musty reek like the scent of old, dead earth seeps from it and
fills the air.  As you cower back in disgust and horror, the figure
halts, examines you through eyes resembling wet pebbles, and
whispers \"Peace, man!\" in a voice like wind rustling through dead
trees.  It then turns and shambles away into the darkness.""",
)
THROW_PIT = mkTEXT("""You have tossed the # down into the pit.""",
)
THROW_FISSURE = mkTEXT("""You have thrown the # down into the fissure.""",
)
THROW_HOLE = mkTEXT("""You have tossed the # down into the hole in the floor.""",
)
THROW_ROOM = mkTEXT("""You have tossed the # down into the room below you.""",
)
THROW_CANYON = mkTEXT("""You have tossed the # down into the canyon beneath your feet.""",
)
THROW_WHIRLPOOL = mkTEXT("""You have hurled the # into the middle of the whirlpool.""",
)
THROW_CAVERN = mkTEXT("""You have thrown the # down into the mist filling the cavern.""",
)
THROW_CHASM = mkTEXT("""You have hurled the # down into the misty bottom of the chasm.""",
)
THROW_GORGE = mkTEXT("""You have hurled the # down into the boiling lava at the bottom
of the volcanic gorge.""",
)
THROW_CHIMNEY = mkTEXT("""You have tossed the # down the chimney.""",
)
THROW_TUBE = mkTEXT("""You have tossed the # down into the lava tube and out of sight.""",
)
THROW_STEPS = mkTEXT("""You have thrown the # down the steps and out of view.""",
)
THROW_SLIDE = mkTEXT("""You have tossed the # down the icy slide and out of sight.""",
)
THROW_BEACH = mkTEXT("""You have thrown the # down onto the beach.""",
)
THROW_RESERVOIR = mkTEXT("""You have negligently tossed the # into the center of the reservoir.""",
)
SHATTERED_IT = mkTEXT("""A delicate crash sounds from below.""",
)
ICE_HINT_ = mkTEXT("""Are you having problems getting out of the ice tunnels?""",
)
mkTEXT("""To get out of here, you'll first have to get your bearings so that
you know where you are.  I suggest that you draw a careful, accurate
map of the tunnel system;  for clarity's sake, keep your lines as
straight as is feasible and draw in all of the dead ends and such.
Once you've got a complete and accurate map, examine it carefully; if
your thoughts refuse to clarify, you might try using the old Yoga
trick of standing on your head, and see if that helps.""",
)
CANT_SEE_ANYTHING = mkTEXT("""It's pitch dark in here - I can't tell whether there's anything here
that I can pick up!""",
)
GROPE_FALL = mkTEXT("""Hmmph - you're not asking for much, are you - it's pitch dark in
here!  Well, I'll grope around and try to find the #.....
{hunt}    {hunt}    {rummage}    {trip}   Aiiieeeee...   >SPLAT!<

You stumbled into a pit and broke your back!""",
)
GROPE_MISS = mkTEXT("""Hmmph - you're not asking for much, are you - it's pitch dark
in here, and I'll have to grope around to try to find the #.
Well, if I must, I must......   {hunt}   {search}    {hunt}
{hunt}    {peer-blindly-into-darkness}   {touch}    {hunt}
{stumble}    {search}     {scrape}   {swear}    {hunt}

No luck - I can't find the #!.  Get me some light and maybe I'll
be able to do better!""",
)
GROPE_FIND = mkTEXT("""Hmmph - you're not asking for much, are you - it's pitch dark in
here, and I'll have to grope around to find the #.  Oh,
well, I suppose that that's part of my job...    {hunt}  {search}
{seek}   Could this be the #?   No.     {search}       {hunt}
{trip}   {curse}   {catch self}   {nurse scraped hand}  {seek}

Aha!    I have located the #!.
""",
)
def label_GETSCORE(s):
  if  ((((((((((((((( EQP(s,QUITTING,0)  or  GTP(s,CLOSURE,2) ) )))))))))))))) :
    opSET(s,SCOREX,9)
  else:
    opSET(s,SCOREX,0)
  opSET(s,MAXSCORE,9)
  for o in all_objects:
    LDA(s, I, o)
    if  ((((((((((((((( BITP(s,I,VALUED) ))))))))))))))) :
      if  ((((((((((((((( LOCP(s,I,BUILDING)  or  GTP(s,CLOSURE,2) ) )))))))))))))) :
        ADD(s,SCOREX,15)
      else:
        if  ((((((((((((((( BITP(s,I,SEEN) ))))))))))))))) :
          ADD(s,SCOREX,2)
      ADD(s,MAXSCORE,15)
  if  ((((((((((((((( LOCP(s,MAGAZINES,WITTSEND) ))))))))))))))) :
    ADD(s,SCOREX,1)
  ADD(s,MAXSCORE,1)
  if  ((((((((((((((( BITP(s,DEBRIS,BEENHERE)  or  BITP(s,Y2,BEENHERE) ) )))))))))))))) :
    ADD(s,SCOREX,20)
    if  ((((((((((((((( BITP(s,LAIR,SEEN) ))))))))))))))) :
      ADD(s,SCOREX,10)
    if  ((((((((((((((( BITP(s,BEACH,SEEN) ))))))))))))))) :
      ADD(s,SCOREX,10)
    if  ((((((((((((((( BITP(s,FACES,SEEN) ))))))))))))))) :
      ADD(s,SCOREX,10)
  ADD(s,MAXSCORE,50)
  opSET(s,I,CLOSURE)
  MULT(s,I,20)
  ADD(s,SCOREX,I)
  ADD(s,MAXSCORE,100)
  opSET(s,L,DEATHS)
  MULT(s,L,10)
  SUB(s,SCOREX,L)
  SUB(s,SCOREX,PENALTIES)
  if  ((((((((((((((( LTP(s,SCOREX,0) ))))))))))))))) :
    opSET(s,SCOREX,0)
GETSCORE = mkLABEL('GETSCORE', label_GETSCORE)

def label_FINIS(s):
  CALL(s,GETSCORE)
  VALUE(s,YOUSCORED,SCOREX)
  VALUE(s,TOPSCORE,MAXSCORE)
  VALUE(s,NMOVES,MOVES)
  if  ((((((((((((((( LTP(s,SCOREX,20) ))))))))))))))) :
    LDA(s,I,FISH)
    SUB(s,SCOREX,20)
  else:
    if  ((((((((((((((( LTP(s,SCOREX,130) ))))))))))))))) :
      LDA(s,I,NOVICE)
      SUB(s,SCOREX,130)
    else:
      if  ((((((((((((((( LTP(s,SCOREX,240) ))))))))))))))) :
        LDA(s,I,EXPERIENCED)
        SUB(s,SCOREX,240)
      else:
        if  ((((((((((((((( LTP(s,SCOREX,350) ))))))))))))))) :
          LDA(s,I,SEASONED)
          SUB(s,SCOREX,350)
        else:
          if  ((((((((((((((( LTP(s,SCOREX,470) ))))))))))))))) :
            LDA(s,I,JUNIORMASTER)
            SUB(s,SCOREX,470)
          else:
            if  ((((((((((((((( LTP(s,SCOREX,510) ))))))))))))))) :
              LDA(s,I,MASTER_C)
              SUB(s,SCOREX,510)
            else:
              if  ((((((((((((((( LTP(s,SCOREX,530) ))))))))))))))) :
                LDA(s,I,MASTER_B)
                SUB(s,SCOREX,530)
              else:
                if  ((((((((((((((( LTP(s,SCOREX,550) ))))))))))))))) :
                  LDA(s,I,MASTER_A)
                  SUB(s,SCOREX,550)
                else:
                  LDA(s,I,GRAND)
                  LDA(s,SCOREX,0)
  opSAY(s,I)
  opSAY(s,BLANK)
  MULT(s,SCOREX,-1)
  if  ((((((((((((((( GTP(s,SCOREX,0) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,SCOREX,1) ))))))))))))))) :
      opSAY(s,NEED1)
    else:
      VALUE(s,NEED,SCOREX)
  opSAY(s,BLANK)
  opSTOP(s)
FINIS = mkLABEL('FINIS', label_FINIS)

def label_PHOG(s):
  if  ((((((((((((((( LTP(s,FOG,8) ))))))))))))))) :
    RANDOM(s,FOG,8)
  RANDOM(s,GLOW,8)
  if  ((((((((((((((( NEARP(s,LAMP)  and  EQP(s,LAMP,1) ) )))))))))))))) :
    APPORT(s,GLOW,LIMBO)
  else:
    APPORT(s,GLOW,PLAIN_2)
    if  ((((((((((((((( ATP(s,PLAIN_2)  and   not  BITP(s,STATUS,MOVED) ) )))))))))))))) :
      opSAY(s,GLOW)
PHOG = mkLABEL('PHOG', label_PHOG)

def label_CORONER(s):
  opSET(s,QUITTING,0)
  opSAY(s,BLANK)
  BIC(s,ADMIN,NOMAGIC)
  BIC(s,ADMIN,TICKER)
  opSET(s,BLOB,0)
  APPORT(s,BLOB,LIMBO)
  APPORT(s,GOBLINS,LIMBO)
  if  ((((((((((((((( EQP(s,BASILISK,1) ))))))))))))))) :
    opSET(s,BASILISK,0)
  else:
    if  ((((((((((((((( EQP(s,BASILISK,3) ))))))))))))))) :
      opSET(s,BASILISK,2)
  APPORT(s,FOG,PLAIN_1)
  opSET(s,FOG,8)
  ADD(s,DEATHS,1)
  if  ((((((((((((((( GTP(s,CLOSURE,1) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,CLOSURE,2) ))))))))))))))) :
      opSAY(s,DEAD_CLOSED)
    else:
      SUB(s,DEATHS,1)
    CALL(s,FINIS)
  LDA(s,I,YOUAREDEAD-2)
  ADD(s,I,DEATHS)
  ADD(s,I,DEATHS)
  opSAY(s,I)
  QUERY(s,SOK_,CORONER_2)
CORONER = mkLABEL('CORONER', label_CORONER)

def label_CORONER_2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    ADD(s,I,1)
    opSAY(s,I)
    opSAY(s,BLANK)
    LDA(s,J,SNIDELEY-1)
    if  ((((((((((((((( LTP(s,I,J) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,VASE) ))))))))))))))) :
        APPORT(s,VASE,LIMBO)
        opGET(s,POTTERY)
      for o in all_objects:
        LDA(s, I, o)
        if  ((((((((((((((( HAVEP(s,I) ))))))))))))))) :
          opDROP(s,I)
      APPORT(s,WATER,LIMBO)
      APPORT(s,OIL,LIMBO)
      opSET(s,INVCT,0)
      opSET(s,LAMP,0)
      APPORT(s,FOG,PLAIN_1)
      opSET(s,FOG,8)
      CALL(s,PHOG)
      opGOTO(s,BUILDING)
      opSET(s,THERE,0)
      APPORT(s,LAMP,ROAD)
      if  ((((((((((((((( EQP(s,LAMPLIFE,0) ))))))))))))))) :
        if  ((((((((((((((( BITP(s,LAMP,SPECIAL1)  or   not  BITP(s,LAIR,BEENHERE) ) )))))))))))))) :
          LOCATE(s,I,BATTERIES)
          if  ((((((((((((((( EQP(s,BATTERIES,1)  or   not  BITP(s,I,NOTINCAVE) ) )))))))))))))) :
            APPORT(s,LAMP,YLEM)
      APPORT(s,DWARF,LIMBO)
      opSET(s,DWARROWS,0)
      BIC(s,PIRATE,SPECIAL1)
      opQUIT(s)
    else:
      CALL(s,FINIS)
  else:
    CALL(s,FINIS)
  opSTOP(s)
CORONER_2 = mkLABEL('CORONER_2', label_CORONER_2)

def label_GETBIRD(s):
  NEAR(s,BIRD)
  if  ((((((((((((((( HAVEP(s,BIRD) ))))))))))))))) :
    opSAY(s,YOUHAVEIT)
    opQUIT(s)
  if  ((((((((((((((( EQP(s,BIRD,1) ))))))))))))))) :
    opGET(s,CAGE)
    opGET(s,BIRD)
    opSAY(s,OK)
  else:
    if  ((((((((((((((( HAVEP(s,CAGE) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,ROD) ))))))))))))))) :
        opSAY(s,BIRDISSCARED)
      else:
        BIC(s,BIRDCHAMBER,HINTABLE)
        opGET(s,BIRD)
        opSET(s,BIRD,1)
        opSAY(s,OK)
    else:
      opSAY(s,NEEDCAGE)
  opQUIT(s)
GETBIRD = mkLABEL('GETBIRD', label_GETBIRD)

def label_GETCAGE(s):
  NEAR(s,CAGE)
  if  ((((((((((((((( HAVEP(s,CAGE) ))))))))))))))) :
    opSAY(s,YOUHAVEIT)
    opQUIT(s)
  opGET(s,CAGE)
  if  ((((((((((((((( NEARP(s,BIRD) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,BIRD,1) ))))))))))))))) :
      opGET(s,BIRD)
  opSAY(s,OK)
  opQUIT(s)
GETCAGE = mkLABEL('GETCAGE', label_GETCAGE)

def label_GETKNIFE(s):
  if  ((((((((((((((( BITP(s,AXE,SEEN) ))))))))))))))) :
    opSAY(s,NO__KNIVES)
    opQUIT(s)
GETKNIFE = mkLABEL('GETKNIFE', label_GETKNIFE)

def label_DROPBIRD(s):
  HAVE(s,BIRD)
  opDROP(s,BIRD)
  opSET(s,BIRD,0)
  if  ((((((((((((((( NEARP(s,SNAKE) ))))))))))))))) :
    opSAY(s,BIRD__SNAKE)
    APPORT(s,SNAKE,LIMBO)
    BIC(s,MTKING,HINTABLE)
    opQUIT(s)
  else:
    if  ((((((((((((((( NEARP(s,DRAGON) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
        APPORT(s,BIRD,LIMBO)
        opSAY(s,BIRD__DRAGON)
        opQUIT(s)
  opSAY(s,OK)
  opQUIT(s)
DROPBIRD = mkLABEL('DROPBIRD', label_DROPBIRD)

def label_DROPCAGE(s):
  HAVE(s,CAGE)
  opDROP(s,CAGE)
  if  ((((((((((((((( HAVEP(s,BIRD) ))))))))))))))) :
    opDROP(s,BIRD)
  opSAY(s,OK)
  opQUIT(s)
DROPCAGE = mkLABEL('DROPCAGE', label_DROPCAGE)

def label_DROPVASE(s):
  HAVE(s,VASE)
  opDROP(s,VASE)
  if  ((((((((((((((( ATP(s,SOFT) ))))))))))))))) :
    opSAY(s,OK)
  else:
    if  ((((((((((((((( HAVEP(s,PILLOW)  or   not  NEARP(s,PILLOW) ) )))))))))))))) :
      opSET(s,VASE,2)
      opSAY(s,VASE)
      APPORT(s,VASE,LIMBO)
      APPORT(s,POTTERY,HERE)
    else:
      opSET(s,VASE,1)
      opSAY(s,VASE)
      opSET(s,VASE,0)
  opQUIT(s)
DROPVASE = mkLABEL('DROPVASE', label_DROPVASE)

def label_DROPLIQUID(s):
  HAVE(s,ARG2)
  APPORT(s,ARG2,LIMBO)
  opSET(s,BOTTLE,1)
  if  ((((((((((((((( NEARP(s,DWARF)  and  KEYP(s,THROW) ) )))))))))))))) :
    if  ((((((((((((((( EQP(s,DWARROWS,1) ))))))))))))))) :
      NAME(s,DOUSED_DWARF,ARG2)
    else:
      NAME(s,DOUSED_DWARVES,ARG2)
    BIS(s,DWARF,SPECIAL2)
  else:
    opSAY(s,POURWATER)
  opQUIT(s)
DROPLIQUID = mkLABEL('DROPLIQUID', label_DROPLIQUID)

def label_DROPBOTTLE(s):
  HAVE(s,BOTTLE)
  opDROP(s,BOTTLE)
  APPORT(s,OIL,LIMBO)
  APPORT(s,WATER,LIMBO)
  opSAY(s,OK)
  opQUIT(s)
DROPBOTTLE = mkLABEL('DROPBOTTLE', label_DROPBOTTLE)

def label_GETBOTTLE(s):
  NEAR(s,BOTTLE)
  if  ((((((((((((((( HAVEP(s,BOTTLE) ))))))))))))))) :
    opSAY(s,YOUHAVEIT)
    opQUIT(s)
  if  ((((((((((((((( LTP(s,INVCT,STRENGTH) ))))))))))))))) :
    opGET(s,BOTTLE)
    if  ((((((((((((((( EQP(s,BOTTLE,0) ))))))))))))))) :
      opGET(s,WATER)
    else:
      if  ((((((((((((((( EQP(s,BOTTLE,2) ))))))))))))))) :
        opGET(s,OIL)
    opSAY(s,OK)
  else:
    opSAY(s,ARMSAREFULL)
  opQUIT(s)
GETBOTTLE = mkLABEL('GETBOTTLE', label_GETBOTTLE)

def label_GETOIL(s):
  AT(s,EASTPIT)
  if  ((((((((((((((( HAVEP(s,BOTTLE) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,BOTTLE,1) ))))))))))))))) :
      opSET(s,BOTTLE,2)
      opGET(s,OIL)
      opSAY(s,BOTTLE__OIL)
    else:
      opSAY(s,BOTTLEWASFULL)
  else:
    opSAY(s,NOWAYTOCARRY)
  opQUIT(s)
GETOIL = mkLABEL('GETOIL', label_GETOIL)

def label_GETWATER(s):
  if  ((((((((((((((( BITP(s,HERE,H20HERE) ))))))))))))))) :
    pass
  else:
    opPROCEED(s)
  if  ((((((((((((((( HAVEP(s,BOTTLE) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,BOTTLE,1) ))))))))))))))) :
      opSET(s,BOTTLE,0)
      opGET(s,WATER)
      opSAY(s,BOTTLE__H20)
    else:
      opSAY(s,BOTTLEWASFULL)
  else:
    opSAY(s,NOWAYTOCARRY)
  opQUIT(s)
GETWATER = mkLABEL('GETWATER', label_GETWATER)

def label_KILLTROLL(s):
  opSAY(s,TROLL_DATA)
  opQUIT(s)
KILLTROLL = mkLABEL('KILLTROLL', label_KILLTROLL)

def label_KILLBEAR(s):
  if  ((((((((((((((( EQP(s,BEAR,0) ))))))))))))))) :
    opSAY(s,KILL__BEAR)
  else:
    opSAY(s,BEAR_PUZZLED)
  opQUIT(s)
KILLBEAR = mkLABEL('KILLBEAR', label_KILLBEAR)

def label_KILLSNAKE(s):
  opSAY(s,CANTKILLSNAKE)
  opQUIT(s)
KILLSNAKE = mkLABEL('KILLSNAKE', label_KILLSNAKE)

def label_KILLDRAGON(s):
  if  ((((((((((((((( GTP(s,DRAGON,0) ))))))))))))))) :
    opSAY(s,IT_IS_DEAD)
    opQUIT(s)
  QUERY(s,WITHWHAT_,KILLDRAGON_2)
KILLDRAGON = mkLABEL('KILLDRAGON', label_KILLDRAGON)

def label_KILLDRAGON_2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    opSET(s,DRAGON,1)
    opSAY(s,DRAGON)
    opSET(s,DRAGON,2)
    APPORT(s,RUG,SECRETCYNNE1)
    APPORT(s,TEETH,SECRETCYNNE1)
    BIC(s,DRAGON,SCHIZOID)
    for o in all_objects:
      LDA(s, I, o)
      if  ((((((((((((((( NEARP(s,I) ))))))))))))))) :
        if  ((((((((((((((( HAVEP(s,I) ))))))))))))))) :
          pass
        else:
          APPORT(s,I,SECRETCYNNE1)
    opGOTO(s,SECRETCYNNE1)
  else:
    opSAY(s,OK)
  opQUIT(s)
KILLDRAGON_2 = mkLABEL('KILLDRAGON_2', label_KILLDRAGON_2)

def label_KILLBIRD(s):
  if  ((((((((((((((( LTP(s,CLOSURE,3) ))))))))))))))) :
    APPORT(s,BIRD,LIMBO)
    opSAY(s,BIRDISDEAD)
  else:
    opSAY(s,LEAVE_BIRD)
  opQUIT(s)
KILLBIRD = mkLABEL('KILLBIRD', label_KILLBIRD)

def label_KILLBIVALVE(s):
  opSAY(s,KILL_OYSTER)
  opQUIT(s)
KILLBIVALVE = mkLABEL('KILLBIVALVE', label_KILLBIVALVE)

def label_KILLDWARF(s):
  QUERY(s,WITHWHAT_,KILLDWARF_2)
KILLDWARF = mkLABEL('KILLDWARF', label_KILLDWARF)

def label_KILLDWARF_2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    opSET(s,I,STRENGTH)
    SUB(s,I,INVCT)
    ADD(s,I,2)
    MULT(s,I,10)
    if  ((((((((((((((( CHANCEP(s,I) ))))))))))))))) :
      opSAY(s,KILLEDDWARF)
      SUB(s,DWARROWS,1)
      if  ((((((((((((((( EQP(s,DWARROWS,0) ))))))))))))))) :
        APPORT(s,DWARF,LIMBO)
      SUB(s,DWARFCOUNT,1)
    else:
      if  ((((((((((((((( CHANCEP(s,I) ))))))))))))))) :
        opSAY(s,DWARFDODGES)
      else:
        opSAY(s,DWARFSTABS)
        CALL(s,CORONER)
  else:
    opSAY(s,OK)
  opQUIT(s)
KILLDWARF_2 = mkLABEL('KILLDWARF_2', label_KILLDWARF_2)

def label_KILLOGRE(s):
  QUERY(s,WITHWHAT_,KILLOGRE_2)
KILLOGRE = mkLABEL('KILLOGRE', label_KILLOGRE)

def label_KILLOGRE_2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
      opSAY(s,OGRE_TOO_TOUGH)
    else:
      opSAY(s,OGRE_RIPS_HEAD_OFF)
      CALL(s,CORONER)
  else:
    opSAY(s,OK)
  opQUIT(s)
KILLOGRE_2 = mkLABEL('KILLOGRE_2', label_KILLOGRE_2)

def label_KILLBLOB(s):
  opSAY(s,BOUNCE_BLOB)
  opQUIT(s)
KILLBLOB = mkLABEL('KILLBLOB', label_KILLBLOB)

def label_KILLDJINN(s):
  opSAY(s,TOUGH_DJINN)
  opQUIT(s)
KILLDJINN = mkLABEL('KILLDJINN', label_KILLDJINN)

def label_KILLGOBLINS(s):
  opSAY(s,KILL_GOBLINS)
  CALL(s,CORONER)
KILLGOBLINS = mkLABEL('KILLGOBLINS', label_KILLGOBLINS)

def label_KILLBASILISK(s):
  if  ((((((((((((((( LTP(s,BASILISK,2) ))))))))))))))) :
    opSAY(s,HIT_BASILISK)
    CALL(s,CORONER)
  else:
    opSAY(s,IT_IS_DEAD)
    opQUIT(s)
KILLBASILISK = mkLABEL('KILLBASILISK', label_KILLBASILISK)

def label_HITGONG(s):
  if  ((((((((((((((( NEARP(s,TURTLE) ))))))))))))))) :
    opSAY(s,GONG_RINGS)
  else:
    opSAY(s,GONG_FETCH)
    APPORT(s,TURTLE,HERE)
  opQUIT(s)
HITGONG = mkLABEL('HITGONG', label_HITGONG)

def label_GETBEAR(s):
  NEAR(s,BEAR)
  if  ((((((((((((((( HAVEP(s,BEAR) ))))))))))))))) :
    opSAY(s,I_C_A_BEAR)
  else:
    if  ((((((((((((((( ATP(s,BEARHERE) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,BEAR,2) ))))))))))))))) :
        opSAY(s,OK)
        opGET(s,BEAR)
      else:
        opSAY(s,BEAR_IS_CHAINED)
    else:
      opSAY(s,OK)
      opGET(s,BEAR)
  opQUIT(s)
GETBEAR = mkLABEL('GETBEAR', label_GETBEAR)

def label_DROPBEAR(s):
  HAVE(s,BEAR)
  opDROP(s,BEAR)
  opSAY(s,OK)
  opQUIT(s)
DROPBEAR = mkLABEL('DROPBEAR', label_DROPBEAR)

def label_FREEDJINN(s):
  NEAR(s,DJINN)
  opSAY(s,DJINN_ADVICE)
  APPORT(s,DJINN,LIMBO)
  BIS(s,DJINN,SPECIAL1)
  opQUIT(s)
FREEDJINN = mkLABEL('FREEDJINN', label_FREEDJINN)

def label_GETCHAIN(s):
  AT(s,BEARHERE)
  NEAR(s,CHAIN)
  if  ((((((((((((((( EQP(s,CHAIN,0) ))))))))))))))) :
    opPROCEED(s)
  else:
    opSAY(s,CHAIN_LOCKED)
  opQUIT(s)
GETCHAIN = mkLABEL('GETCHAIN', label_GETCHAIN)

def label_GETSWORD(s):
  NEAR(s,SWORD)
  if  ((((((((((((((( EQP(s,SWORD,0)  and  LTP(s,INVCT,STRENGTH) )  and   not  HAVEP(s,SWORD) ) ))))))))))))) :
    if  ((((((((((((((( EQP(s,MUSHROOM,2) ))))))))))))))) :
      opSAY(s,GOT_THE_SWORD)
      opSET(s,SWORD,1)
      opGET(s,SWORD)
    else:
      opSAY(s,SWORD_IS_STUCK)
    opQUIT(s)
GETSWORD = mkLABEL('GETSWORD', label_GETSWORD)

def label_GETSCEPTRE(s):
  NEAR(s,SCEPTRE)
  if  ((((((((((((((( EQP(s,SCEPTRE,0)  and  LTP(s,INVCT,STRENGTH) ) )))))))))))))) :
    opGET(s,SCEPTRE)
    opSET(s,SCEPTRE,1)
    RANDOM(s,PASSWORD,5)
    if  ((((((((((((((( EQP(s,PASSWORD,0) ))))))))))))))) :
      LDA(s,PASSWORD,BLERBI)
    else:
      if  ((((((((((((((( EQP(s,PASSWORD,1) ))))))))))))))) :
        LDA(s,PASSWORD,KLAETU)
      else:
        if  ((((((((((((((( EQP(s,PASSWORD,2) ))))))))))))))) :
          LDA(s,PASSWORD,KNERL)
        else:
          if  ((((((((((((((( EQP(s,PASSWORD,3) ))))))))))))))) :
            LDA(s,PASSWORD,SNOEZE)
          else:
            LDA(s,PASSWORD,ZORTON)
    if  ((((((((((((((( EQP(s,SAFE,0) ))))))))))))))) :
      NAME(s,WHISPER,PASSWORD)
    else:
      opSAY(s,BLEW_SAFE)
    APPORT(s,SKELETON,LIMBO)
    opQUIT(s)
GETSCEPTRE = mkLABEL('GETSCEPTRE', label_GETSCEPTRE)

def label_SPLATTER(s):
  LDA(s,I,PLUMMET)
  ADD(s,I,DEATHS)
  opSAY(s,I)
  CALL(s,CORONER)
SPLATTER = mkLABEL('SPLATTER', label_SPLATTER)

def label_DO_CAMEO(s):
  if  ((((((((((((((( BITP(s,HERE,NOTINCAVE)  or  BITP(s,HERE,NODWARF) )  or  BITP(s,HERE,LIT) )  or  BITP(s,HERE,ONE_EXIT) )  or   not  HAVEP(s,LAMP) )  or  EQP(s,LAMP,0) )  or  BITP(s,PIRATE,SPECIAL1) )  or  NEARP(s,DWARF) )  or  NEARP(s,DRAGON) )  or  NEARP(s,TROLL) )  or  NEARP(s,SNAKE) )  or  NEARP(s,QUICKSAND) ) )))) :
    opPROCEED(s)
  opSET(s,CAMEO_TIME,0)
  LDA(s,I,CAMEO)
  RANDOM(s,J,LAST_CAMEO-CAMEO+1)
  ADD(s,I,J)
  opSAY(s,BLANK)
  opSAY(s,I)
  opSAY(s,BLANK)
DO_CAMEO = mkLABEL('DO_CAMEO', label_DO_CAMEO)

def label_CLOSE_THE_CAVE(s):
  opSAY(s,GO_REPOSIT)
  BIC(s,STATUS,FASTMODE)
  BIC(s,STATUS,QUICKIE)
  for o in all_objects:
    LDA(s, I, o)
    LOCATE(s,J,I)
    if  ((((((((((((((( BITP(s,J,NOTINCAVE)  or  HAVEP(s,I) )  and  BITP(s,I,PORTABLE) ) ))))))))))))) :
      APPORT(s,I,YLEM)
  for p in all_places:
    LDA(s, I, p)
    if  ((((((((((((((( BITP(s,I,NOTINCAVE) ))))))))))))))) :
      BIC(s,I,BEENHERE)
  opSET(s,CLOSURE,3)
  opSET(s,CLOCK,999)
  opGOTO(s,CYLINDRICAL)
  opSET(s,ESCAPE,0)
  opQUIT(s)
CLOSE_THE_CAVE = mkLABEL('CLOSE_THE_CAVE', label_CLOSE_THE_CAVE)

def label_CLOCK4(s):
  if  ((((((((((((((( EQP(s,CLOSURE,0) ))))))))))))))) :
    opSET(s,CLOSURE,1)
    for o in all_objects:
      LDA(s, I, o)
      if  ((((((((((((((( BITP(s,I,VALUED)  and   not  LOCP(s,I,BUILDING) ) )))))))))))))) :
        opSET(s,CLOSURE,0)
    if  ((((((((((((((( EQP(s,CLOSURE,1) ))))))))))))))) :
      opSET(s,CLOCK,35)
    else:
      RANDOM(s,CLOCK,10)
      ADD(s,CLOCK,30)
    if  ((((((((((((((( GTP(s,SCULPTURE,0) ))))))))))))))) :
      RANDOM(s,SCULPTURE,get_value(s, SCULPTURE)-1)
      ADD(s,SCULPTURE,1)
    if  ((((((((((((((( GTP(s,SWORD,0) ))))))))))))))) :
      RANDOM(s,SWORD,get_value(s, SWORD)-1)
      ADD(s,SWORD,1)
    if  ((((((((((((((( EQP(s,DRAGON,2) ))))))))))))))) :
      SUB(s,DRAGTIME,LASTCLOCK)
      if  ((((((((((((((( LTP(s,DRAGTIME,0) ))))))))))))))) :
        opSET(s,DRAGON,3)
    if  ((((((((((((((( BITP(s,DJINN,SPECIAL1)  and   not  BITP(s,DJINN,SPECIAL2) )  and   not  NEARP(s,DWARF) ) ))))))))))))) :
      BIS(s,DJINN,SPECIAL2)
      opSAY(s,PHUGGG_DATA)
      opSET(s,CLOCK,5)
      opPROCEED(s)
    if  ((((((((((((((( GTP(s,MUSHROOM,1) ))))))))))))))) :
      SUB(s,MUSHTIME,LASTCLOCK)
      if  ((((((((((((((( LTP(s,MUSHTIME,0) ))))))))))))))) :
        if  ((((((((((((((( EQP(s,MUSHROOM,2) ))))))))))))))) :
          opSET(s,MUSHROOM,3)
          opSET(s,MUSHTIME,40)
          opSAY(s,MUSHROOM)
          opSET(s,STRENGTH,7)
          opSET(s,CLOCK,8)
          opPROCEED(s)
        else:
          opSET(s,MUSHROOM,0)
          APPORT(s,MUSHROOM,CUBICLE)
    if  ((((((((((((((( GTP(s,CAMEO_TIME,0)  and  LTP(s,CAMEO_TIME,MOVES) ) )))))))))))))) :
      RANDOM(s,CLOCK,10)
      ADD(s,CLOCK,10)
      CALL(s,DO_CAMEO)
      opPROCEED(s)
    if  ((((((((((((((( BITP(s,MISTS,BEENHERE)  or  BITP(s,Y2,BEENHERE) ) )))))))))))))) :
      if  ((((((((((((((( GTP(s,MOVES,150)  and   not  BITP(s,CHEST,SEEN) ) )))))))))))))) :
        BIS(s,PIRATE,SPECIAL1)
      if  ((((((((((((((( BITP(s,HERE,NODWARF)  or  BITP(s,HERE,NOTINCAVE) ) )))))))))))))) :
        BIC(s,PIRATE,SPECIAL1)
        RANDOM(s,CLOCK,10)
        ADD(s,CLOCK,8)
      else:
        opSET(s,I,DWARFCOUNT)
        ADD(s,I,4)
        MULT(s,I,10)
        if  ((((((((((((((( CHANCEP(s,I)  or  BITP(s,PIRATE,SPECIAL1) ) )))))))))))))) :
          RANDOM(s,I,10)
          ADD(s,I,DWARROWS)
          if  ((((((((((((((( EQP(s,I,0)  or  BITP(s,PIRATE,SPECIAL1) ) )))))))))))))) :
            if  ((((((((((((((( BITP(s,CHEST,SEEN)  or  BITP(s,HERE,LIT) )  or   not  HAVEP(s,LAMP) )  or  EQP(s,LAMP,0) ) )))))))))))) :
              pass
            else:
              BIC(s,PIRATE,SPECIAL1)
              opSET(s,J,0)
              BIC(s,RING,VALUED)
              for o in all_objects:
                LDA(s, I, o)
                if  ((((((((((((((( BITP(s,I,VALUED)  and  NEARP(s,I) ) )))))))))))))) :
                  APPORT(s,I,MAZEA_114)
                  opSET(s,J,1)
              BIS(s,RING,VALUED)
              if  ((((((((((((((( EQP(s,J,0) ))))))))))))))) :
                if  ((((((((((((((( LOCP(s,CHEST,LIMBO) ))))))))))))))) :
                  opSAY(s,PIRATE_RUNS)
                else:
                  opSAY(s,RUSTLING)
                  BIS(s,PIRATE,SPECIAL1)
                  RANDOM(s,CLOCK,10)
                  ADD(s,CLOCK,4)
              else:
                opSAY(s,PIRATE__ZOTZ)
              if  ((((((((((((((( LOCP(s,CHEST,LIMBO) ))))))))))))))) :
                APPORT(s,CHEST,MAZEA_114)
                APPORT(s,MESSAGE,MAZED_140)
          else:
            if  ((((((((((((((( GTP(s,DWARFCOUNT,0) ))))))))))))))) :
              if  ((((((((((((((( BITP(s,AXE,SEEN) ))))))))))))))) :
                APPORT(s,DWARF,HERE)
                ADD(s,DWARROWS,1)
                if  ((((((((((((((( EQP(s,DWARROWS,1) ))))))))))))))) :
                  BIS(s,DWARF,SPECIAL1)
                  BIC(s,DWARF,SPECIAL2)
              else:
                APPORT(s,AXE,HERE)
                BIS(s,AXE,SEEN)
                opSAY(s,FIRSTDWARF)
  else:
    if  ((((((((((((((( EQP(s,CLOSURE,1) ))))))))))))))) :
      opSET(s,CLOSURE,2)
      opSET(s,GRATE,0)
      opSAY(s,CLOSING_NOW)
      if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
        opSAY(s,DWARF_QUITS)
      APPORT(s,DWARF,LIMBO)
      opSET(s,DWARROWS,0)
      opSET(s,DWARFCOUNT,0)
      opSET(s,FISSURE,0)
      opSET(s,GORGE,0)
      APPORT(s,TROLL,LIMBO)
      APPORT(s,DRAGON,LIMBO)
      opSET(s,TROLL,5)
      APPORT(s,TROLL2,SWOFCHASM)
      BIS(s,FISSURE,INVISIBLE)
      BIS(s,GORGE,INVISIBLE)
      opSET(s,CLOCK,25)
    else:
      if  ((((((((((((((( BITP(s,ADMIN,PANICED) ))))))))))))))) :
        BIC(s,ADMIN,PANICED)
        opSET(s,CLOCK,15)
      else:
        CALL(s,CLOSE_THE_CAVE)
  opSET(s,LASTCLOCK,CLOCK)
CLOCK4 = mkLABEL('CLOCK4', label_CLOCK4)

def label_BAILOUT(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    NAME(s,CLARIFY,ARG1)
  else:
    if  ((((((((((((((( EQP(s,STATUS,2)  and  BITP(s,ARG2,OBJECT) ) )))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        NAME(s,DUNNO_HAO,ARG1)
      else:
        NAME(s,IDONTSEE,ARG2)
    else:
      NAME(s,DUNNO_HAO,ARG1)
  opQUIT(s)
BAILOUT = mkLABEL('BAILOUT', label_BAILOUT)

def label_LAMPREY(s):
  if  ((((((((((((((( GTP(s,LAMPLIFE,0) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,BATTERIES,1) ))))))))))))))) :
      opSAY(s,LAMP_NOFUEL)
    else:
      if  ((((((((((((((( NEARP(s,BATTERIES) ))))))))))))))) :
        opSAY(s,LAMP_REFUEL)
        opSET(s,BATTERIES,1)
        ADD(s,LAMPLIFE,300)
        BIC(s,LAMP,SPECIAL1)
      else:
        if  ((((((((((((((( BITP(s,BATTERIES,SEEN) ))))))))))))))) :
          opSAY(s,LAMP_BATTERIES)
        else:
          opSAY(s,LAMP_IS_DIM)
  else:
    if  ((((((((((((((( EQP(s,CLOSURE,2) ))))))))))))))) :
      CALL(s,CLOSE_THE_CAVE)
    else:
      if  ((((((((((((((( NEARP(s,BATTERIES)  and  EQP(s,BATTERIES,0) ) )))))))))))))) :
        opSAY(s,LAMP_REFUEL)
        opSET(s,BATTERIES,1)
        ADD(s,LAMPLIFE,300)
      else:
        opSAY(s,LAMP_IS_DEAD)
        opSET(s,LAMP,0)
        BIS(s,ADMIN,RANOUT)
        CALL(s,PHOG)
LAMPREY = mkLABEL('LAMPREY', label_LAMPREY)

def label_READ_MAGAZINES(s):
  opSAY(s,MAG_DWARVISH)
  opQUIT(s)
READ_MAGAZINES = mkLABEL('READ_MAGAZINES', label_READ_MAGAZINES)

def label_READ_TABLET(s):
  opSAY(s,DARK_ROOM)
  opQUIT(s)
READ_TABLET = mkLABEL('READ_TABLET', label_READ_TABLET)

def label_READ_MESSAGE(s):
  opSAY(s,CHEST_ELSEWHERE)
READ_MESSAGE = mkLABEL('READ_MESSAGE', label_READ_MESSAGE)

def label_READ_MACHINE(s):
  opSAY(s,MACHINE_SIGN)
  opQUIT(s)
READ_MACHINE = mkLABEL('READ_MACHINE', label_READ_MACHINE)

def label_HINT_LOGIC(s):
  opSET(s,HINT_TIME,0)
  opSET(s,I,0)
  if  ((((((((((((((( ATP(s,DEPRESSION) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,GRATE,0) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,KEYS) ))))))))))))))) :
        pass
      else:
        LDA(s,I,LOOKINGCAVE)
  if  ((((((((((((((( ATP(s,BIRDCHAMBER) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,BIRD) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,BIRD,0) ))))))))))))))) :
        if  ((((((((((((((( HAVEP(s,ROD) ))))))))))))))) :
          LDA(s,I,BIRDHINT_)
  if  ((((((((((((((( ATP(s,MTKING) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,SNAKE) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,BIRD) ))))))))))))))) :
        pass
      else:
        LDA(s,I,GETPASTSNAKE)
  if  ((((((((((((((( ATP(s,WITTSEND) ))))))))))))))) :
    LDA(s,I,HINT_WITTS_)
  if  ((((((((((((((( ATP(s,PLOVER)  or  ATP(s,ALCOVE) )  or  ATP(s,DARK) ) ))))))))))))) :
    if  ((((((((((((((( BITP(s,DARK,BEENHERE) ))))))))))))))) :
      pass
    else:
      LDA(s,I,HINT_PLOVER_)
  if  ((((((((((((((( ATP(s,PLAIN_2) ))))))))))))))) :
    LDA(s,I,PLAIN_HINT)
  if  ((((((((((((((( BITP(s,HERE,INMAZE) ))))))))))))))) :
    LDA(s,I,HINT_MAZE_)
  LDA(s,J,SLIDE.rank-1)
  LDA(s,K,ICECAVE_30.rank+1)
  if  ((((((((((((((( GTP(s,HERE,J)  and  LTP(s,HERE,K) ) )))))))))))))) :
    LDA(s,I,ICE_HINT_)
  if  ((((((((((((((( GTP(s,I,0) ))))))))))))))) :
    QUERY(s,I,HINT_LOGIC_2)
HINT_LOGIC = mkLABEL('HINT_LOGIC', label_HINT_LOGIC)

def label_HINT_LOGIC_2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    VALUE(s,ILL_GIVE_HINT,HINT_COST)
    QUERY(s,WANT_HINT_,HINT_LOGIC_3)
  else:
    opQUIT(s)
HINT_LOGIC_2 = mkLABEL('HINT_LOGIC_2', label_HINT_LOGIC_2)

def label_HINT_LOGIC_3(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    ADD(s,I,1)
    opSAY(s,I)
    ADD(s,PENALTIES,HINT_COST)
    BIC(s,HERE,HINTABLE)
    if  ((((((((((((((( ATP(s,PLOVER)  or  ATP(s,ALCOVE) )  or  ATP(s,DARK) ) ))))))))))))) :
      BIC(s,PLOVER,HINTABLE)
      BIC(s,DARK,HINTABLE)
      BIC(s,ALCOVE,HINTABLE)
    else:
      if  ((((((((((((((( BITP(s,HERE,INMAZE) ))))))))))))))) :
        for p in all_places:
          LDA(s, I, p)
          if  ((((((((((((((( BITP(s,I,INMAZE) ))))))))))))))) :
            BIC(s,I,HINTABLE)
  opQUIT(s)
HINT_LOGIC_3 = mkLABEL('HINT_LOGIC_3', label_HINT_LOGIC_3)

def label_NO_MOVE_POSSIBLE(s):
  if  ((((((((((((((( NEARP(s,LAMP)  and  EQP(s,LAMP,1) )  or  BITP(s,HERE,LIT) ) ))))))))))))) :
    opSAY(s,NOCANGO)
  else:
    if  ((((((((((((((( CHANCEP(s,25) ))))))))))))))) :
      opSAY(s,CRUNCH)
      CALL(s,CORONER)
    else:
      opSAY(s,OOF_)
  if  ((((((((((((((( NEARP(s,LAMP)  and  EQP(s,LAMP,1) ) )))))))))))))) :
    SUB(s,LAMPLIFE,1)
    if  ((((((((((((((( EQP(s,LAMPLIFE,0)  or  EQP(s,LAMPLIFE,40) ) )))))))))))))) :
      CALL(s,LAMPREY)
  opQUIT(s)
NO_MOVE_POSSIBLE = mkLABEL('NO_MOVE_POSSIBLE', label_NO_MOVE_POSSIBLE)

def label_BREAK_VIAL(s):
  APPORT(s,VIAL,LIMBO)
  opSAY(s,VIAL_BANG)
  RANDOM(s,I,LAST_FUME-FIRST_FUME+1)
  LDA(s,J,FIRST_FUME)
  ADD(s,I,J)
  opSAY(s,I)
  opSAY(s,BLANK)
  if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,DWARROWS,1) ))))))))))))))) :
      opSET(s,VIAL,1)
    else:
      opSET(s,VIAL,2)
    opSAY(s,VIAL)
    APPORT(s,DWARF,LIMBO)
    SUB(s,DWARFCOUNT,DWARROWS)
    opSET(s,DWARROWS,0)
  if  ((((((((((((((( NEARP(s,TROLL) ))))))))))))))) :
    opSET(s,VIAL,3)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,BEAR) ))))))))))))))) :
    opSET(s,VIAL,4)
    if  ((((((((((((((( GTP(s,BEAR,0) ))))))))))))))) :
      opSET(s,VIAL,5)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,SNAKE) ))))))))))))))) :
    opSET(s,VIAL,6)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,BIRD) ))))))))))))))) :
    opSET(s,VIAL,7)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,SLIME) ))))))))))))))) :
    opSET(s,VIAL,8)
    opSAY(s,VIAL)
    APPORT(s,SLIME,LIMBO)
  if  ((((((((((((((( NEARP(s,DRAGON)  and  EQP(s,DRAGON,0) ) )))))))))))))) :
    opSET(s,VIAL,9)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,DJINN) ))))))))))))))) :
    opSET(s,VIAL,10)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,BASILISK)  and  LTP(s,BASILISK,2) ) )))))))))))))) :
    opSET(s,VIAL,11)
    opSAY(s,VIAL)
  if  ((((((((((((((( NEARP(s,GOBLINS) ))))))))))))))) :
    opSET(s,VIAL,12)
    opSAY(s,VIAL)
    APPORT(s,GOBLINS,LIMBO)
  opQUIT(s)
BREAK_VIAL = mkLABEL('BREAK_VIAL', label_BREAK_VIAL)

def label_DROPVIAL(s):
  if  ((((((((((((((( HAVEP(s,VIAL) ))))))))))))))) :
    if  ((((((((((((((( CHANCEP(s,10) ))))))))))))))) :
      opSAY(s,VIAL_EXPLODES)
      APPORT(s,VIAL,LIMBO)
      CALL(s,CORONER)
DROPVIAL = mkLABEL('DROPVIAL', label_DROPVIAL)

def label_WEAPONRY_2(s):
  if  ((((((((((((((( NEARP(s,BASILISK) ))))))))))))))) :
    if  ((((((((((((((( GTP(s,BASILISK,1) ))))))))))))))) :
      opSAY(s,IT_IS_DEAD)
      if  ((((((((((((((( KEYP(s,THROW) ))))))))))))))) :
        opGET(s,ARG2)
    else:
      NAME(s,AXE_BASILISK,ARG2)
      CALL(s,CORONER)
  else:
    if  ((((((((((((((( NEARP(s,DJINN) ))))))))))))))) :
      NAME(s,REBOUND,ARG2)
    else:
      if  ((((((((((((((( NEARP(s,GOBLINS) ))))))))))))))) :
        NAME(s,KILL_A_FEW,ARG2)
        CALL(s,CORONER)
      else:
        if  ((((((((((((((( KEYP(s,THROW) ))))))))))))))) :
          opGET(s,ARG2)
          opPROCEED(s)
        else:
          opSAY(s,OK)
  opQUIT(s)
WEAPONRY_2 = mkLABEL('WEAPONRY_2', label_WEAPONRY_2)

def label_WEAPONRY(s):
  if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
    if  ((((((((((((((( KEYP(s,THROW) ))))))))))))))) :
      opDROP(s,ARG2)
    if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
      opSET(s,I,STRENGTH)
      SUB(s,I,INVCT)
      MULT(s,I,5)
      opSET(s,J,DWARROWS)
      ADD(s,J,2)
      MULT(s,J,15)
      ADD(s,I,J)
      if  ((((((((((((((( KEYP(s,AXE)  or  KEYP(s,SWING) ) )))))))))))))) :
        ADD(s,I,15)
      if  ((((((((((((((( CHANCEP(s,I) ))))))))))))))) :
        opSAY(s,DWARF_POOF)
        SUB(s,DWARROWS,1)
        if  ((((((((((((((( EQP(s,DWARROWS,0) ))))))))))))))) :
          APPORT(s,DWARF,LIMBO)
        SUB(s,DWARFCOUNT,1)
      else:
        opSAY(s,DWARFDODGES)
        opSET(s,J,DWARROWS)
        ADD(s,J,1)
        RANDOM(s,J,J)
        if  ((((((((((((((( GTP(s,J,0) ))))))))))))))) :
          if  ((((((((((((((( EQP(s,J,1) ))))))))))))))) :
            opSAY(s,KNIFETHROWN)
          else:
            VALUE(s,KNIVESTHROWN,J)
          if  ((((((((((((((( BITP(s,DWARF,SPECIAL2) ))))))))))))))) :
            SUB(s,I,20)
          if  ((((((((((((((( CHANCEP(s,I)  or  BITP(s,DWARF,SPECIAL1) ) )))))))))))))) :
            if  ((((((((((((((( EQP(s,J,1) ))))))))))))))) :
              opSAY(s,MISSES)
            else:
              opSAY(s,KNIVESMISS)
            BIC(s,DWARF,SPECIAL1)
          else:
            opSAY(s,GETSYOU)
            CALL(s,CORONER)
    else:
      if  ((((((((((((((( NEARP(s,SNAKE) ))))))))))))))) :
        opSAY(s,CANTKILLSNAKE)
        if  ((((((((((((((( KEYP(s,THROW) ))))))))))))))) :
          opGET(s,ARG2)
      else:
        if  ((((((((((((((( NEARP(s,DRAGON) ))))))))))))))) :
          NAME(s,KILL_DRAGON,ARG2)
        else:
          if  ((((((((((((((( NEARP(s,BEAR) ))))))))))))))) :
            if  ((((((((((((((( EQP(s,BEAR,0) ))))))))))))))) :
              if  ((((((((((((((( KEYP(s,THROW) ))))))))))))))) :
                if  ((((((((((((((( KEYP(s,AXE) ))))))))))))))) :
                  opSAY(s,AXE__BEAR)
                  opSET(s,AXE,1)
                else:
                  opSAY(s,SWORD_MISSES)
              else:
                if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
                  opSAY(s,BEAR_MISSES)
                else:
                  opSAY(s,BEAR_GETS_YOU)
                  CALL(s,CORONER)
            else:
              opSAY(s,BEAR_PUZZLED)
            opQUIT(s)
          else:
            if  ((((((((((((((( NEARP(s,TROLL) ))))))))))))))) :
              opSAY(s,TROLL_DATA)
            else:
              if  ((((((((((((((( NEARP(s,OGRE) ))))))))))))))) :
                if  ((((((((((((((( KEYP(s,SWING) ))))))))))))))) :
                  NAME(s,OGRE_REBUFF,ARG2)
                  CALL(s,CORONER)
                else:
                  if  ((((((((((((((( KEYP(s,AXE) ))))))))))))))) :
                    NAME(s,OGRE_CATCH,ARG2)
                    CALL(s,CORONER)
                  else:
                    opSAY(s,OGRE_KILLED)
                    APPORT(s,SWORD,LIMBO)
                    APPORT(s,OGRE,LIMBO)
                    APPORT(s,RING,HERE)
                    opQUIT(s)
              else:
                if  ((((((((((((((( NEARP(s,BLOB) ))))))))))))))) :
                  NAME(s,SLICE_BLOB,ARG2)
                  opQUIT(s)
                else:
                  CALL(s,WEAPONRY_2)
                  opPROCEED(s)
  else:
    NAME(s,YOUDONTHAVE,ARG2)
  opQUIT(s)
WEAPONRY = mkLABEL('WEAPONRY', label_WEAPONRY)

def label_PASSPHRASE(s):
  if  ((((((((((((((( NEARP(s,SAFE) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,SAFE,0) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,STATUS,2)  and  EQP(s,ARG2,PASSWORD) )  or  EQP(s,ARG1,PASSWORD) ) ))))))))))))) :
        opSAY(s,SAFE_OPENS)
        opSET(s,SAFE,1)
        BIS(s,SAFE,SPECIAL1)
        opQUIT(s)
      else:
        if  ((((((((((((((( BITP(s,SAFE,SPECIAL1) ))))))))))))))) :
          pass
        else:
          opSAY(s,SAFE_FUSES)
          opSET(s,SAFE,2)
          opSET(s,BLOB,1)
          BIS(s,ADMIN,TICKER)
          BIS(s,ADMIN,NOMAGIC)
          opSET(s,GRATE,0)
          opQUIT(s)
  opSAY(s,NOTHING)
  opQUIT(s)
PASSPHRASE = mkLABEL('PASSPHRASE', label_PASSPHRASE)

def label_TICK(s):
  if  ((((((((((((((( GTP(s,BLOB,0) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,BLOB,16) ))))))))))))))) :
      opSET(s,BLOB,17)
      opSAY(s,BLOB)
      CALL(s,CORONER)
    opSAY(s,BLOB)
    ADD(s,BLOB,1)
TICK = mkLABEL('TICK', label_TICK)

def label_PRESAY(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    NAME(s,SAID,ARG2)
PRESAY = mkLABEL('PRESAY', label_PRESAY)

def label_PLUNGE(s):
  opGOTO(s,YLEM)
  if  ((((((((((((((( EQP(s,LAMP,1) ))))))))))))))) :
    opSET(s,LAMPLIFE,0)
    if  ((((((((((((((( HAVEP(s,LAMP) ))))))))))))))) :
      opSAY(s,FALL_STARVE)
    else:
      opSAY(s,FALL_STARVED)
  else:
    opSAY(s,FALL_STARVED)
  CALL(s,CORONER)
PLUNGE = mkLABEL('PLUNGE', label_PLUNGE)

def label_UPCHUCK(s):
  opSET(s,I,0)
  if  ((((((((((((((( ATP(s,PIT) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,MISTS)
  if  ((((((((((((((( ATP(s,EASTOFFISSURE) ))))))))))))))) :
    LDA(s,I,THROW_FISSURE)
    LDA(s,J,CAVERN)
  if  ((((((((((((((( ATP(s,WESTOFFISSURE) ))))))))))))))) :
    LDA(s,I,THROW_FISSURE)
    LDA(s,J,CAVERN)
  if  ((((((((((((((( ATP(s,WEND2PIT) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,WESTPIT)
  if  ((((((((((((((( ATP(s,EEND2PIT) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,EASTPIT)
  if  ((((((((((((((( ATP(s,LOWNSPASSAGE) ))))))))))))))) :
    LDA(s,I,THROW_HOLE)
    LDA(s,J,DIRTY)
  if  ((((((((((((((( ATP(s,WINDOW) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,MIRRORCNYN)
  if  ((((((((((((((( ATP(s,WINDOW2) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,MIRRORCNYN)
  if  ((((((((((((((( ATP(s,BRINK) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,STREAMPIT)
  if  ((((((((((((((( ATP(s,DUSTY) ))))))))))))))) :
    LDA(s,I,THROW_HOLE)
    LDA(s,J,COMPLEX)
  if  ((((((((((((((( ATP(s,MAZEA_57_PIT) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,BIRDCHAMBER)
  if  ((((((((((((((( ATP(s,SECRETNSCYN) ))))))))))))))) :
    LDA(s,I,THROW_ROOM)
    LDA(s,J,SLAB)
  if  ((((((((((((((( ATP(s,SECRETNSCPAS) ))))))))))))))) :
    LDA(s,I,THROW_ROOM)
    LDA(s,J,BEDQUILT)
  if  ((((((((((((((( ATP(s,SECRETEW_TITE) ))))))))))))))) :
    LDA(s,I,THROW_CANYON)
    LDA(s,J,NSCANYONWIDE)
  if  ((((((((((((((( ATP(s,INCLINE) ))))))))))))))) :
    LDA(s,I,THROW_ROOM)
    LDA(s,J,LOW)
  if  ((((((((((((((( ATP(s,CAVERN) ))))))))))))))) :
    LDA(s,I,THROW_WHIRLPOOL)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,MISTY) ))))))))))))))) :
    LDA(s,I,THROW_CAVERN)
    LDA(s,J,CAVERN)
  if  ((((((((((((((( ATP(s,STALACT) ))))))))))))))) :
    LDA(s,I,THROW_ROOM)
    LDA(s,J,MAZEA_53)
  if  ((((((((((((((( ATP(s,RESERVOIR)  or  ATP(s,RESERVOIR_N) ) )))))))))))))) :
    LDA(s,I,THROW_RESERVOIR)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,BALCONY) ))))))))))))))) :
    LDA(s,I,THROW_ROOM)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,SWOFCHASM) ))))))))))))))) :
    LDA(s,I,THROW_CHASM)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,NEOFCHASM) ))))))))))))))) :
    LDA(s,I,THROW_CHASM)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,BREATHTAKER) ))))))))))))))) :
    LDA(s,I,THROW_GORGE)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,FACES) ))))))))))))))) :
    LDA(s,I,THROW_GORGE)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,TUBE) ))))))))))))))) :
    LDA(s,I,THROW_CHIMNEY)
    LDA(s,J,CHIMNEY)
  if  ((((((((((((((( ATP(s,TUBE_SLIDE) ))))))))))))))) :
    LDA(s,I,THROW_TUBE)
    LDA(s,J,PLAIN_1)
  if  ((((((((((((((( ATP(s,BASQUE_FORK) ))))))))))))))) :
    LDA(s,I,THROW_STEPS)
    LDA(s,J,ON_STEPS)
  if  ((((((((((((((( ATP(s,ON_STEPS) ))))))))))))))) :
    LDA(s,I,THROW_STEPS)
    LDA(s,J,STEPS_EXIT)
  if  ((((((((((((((( ATP(s,STEPS_EXIT) ))))))))))))))) :
    LDA(s,I,THROW_STEPS)
    LDA(s,J,STORAGE)
  if  ((((((((((((((( ATP(s,BRINK_1) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,BRINK_2) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,ICE) ))))))))))))))) :
    LDA(s,I,THROW_SLIDE)
    LDA(s,J,SLIDE)
  if  ((((((((((((((( ATP(s,BRINK_3) ))))))))))))))) :
    LDA(s,I,THROW_PIT)
    LDA(s,J,YLEM)
  if  ((((((((((((((( ATP(s,SHELF) ))))))))))))))) :
    LDA(s,I,THROW_BEACH)
    LDA(s,J,BEACH)
  if  ((((((((((((((( ATP(s,PLATFORM) ))))))))))))))) :
    LDA(s,I,THROW_GORGE)
    LDA(s,J,YLEM)
  if  ((((((((((((((( EQP(s,I,0)  or  KEYP(s,BEAR) ) )))))))))))))) :
    opPROCEED(s)
  NAME(s,I,ARG2)
  APPORT(s,ARG2,J)
  if  ((((((((((((((( KEYP(s,VASE) ))))))))))))))) :
    APPORT(s,VASE,YLEM)
    APPORT(s,SHARDS,J)
    LDA(s,I,YLEM)
    if  ((((((((((((((( EQP(s,I,J) ))))))))))))))) :
      pass
    else:
      opSAY(s,SHATTERED_IT)
  if  ((((((((((((((( KEYP(s,BOTTLE) ))))))))))))))) :
    APPORT(s,OIL,LIMBO)
    APPORT(s,WATER,LIMBO)
  if  ((((((((((((((( KEYP(s,OIL)  or  KEYP(s,WATER) ) )))))))))))))) :
    opSET(s,BOTTLE,1)
    APPORT(s,ARG2,LIMBO)
  if  ((((((((((((((( KEYP(s,CAGE)  and  HAVEP(s,BIRD) ) )))))))))))))) :
    APPORT(s,BIRD,J)
  if  ((((((((((((((( KEYP(s,LAMP)  and  EQP(s,LAMP,1) )  and   not  BITP(s,HERE,LIT) ) ))))))))))))) :
    opSAY(s,ITISNOWDARK)
  if  ((((((((((((((( KEYP(s,BIRD) ))))))))))))))) :
    opSET(s,BIRD,0)
  opQUIT(s)
UPCHUCK = mkLABEL('UPCHUCK', label_UPCHUCK)

def label_GROPE_FOR_IT(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opSAY(s,CANT_SEE_ANYTHING)
    opQUIT(s)
  if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
    if  ((((((((((((((( HAVEP(s,ARG2)  or   not  BITP(s,ARG2,PORTABLE) ) )))))))))))))) :
      opPROCEED(s)
    opSET(s,I,INVCT)
    SUB(s,I,STRENGTH)
    MULT(s,I,5)
    ADD(s,I,60)
    if  ((((((((((((((( CHANCEP(s,I) ))))))))))))))) :
      NAME(s,GROPE_FALL,ARG2)
      CALL(s,CORONER)
    else:
      if  ((((((((((((((( CHANCEP(s,50)  or   not  NEARP(s,ARG2) ) )))))))))))))) :
        NAME(s,GROPE_MISS,ARG2)
        opQUIT(s)
      else:
        NAME(s,GROPE_FIND,ARG2)
        opPROCEED(s)
GROPE_FOR_IT = mkLABEL('GROPE_FOR_IT', label_GROPE_FOR_IT)

def label_CAVERN2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    LDA(s,J,LAMP)
    opSET(s,K,0)
    for o in all_objects:
      LDA(s, I, o)
      if  ((((((((((((((( HAVEP(s,I)  and   not  EQP(s,I,J) ) )))))))))))))) :
        APPORT(s,I,YLEM)
        ADD(s,K,1)
    if  ((((((((((((((( HAVEP(s,LAMP) ))))))))))))))) :
      opSET(s,INVCT,1)
      if  ((((((((((((((( EQP(s,K,0) ))))))))))))))) :
        opSAY(s,FLOW_DOWN)
      else:
        opSAY(s,FLOW_RIP)
    else:
      opSET(s,INVCT,0)
      if  ((((((((((((((( EQP(s,K,0) ))))))))))))))) :
        opSAY(s,FLOW_DARK)
      else:
        opSAY(s,FLOW_D_RIP)
    opGOTO(s,RESERVOIR_N)
    opSAY(s,WHIRL_LAND)
  else:
    opSAY(s,OK)
  opQUIT(s)
CAVERN2 = mkLABEL('CAVERN2', label_CAVERN2)

def at_func_ROAD(s):
  MOVE(s,ROAD,HILL)
  MOVE(s,WEST,HILL)
  MOVE(s,UP,HILL)
  MOVE(s,ENTER,BUILDING)
  MOVE(s,BUILDING,BUILDING)
  MOVE(s,INWARD,BUILDING)
  MOVE(s,EAST,BUILDING)
  MOVE(s,DOWNSTREAM,VALLEY)
  MOVE(s,GULLY,VALLEY)
  MOVE(s,STREAM,VALLEY)
  MOVE(s,SOUTH,VALLEY)
  MOVE(s,DOWN,VALLEY)
  MOVE(s,FOREST,FOREST)
  MOVE(s,NORTH,FOREST)
  MOVE(s,EAST,FOREST)
  MOVE(s,DEPRESSION,DEPRESSION)
at_ROAD = mkAT('ROAD', at_func_ROAD)

def at_func_HILL(s):
  MOVE(s,ROAD,ROAD)
  MOVE(s,BUILDING,ROAD)
  MOVE(s,FORWARD,ROAD)
  MOVE(s,EAST,ROAD)
  MOVE(s,NORTH,ROAD)
  MOVE(s,FOREST,FOREST)
  MOVE(s,NORTH,FOREST)
  MOVE(s,SOUTH,FOREST)
at_HILL = mkAT('HILL', at_func_HILL)

def at_func_BUILDING(s):
  MOVE(s,ROAD,ROAD)
  MOVE(s,OUT,ROAD)
  MOVE(s,OUTDOORS,ROAD)
  MOVE(s,WEST,ROAD)
  if  ((((((((((((((( LTP(s,CLOSURE,2) ))))))))))))))) :
    SMOVE(s,XYZZY,DEBRIS,FOOF)
    SMOVE(s,PLUGH,Y2,FOOF)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,DEBRIS)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANTGOBACK)
      opQUIT(s)
    LDA(s,I,Y2)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANTGOBACK)
      opQUIT(s)
at_BUILDING = mkAT('BUILDING', at_func_BUILDING)

def at_func_BUILDING_1(s):
  ANYOF(s,[STREAM,DOWNSTREAM ])
  opSAY(s,PIPEFIT)
  opQUIT(s)
at_BUILDING_1 = mkAT('BUILDING', at_func_BUILDING_1)

def at_func_VALLEY(s):
  MOVE(s,UPSTREAM,ROAD)
  MOVE(s,BUILDING,ROAD)
  MOVE(s,NORTH,ROAD)
  MOVE(s,FOREST,FOREST)
  MOVE(s,EAST,FOREST)
  MOVE(s,WEST,FOREST)
  MOVE(s,UP,FOREST)
  MOVE(s,DEPRESSION,DEPRESSION)
  ANYOF(s,[SOUTH,DOWN,DOWNSTREAM ])
  if  ((((((((((((((( LTP(s,CLOSURE,2) ))))))))))))))) :
    opGOTO(s,SLIT)
  else:
    opGOTO(s,FAKE_SLIT)
  opQUIT(s)
at_VALLEY = mkAT('VALLEY', at_func_VALLEY)

def at_func_FOREST(s):
  MOVE(s,VALLEY,VALLEY)
  MOVE(s,EAST,VALLEY)
  MOVE(s,DOWN,VALLEY)
  MOVE(s,WEST,FOREST)
  MOVE(s,SOUTH,FOREST)
at_FOREST = mkAT('FOREST', at_func_FOREST)

def at_func_FOREST_1(s):
  ANYOF(s,[FOREST,FORWARD,NORTH ])
  if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
    opGOTO(s,FOREST)
  else:
    opGOTO(s,FOREST2)
  opQUIT(s)
at_FOREST_1 = mkAT('FOREST', at_func_FOREST_1)

def at_func_FOREST2(s):
  MOVE(s,ROAD,ROAD)
  MOVE(s,NORTH,ROAD)
  MOVE(s,VALLEY,VALLEY)
  MOVE(s,EAST,VALLEY)
  MOVE(s,WEST,VALLEY)
  MOVE(s,DOWN,VALLEY)
  MOVE(s,FOREST,FOREST)
  MOVE(s,SOUTH,FOREST)
at_FOREST2 = mkAT('FOREST2', at_func_FOREST2)

def at_func_SLIT(s):
  MOVE(s,BUILDING,ROAD)
  MOVE(s,UPSTREAM,VALLEY)
  MOVE(s,NORTH,VALLEY)
  MOVE(s,FOREST,FOREST)
  MOVE(s,EAST,FOREST)
  MOVE(s,WEST,FOREST)
  MOVE(s,DOWNSTREAM,DEPRESSION)
  MOVE(s,ROCK,DEPRESSION)
  MOVE(s,BED,DEPRESSION)
  MOVE(s,SOUTH,DEPRESSION)
at_SLIT = mkAT('SLIT', at_func_SLIT)

def at_func_FAKE_SLIT(s):
  MOVE(s,BUILDING,ROAD)
  MOVE(s,UPSTREAM,VALLEY)
  MOVE(s,NORTH,VALLEY)
  MOVE(s,FOREST,FOREST)
  MOVE(s,EAST,FOREST)
  MOVE(s,WEST,FOREST)
  MOVE(s,DOWNSTREAM,DEPRESSION)
  MOVE(s,ROCK,DEPRESSION)
  MOVE(s,BED,DEPRESSION)
  MOVE(s,SOUTH,DEPRESSION)
at_FAKE_SLIT = mkAT('FAKE_SLIT', at_func_FAKE_SLIT)

def at_func_SLIT_1(s):
  ANYOF(s,[SLIT,STREAM,DOWN,ENTER ])
  opSAY(s,DONTFITSLIT)
  opQUIT(s)
at_SLIT_1 = mkAT('SLIT', at_func_SLIT_1)

def at_func_FAKE_SLIT_1(s):
  ANYOF(s,[SLIT,STREAM,DOWN,ENTER ])
  opSET(s,CLOSURE,5)
  BIC(s,STATUS,FASTMODE)
  BIC(s,STATUS,QUICKIE)
  opSAY(s,TREASUREROOM)
  opSET(s,QUITTING,0)
  CALL(s,FINIS)
at_FAKE_SLIT_1 = mkAT('FAKE_SLIT', at_func_FAKE_SLIT_1)

def at_func_DEPRESSION(s):
  MOVE(s,FOREST,FOREST)
  MOVE(s,EAST,FOREST2)
  MOVE(s,WEST,FOREST)
  MOVE(s,SOUTH,FOREST2)
  MOVE(s,BUILDING,ROAD)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,INCAVE)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,GRATE,0) ) )))))))))))))) :
      opSAY(s,CANTPASSLOCK)
      opQUIT(s)
  ANYOF(s,[UPSTREAM,GULLY,NORTH,SLIT ])
  if  ((((((((((((((( LTP(s,CLOSURE,2) ))))))))))))))) :
    opGOTO(s,SLIT)
  else:
    opGOTO(s,FAKE_SLIT)
  opQUIT(s)
at_DEPRESSION = mkAT('DEPRESSION', at_func_DEPRESSION)

def at_func_DEPRESSION_1(s):
  ANYOF(s,[IN,DOWN,ENTER ])
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    opGOTO(s,INCAVE)
  else:
    opSAY(s,CANTPASSLOCK)
  opQUIT(s)
at_DEPRESSION_1 = mkAT('DEPRESSION', at_func_DEPRESSION_1)

def at_func_INCAVE(s):
  ANYOF(s,[UP,OUT,LEAVE,SURFACE ])
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    opGOTO(s,DEPRESSION)
  else:
    opSAY(s,CANTPASSLOCK)
  opQUIT(s)
at_INCAVE = mkAT('INCAVE', at_func_INCAVE)

def at_func_INCAVE_1(s):
  MOVE(s,CRAWL,COBBLES)
  MOVE(s,COBBLES,COBBLES)
  MOVE(s,INWARD,COBBLES)
  MOVE(s,WEST,COBBLES)
  MOVE(s,PIT,PIT)
  MOVE(s,DEBRIS,DEBRIS)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,DEPRESSION)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,GRATE,0) ) )))))))))))))) :
      opSAY(s,CANTPASSLOCK)
      opQUIT(s)
at_INCAVE_1 = mkAT('INCAVE', at_func_INCAVE_1)

def at_func_COBBLES(s):
  MOVE(s,OUT,INCAVE)
  MOVE(s,SURFACE,INCAVE)
  MOVE(s,NULL,INCAVE)
  MOVE(s,ENTRANCE,INCAVE)
  MOVE(s,EAST,INCAVE)
  MOVE(s,INWARD,DEBRIS)
  MOVE(s,DARK,DEBRIS)
  MOVE(s,WEST,DEBRIS)
  MOVE(s,DEBRIS,DEBRIS)
  MOVE(s,PIT,PIT)
at_COBBLES = mkAT('COBBLES', at_func_COBBLES)

def at_func_DEBRIS(s):
  MOVE(s,ENTRANCE,INCAVE)
  MOVE(s,CRAWL,COBBLES)
  MOVE(s,COBBLES,COBBLES)
  MOVE(s,PASSAGE,COBBLES)
  MOVE(s,LOW,COBBLES)
  MOVE(s,EAST,COBBLES)
  MOVE(s,CANYON,CANYON)
  MOVE(s,INWARD,CANYON)
  MOVE(s,UP,CANYON)
  MOVE(s,WEST,CANYON)
  MOVE(s,PIT,PIT)
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    MOVE(s,DEPRESSION,DEPRESSION)
  else:
    SMOVE(s,DEPRESSION,INCAVE,CANTPASSLOCK)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,BUILDING)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANTGOBACK)
      opQUIT(s)
at_DEBRIS = mkAT('DEBRIS', at_func_DEBRIS)

def at_func_DEBRIS_1(s):
  KEYWORD(s,XYZZY)
  if  ((((((((((((((( GTP(s,CLOSURE,1)  or  BITP(s,ADMIN,NOMAGIC) ) )))))))))))))) :
    opSAY(s,NOTHING)
    BIS(s,ADMIN,PANICED)
    opQUIT(s)
  else:
    SMOVE(s,XYZZY,BUILDING,FOOF)
  opQUIT(s)
at_DEBRIS_1 = mkAT('DEBRIS', at_func_DEBRIS_1)

def at_func_CANYON(s):
  MOVE(s,ENTRANCE,INCAVE)
  MOVE(s,DOWN,DEBRIS)
  MOVE(s,EAST,DEBRIS)
  MOVE(s,DEBRIS,DEBRIS)
  MOVE(s,INWARD,BIRDCHAMBER)
  MOVE(s,UP,BIRDCHAMBER)
  MOVE(s,WEST,BIRDCHAMBER)
  MOVE(s,PIT,PIT)
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    MOVE(s,DEPRESSION,DEPRESSION)
  else:
    SMOVE(s,DEPRESSION,INCAVE,CANTPASSLOCK)
at_CANYON = mkAT('CANYON', at_func_CANYON)

def at_func_BIRDCHAMBER(s):
  MOVE(s,ENTRANCE,INCAVE)
  MOVE(s,DEBRIS,DEBRIS)
  MOVE(s,CANYON,CANYON)
  MOVE(s,EAST,CANYON)
  MOVE(s,PASSAGE,PIT)
  MOVE(s,PIT,PIT)
  MOVE(s,WEST,PIT)
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    MOVE(s,DEPRESSION,DEPRESSION)
  else:
    SMOVE(s,DEPRESSION,INCAVE,CANTPASSLOCK)
at_BIRDCHAMBER = mkAT('BIRDCHAMBER', at_func_BIRDCHAMBER)

def at_func_PIT(s):
  MOVE(s,ENTRANCE,INCAVE)
  MOVE(s,DEBRIS,DEBRIS)
  MOVE(s,PASSAGE,BIRDCHAMBER)
  MOVE(s,EAST,BIRDCHAMBER)
  MOVE(s,DOWN,MISTS)
  if  ((((((((((((((( EQP(s,GRATE,1) ))))))))))))))) :
    MOVE(s,DEPRESSION,DEPRESSION)
  else:
    SMOVE(s,DEPRESSION,INCAVE,CANTPASSLOCK)
at_PIT = mkAT('PIT', at_func_PIT)

def at_func_PIT_1(s):
  ANYOF(s,[DOWN,STEPS,PIT ])
  if  ((((((((((((((( HAVEP(s,GOLD) ))))))))))))))) :
    opSAY(s,BROKENECK)
    opGOTO(s,MISTS)
    CALL(s,CORONER)
  else:
    opGOTO(s,MISTS)
  opQUIT(s)
at_PIT_1 = mkAT('PIT', at_func_PIT_1)

def at_func_PIT_2(s):
  ANYOF(s,[WEST,CRACK ])
  opSAY(s,MISTCRACK)
  opQUIT(s)
at_PIT_2 = mkAT('PIT', at_func_PIT_2)

def at_func_PIT_3(s):
  KEYWORD(s,JUMP)
  opGOTO(s,MISTS)
  CALL(s,SPLATTER)
  opQUIT(s)
at_PIT_3 = mkAT('PIT', at_func_PIT_3)

def at_func_MISTS(s):
  MOVE(s,LEFT,GOLDROOM)
  MOVE(s,SOUTH,GOLDROOM)
  MOVE(s,EAST,SANDSTONE)
  MOVE(s,FORWARD,EASTOFFISSURE)
  MOVE(s,HALL,EASTOFFISSURE)
  MOVE(s,WEST,EASTOFFISSURE)
  MOVE(s,STAIRS,MTKING)
  MOVE(s,DOWN,MTKING)
  MOVE(s,NORTH,MTKING)
  MOVE(s,Y2,JUMBLE)
at_MISTS = mkAT('MISTS', at_func_MISTS)

def at_func_MISTS_1(s):
  ANYOF(s,[UP,PIT,STEPS,DOME,PASSAGE,ENTER ])
  if  ((((((((((((((( HAVEP(s,GOLD) ))))))))))))))) :
    opSAY(s,UNCLIMBABLE)
  else:
    opGOTO(s,PIT)
  opQUIT(s)
at_MISTS_1 = mkAT('MISTS', at_func_MISTS_1)

def at_func_EASTOFFISSURE(s):
  MOVE(s,HALL,MISTS)
  MOVE(s,EAST,MISTS)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,WESTOFFISSURE)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,FISSURE,0) ) )))))))))))))) :
      opSAY(s,NOWAYACROSS)
      opQUIT(s)
at_EASTOFFISSURE = mkAT('EASTOFFISSURE', at_func_EASTOFFISSURE)

def at_func_EASTOFFISSURE_1(s):
  ANYOF(s,[FORWARD,OVER,WEST ])
  if  ((((((((((((((( EQP(s,FISSURE,0) ))))))))))))))) :
    opSAY(s,NOWAYACROSS)
  else:
    opGOTO(s,WESTOFFISSURE)
  opQUIT(s)
at_EASTOFFISSURE_1 = mkAT('EASTOFFISSURE', at_func_EASTOFFISSURE_1)

def at_func_EASTOFFISSURE_2(s):
  KEYWORD(s,JUMP)
  if  ((((((((((((((( EQP(s,FISSURE,1) ))))))))))))))) :
    opSAY(s,TRYTHEBRIDGE)
  else:
    opGOTO(s,CAVERN)
    CALL(s,SPLATTER)
  opQUIT(s)
at_EASTOFFISSURE_2 = mkAT('EASTOFFISSURE', at_func_EASTOFFISSURE_2)

def at_func_GOLDROOM(s):
  MOVE(s,HALL,MISTS)
  MOVE(s,OUT,MISTS)
  MOVE(s,NORTH,MISTS)
at_GOLDROOM = mkAT('GOLDROOM', at_func_GOLDROOM)

def at_func_MTKING(s):
  MOVE(s,STAIRS,MISTS)
  MOVE(s,UP,MISTS)
  MOVE(s,EAST,MISTS)
at_MTKING = mkAT('MTKING', at_func_MTKING)

def at_func_MTKING_1(s):
  ANYOF(s,[NORTH,LEFT,SOUTH,RIGHT,WEST,FORWARD,SW,SECRET ,NW,SE,NE,DOWN ])
  if  ((((((((((((((( NEARP(s,SNAKE) ))))))))))))))) :
    opSAY(s,SNAKEBLOCKS)
    opQUIT(s)
  else:
    MOVE(s,NORTH,LOWNSPASSAGE)
    MOVE(s,LEFT,LOWNSPASSAGE)
    MOVE(s,SOUTH,SOUTHSIDE)
    MOVE(s,RIGHT,SOUTHSIDE)
    MOVE(s,WEST,WESTSIDE)
    MOVE(s,FORWARD,WESTSIDE)
    MOVE(s,DOWN,VAULT)
    MOVE(s,NORTHEAST,MORION)
    MOVE(s,NORTHWEST,CORRID_3)
    MOVE(s,SOUTHEAST,CORRID_1)
    MOVE(s,SECRET,SECRETEW_TITE)
    if  ((((((((((((((( CHANCEP(s,35) ))))))))))))))) :
      MOVE(s,SW,SECRETEW_TITE)
    else:
      opSAY(s,YOUDIDNTMOVE)
    opQUIT(s)
at_MTKING_1 = mkAT('MTKING', at_func_MTKING_1)

def at_func_WEND2PIT(s):
  MOVE(s,EAST,EEND2PIT)
  MOVE(s,CROSS,EEND2PIT)
  MOVE(s,WEST,SLAB)
  MOVE(s,SLAB,SLAB)
  MOVE(s,DOWN,WESTPIT)
  MOVE(s,PIT,WESTPIT)
at_WEND2PIT = mkAT('WEND2PIT', at_func_WEND2PIT)

def at_func_WEND2PIT_1(s):
  KEYWORD(s,HOLE)
  opSAY(s,TOO_FAR_UP)
  opQUIT(s)
at_WEND2PIT_1 = mkAT('WEND2PIT', at_func_WEND2PIT_1)

def at_func_EASTPIT(s):
  MOVE(s,UP,EEND2PIT)
  MOVE(s,OUT,EEND2PIT)
at_EASTPIT = mkAT('EASTPIT', at_func_EASTPIT)

def at_func_WESTPIT(s):
  MOVE(s,UP,WEND2PIT)
  MOVE(s,OUT,WEND2PIT)
at_WESTPIT = mkAT('WESTPIT', at_func_WESTPIT)

def at_func_WESTPIT_1(s):
  KEYWORD(s,CLIMB)
  if  ((((((((((((((( EQP(s,PLANT,0) ))))))))))))))) :
    opSAY(s,NOCLIMBUP)
  else:
    if  ((((((((((((((( EQP(s,PLANT,2) ))))))))))))))) :
      opSAY(s,SHORTPLANT)
      opGOTO(s,WEND2PIT)
    else:
      opSAY(s,LONGPLANT)
      opGOTO(s,NARROWCORRIDOR)
  opQUIT(s)
at_WESTPIT_1 = mkAT('WESTPIT', at_func_WESTPIT_1)

def at_func_WESTPIT_2(s):
  KEYWORD(s,GET,PLANT)
  opSAY(s,GET__PLANT)
  opQUIT(s)
at_WESTPIT_2 = mkAT('WESTPIT', at_func_WESTPIT_2)

def at_func_WESTOFFISSURE(s):
  MOVE(s,WEST,WENDMISTS)
at_WESTOFFISSURE = mkAT('WESTOFFISSURE', at_func_WESTOFFISSURE)

def at_func_WESTOFFISSURE_1(s):
  ANYOF(s,[FORWARD,OVER,EAST ])
  if  ((((((((((((((( EQP(s,FISSURE,0) ))))))))))))))) :
    opSAY(s,NOWAYACROSS)
  else:
    opGOTO(s,EASTOFFISSURE)
  opQUIT(s)
at_WESTOFFISSURE_1 = mkAT('WESTOFFISSURE', at_func_WESTOFFISSURE_1)

def at_func_WESTOFFISSURE_2(s):
  KEYWORD(s,JUMP)
  if  ((((((((((((((( EQP(s,FISSURE,1) ))))))))))))))) :
    opSAY(s,TRYTHEBRIDGE)
  else:
    opGOTO(s,CAVERN)
    CALL(s,SPLATTER)
  opQUIT(s)
at_WESTOFFISSURE_2 = mkAT('WESTOFFISSURE', at_func_WESTOFFISSURE_2)

def at_func_WESTOFFISSURE_3(s):
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,EASTOFFISSURE)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,FISSURE,0) ) )))))))))))))) :
      opSAY(s,NOWAYACROSS)
      opQUIT(s)
  KEYWORD(s,NORTH)
  opSAY(s,MISTCRAWL)
  opGOTO(s,WENDMISTS)
  opQUIT(s)
at_WESTOFFISSURE_3 = mkAT('WESTOFFISSURE', at_func_WESTOFFISSURE_3)

def at_func_LOWNSPASSAGE(s):
  MOVE(s,HALL,MTKING)
  MOVE(s,OUT,MTKING)
  MOVE(s,SOUTH,MTKING)
  MOVE(s,NORTH,Y2)
  MOVE(s,Y2,Y2)
  MOVE(s,DOWN,DIRTY)
  MOVE(s,HOLE,DIRTY)
at_LOWNSPASSAGE = mkAT('LOWNSPASSAGE', at_func_LOWNSPASSAGE)

def at_func_SOUTHSIDE(s):
  MOVE(s,HALL,MTKING)
  MOVE(s,OUT,MTKING)
  MOVE(s,NORTH,MTKING)
at_SOUTHSIDE = mkAT('SOUTHSIDE', at_func_SOUTHSIDE)

def at_func_WESTSIDE(s):
  MOVE(s,HALL,MTKING)
  MOVE(s,OUT,MTKING)
  MOVE(s,EAST,MTKING)
  MOVE(s,WEST,CROSSOVER)
  MOVE(s,UP,CROSSOVER)
at_WESTSIDE = mkAT('WESTSIDE', at_func_WESTSIDE)

def at_func_Y2(s):
  MOVE(s,SOUTH,LOWNSPASSAGE)
  MOVE(s,EAST,JUMBLE)
  MOVE(s,JUMBLE,JUMBLE)
  MOVE(s,WEST,WINDOW)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,BUILDING)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANTGOBACK)
      opQUIT(s)
    LDA(s,I,PLOVER)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANTGOBACK)
      opQUIT(s)
at_Y2 = mkAT('Y2', at_func_Y2)

def at_func_Y2_1(s):
  ANYOF(s,[PLUGH,PLOVER ])
  if  ((((((((((((((( GTP(s,CLOSURE,1)  or  BITP(s,ADMIN,NOMAGIC) ) )))))))))))))) :
    opSAY(s,NOTHING)
    BIS(s,ADMIN,PANICED)
    opQUIT(s)
  else:
    SMOVE(s,PLUGH,BUILDING,FOOF)
    SMOVE(s,PLOVER,PLOVER,FOOF)
at_Y2_1 = mkAT('Y2', at_func_Y2_1)

def at_func_JUMBLE(s):
  MOVE(s,DOWN,Y2)
  MOVE(s,Y2,Y2)
  MOVE(s,UP,MISTS)
at_JUMBLE = mkAT('JUMBLE', at_func_JUMBLE)

def at_func_WINDOW(s):
  MOVE(s,EAST,Y2)
  MOVE(s,Y2,Y2)
at_WINDOW = mkAT('WINDOW', at_func_WINDOW)

def at_func_WINDOW_1(s):
  KEYWORD(s,JUMP)
  opSAY(s,BROKENECK)
  opGOTO(s,MIRRORCNYN)
  CALL(s,CORONER)
at_WINDOW_1 = mkAT('WINDOW', at_func_WINDOW_1)

def at_func_DIRTY(s):
  MOVE(s,EAST,BRINK)
  MOVE(s,CRAWL,BRINK)
  MOVE(s,UP,LOWNSPASSAGE)
  MOVE(s,HOLE,LOWNSPASSAGE)
  MOVE(s,WEST,DUSTY)
  MOVE(s,BEDQUILT,BEDQUILT)
at_DIRTY = mkAT('DIRTY', at_func_DIRTY)

def at_func_BRINK(s):
  MOVE(s,WEST,DIRTY)
  MOVE(s,CRAWL,DIRTY)
  MOVE(s,DOWN,STREAMPIT)
  MOVE(s,PIT,STREAMPIT)
  MOVE(s,CLIMB,STREAMPIT)
at_BRINK = mkAT('BRINK', at_func_BRINK)

def at_func_STREAMPIT(s):
  MOVE(s,CLIMB,BRINK)
  MOVE(s,UP,BRINK)
  MOVE(s,OUT,BRINK)
at_STREAMPIT = mkAT('STREAMPIT', at_func_STREAMPIT)

def at_func_STREAMPIT_1(s):
  ANYOF(s,[SLIT,STREAM,DOWN,UPSTREAM,DOWNSTREAM ])
  opSAY(s,DONTFITSLIT)
  opQUIT(s)
at_STREAMPIT_1 = mkAT('STREAMPIT', at_func_STREAMPIT_1)

def at_func_DUSTY(s):
  MOVE(s,EAST,DIRTY)
  MOVE(s,PASSAGE,DIRTY)
  MOVE(s,DOWN,COMPLEX)
  MOVE(s,HOLE,COMPLEX)
  MOVE(s,BEDQUILT,BEDQUILT)
at_DUSTY = mkAT('DUSTY', at_func_DUSTY)

def at_func_WENDMISTS(s):
  MOVE(s,SOUTH,MAZEA_42)
  MOVE(s,UP,MAZEA_42)
  MOVE(s,PASSAGE,MAZEA_42)
  MOVE(s,CLIMB,MAZEA_42)
  MOVE(s,EAST,WESTOFFISSURE)
  MOVE(s,WEST,LONGHALLEAST)
  MOVE(s,CRAWL,LONGHALLEAST)
at_WENDMISTS = mkAT('WENDMISTS', at_func_WENDMISTS)

def at_func_WENDMISTS_1(s):
  KEYWORD(s,NORTH)
  opSAY(s,MISTCRAWL)
  opGOTO(s,WESTOFFISSURE)
  opQUIT(s)
at_WENDMISTS_1 = mkAT('WENDMISTS', at_func_WENDMISTS_1)

def at_func_MAZEA_42(s):
  MOVE(s,UP,WENDMISTS)
  MOVE(s,NORTH,MAZEA_42)
  MOVE(s,EAST,MAZEA_43)
  MOVE(s,SOUTH,MAZEA_45)
  MOVE(s,WEST,MAZEA_80)
at_MAZEA_42 = mkAT('MAZEA_42', at_func_MAZEA_42)

def at_func_MAZEA_43(s):
  MOVE(s,WEST,MAZEA_42)
  MOVE(s,SOUTH,MAZEA_44)
  MOVE(s,EAST,MAZEA_45)
at_MAZEA_43 = mkAT('MAZEA_43', at_func_MAZEA_43)

def at_func_MAZEA_44(s):
  MOVE(s,EAST,MAZEA_43)
  MOVE(s,DOWN,MAZEA_48)
  MOVE(s,SOUTH,MAZEA_50)
  MOVE(s,NORTH,MAZEA_82)
at_MAZEA_44 = mkAT('MAZEA_44', at_func_MAZEA_44)

def at_func_MAZEA_45(s):
  MOVE(s,WEST,MAZEA_42)
  MOVE(s,NORTH,MAZEA_43)
  MOVE(s,EAST,MAZEA_46)
  MOVE(s,SOUTH,MAZEA_47)
  MOVE(s,UP,MAZEA_87)
  MOVE(s,DOWN,MAZEA_87)
at_MAZEA_45 = mkAT('MAZEA_45', at_func_MAZEA_45)

def at_func_MAZEA_46(s):
  MOVE(s,WEST,MAZEA_45)
  MOVE(s,OUT,MAZEA_45)
at_MAZEA_46 = mkAT('MAZEA_46', at_func_MAZEA_46)

def at_func_MAZEA_47(s):
  MOVE(s,EAST,MAZEA_45)
  MOVE(s,OUT,MAZEA_45)
at_MAZEA_47 = mkAT('MAZEA_47', at_func_MAZEA_47)

def at_func_MAZEA_48(s):
  MOVE(s,UP,MAZEA_44)
  MOVE(s,OUT,MAZEA_44)
at_MAZEA_48 = mkAT('MAZEA_48', at_func_MAZEA_48)

def at_func_MAZEA_49(s):
  MOVE(s,EAST,MAZEA_50)
  MOVE(s,WEST,MAZEA_51)
at_MAZEA_49 = mkAT('MAZEA_49', at_func_MAZEA_49)

def at_func_MAZEA_50(s):
  MOVE(s,EAST,MAZEA_44)
  MOVE(s,WEST,MAZEA_49)
  MOVE(s,DOWN,MAZEA_51)
  MOVE(s,SOUTH,MAZEA_52)
at_MAZEA_50 = mkAT('MAZEA_50', at_func_MAZEA_50)

def at_func_MAZEA_51(s):
  MOVE(s,WEST,MAZEA_49)
  MOVE(s,UP,MAZEA_50)
  MOVE(s,EAST,MAZEA_52)
  MOVE(s,SOUTH,MAZEA_53)
at_MAZEA_51 = mkAT('MAZEA_51', at_func_MAZEA_51)

def at_func_MAZEA_52(s):
  MOVE(s,WEST,MAZEA_50)
  MOVE(s,EAST,MAZEA_51)
  MOVE(s,SOUTH,MAZEA_52)
  MOVE(s,UP,MAZEA_53)
  MOVE(s,NORTH,MAZEA_55)
  MOVE(s,DOWN,MAZEA_86)
at_MAZEA_52 = mkAT('MAZEA_52', at_func_MAZEA_52)

def at_func_MAZEA_53(s):
  MOVE(s,WEST,MAZEA_51)
  MOVE(s,NORTH,MAZEA_52)
  MOVE(s,SOUTH,MAZEA_54)
at_MAZEA_53 = mkAT('MAZEA_53', at_func_MAZEA_53)

def at_func_MAZEA_54(s):
  MOVE(s,WEST,MAZEA_53)
  MOVE(s,OUT,MAZEA_53)
at_MAZEA_54 = mkAT('MAZEA_54', at_func_MAZEA_54)

def at_func_MAZEA_55(s):
  MOVE(s,WEST,MAZEA_52)
  MOVE(s,NORTH,MAZEA_55)
  MOVE(s,DOWN,MAZEA_56)
  MOVE(s,EAST,MAZEA_57_PIT)
at_MAZEA_55 = mkAT('MAZEA_55', at_func_MAZEA_55)

def at_func_MAZEA_56(s):
  MOVE(s,UP,MAZEA_55)
  MOVE(s,OUT,MAZEA_55)
at_MAZEA_56 = mkAT('MAZEA_56', at_func_MAZEA_56)

def at_func_MAZEA_57_PIT(s):
  MOVE(s,DOWN,BIRDCHAMBER)
  MOVE(s,CLIMB,BIRDCHAMBER)
  MOVE(s,WEST,MAZEA_55)
  MOVE(s,SOUTH,MAZEA_58)
  MOVE(s,NORTH,MAZEA_83)
  MOVE(s,EAST,MAZEA_84)
at_MAZEA_57_PIT = mkAT('MAZEA_57_PIT', at_func_MAZEA_57_PIT)

def at_func_MAZEA_58(s):
  MOVE(s,EAST,MAZEA_57_PIT)
  MOVE(s,OUT,MAZEA_57_PIT)
at_MAZEA_58 = mkAT('MAZEA_58', at_func_MAZEA_58)

def at_func_LONGHALLEAST(s):
  MOVE(s,EAST,WENDMISTS)
  MOVE(s,UP,WENDMISTS)
  MOVE(s,CRAWL,WENDMISTS)
  MOVE(s,WEST,LONGHALLWEST)
  MOVE(s,NORTH,CROSSOVER)
  MOVE(s,DOWN,CROSSOVER)
  MOVE(s,HOLE,CROSSOVER)
at_LONGHALLEAST = mkAT('LONGHALLEAST', at_func_LONGHALLEAST)

def at_func_LONGHALLWEST(s):
  MOVE(s,EAST,LONGHALLEAST)
  MOVE(s,NORTH,CROSSOVER)
  MOVE(s,SOUTH,MAZED_107)
at_LONGHALLWEST = mkAT('LONGHALLWEST', at_func_LONGHALLWEST)

def at_func_CROSSOVER(s):
  MOVE(s,WEST,LONGHALLEAST)
  MOVE(s,NORTH,DEADEND1)
  MOVE(s,EAST,WESTSIDE)
  MOVE(s,SOUTH,LONGHALLWEST)
at_CROSSOVER = mkAT('CROSSOVER', at_func_CROSSOVER)

def at_func_DEADEND1(s):
  MOVE(s,SOUTH,CROSSOVER)
  MOVE(s,OUT,CROSSOVER)
at_DEADEND1 = mkAT('DEADEND1', at_func_DEADEND1)

def at_func_COMPLEX(s):
  MOVE(s,UP,DUSTY)
  MOVE(s,CLIMB,DUSTY)
  MOVE(s,WEST,BEDQUILT)
  MOVE(s,BEDQUILT,BEDQUILT)
  MOVE(s,NORTH,SHELL)
  MOVE(s,SHELL,SHELL)
  MOVE(s,EAST,ANTEROOM)
at_COMPLEX = mkAT('COMPLEX', at_func_COMPLEX)

def at_func_BEDQUILT(s):
  MOVE(s,EAST,COMPLEX)
  MOVE(s,WEST,SWISS)
  MOVE(s,SLAB,SLAB)
at_BEDQUILT = mkAT('BEDQUILT', at_func_BEDQUILT)

def at_func_BEDQUILT_1(s):
  ANYOF(s,[NORTH,SOUTH,UP,DOWN ])
  if  ((((((((((((((( CHANCEP(s,65) ))))))))))))))) :
    opSAY(s,CRAWL__CAVEIN)
    opQUIT(s)
  else:
    MOVE(s,DOWN,ANTEROOM)
    if  ((((((((((((((( CHANCEP(s,75) ))))))))))))))) :
      MOVE(s,NORTH,LOW)
      MOVE(s,UP,DUSTY)
      MOVE(s,SOUTH,SLAB)
    else:
      MOVE(s,NORTH,SECRETJUNCTION)
      MOVE(s,UP,SECRETNSCPAS)
      MOVE(s,SOUTH,TALLEWCNYN)
at_BEDQUILT_1 = mkAT('BEDQUILT', at_func_BEDQUILT_1)

def at_func_BEDQUILT_2(s):
  KEYWORD(s,NW)
  if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
    opSAY(s,YOUDIDNTMOVE)
  else:
    opGOTO(s,ORIENTAL)
  opQUIT(s)
at_BEDQUILT_2 = mkAT('BEDQUILT', at_func_BEDQUILT_2)

def at_func_SWISS(s):
  MOVE(s,NE,BEDQUILT)
  MOVE(s,WEST,EEND2PIT)
  MOVE(s,CANYON,TALLEWCNYN)
  MOVE(s,EAST,SOFT)
  MOVE(s,ORIENTAL,ORIENTAL)
  MOVE(s,SOFT,SOFT)
  ANYOF(s,[NW,SOUTH ])
  if  ((((((((((((((( CHANCEP(s,65) ))))))))))))))) :
    MOVE(s,NW,ORIENTAL)
    opSAY(s,YOUDIDNTMOVE)
  else:
    MOVE(s,SOUTH,TALLEWCNYN)
    opSAY(s,YOUDIDNTMOVE)
  opQUIT(s)
at_SWISS = mkAT('SWISS', at_func_SWISS)

def at_func_EEND2PIT(s):
  MOVE(s,EAST,SWISS)
  MOVE(s,WEST,WEND2PIT)
  MOVE(s,CROSS,WEND2PIT)
  MOVE(s,DOWN,EASTPIT)
  MOVE(s,PIT,EASTPIT)
at_EEND2PIT = mkAT('EEND2PIT', at_func_EEND2PIT)

def at_func_SLAB(s):
  MOVE(s,SOUTH,WEND2PIT)
  MOVE(s,UP,SECRETNSCYN)
  MOVE(s,CLIMB,SECRETNSCYN)
  MOVE(s,NORTH,BEDQUILT)
  MOVE(s,BEDQUILT,BEDQUILT)
at_SLAB = mkAT('SLAB', at_func_SLAB)

def at_func_SECRETNSCYN(s):
  MOVE(s,DOWN,SLAB)
  MOVE(s,SLAB,SLAB)
  MOVE(s,NORTH,MIRRORCNYN)
  MOVE(s,MIRROR,MIRRORCNYN)
  MOVE(s,RESERVOIR,RESERVOIR)
  MOVE(s,SOUTH,SECRETCYNNE1)
at_SECRETNSCYN = mkAT('SECRETNSCYN', at_func_SECRETNSCYN)

def at_func_SECRETNSCPAS(s):
  MOVE(s,NORTH,SECRETJUNCTION)
  MOVE(s,DOWN,BEDQUILT)
  MOVE(s,PASSAGE,BEDQUILT)
  MOVE(s,SOUTH,STALACT)
at_SECRETNSCPAS = mkAT('SECRETNSCPAS', at_func_SECRETNSCPAS)

def at_func_SECRETJUNCTION(s):
  MOVE(s,SE,BEDQUILT)
  MOVE(s,SOUTH,SECRETNSCPAS)
  MOVE(s,NORTH,WINDOW2)
at_SECRETJUNCTION = mkAT('SECRETJUNCTION', at_func_SECRETJUNCTION)

def at_func_LOW(s):
  MOVE(s,BEDQUILT,BEDQUILT)
  MOVE(s,SW,SLOPING)
  MOVE(s,NORTH,DEADEND2)
  MOVE(s,SE,ORIENTAL)
  MOVE(s,ORIENTAL,ORIENTAL)
at_LOW = mkAT('LOW', at_func_LOW)

def at_func_DEADEND2(s):
  MOVE(s,SOUTH,LOW)
  MOVE(s,CRAWL,LOW)
  MOVE(s,OUT,LOW)
at_DEADEND2 = mkAT('DEADEND2', at_func_DEADEND2)

def at_func_SECRETEW_TITE(s):
  MOVE(s,EAST,MTKING)
  MOVE(s,DOWN,NSCANYONWIDE)
at_SECRETEW_TITE = mkAT('SECRETEW_TITE', at_func_SECRETEW_TITE)

def at_func_SECRETEW_TITE_1(s):
  KEYWORD(s,WEST)
  if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
    opGOTO(s,SECRETCYNNE2)
  else:
    opGOTO(s,SECRETCYNNE1)
  opQUIT(s)
at_SECRETEW_TITE_1 = mkAT('SECRETEW_TITE', at_func_SECRETEW_TITE_1)

def at_func_NSCANYONWIDE(s):
  MOVE(s,SOUTH,TIGHTERSTILL)
  MOVE(s,NORTH,TALLEWCNYN)
at_NSCANYONWIDE = mkAT('NSCANYONWIDE', at_func_NSCANYONWIDE)

def at_func_TIGHTERSTILL(s):
  MOVE(s,NORTH,NSCANYONWIDE)
at_TIGHTERSTILL = mkAT('TIGHTERSTILL', at_func_TIGHTERSTILL)

def at_func_TALLEWCNYN(s):
  MOVE(s,EAST,NSCANYONWIDE)
  MOVE(s,WEST,DEADEND3)
  MOVE(s,NORTH,SWISS)
  MOVE(s,CRAWL,SWISS)
at_TALLEWCNYN = mkAT('TALLEWCNYN', at_func_TALLEWCNYN)

def at_func_DEADEND3(s):
  MOVE(s,SOUTH,TALLEWCNYN)
at_DEADEND3 = mkAT('DEADEND3', at_func_DEADEND3)

def at_func_MAZEA_80(s):
  MOVE(s,NORTH,MAZEA_42)
  MOVE(s,WEST,MAZEA_80)
  MOVE(s,SOUTH,MAZEA_80)
  MOVE(s,EAST,MAZEA_81)
at_MAZEA_80 = mkAT('MAZEA_80', at_func_MAZEA_80)

def at_func_MAZEA_81(s):
  MOVE(s,WEST,MAZEA_80)
  MOVE(s,OUT,MAZEA_80)
at_MAZEA_81 = mkAT('MAZEA_81', at_func_MAZEA_81)

def at_func_MAZEA_82(s):
  MOVE(s,SOUTH,MAZEA_44)
  MOVE(s,OUT,MAZEA_44)
at_MAZEA_82 = mkAT('MAZEA_82', at_func_MAZEA_82)

def at_func_MAZEA_83(s):
  MOVE(s,SOUTH,MAZEA_57_PIT)
  MOVE(s,EAST,MAZEA_84)
  MOVE(s,WEST,MAZEA_85)
at_MAZEA_83 = mkAT('MAZEA_83', at_func_MAZEA_83)

def at_func_MAZEA_84(s):
  MOVE(s,NORTH,MAZEA_57_PIT)
  MOVE(s,WEST,MAZEA_83)
  MOVE(s,NW,MAZEA_114)
at_MAZEA_84 = mkAT('MAZEA_84', at_func_MAZEA_84)

def at_func_MAZEA_85(s):
  MOVE(s,EAST,MAZEA_83)
  MOVE(s,OUT,MAZEA_83)
at_MAZEA_85 = mkAT('MAZEA_85', at_func_MAZEA_85)

def at_func_MAZEA_86(s):
  MOVE(s,UP,MAZEA_52)
  MOVE(s,OUT,MAZEA_52)
at_MAZEA_86 = mkAT('MAZEA_86', at_func_MAZEA_86)

def at_func_MAZEA_87(s):
  MOVE(s,UP,MAZEA_45)
  MOVE(s,DOWN,MAZEA_45)
at_MAZEA_87 = mkAT('MAZEA_87', at_func_MAZEA_87)

def at_func_NARROWCORRIDOR(s):
  MOVE(s,DOWN,WESTPIT)
  MOVE(s,CLIMB,WESTPIT)
  MOVE(s,EAST,WESTPIT)
  MOVE(s,WEST,GIANT)
  MOVE(s,GIANT,GIANT)
at_NARROWCORRIDOR = mkAT('NARROWCORRIDOR', at_func_NARROWCORRIDOR)

def at_func_NARROWCORRIDOR_1(s):
  KEYWORD(s,JUMP)
  opGOTO(s,WESTPIT)
  CALL(s,SPLATTER)
at_NARROWCORRIDOR_1 = mkAT('NARROWCORRIDOR', at_func_NARROWCORRIDOR_1)

def at_func_INCLINE(s):
  MOVE(s,NORTH,CAVERN)
  MOVE(s,CAVERN,CAVERN)
  MOVE(s,PASSAGE,CAVERN)
  SMOVE(s,DOWN,LOW,OOF)
  SMOVE(s,CLIMB,LOW,OOF)
at_INCLINE = mkAT('INCLINE', at_func_INCLINE)

def at_func_GIANT(s):
  MOVE(s,SOUTH,NARROWCORRIDOR)
  MOVE(s,CORRIDOR,NARROWCORRIDOR)
  MOVE(s,EAST,TUNNEL_1)
  MOVE(s,NORTH,IMMENSENSPASS)
at_GIANT = mkAT('GIANT', at_func_GIANT)

def at_func_IMMENSENSPASS(s):
  MOVE(s,SOUTH,GIANT)
  MOVE(s,GIANT,GIANT)
  MOVE(s,PASSAGE,GIANT)
at_IMMENSENSPASS = mkAT('IMMENSENSPASS', at_func_IMMENSENSPASS)

def at_func_IMMENSENSPASS_1(s):
  ANYOF(s,[NORTH,ENTER,CAVERN ])
  if  ((((((((((((((( EQP(s,DOOR,0) ))))))))))))))) :
    opSAY(s,DOORNEEDSOIL)
  else:
    opGOTO(s,CAVERN)
  opQUIT(s)
at_IMMENSENSPASS_1 = mkAT('IMMENSENSPASS', at_func_IMMENSENSPASS_1)

def at_func_CAVERN(s):
  MOVE(s,SOUTH,IMMENSENSPASS)
  MOVE(s,OUT,IMMENSENSPASS)
  MOVE(s,GIANT,GIANT)
  MOVE(s,WEST,INCLINE)
  MOVE(s,INCLINE,INCLINE)
at_CAVERN = mkAT('CAVERN', at_func_CAVERN)

def at_func_CAVERN_1(s):
  ANYOF(s,[DOWN,JUMP ])
  QUERY(s,WHIRLPOOL_,CAVERN2)
at_CAVERN_1 = mkAT('CAVERN', at_func_CAVERN_1)

def at_func_SOFT(s):
  MOVE(s,WEST,SWISS)
  MOVE(s,OUT,SWISS)
  MOVE(s,SWISS,SWISS)
at_SOFT = mkAT('SOFT', at_func_SOFT)

def at_func_ORIENTAL(s):
  MOVE(s,SE,SWISS)
  MOVE(s,WEST,LOW)
  MOVE(s,CRAWL,LOW)
  MOVE(s,UP,MISTY)
  MOVE(s,NORTH,MISTY)
  MOVE(s,CAVERN,MISTY)
at_ORIENTAL = mkAT('ORIENTAL', at_func_ORIENTAL)

def at_func_MISTY(s):
  MOVE(s,SOUTH,ORIENTAL)
  MOVE(s,ORIENTAL,ORIENTAL)
  MOVE(s,WEST,ALCOVE)
at_MISTY = mkAT('MISTY', at_func_MISTY)

def at_func_MISTY_1(s):
  KEYWORD(s,JUMP)
  opGOTO(s,CAVERN)
  CALL(s,SPLATTER)
  opQUIT(s)
at_MISTY_1 = mkAT('MISTY', at_func_MISTY_1)

def at_func_ALCOVE(s):
  ANYOF(s,[EAST,PASSAGE,PLOVER ])
  if  ((((((((((((((( EQP(s,INVCT,0) ))))))))))))))) :
    opGOTO(s,PLOVER)
  else:
    if  ((((((((((((((( EQP(s,INVCT,1) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,EMERALD) ))))))))))))))) :
        opGOTO(s,PLOVER)
      else:
        opSAY(s,WONT__FIT)
    else:
      opSAY(s,WONT__FIT)
  opQUIT(s)
at_ALCOVE = mkAT('ALCOVE', at_func_ALCOVE)

def at_func_ALCOVE_1(s):
  MOVE(s,NW,MISTY)
  MOVE(s,CAVERN,MISTY)
at_ALCOVE_1 = mkAT('ALCOVE', at_func_ALCOVE_1)

def at_func_PLOVER(s):
  AT(s,PLOVER)
  KEYWORD(s,PLOVER)
  if  ((((((((((((((( EQP(s,STATUS,1)  or  KEYP(s,SAY) ) )))))))))))))) :
    if  ((((((((((((((( HAVEP(s,EMERALD) ))))))))))))))) :
      opDROP(s,EMERALD)
    opSAY(s,FOOF)
    opGOTO(s,Y2)
    opSET(s,THERE,0)
    opQUIT(s)
at_PLOVER = mkAT('PLOVER', at_func_PLOVER)

def at_func_PLOVER_1(s):
  ANYOF(s,[WEST,PASSAGE,ALCOVE ])
  if  ((((((((((((((( EQP(s,INVCT,0) ))))))))))))))) :
    opGOTO(s,ALCOVE)
  else:
    if  ((((((((((((((( EQP(s,INVCT,1) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,EMERALD) ))))))))))))))) :
        opGOTO(s,ALCOVE)
      else:
        opSAY(s,WONT__FIT)
    else:
      opSAY(s,WONT__FIT)
  opQUIT(s)
at_PLOVER_1 = mkAT('PLOVER', at_func_PLOVER_1)

def at_func_PLOVER_2(s):
  MOVE(s,NE,DARK)
  MOVE(s,DARK,DARK)
at_PLOVER_2 = mkAT('PLOVER', at_func_PLOVER_2)

def at_func_DARK(s):
  MOVE(s,SOUTH,PLOVER)
  MOVE(s,PLOVER,PLOVER)
  MOVE(s,OUT,PLOVER)
at_DARK = mkAT('DARK', at_func_DARK)

def at_func_ARCHED(s):
  MOVE(s,DOWN,SHELL)
  MOVE(s,SHELL,SHELL)
  MOVE(s,UP,ARCH_COR_1)
  MOVE(s,EAST,ARCH_COR_1)
at_ARCHED = mkAT('ARCHED', at_func_ARCHED)

def at_func_SHELL(s):
  MOVE(s,UP,ARCHED)
  MOVE(s,HALL,ARCHED)
  MOVE(s,DOWN,RAGGEDCORRID)
  MOVE(s,CORRIDOR,RAGGEDCORRID)
at_SHELL = mkAT('SHELL', at_func_SHELL)

def at_func_SHELL_1(s):
  ANYOF(s,[SOUTH,COMPLEX ])
  if  ((((((((((((((( HAVEP(s,CLAM) ))))))))))))))) :
    opSAY(s,CLAM_2_BIG)
  else:
    if  ((((((((((((((( HAVEP(s,OYSTER) ))))))))))))))) :
      opSAY(s,OYSTER_2_BIG)
    else:
      opGOTO(s,COMPLEX)
  opQUIT(s)
at_SHELL_1 = mkAT('SHELL', at_func_SHELL_1)

def at_func_RAGGEDCORRID(s):
  MOVE(s,UP,SHELL)
  MOVE(s,SHELL,SHELL)
  MOVE(s,DOWN,CULDESAC)
at_RAGGEDCORRID = mkAT('RAGGEDCORRID', at_func_RAGGEDCORRID)

def at_func_CULDESAC(s):
  MOVE(s,UP,RAGGEDCORRID)
  MOVE(s,OUT,RAGGEDCORRID)
  MOVE(s,CORRIDOR,RAGGEDCORRID)
  MOVE(s,SHELL,SHELL)
at_CULDESAC = mkAT('CULDESAC', at_func_CULDESAC)

def at_func_ANTEROOM(s):
  MOVE(s,UP,COMPLEX)
  MOVE(s,WEST,BEDQUILT)
  MOVE(s,EAST,WITTSEND)
at_ANTEROOM = mkAT('ANTEROOM', at_func_ANTEROOM)

def at_func_MAZED_107(s):
  MOVE(s,SOUTH,MAZED_131)
  MOVE(s,SW,MAZED_132)
  MOVE(s,NE,MAZED_133)
  MOVE(s,SE,MAZED_134)
  MOVE(s,UP,MAZED_135)
  MOVE(s,NW,MAZED_136)
  MOVE(s,EAST,MAZED_137)
  MOVE(s,WEST,MAZED_138)
  MOVE(s,NORTH,MAZED_139)
  MOVE(s,DOWN,LONGHALLWEST)
at_MAZED_107 = mkAT('MAZED_107', at_func_MAZED_107)

def at_func_WITTSEND(s):
  ANYOF(s,[NORTH,SOUTH,EAST,UP,DOWN,NE,NW,SE,SW ])
  if  ((((((((((((((( CHANCEP(s,95) ))))))))))))))) :
    opGOTO(s,WITTSEND)
  else:
    opGOTO(s,ANTEROOM)
  opQUIT(s)
at_WITTSEND = mkAT('WITTSEND', at_func_WITTSEND)

def at_func_WITTSEND_1(s):
  KEYWORD(s,WEST)
  opGOTO(s,WITTSEND)
  opQUIT(s)
at_WITTSEND_1 = mkAT('WITTSEND', at_func_WITTSEND_1)

def at_func_MIRRORCNYN(s):
  KEYWORD(s,MIRROR)
  opSAY(s,TOO_FAR_UP)
  opQUIT(s)
at_MIRRORCNYN = mkAT('MIRRORCNYN', at_func_MIRRORCNYN)

def at_func_MIRRORCNYN_1(s):
  MOVE(s,SOUTH,SECRETNSCYN)
  MOVE(s,NORTH,RESERVOIR)
  MOVE(s,RESERVOIR,RESERVOIR)
at_MIRRORCNYN_1 = mkAT('MIRRORCNYN', at_func_MIRRORCNYN_1)

def at_func_WINDOW2(s):
  MOVE(s,WEST,SECRETJUNCTION)
at_WINDOW2 = mkAT('WINDOW2', at_func_WINDOW2)

def at_func_WINDOW2_1(s):
  KEYWORD(s,JUMP)
  opSAY(s,BROKENECK)
  opGOTO(s,MIRRORCNYN)
  CALL(s,CORONER)
at_WINDOW2_1 = mkAT('WINDOW2', at_func_WINDOW2_1)

def at_func_STALACT(s):
  MOVE(s,NORTH,SECRETNSCPAS)
at_STALACT = mkAT('STALACT', at_func_STALACT)

def at_func_STALACT_1(s):
  ANYOF(s,[DOWN,JUMP,CLIMB ])
  if  ((((((((((((((( CHANCEP(s,40) ))))))))))))))) :
    opGOTO(s,MAZEA_50)
  else:
    if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
      opGOTO(s,MAZEA_53)
    else:
      opGOTO(s,MAZEA_45)
  opQUIT(s)
at_STALACT_1 = mkAT('STALACT', at_func_STALACT_1)

def at_func_MAZED_112(s):
  MOVE(s,SW,MAZED_131)
  MOVE(s,NORTH,MAZED_132)
  MOVE(s,EAST,MAZED_133)
  MOVE(s,NW,MAZED_134)
  MOVE(s,SE,MAZED_135)
  MOVE(s,NE,MAZED_136)
  MOVE(s,WEST,MAZED_137)
  MOVE(s,DOWN,MAZED_138)
  MOVE(s,UP,MAZED_139)
  MOVE(s,SOUTH,MAZED_140)
at_MAZED_112 = mkAT('MAZED_112', at_func_MAZED_112)

def at_func_RESERVOIR(s):
  MOVE(s,SOUTH,MIRRORCNYN)
  MOVE(s,OUT,MIRRORCNYN)
  MOVE(s,MIRROR,MIRRORCNYN)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,RESERVOIR_N)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANT_SWIM)
      opQUIT(s)
  ANYOF(s,[NORTH,CROSS ])
  opSAY(s,CANT_SWIM)
  opQUIT(s)
at_RESERVOIR = mkAT('RESERVOIR', at_func_RESERVOIR)

def at_func_RESERVOIR_N(s):
  MOVE(s,NORTH,WARM)
  MOVE(s,PASSAGE,WARM)
  MOVE(s,WARM,WARM)
  MOVE(s,BALCONY,BALCONY)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,CAVERN)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,IAMGAME)
      opQUIT(s)
    LDA(s,I,RESERVOIR)
    if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
      opSAY(s,CANT_SWIM)
      opQUIT(s)
  ANYOF(s,[SOUTH,CROSS ])
  if  ((((((((((((((( NEARP(s,TURTLE) ))))))))))))))) :
    opSAY(s,TURTLE_BACK)
    APPORT(s,TURTLE,LIMBO)
    opGOTO(s,RESERVOIR)
  else:
    opSAY(s,CANT_SWIM)
  opQUIT(s)
at_RESERVOIR_N = mkAT('RESERVOIR_N', at_func_RESERVOIR_N)

def at_func_WARM(s):
  MOVE(s,SOUTH,RESERVOIR_N)
  MOVE(s,RESERVOIR,RESERVOIR_N)
  MOVE(s,NORTHEAST,BALCONY)
  MOVE(s,BALCONY,BALCONY)
at_WARM = mkAT('WARM', at_func_WARM)

def at_func_BALCONY(s):
  MOVE(s,WEST,WARM)
  MOVE(s,OUT,WARM)
  MOVE(s,WARM,WARM)
  MOVE(s,RESERVOIR,RESERVOIR_N)
  KEYWORD(s,JUMP)
  opGOTO(s,YLEM)
  CALL(s,SPLATTER)
at_BALCONY = mkAT('BALCONY', at_func_BALCONY)

def at_func_MAZEA_114(s):
  MOVE(s,SE,MAZEA_84)
at_MAZEA_114 = mkAT('MAZEA_114', at_func_MAZEA_114)

def at_func_SWOFCHASM(s):
  MOVE(s,SW,SLOPING)
  MOVE(s,SLOPING,SLOPING)
  MOVE(s,CORRIDOR,SLOPING)
at_SWOFCHASM = mkAT('SWOFCHASM', at_func_SWOFCHASM)

def at_func_SWOFCHASM_1(s):
  KEYWORD(s,THROW)
  if  ((((((((((((((( EQP(s,STATUS,1)  or  NEARP(s,TROLL2) ) )))))))))))))) :
    opPROCEED(s)
  else:
    if  ((((((((((((((( KEYP(s,AXE)  or  KEYP(s,SWORD) ) )))))))))))))) :
      if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
        NAME(s,EL_CHEAPO,ARG2)
        opDROP(s,ARG2)
      else:
        opPROCEED(s)
    else:
      if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
        if  ((((((((((((((( BITP(s,ARG2,VALUED) ))))))))))))))) :
          if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
            if  ((((((((((((((( KEYP(s,EGGS) ))))))))))))))) :
              if  ((((((((((((((( BITP(s,TROLL,SPECIAL1) ))))))))))))))) :
                opSET(s,TROLL,6)
                opSAY(s,TROLL)
                opSET(s,TROLL,0)
                APPORT(s,EGGS,YLEM)
                opQUIT(s)
            NAME(s,BOUGHTHIMOFF,ARG2)
            opSET(s,TROLL,1)
            APPORT(s,TROLL,LIMBO)
            APPORT(s,TROLL2,SWOFCHASM)
            APPORT(s,ARG2,LIMBO)
          else:
            opPROCEED(s)
        else:
          opPROCEED(s)
      else:
        opPROCEED(s)
  opQUIT(s)
at_SWOFCHASM_1 = mkAT('SWOFCHASM', at_func_SWOFCHASM_1)

def at_func_SWOFCHASM_2(s):
  ANYOF(s,[CROSS,NE ])
  if  ((((((((((((((( GTP(s,CHASM,0) ))))))))))))))) :
    opSAY(s,NO_BRIDGE)
  else:
    if  ((((((((((((((( EQP(s,TROLL,0) ))))))))))))))) :
      opSAY(s,TROLL_SEZ_NO)
    else:
      if  ((((((((((((((( EQP(s,TROLL,2) ))))))))))))))) :
        opSET(s,TROLL,3)
        opSAY(s,TROLL)
        opSET(s,TROLL,0)
        APPORT(s,TROLL,SWOFCHASM)
        APPORT(s,TROLL2,LIMBO)
      else:
        if  ((((((((((((((( EQP(s,TROLL,1) ))))))))))))))) :
          opSET(s,TROLL,2)
        opGOTO(s,NEOFCHASM)
  opQUIT(s)
at_SWOFCHASM_2 = mkAT('SWOFCHASM', at_func_SWOFCHASM_2)

def at_func_SWOFCHASM_3(s):
  KEYWORD(s,JUMP)
  if  ((((((((((((((( EQP(s,CHASM,0) ))))))))))))))) :
    opSAY(s,TRYTHEBRIDGE)
  else:
    opGOTO(s,YLEM)
    CALL(s,SPLATTER)
  opQUIT(s)
at_SWOFCHASM_3 = mkAT('SWOFCHASM', at_func_SWOFCHASM_3)

def at_func_SLOPING(s):
  MOVE(s,DOWN,LOW)
  MOVE(s,UP,SWOFCHASM)
  MOVE(s,CHASM,SWOFCHASM)
  MOVE(s,LOW,LOW)
  MOVE(s,OUT,LOW)
at_SLOPING = mkAT('SLOPING', at_func_SLOPING)

def at_func_SECRETCYNNE1(s):
  KEYWORD(s,RUG)
  if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
    opSAY(s,DRAGON_RUG)
    opQUIT(s)
at_SECRETCYNNE1 = mkAT('SECRETCYNNE1', at_func_SECRETCYNNE1)

def at_func_SECRETCYNNE1_1(s):
  MOVE(s,NORTH,SECRETNSCYN)
  MOVE(s,OUT,SECRETNSCYN)
at_SECRETCYNNE1_1 = mkAT('SECRETCYNNE1', at_func_SECRETCYNNE1_1)

def at_func_SECRETCYNNE1_2(s):
  ANYOF(s,[FORWARD,EAST ])
  if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
    opSAY(s,PAST_DRAGON)
  else:
    opGOTO(s,SECRETEW_TITE)
  opQUIT(s)
at_SECRETCYNNE1_2 = mkAT('SECRETCYNNE1', at_func_SECRETCYNNE1_2)

def at_func_SECRETCYNNE2(s):
  KEYWORD(s,RUG)
  if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
    opSAY(s,DRAGON_RUG)
    opQUIT(s)
at_SECRETCYNNE2 = mkAT('SECRETCYNNE2', at_func_SECRETCYNNE2)

def at_func_SECRETCYNNE2_1(s):
  MOVE(s,EAST,SECRETEW_TITE)
  MOVE(s,OUT,SECRETEW_TITE)
at_SECRETCYNNE2_1 = mkAT('SECRETCYNNE2', at_func_SECRETCYNNE2_1)

def at_func_SECRETCYNNE2_2(s):
  ANYOF(s,[FORWARD,NORTH ])
  if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
    opSAY(s,PAST_DRAGON)
  else:
    opGOTO(s,SECRETNSCYN)
  opQUIT(s)
at_SECRETCYNNE2_2 = mkAT('SECRETCYNNE2', at_func_SECRETCYNNE2_2)

def at_func_NEOFCHASM(s):
  KEYWORD(s,RELEASE,BEAR)
  HAVE(s,BEAR)
  NEAR(s,TROLL)
  opSET(s,TROLL,4)
  opSAY(s,BEAR__TROLL)
  APPORT(s,TROLL,LIMBO)
  APPORT(s,TROLL2,SWOFCHASM)
  opDROP(s,BEAR)
  opQUIT(s)
at_NEOFCHASM = mkAT('NEOFCHASM', at_func_NEOFCHASM)

def at_func_NEOFCHASM_1(s):
  KEYWORD(s,THROW)
  if  ((((((((((((((( EQP(s,STATUS,1)  or  NEARP(s,TROLL2) ) )))))))))))))) :
    opPROCEED(s)
  else:
    if  ((((((((((((((( KEYP(s,AXE)  or  KEYP(s,SWORD) ) )))))))))))))) :
      if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
        NAME(s,EL_CHEAPO,ARG2)
        opDROP(s,ARG2)
      else:
        opPROCEED(s)
    else:
      if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
        if  ((((((((((((((( BITP(s,ARG2,VALUED) ))))))))))))))) :
          if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
            if  ((((((((((((((( KEYP(s,EGGS) ))))))))))))))) :
              if  ((((((((((((((( BITP(s,TROLL,SPECIAL1) ))))))))))))))) :
                opSET(s,TROLL,6)
                opSAY(s,TROLL)
                opSET(s,TROLL,0)
                APPORT(s,EGGS,YLEM)
                opQUIT(s)
            NAME(s,BOUGHTHIMOFF,ARG2)
            opSET(s,TROLL,1)
            APPORT(s,TROLL,LIMBO)
            APPORT(s,TROLL2,SWOFCHASM)
            APPORT(s,ARG2,LIMBO)
          else:
            opPROCEED(s)
        else:
          opPROCEED(s)
      else:
        opPROCEED(s)
  opQUIT(s)
at_NEOFCHASM_1 = mkAT('NEOFCHASM', at_func_NEOFCHASM_1)

def at_func_NEOFCHASM_2(s):
  ANYOF(s,[CROSS,SW ])
  if  ((((((((((((((( GTP(s,CHASM,0) ))))))))))))))) :
    opSAY(s,NO_BRIDGE)
  else:
    if  ((((((((((((((( EQP(s,TROLL,0) ))))))))))))))) :
      opSAY(s,TROLL_SEZ_NO)
    else:
      if  ((((((((((((((( EQP(s,TROLL,2) ))))))))))))))) :
        opSET(s,TROLL,3)
        opSAY(s,TROLL)
        opSET(s,TROLL,0)
        APPORT(s,TROLL,SWOFCHASM)
        APPORT(s,TROLL2,LIMBO)
      else:
        if  ((((((((((((((( EQP(s,TROLL,1) ))))))))))))))) :
          opSET(s,TROLL,2)
        if  ((((((((((((((( HAVEP(s,BEAR) ))))))))))))))) :
          opSAY(s,BEAR__BRIDGE)
          opSET(s,CHASM,1)
          APPORT(s,TROLL2,LIMBO)
          opGOTO(s,YLEM)
          CALL(s,CORONER)
        else:
          if  ((((((((((((((( EQP(s,TROLL,4)  and  BITP(s,TROLL,SPECIAL1) ) )))))))))))))) :
            if  ((((((((((((((( NEARP(s,BEAR) ))))))))))))))) :
              opGET(s,BEAR)
              opSET(s,CHASM,1)
              opSAY(s,REVENGE)
            else:
              opSET(s,CHASM,2)
              opSAY(s,REVENGE_1)
            APPORT(s,TROLL2,LIMBO)
            opGOTO(s,YLEM)
            CALL(s,CORONER)
          else:
            opGOTO(s,SWOFCHASM)
  opQUIT(s)
at_NEOFCHASM_2 = mkAT('NEOFCHASM', at_func_NEOFCHASM_2)

def at_func_NEOFCHASM_3(s):
  KEYWORD(s,JUMP)
  if  ((((((((((((((( EQP(s,CHASM,0) ))))))))))))))) :
    opSAY(s,TRYTHEBRIDGE)
  else:
    opGOTO(s,YLEM)
    CALL(s,SPLATTER)
  opQUIT(s)
at_NEOFCHASM_3 = mkAT('NEOFCHASM', at_func_NEOFCHASM_3)

def at_func_NEOFCHASM_4(s):
  MOVE(s,NE,CORRIDOR)
  MOVE(s,CORRIDOR,CORRIDOR)
  MOVE(s,FORK,FORK)
  MOVE(s,VIEW,BREATHTAKER)
  MOVE(s,BARREN,BARREN)
at_NEOFCHASM_4 = mkAT('NEOFCHASM', at_func_NEOFCHASM_4)

def at_func_CORRIDOR(s):
  MOVE(s,CHASM,NEOFCHASM)
  MOVE(s,WEST,NEOFCHASM)
  MOVE(s,EAST,FORK)
  MOVE(s,FORK,FORK)
  MOVE(s,VIEW,BREATHTAKER)
  MOVE(s,BARREN,BARREN)
at_CORRIDOR = mkAT('CORRIDOR', at_func_CORRIDOR)

def at_func_FORK(s):
  MOVE(s,CHASM,NEOFCHASM)
  MOVE(s,WEST,CORRIDOR)
  MOVE(s,CORRIDOR,CORRIDOR)
  MOVE(s,NE,WARMJUNCTN)
  MOVE(s,LEFT,WARMJUNCTN)
  MOVE(s,SE,LIMESTONE)
  MOVE(s,RIGHT,LIMESTONE)
  MOVE(s,DOWN,LIMESTONE)
  MOVE(s,VIEW,BREATHTAKER)
  MOVE(s,BARREN,BARREN)
at_FORK = mkAT('FORK', at_func_FORK)

def at_func_WARMJUNCTN(s):
  MOVE(s,SOUTH,FORK)
  MOVE(s,FORK,FORK)
  MOVE(s,NORTH,BREATHTAKER)
  MOVE(s,VIEW,BREATHTAKER)
  MOVE(s,EAST,BOULDERS)
  MOVE(s,CRAWL,BOULDERS)
at_WARMJUNCTN = mkAT('WARMJUNCTN', at_func_WARMJUNCTN)

def at_func_BREATHTAKER(s):
  MOVE(s,SOUTH,WARMJUNCTN)
  MOVE(s,PASSAGE,WARMJUNCTN)
  MOVE(s,OUT,WARMJUNCTN)
  MOVE(s,FORK,FORK)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,FACES)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,GORGE,0) ) )))))))))))))) :
      opSAY(s,NO_ARCH)
      opQUIT(s)
at_BREATHTAKER = mkAT('BREATHTAKER', at_func_BREATHTAKER)

def at_func_BREATHTAKER_1(s):
  ANYOF(s,[JUMP,DOWN,CLIMB ])
  opGOTO(s,YLEM)
  CALL(s,SPLATTER)
at_BREATHTAKER_1 = mkAT('BREATHTAKER', at_func_BREATHTAKER_1)

def at_func_BREATHTAKER_2(s):
  ANYOF(s,[VALLEY,CROSS,GORGE,NORTH ])
  if  ((((((((((((((( EQP(s,GORGE,0) ))))))))))))))) :
    opSAY(s,NO_ARCH)
  else:
    if  ((((((((((((((( HAVEP(s,BEAR) ))))))))))))))) :
      opSAY(s,LEAVE_BEAR)
    else:
      if  ((((((((((((((( HAVEP(s,RING) ))))))))))))))) :
        if  ((((((((((((((( BITP(s,FACES,BEENHERE) ))))))))))))))) :
          pass
        else:
          opSAY(s,FUMES_MISS)
        opGOTO(s,FACES)
      else:
        opSAY(s,FUMES_BURN)
        opGOTO(s,YLEM)
        CALL(s,CORONER)
  opQUIT(s)
at_BREATHTAKER_2 = mkAT('BREATHTAKER', at_func_BREATHTAKER_2)

def at_func_BOULDERS(s):
  MOVE(s,WEST,WARMJUNCTN)
  MOVE(s,OUT,WARMJUNCTN)
  MOVE(s,CRAWL,WARMJUNCTN)
  MOVE(s,FORK,FORK)
  MOVE(s,VIEW,BREATHTAKER)
at_BOULDERS = mkAT('BOULDERS', at_func_BOULDERS)

def at_func_LIMESTONE(s):
  MOVE(s,NORTH,FORK)
  MOVE(s,UP,FORK)
  MOVE(s,FORK,FORK)
  MOVE(s,SOUTH,BARREN)
  MOVE(s,DOWN,BARREN)
  MOVE(s,BARREN,BARREN)
  MOVE(s,VIEW,BREATHTAKER)
at_LIMESTONE = mkAT('LIMESTONE', at_func_LIMESTONE)

def at_func_BARREN(s):
  MOVE(s,WEST,LIMESTONE)
  MOVE(s,UP,LIMESTONE)
  MOVE(s,FORK,FORK)
  MOVE(s,EAST,BEARHERE)
  MOVE(s,INWARD,BEARHERE)
  MOVE(s,BARREN,BEARHERE)
  MOVE(s,ENTER,BEARHERE)
  MOVE(s,VIEW,BREATHTAKER)
at_BARREN = mkAT('BARREN', at_func_BARREN)

def at_func_BEARHERE(s):
  KEYWORD(s,GET,AXE)
  NEAR(s,AXE)
  if  ((((((((((((((( HAVEP(s,AXE)  or  EQP(s,AXE,0) ) )))))))))))))) :
    opPROCEED(s)
  else:
    NAME(s,CANTGETAXE,ARG2)
    opQUIT(s)
at_BEARHERE = mkAT('BEARHERE', at_func_BEARHERE)

def at_func_BEARHERE_1(s):
  MOVE(s,WEST,BARREN)
  MOVE(s,OUT,BARREN)
  MOVE(s,FORK,FORK)
  MOVE(s,VIEW,BREATHTAKER)
at_BEARHERE_1 = mkAT('BEARHERE', at_func_BEARHERE_1)

def at_func_MAZED_131(s):
  MOVE(s,WEST,MAZED_107)
  MOVE(s,SE,MAZED_132)
  MOVE(s,NW,MAZED_133)
  MOVE(s,SW,MAZED_134)
  MOVE(s,NE,MAZED_135)
  MOVE(s,UP,MAZED_136)
  MOVE(s,DOWN,MAZED_137)
  MOVE(s,NORTH,MAZED_138)
  MOVE(s,SOUTH,MAZED_139)
  MOVE(s,EAST,MAZED_112)
at_MAZED_131 = mkAT('MAZED_131', at_func_MAZED_131)

def at_func_MAZED_132(s):
  MOVE(s,NW,MAZED_107)
  MOVE(s,UP,MAZED_131)
  MOVE(s,NORTH,MAZED_133)
  MOVE(s,SOUTH,MAZED_134)
  MOVE(s,WEST,MAZED_135)
  MOVE(s,SW,MAZED_136)
  MOVE(s,NE,MAZED_137)
  MOVE(s,EAST,MAZED_138)
  MOVE(s,DOWN,MAZED_139)
  MOVE(s,SE,MAZED_112)
at_MAZED_132 = mkAT('MAZED_132', at_func_MAZED_132)

def at_func_MAZED_133(s):
  MOVE(s,UP,MAZED_107)
  MOVE(s,DOWN,MAZED_131)
  MOVE(s,WEST,MAZED_132)
  MOVE(s,NE,MAZED_134)
  MOVE(s,SW,MAZED_135)
  MOVE(s,EAST,MAZED_136)
  MOVE(s,NORTH,MAZED_137)
  MOVE(s,NW,MAZED_138)
  MOVE(s,SE,MAZED_139)
  MOVE(s,SOUTH,MAZED_112)
at_MAZED_133 = mkAT('MAZED_133', at_func_MAZED_133)

def at_func_MAZED_134(s):
  MOVE(s,NE,MAZED_107)
  MOVE(s,NORTH,MAZED_131)
  MOVE(s,NW,MAZED_132)
  MOVE(s,SE,MAZED_133)
  MOVE(s,EAST,MAZED_135)
  MOVE(s,DOWN,MAZED_136)
  MOVE(s,SOUTH,MAZED_137)
  MOVE(s,UP,MAZED_138)
  MOVE(s,WEST,MAZED_139)
  MOVE(s,SW,MAZED_112)
at_MAZED_134 = mkAT('MAZED_134', at_func_MAZED_134)

def at_func_MAZED_135(s):
  MOVE(s,NORTH,MAZED_107)
  MOVE(s,SE,MAZED_131)
  MOVE(s,DOWN,MAZED_132)
  MOVE(s,SOUTH,MAZED_133)
  MOVE(s,EAST,MAZED_134)
  MOVE(s,WEST,MAZED_136)
  MOVE(s,SW,MAZED_137)
  MOVE(s,NE,MAZED_138)
  MOVE(s,NW,MAZED_139)
  MOVE(s,UP,MAZED_112)
at_MAZED_135 = mkAT('MAZED_135', at_func_MAZED_135)

def at_func_MAZED_136(s):
  MOVE(s,EAST,MAZED_107)
  MOVE(s,WEST,MAZED_131)
  MOVE(s,UP,MAZED_132)
  MOVE(s,SW,MAZED_133)
  MOVE(s,DOWN,MAZED_134)
  MOVE(s,SOUTH,MAZED_135)
  MOVE(s,NW,MAZED_137)
  MOVE(s,SE,MAZED_138)
  MOVE(s,NE,MAZED_139)
  MOVE(s,NORTH,MAZED_112)
at_MAZED_136 = mkAT('MAZED_136', at_func_MAZED_136)

def at_func_MAZED_137(s):
  MOVE(s,SE,MAZED_107)
  MOVE(s,NE,MAZED_131)
  MOVE(s,SOUTH,MAZED_132)
  MOVE(s,DOWN,MAZED_133)
  MOVE(s,UP,MAZED_134)
  MOVE(s,NW,MAZED_135)
  MOVE(s,NORTH,MAZED_136)
  MOVE(s,SW,MAZED_138)
  MOVE(s,EAST,MAZED_139)
  MOVE(s,WEST,MAZED_112)
at_MAZED_137 = mkAT('MAZED_137', at_func_MAZED_137)

def at_func_MAZED_138(s):
  MOVE(s,DOWN,MAZED_107)
  MOVE(s,EAST,MAZED_131)
  MOVE(s,NE,MAZED_132)
  MOVE(s,UP,MAZED_133)
  MOVE(s,WEST,MAZED_134)
  MOVE(s,NORTH,MAZED_135)
  MOVE(s,SOUTH,MAZED_136)
  MOVE(s,SE,MAZED_137)
  MOVE(s,SW,MAZED_139)
  MOVE(s,NW,MAZED_112)
at_MAZED_138 = mkAT('MAZED_138', at_func_MAZED_138)

def at_func_MAZED_139(s):
  MOVE(s,SW,MAZED_107)
  MOVE(s,NW,MAZED_131)
  MOVE(s,EAST,MAZED_132)
  MOVE(s,WEST,MAZED_133)
  MOVE(s,NORTH,MAZED_134)
  MOVE(s,DOWN,MAZED_135)
  MOVE(s,SE,MAZED_136)
  MOVE(s,UP,MAZED_137)
  MOVE(s,SOUTH,MAZED_138)
  MOVE(s,NE,MAZED_112)
at_MAZED_139 = mkAT('MAZED_139', at_func_MAZED_139)

def at_func_MAZED_140(s):
  MOVE(s,NORTH,MAZED_112)
  MOVE(s,OUT,MAZED_112)
at_MAZED_140 = mkAT('MAZED_140', at_func_MAZED_140)

def at_func_MAZED_140_1(s):
  KEYWORD(s,DROP,COINS)
  HAVE(s,COINS)
  APPORT(s,COINS,LIMBO)
  APPORT(s,BATTERIES,HERE)
  opSAY(s,OK)
  opSAY(s,BATTERIES)
  opQUIT(s)
at_MAZED_140_1 = mkAT('MAZED_140', at_func_MAZED_140_1)

def at_func_LIMBO(s):
  MOVE(s,OUT,BUILDING)
at_LIMBO = mkAT('LIMBO', at_func_LIMBO)

def at_func_SANDSTONE(s):
  MOVE(s,WEST,MISTS)
  MOVE(s,OUT,MISTS)
  MOVE(s,MISTS,MISTS)
at_SANDSTONE = mkAT('SANDSTONE', at_func_SANDSTONE)

def at_func_MORION(s):
  MOVE(s,SOUTH,MTKING)
  MOVE(s,OUT,MTKING)
at_MORION = mkAT('MORION', at_func_MORION)

def at_func_VAULT(s):
  ANYOF(s,[UP,OUT,NORTH ])
  if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
    opSAY(s,SAFE_BLOCKS)
  else:
    opGOTO(s,MTKING)
  opQUIT(s)
at_VAULT = mkAT('VAULT', at_func_VAULT)

def at_func_VAULT_1(s):
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,INSAFE)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,SAFE,0) ) )))))))))))))) :
      opSAY(s,CANTENTERSAFE)
      opQUIT(s)
  KEYWORD(s,IN)
  if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
    opSET(s,SAFEEXIT,HERE)
    opGOTO(s,INSAFE)
  else:
    opSAY(s,CANTENTERSAFE)
  opQUIT(s)
at_VAULT_1 = mkAT('VAULT', at_func_VAULT_1)

def at_func_INSAFE(s):
  KEYWORD(s,OUT)
  opGOTO(s,SAFEEXIT)
  opQUIT(s)
at_INSAFE = mkAT('INSAFE', at_func_INSAFE)

def at_func_INSAFE_1(s):
  KEYWORD(s,SAFE)
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    NAME(s,WHAT_DO,ARG2)
  else:
    if  ((((((((((((((( KEYP(s,CLOSE) ))))))))))))))) :
      opSAY(s,NO_HANDLE)
    else:
      if  ((((((((((((((( KEYP(s,OPEN) ))))))))))))))) :
        NAME(s,ALREADY_OPEN,ARG2)
      else:
        opSAY(s,HAH_)
  opQUIT(s)
at_INSAFE_1 = mkAT('INSAFE', at_func_INSAFE_1)

def at_func_CORRID_1(s):
  MOVE(s,SOUTH,MTKING)
  MOVE(s,NORTH,CORRID_2)
at_CORRID_1 = mkAT('CORRID_1', at_func_CORRID_1)

def at_func_CORRID_2(s):
  MOVE(s,SOUTH,CORRID_1)
  MOVE(s,WEST,CORRID_1)
  MOVE(s,NORTH,TOOL)
  MOVE(s,EAST,TOOL)
at_CORRID_2 = mkAT('CORRID_2', at_func_CORRID_2)

def at_func_TOOL(s):
  MOVE(s,OUT,CORRID_2)
  MOVE(s,SOUTH,CORRID_2)
at_TOOL = mkAT('TOOL', at_func_TOOL)

def at_func_CORRID_3(s):
  MOVE(s,SOUTH,MTKING)
  MOVE(s,NORTH,SPHERICAL)
  MOVE(s,EAST,CUBICLE)
at_CORRID_3 = mkAT('CORRID_3', at_func_CORRID_3)

def at_func_CUBICLE(s):
  MOVE(s,OUT,CORRID_3)
  MOVE(s,CORRIDOR,CORRID_3)
  MOVE(s,SOUTH,CORRID_3)
at_CUBICLE = mkAT('CUBICLE', at_func_CUBICLE)

def at_func_SPHERICAL(s):
  MOVE(s,OUT,CORRID_3)
  MOVE(s,NORTH,CORRID_3)
  MOVE(s,CORRIDOR,CORRID_3)
at_SPHERICAL = mkAT('SPHERICAL', at_func_SPHERICAL)

def at_func_TUNNEL_1(s):
  MOVE(s,SOUTH,GIANT)
  MOVE(s,NORTH,GLASSY)
at_TUNNEL_1 = mkAT('TUNNEL_1', at_func_TUNNEL_1)

def at_func_GLASSY(s):
  MOVE(s,SOUTH,TUNNEL_1)
at_GLASSY = mkAT('GLASSY', at_func_GLASSY)

def at_func_GLASSY_1(s):
  ANYOF(s,[NORTH,LAIR ])
  if  ((((((((((((((( NEARP(s,OGRE) ))))))))))))))) :
    opSAY(s,OGRE_BLOCKS)
  else:
    opGOTO(s,LAIR)
  opQUIT(s)
at_GLASSY_1 = mkAT('GLASSY', at_func_GLASSY_1)

def at_func_LAIR(s):
  MOVE(s,EAST,BRINK_1)
  MOVE(s,WEST,GLASSY)
at_LAIR = mkAT('LAIR', at_func_LAIR)

def at_func_BRINK_1(s):
  MOVE(s,NORTH,LAIR)
  MOVE(s,WEST,BRINK_2)
  MOVE(s,EAST,BRINK_3)
  MOVE(s,NORTH,LAIR)
at_BRINK_1 = mkAT('BRINK_1', at_func_BRINK_1)

def at_func_BRINK_1_1(s):
  KEYWORD(s,JUMP)
  CALL(s,PLUNGE)
at_BRINK_1_1 = mkAT('BRINK_1', at_func_BRINK_1_1)

def at_func_BRINK_2(s):
  MOVE(s,NORTH,BRINK_1)
  MOVE(s,SOUTHEAST,ICE)
at_BRINK_2 = mkAT('BRINK_2', at_func_BRINK_2)

def at_func_BRINK_2_1(s):
  KEYWORD(s,JUMP)
  CALL(s,PLUNGE)
at_BRINK_2_1 = mkAT('BRINK_2', at_func_BRINK_2_1)

def at_func_ICE(s):
  MOVE(s,NORTHWEST,BRINK_2)
  SMOVE(s,DOWN,SLIDE,OOF)
  SMOVE(s,EAST,SLIDE,OOF)
  SMOVE(s,SLIDE,SLIDE,OOF)
at_ICE = mkAT('ICE', at_func_ICE)

def at_func_SLIDE(s):
  ANYOF(s,[SLIDE,UP,NORTH,CLIMB ])
  opSAY(s,SLIDE_SLIPPERY)
  opQUIT(s)
at_SLIDE = mkAT('SLIDE', at_func_SLIDE)

def at_func_SLIDE_1(s):
  MOVE(s,SOUTH,ICECAVE_2A)
  MOVE(s,NORTHWEST,ICECAVE_4)
at_SLIDE_1 = mkAT('SLIDE', at_func_SLIDE_1)

def at_func_ICECAVE_1(s):
  MOVE(s,WEST,ICECAVE_2)
  MOVE(s,NORTH,ICECAVE_1A)
at_ICECAVE_1 = mkAT('ICECAVE_1', at_func_ICECAVE_1)

def at_func_ICECAVE_1A(s):
  MOVE(s,SOUTH,ICECAVE_1)
at_ICECAVE_1A = mkAT('ICECAVE_1A', at_func_ICECAVE_1A)

def at_func_ICECAVE_2(s):
  MOVE(s,EAST,ICECAVE_1)
  MOVE(s,WEST,ICECAVE_3)
  MOVE(s,NORTH,ICECAVE_2A)
at_ICECAVE_2 = mkAT('ICECAVE_2', at_func_ICECAVE_2)

def at_func_ICECAVE_2A(s):
  MOVE(s,NORTH,SLIDE)
  MOVE(s,SOUTH,ICECAVE_2)
at_ICECAVE_2A = mkAT('ICECAVE_2A', at_func_ICECAVE_2A)

def at_func_ICECAVE_3(s):
  MOVE(s,EAST,ICECAVE_2)
  MOVE(s,NORTH,ICECAVE_3A)
at_ICECAVE_3 = mkAT('ICECAVE_3', at_func_ICECAVE_3)

def at_func_ICECAVE_3A(s):
  MOVE(s,SOUTH,ICECAVE_3)
at_ICECAVE_3A = mkAT('ICECAVE_3A', at_func_ICECAVE_3A)

def at_func_ICECAVE_4(s):
  MOVE(s,EAST,SLIDE)
  MOVE(s,WEST,ICECAVE_5)
at_ICECAVE_4 = mkAT('ICECAVE_4', at_func_ICECAVE_4)

def at_func_ICECAVE_5(s):
  MOVE(s,NORTHEAST,ICECAVE_4)
  MOVE(s,SOUTH,ICECAVE_6)
at_ICECAVE_5 = mkAT('ICECAVE_5', at_func_ICECAVE_5)

def at_func_ICECAVE_6(s):
  MOVE(s,NORTH,ICECAVE_5)
  MOVE(s,SOUTH,ICECAVE_7)
  MOVE(s,WEST,ICECAVE_9)
at_ICECAVE_6 = mkAT('ICECAVE_6', at_func_ICECAVE_6)

def at_func_ICECAVE_7(s):
  MOVE(s,NORTH,ICECAVE_6)
at_ICECAVE_7 = mkAT('ICECAVE_7', at_func_ICECAVE_7)

def at_func_ICECAVE_8(s):
  MOVE(s,NORTH,ICECAVE_9)
at_ICECAVE_8 = mkAT('ICECAVE_8', at_func_ICECAVE_8)

def at_func_ICECAVE_9(s):
  MOVE(s,EAST,ICECAVE_6)
  MOVE(s,SOUTH,ICECAVE_8)
  MOVE(s,NORTH,ICECAVE_10)
at_ICECAVE_9 = mkAT('ICECAVE_9', at_func_ICECAVE_9)

def at_func_ICECAVE_10(s):
  MOVE(s,SOUTH,ICECAVE_9)
  MOVE(s,NORTHWEST,ICECAVE_11)
at_ICECAVE_10 = mkAT('ICECAVE_10', at_func_ICECAVE_10)

def at_func_ICECAVE_11(s):
  MOVE(s,EAST,ICECAVE_10)
  MOVE(s,WEST,ICECAVE_12)
at_ICECAVE_11 = mkAT('ICECAVE_11', at_func_ICECAVE_11)

def at_func_ICECAVE_12(s):
  MOVE(s,NORTHEAST,ICECAVE_11)
  MOVE(s,SOUTH,ICECAVE_12A)
  MOVE(s,WEST,ICECAVE_15)
at_ICECAVE_12 = mkAT('ICECAVE_12', at_func_ICECAVE_12)

def at_func_ICECAVE_12A(s):
  MOVE(s,NORTH,ICECAVE_12)
  MOVE(s,SOUTH,ICECAVE_13)
at_ICECAVE_12A = mkAT('ICECAVE_12A', at_func_ICECAVE_12A)

def at_func_ICECAVE_13(s):
  MOVE(s,NORTH,ICECAVE_12A)
at_ICECAVE_13 = mkAT('ICECAVE_13', at_func_ICECAVE_13)

def at_func_ICECAVE_14(s):
  MOVE(s,NORTH,ICECAVE_15A)
at_ICECAVE_14 = mkAT('ICECAVE_14', at_func_ICECAVE_14)

def at_func_ICECAVE_15(s):
  MOVE(s,EAST,ICECAVE_12)
  MOVE(s,SOUTH,ICECAVE_15A)
  MOVE(s,NORTHWEST,ICECAVE_16)
at_ICECAVE_15 = mkAT('ICECAVE_15', at_func_ICECAVE_15)

def at_func_ICECAVE_15A(s):
  MOVE(s,SOUTH,ICECAVE_14)
  MOVE(s,NORTH,ICECAVE_15)
at_ICECAVE_15A = mkAT('ICECAVE_15A', at_func_ICECAVE_15A)

def at_func_ICECAVE_16(s):
  MOVE(s,EAST,ICECAVE_15)
  MOVE(s,WEST,ICECAVE_17)
at_ICECAVE_16 = mkAT('ICECAVE_16', at_func_ICECAVE_16)

def at_func_ICECAVE_17(s):
  MOVE(s,NORTHEAST,ICECAVE_16)
  MOVE(s,SOUTH,ICECAVE_18)
at_ICECAVE_17 = mkAT('ICECAVE_17', at_func_ICECAVE_17)

def at_func_ICECAVE_18(s):
  MOVE(s,NORTH,ICECAVE_17)
  MOVE(s,SOUTH,ICECAVE_19)
  MOVE(s,WEST,ICECAVE_21)
  MOVE(s,NORTHWEST,ICECAVE_22)
at_ICECAVE_18 = mkAT('ICECAVE_18', at_func_ICECAVE_18)

def at_func_ICECAVE_19(s):
  MOVE(s,NORTH,ICECAVE_18)
  MOVE(s,WEST,ICECAVE_20)
at_ICECAVE_19 = mkAT('ICECAVE_19', at_func_ICECAVE_19)

def at_func_ICECAVE_20(s):
  MOVE(s,EAST,ICECAVE_19)
  MOVE(s,NORTH,ICECAVE_21)
at_ICECAVE_20 = mkAT('ICECAVE_20', at_func_ICECAVE_20)

def at_func_ICECAVE_21(s):
  MOVE(s,EAST,ICECAVE_18)
  MOVE(s,SOUTH,ICECAVE_20)
at_ICECAVE_21 = mkAT('ICECAVE_21', at_func_ICECAVE_21)

def at_func_ICECAVE_22(s):
  MOVE(s,SOUTHEAST,ICECAVE_18)
  MOVE(s,NORTHWEST,ICECAVE_23)
at_ICECAVE_22 = mkAT('ICECAVE_22', at_func_ICECAVE_22)

def at_func_ICECAVE_23(s):
  MOVE(s,EAST,ICECAVE_22)
  MOVE(s,WEST,ICECAVE_24)
at_ICECAVE_23 = mkAT('ICECAVE_23', at_func_ICECAVE_23)

def at_func_ICECAVE_24(s):
  MOVE(s,NORTHEAST,ICECAVE_23)
  MOVE(s,SOUTH,ICECAVE_25)
  MOVE(s,WEST,ICECAVE_29)
at_ICECAVE_24 = mkAT('ICECAVE_24', at_func_ICECAVE_24)

def at_func_ICECAVE_25(s):
  MOVE(s,NORTH,ICECAVE_24)
  MOVE(s,SOUTH,ICECAVE_26)
  MOVE(s,WEST,ICECAVE_28)
  MOVE(s,NORTHWEST,ICECAVE_28A)
at_ICECAVE_25 = mkAT('ICECAVE_25', at_func_ICECAVE_25)

def at_func_ICECAVE_26(s):
  MOVE(s,NORTH,ICECAVE_25)
  MOVE(s,NORTHWEST,ICECAVE_27)
at_ICECAVE_26 = mkAT('ICECAVE_26', at_func_ICECAVE_26)

def at_func_ICECAVE_27(s):
  MOVE(s,SOUTHEAST,ICECAVE_26)
  MOVE(s,NORTH,ICECAVE_28)
at_ICECAVE_27 = mkAT('ICECAVE_27', at_func_ICECAVE_27)

def at_func_ICECAVE_28(s):
  MOVE(s,EAST,ICECAVE_25)
  MOVE(s,SOUTH,ICECAVE_27)
at_ICECAVE_28 = mkAT('ICECAVE_28', at_func_ICECAVE_28)

def at_func_ICECAVE_28A(s):
  MOVE(s,SOUTHEAST,ICECAVE_25)
  MOVE(s,NORTH,ICECAVE_29)
at_ICECAVE_28A = mkAT('ICECAVE_28A', at_func_ICECAVE_28A)

def at_func_ICECAVE_29(s):
  MOVE(s,EAST,ICECAVE_24)
  MOVE(s,SOUTH,ICECAVE_28A)
  MOVE(s,NORTHWEST,ICECAVE_30)
at_ICECAVE_29 = mkAT('ICECAVE_29', at_func_ICECAVE_29)

def at_func_ICECAVE_30(s):
  MOVE(s,EAST,ICECAVE_29)
  SMOVE(s,THURB,ICE,FOOF)
at_ICECAVE_30 = mkAT('ICECAVE_30', at_func_ICECAVE_30)

def at_func_BRINK_3(s):
  MOVE(s,NORTH,BRINK_1)
  MOVE(s,NORTHEAST,CRACK_1)
  MOVE(s,CRACK,CRACK_1)
at_BRINK_3 = mkAT('BRINK_3', at_func_BRINK_3)

def at_func_BRINK_3_1(s):
  KEYWORD(s,JUMP)
  CALL(s,PLUNGE)
at_BRINK_3_1 = mkAT('BRINK_3', at_func_BRINK_3_1)

def at_func_CRACK_1(s):
  MOVE(s,SOUTHWEST,BRINK_3)
  MOVE(s,SOUTHEAST,CRACK_2)
at_CRACK_1 = mkAT('CRACK_1', at_func_CRACK_1)

def at_func_CRACK_2(s):
  MOVE(s,WEST,CRACK_1)
at_CRACK_2 = mkAT('CRACK_2', at_func_CRACK_2)

def at_func_CRACK_2_1(s):
  KEYWORD(s,SOUTH)
  if  ((((((((((((((( NEARP(s,SLIME) ))))))))))))))) :
    opSAY(s,SLIMED)
    CALL(s,CORONER)
  else:
    opGOTO(s,CRACK_3)
  opQUIT(s)
at_CRACK_2_1 = mkAT('CRACK_2', at_func_CRACK_2_1)

def at_func_CRACK_3(s):
  MOVE(s,NORTH,CRACK_2)
  MOVE(s,SOUTH,CRACK_4)
  MOVE(s,CRAWL,CRACK_4)
at_CRACK_3 = mkAT('CRACK_3', at_func_CRACK_3)

def at_func_CRACK_4(s):
  MOVE(s,NORTH,CRACK_3)
  MOVE(s,OUT,CRACK_3)
  MOVE(s,CRAWL,CRACK_3)
at_CRACK_4 = mkAT('CRACK_4', at_func_CRACK_4)

def at_func_ARCH_COR_1(s):
  MOVE(s,WEST,ARCHED)
at_ARCH_COR_1 = mkAT('ARCH_COR_1', at_func_ARCH_COR_1)

def at_func_ARCH_COR_1_1(s):
  KEYWORD(s,EAST)
  if  ((((((((((((((( EQP(s,QUICKSAND,0)  or  HAVEP(s,CLAM) )  or  HAVEP(s,OYSTER) ) ))))))))))))) :
    opSET(s,QUICKSAND,0)
    if  ((((((((((((((( BITP(s,QUICKSAND,SPECIAL1) ))))))))))))))) :
      opSAY(s,SCHLURP2)
    else:
      opSAY(s,SCHLURP)
      BIS(s,QUICKSAND,SPECIAL1)
    opGOTO(s,YLEM)
    CALL(s,CORONER)
  else:
    opGOTO(s,ARCH_COR_2)
    opSET(s,QUICKSAND,0)
  opQUIT(s)
at_ARCH_COR_1_1 = mkAT('ARCH_COR_1', at_func_ARCH_COR_1_1)

def at_func_ARCH_COR_2(s):
  MOVE(s,NORTH,ARCH_FORK)
at_ARCH_COR_2 = mkAT('ARCH_COR_2', at_func_ARCH_COR_2)

def at_func_ARCH_COR_2_1(s):
  KEYWORD(s,WEST)
  if  ((((((((((((((( EQP(s,QUICKSAND,0) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,QUICKSAND,SPECIAL1) ))))))))))))))) :
      opSAY(s,SCHLURP2)
    else:
      opSAY(s,SCHLURP)
      BIS(s,QUICKSAND,SPECIAL1)
    opGOTO(s,YLEM)
    CALL(s,CORONER)
  else:
    opGOTO(s,ARCH_COR_1)
    opSET(s,QUICKSAND,0)
  opQUIT(s)
at_ARCH_COR_2_1 = mkAT('ARCH_COR_2', at_func_ARCH_COR_2_1)

def at_func_ARCH_FORK(s):
  MOVE(s,SOUTH,ARCH_COR_2)
  MOVE(s,NORTH,FOURIER)
  MOVE(s,EAST,JONAH)
  MOVE(s,JONAH,JONAH)
  MOVE(s,FOURIER,FOURIER)
at_ARCH_FORK = mkAT('ARCH_FORK', at_func_ARCH_FORK)

def at_func_FOURIER(s):
  MOVE(s,NORTHWEST,ARCH_FORK)
  MOVE(s,SOUTHWEST,SHELF)
at_FOURIER = mkAT('FOURIER', at_func_FOURIER)

def at_func_SHELF(s):
  MOVE(s,WEST,FOURIER)
  MOVE(s,DOWN,BEACH)
  MOVE(s,STEPS,BEACH)
at_SHELF = mkAT('SHELF', at_func_SHELF)

def at_func_BEACH(s):
  ANYOF(s,[UP,SHELF,STEPS,WEST ])
  opSET(s,DINGHY,1)
  opGOTO(s,SHELF)
  opQUIT(s)
at_BEACH = mkAT('BEACH', at_func_BEACH)

def at_func_BEACH_1(s):
  ANYOF(s,[WATER,FILL,DRINK ])
  opSAY(s,SALT_H20_BAD)
  opQUIT(s)
at_BEACH_1 = mkAT('BEACH', at_func_BEACH_1)

def at_func_JONAH(s):
  MOVE(s,SOUTH,IN_JONAH)
  MOVE(s,WEST,ARCH_FORK)
at_JONAH = mkAT('JONAH', at_func_JONAH)

def at_func_IN_JONAH(s):
  MOVE(s,NORTH,JONAH)
  MOVE(s,OUT,JONAH)
at_IN_JONAH = mkAT('IN_JONAH', at_func_IN_JONAH)

def at_func_FACES(s):
  MOVE(s,NORTH,BY_FIGURE)
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,BREATHTAKER)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,GORGE,0) ) )))))))))))))) :
      opSAY(s,NO_ARCH)
      opQUIT(s)
at_FACES = mkAT('FACES', at_func_FACES)

def at_func_FACES_1(s):
  ANYOF(s,[CROSS,GORGE,SOUTH ])
  if  ((((((((((((((( EQP(s,GORGE,0) ))))))))))))))) :
    opSAY(s,NO_ARCH)
  else:
    if  ((((((((((((((( HAVEP(s,RING) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,SCEPTRE) ))))))))))))))) :
        opSAY(s,GHOST_BANG)
        opGOTO(s,YLEM)
        opSET(s,GORGE,0)
        CALL(s,CORONER)
      else:
        opGOTO(s,BREATHTAKER)
    else:
      opSAY(s,FUMES_BURN)
      opGOTO(s,YLEM)
      CALL(s,CORONER)
  opQUIT(s)
at_FACES_1 = mkAT('FACES', at_func_FACES_1)

def at_func_BY_FIGURE(s):
  if  ((((((((((((((( EQP(s,STATUE,1) ))))))))))))))) :
    MOVE(s,NORTHWEST,PLAIN_1)
    MOVE(s,NORTH,BASQUE_1)
    MOVE(s,NORTHEAST,BANSHEE_1)
  MOVE(s,SOUTH,FACES)
at_BY_FIGURE = mkAT('BY_FIGURE', at_func_BY_FIGURE)

def at_func_PLAIN_1(s):
  MOVE(s,SOUTH,BY_FIGURE)
  if  ((((((((((((((( KEYP(s,NORTH) ))))))))))))))) :
    opSET(s,FOG,0)
    APPORT(s,FOG,PLAIN_2)
    opGOTO(s,PLAIN_2)
    opQUIT(s)
at_PLAIN_1 = mkAT('PLAIN_1', at_func_PLAIN_1)

def at_func_PLAIN_2(s):
  ANYOF(s,[NORTH,EAST,SOUTH,WEST ,NE,NW,SE,SW ])
  for o in all_objects:
    if not NEARP(s, o): continue
    LDA(s, I, o)
    if  ((((((((((((((( NEARP(s,I)  and   not  HAVEP(s,I) )  and  BITP(s,I,PORTABLE) ) ))))))))))))) :
      APPORT(s,I,YLEM)
  LDA(s,I,EAST)
  ADD(s,I,GLOW)
  if  ((((((((((((((( EQP(s,I,ARG2)  and  EQP(s,STATUS,2) )  or  EQP(s,I,ARG1) )  and  NEARP(s,GLOW) ) )))))))))))) :
    opGOTO(s,PLAIN_3)
    opSET(s,FOG,8)
  else:
    opGOTO(s,PLAIN_2)
  opQUIT(s)
at_PLAIN_2 = mkAT('PLAIN_2', at_func_PLAIN_2)

def at_func_PLAIN_3(s):
  if  ((((((((((((((( KEYP(s,DOWN) ))))))))))))))) :
    opGOTO(s,NONDESCRIPT)
    APPORT(s,FOG,PLAIN_1)
    opQUIT(s)
at_PLAIN_3 = mkAT('PLAIN_3', at_func_PLAIN_3)

def at_func_PLAIN_3_1(s):
  ANYOF(s,[NORTH,EAST,SOUTH,WEST ,NE,NW,SE,SW ])
  opGOTO(s,PLAIN_2)
  opSET(s,FOG,0)
  opQUIT(s)
at_PLAIN_3_1 = mkAT('PLAIN_3', at_func_PLAIN_3_1)

def at_func_NONDESCRIPT(s):
  MOVE(s,NORTH,PENTAGRAM)
  MOVE(s,PENTAGRAM,PENTAGRAM)
at_NONDESCRIPT = mkAT('NONDESCRIPT', at_func_NONDESCRIPT)

def at_func_NONDESCRIPT_1(s):
  ANYOF(s,[UP,SOUTH ])
  APPORT(s,FOG,PLAIN_2)
  opGOTO(s,PLAIN_3)
  opQUIT(s)
at_NONDESCRIPT_1 = mkAT('NONDESCRIPT', at_func_NONDESCRIPT_1)

def at_func_PENTAGRAM(s):
  KEYWORD(s,FLASK)
  ANYOF(s,[DROP,THROW ])
  HAVE(s,FLASK)
  if  ((((((((((((((( EQP(s,FLASK,1) ))))))))))))))) :
    opDROP(s,FLASK)
    opSAY(s,SET_FLASK_DOWN)
    opSET(s,FLASK,0)
    opQUIT(s)
at_PENTAGRAM = mkAT('PENTAGRAM', at_func_PENTAGRAM)

def at_func_PENTAGRAM_1(s):
  MOVE(s,WEST,NONDESCRIPT)
  MOVE(s,OUT,NONDESCRIPT)
  MOVE(s,NONDESCRIPT,NONDESCRIPT)
  MOVE(s,NORTH,CHIMNEY)
  MOVE(s,CRACK,CHIMNEY)
  MOVE(s,CHIMNEY,CHIMNEY)
at_PENTAGRAM_1 = mkAT('PENTAGRAM', at_func_PENTAGRAM_1)

def at_func_CHIMNEY(s):
  MOVE(s,UP,TUBE)
  MOVE(s,CLIMB,TUBE)
  MOVE(s,TUBE,TUBE)
  MOVE(s,SOUTH,PENTAGRAM)
  MOVE(s,PENTAGRAM,PENTAGRAM)
  MOVE(s,CRACK,PENTAGRAM)
at_CHIMNEY = mkAT('CHIMNEY', at_func_CHIMNEY)

def at_func_TUBE(s):
  MOVE(s,DOWN,CHIMNEY)
  MOVE(s,CHIMNEY,CHIMNEY)
  MOVE(s,CLIMB,CHIMNEY)
  MOVE(s,TUBE,TUBE_SLIDE)
  MOVE(s,SLIDE,TUBE_SLIDE)
  MOVE(s,SOUTH,TUBE_SLIDE)
at_TUBE = mkAT('TUBE', at_func_TUBE)

def at_func_TUBE_SLIDE(s):
  SMOVE(s,SOUTH,PLAIN_1,OOF)
  SMOVE(s,DOWN,PLAIN_1,OOF)
  SMOVE(s,SLIDE,PLAIN_1,OOF)
  MOVE(s,NORTH,TUBE)
  MOVE(s,CHIMNEY,CHIMNEY)
  MOVE(s,TUBE,CHIMNEY)
at_TUBE_SLIDE = mkAT('TUBE_SLIDE', at_func_TUBE_SLIDE)

def at_func_BASQUE_1(s):
  MOVE(s,SOUTH,BY_FIGURE)
  if  ((((((((((((((( KEYP(s,NORTH) ))))))))))))))) :
    opGOTO(s,BASQUE_2)
    ADD(s,BASILISK,1)
    if  ((((((((((((((( EQP(s,BASILISK,1) ))))))))))))))) :
      opSAY(s,BAS_GRUMBLE)
    opQUIT(s)
at_BASQUE_1 = mkAT('BASQUE_1', at_func_BASQUE_1)

def at_func_BASQUE_2(s):
  MOVE(s,NORTH,BASQUE_FORK)
  if  ((((((((((((((( KEYP(s,SOUTH) ))))))))))))))) :
    SUB(s,BASILISK,1)
    if  ((((((((((((((( EQP(s,BASILISK,0) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,PLATE) ))))))))))))))) :
        opSAY(s,PETRIFY_SELF)
        opSET(s,BASILISK,2)
      else:
        opSAY(s,PETRIFY_ME)
        CALL(s,CORONER)
    opGOTO(s,BASQUE_1)
    opQUIT(s)
at_BASQUE_2 = mkAT('BASQUE_2', at_func_BASQUE_2)

def at_func_BASQUE_FORK(s):
  MOVE(s,NORTH,PEELGRUNT)
  MOVE(s,PEELGRUNT,PEELGRUNT)
  MOVE(s,SOUTH,BASQUE_2)
  MOVE(s,DOWN,ON_STEPS)
  MOVE(s,STEPS,ON_STEPS)
at_BASQUE_FORK = mkAT('BASQUE_FORK', at_func_BASQUE_FORK)

def at_func_PEELGRUNT(s):
  ANYOF(s,[SOUTH,OUT,FORK ])
  if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
    opSAY(s,SAFE_BLOCKS)
  else:
    opGOTO(s,BASQUE_FORK)
  opQUIT(s)
at_PEELGRUNT = mkAT('PEELGRUNT', at_func_PEELGRUNT)

def at_func_PEELGRUNT_1(s):
  if  ((((((((((((((( KEYP(s,BACK) ))))))))))))))) :
    LDA(s,I,INSAFE)
    if  ((((((((((((((( EQP(s,I,THERE)  and  EQP(s,SAFE,0) ) )))))))))))))) :
      opSAY(s,CANTENTERSAFE)
      opQUIT(s)
  KEYWORD(s,IN)
  if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
    opSET(s,SAFEEXIT,HERE)
    opGOTO(s,INSAFE)
  else:
    opSAY(s,CANTENTERSAFE)
  opQUIT(s)
at_PEELGRUNT_1 = mkAT('PEELGRUNT', at_func_PEELGRUNT_1)

def at_func_ON_STEPS(s):
  MOVE(s,UP,BASQUE_FORK)
  MOVE(s,DOWN,STEPS_EXIT)
  MOVE(s,STEPS,STEPS_EXIT)
at_ON_STEPS = mkAT('ON_STEPS', at_func_ON_STEPS)

def at_func_STEPS_EXIT(s):
  MOVE(s,UP,ON_STEPS)
  MOVE(s,DOWN,STORAGE)
  MOVE(s,NORTH,FAKE_Y2)
  MOVE(s,STEPS,STORAGE)
  MOVE(s,EXIT,FAKE_Y2)
at_STEPS_EXIT = mkAT('STEPS_EXIT', at_func_STEPS_EXIT)

def at_func_STORAGE(s):
  MOVE(s,UP,STEPS_EXIT)
  MOVE(s,STEPS,STEPS_EXIT)
at_STORAGE = mkAT('STORAGE', at_func_STORAGE)

def at_func_FAKE_Y2(s):
  MOVE(s,SOUTH,STEPS_EXIT)
  MOVE(s,WEST,CATACOMBS_1)
  MOVE(s,EAST,FAKE_JUMBLE)
at_FAKE_Y2 = mkAT('FAKE_Y2', at_func_FAKE_Y2)

def at_func_FAKE_Y2_1(s):
  ANYOF(s,[PLUGH,PLOVER ])
  if  ((((((((((((((( BITP(s,ADMIN,NOMAGIC) ))))))))))))))) :
    opSAY(s,NOTHING)
  else:
    opSAY(s,FOOF)
    opGOTO(s,PLATFORM)
  opQUIT(s)
at_FAKE_Y2_1 = mkAT('FAKE_Y2', at_func_FAKE_Y2_1)

def at_func_FAKE_JUMBLE(s):
  MOVE(s,DOWN,FAKE_Y2)
  MOVE(s,WEST,FAKE_Y2)
  MOVE(s,UP,CATACOMBS_1)
at_FAKE_JUMBLE = mkAT('FAKE_JUMBLE', at_func_FAKE_JUMBLE)

def at_func_AUDIENCE(s):
  MOVE(s,EAST,AUDIENCE_E)
  MOVE(s,WEST,CATACOMBS_11)
at_AUDIENCE = mkAT('AUDIENCE', at_func_AUDIENCE)

def at_func_AUDIENCE_E(s):
  MOVE(s,WEST,AUDIENCE)
at_AUDIENCE_E = mkAT('AUDIENCE_E', at_func_AUDIENCE_E)

def at_func_CATACOMBS_1(s):
  MOVE(s,SOUTH,CATACOMBS_2)
  ANYOF(s,[NORTH,NW,WEST,SW,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_1)
  opQUIT(s)
at_CATACOMBS_1 = mkAT('CATACOMBS_1', at_func_CATACOMBS_1)

def at_func_CATACOMBS_2(s):
  MOVE(s,SW,CATACOMBS_3)
  ANYOF(s,[NORTH,NW,WEST,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_1)
  opQUIT(s)
at_CATACOMBS_2 = mkAT('CATACOMBS_2', at_func_CATACOMBS_2)

def at_func_CATACOMBS_3(s):
  MOVE(s,NW,CATACOMBS_4)
  ANYOF(s,[NORTH,WEST,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_2)
  opQUIT(s)
at_CATACOMBS_3 = mkAT('CATACOMBS_3', at_func_CATACOMBS_3)

def at_func_CATACOMBS_4(s):
  MOVE(s,SOUTH,CATACOMBS_5)
  ANYOF(s,[NORTH,NW,WEST,SW,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_3)
  opQUIT(s)
at_CATACOMBS_4 = mkAT('CATACOMBS_4', at_func_CATACOMBS_4)

def at_func_CATACOMBS_5(s):
  MOVE(s,DOWN,CATACOMBS_6)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,SE,EAST,NE,UP ])
  opGOTO(s,CATACOMBS_4)
  opQUIT(s)
at_CATACOMBS_5 = mkAT('CATACOMBS_5', at_func_CATACOMBS_5)

def at_func_CATACOMBS_6(s):
  MOVE(s,WEST,CATACOMBS_7)
  ANYOF(s,[NORTH,NW,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_5)
  opQUIT(s)
at_CATACOMBS_6 = mkAT('CATACOMBS_6', at_func_CATACOMBS_6)

def at_func_CATACOMBS_7(s):
  MOVE(s,NW,CATACOMBS_8)
  ANYOF(s,[NORTH,WEST,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_6)
  opQUIT(s)
at_CATACOMBS_7 = mkAT('CATACOMBS_7', at_func_CATACOMBS_7)

def at_func_CATACOMBS_8(s):
  MOVE(s,NORTH,CATACOMBS_9)
  ANYOF(s,[NW,WEST,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_7)
  opQUIT(s)
at_CATACOMBS_8 = mkAT('CATACOMBS_8', at_func_CATACOMBS_8)

def at_func_CATACOMBS_9(s):
  MOVE(s,SOUTH,CATACOMBS_10)
  ANYOF(s,[NORTH,NW,WEST,SW,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_8)
  opQUIT(s)
at_CATACOMBS_9 = mkAT('CATACOMBS_9', at_func_CATACOMBS_9)

def at_func_CATACOMBS_10(s):
  MOVE(s,NORTH,CATACOMBS_11)
  ANYOF(s,[NW,WEST,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_9)
  opQUIT(s)
at_CATACOMBS_10 = mkAT('CATACOMBS_10', at_func_CATACOMBS_10)

def at_func_CATACOMBS_11(s):
  MOVE(s,SW,CATACOMBS_12)
  MOVE(s,EAST,AUDIENCE)
  ANYOF(s,[NORTH,NW,WEST,SOUTH,SE,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_10)
  opQUIT(s)
at_CATACOMBS_11 = mkAT('CATACOMBS_11', at_func_CATACOMBS_11)

def at_func_CATACOMBS_12(s):
  MOVE(s,EAST,CATACOMBS_13)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,SE,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_11)
  opQUIT(s)
at_CATACOMBS_12 = mkAT('CATACOMBS_12', at_func_CATACOMBS_12)

def at_func_CATACOMBS_13(s):
  MOVE(s,SE,CATACOMBS_14)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_12)
  opQUIT(s)
at_CATACOMBS_13 = mkAT('CATACOMBS_13', at_func_CATACOMBS_13)

def at_func_CATACOMBS_14(s):
  MOVE(s,NE,CATACOMBS_15)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,SE,EAST,UP,DOWN ])
  opGOTO(s,CATACOMBS_13)
  opQUIT(s)
at_CATACOMBS_14 = mkAT('CATACOMBS_14', at_func_CATACOMBS_14)

def at_func_CATACOMBS_15(s):
  MOVE(s,EAST,CATACOMBS_16)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,SE,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_14)
  opQUIT(s)
at_CATACOMBS_15 = mkAT('CATACOMBS_15', at_func_CATACOMBS_15)

def at_func_CATACOMBS_16(s):
  MOVE(s,SE,CATACOMBS_17)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_15)
  opQUIT(s)
at_CATACOMBS_16 = mkAT('CATACOMBS_16', at_func_CATACOMBS_16)

def at_func_CATACOMBS_17(s):
  MOVE(s,DOWN,CATACOMBS_18)
  ANYOF(s,[NORTH,NW,WEST,SW,SOUTH,SE,EAST,NE,UP ])
  opGOTO(s,CATACOMBS_16)
  opQUIT(s)
at_CATACOMBS_17 = mkAT('CATACOMBS_17', at_func_CATACOMBS_17)

def at_func_CATACOMBS_18(s):
  MOVE(s,SOUTH,CATACOMBS_19)
  ANYOF(s,[NORTH,NW,WEST,SW,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_17)
  opQUIT(s)
at_CATACOMBS_18 = mkAT('CATACOMBS_18', at_func_CATACOMBS_18)

def at_func_CATACOMBS_19(s):
  MOVE(s,NORTH,FAKE_Y2)
  ANYOF(s,[NW,WEST,SW,SOUTH,SE,EAST,NE,UP,DOWN ])
  opGOTO(s,CATACOMBS_18)
  opQUIT(s)
at_CATACOMBS_19 = mkAT('CATACOMBS_19', at_func_CATACOMBS_19)

def at_func_BANSHEE_1(s):
  MOVE(s,NORTHWEST,BY_FIGURE)
  MOVE(s,NORTH,GOLDEN)
  MOVE(s,GOLDEN,GOLDEN)
at_BANSHEE_1 = mkAT('BANSHEE_1', at_func_BANSHEE_1)

def at_func_GOLDEN(s):
  MOVE(s,NORTHEAST,ARABESQUE)
  MOVE(s,NORTHWEST,TRANSLUCENT)
  MOVE(s,ARABESQUE,ARABESQUE)
  MOVE(s,TRANSLUCENT,TRANSLUCENT)
  MOVE(s,SOUTH,BANSHEE_1)
at_GOLDEN = mkAT('GOLDEN', at_func_GOLDEN)

def at_func_ARABESQUE(s):
  MOVE(s,SOUTH,GOLDEN)
  MOVE(s,OUT,GOLDEN)
  MOVE(s,GOLDEN,GOLDEN)
at_ARABESQUE = mkAT('ARABESQUE', at_func_ARABESQUE)

def at_func_TRANSLUCENT(s):
  ANYOF(s,[OUT,EAST,GOLDEN ])
  if  ((((((((((((((( BITP(s,GOBLINS,SPECIAL1) ))))))))))))))) :
    pass
  else:
    BIS(s,GOBLINS,SPECIAL1)
    APPORT(s,GOBLINS,HERE)
    opSET(s,GOBLINS,-1)
  opGOTO(s,GOLDEN)
  opQUIT(s)
at_TRANSLUCENT = mkAT('TRANSLUCENT', at_func_TRANSLUCENT)

def at_func_PLATFORM(s):
  SMOVE(s,PLUGH,FAKE_Y2,FOOF)
  SMOVE(s,PLOVER,FAKE_Y2,FOOF)
at_PLATFORM = mkAT('PLATFORM', at_func_PLATFORM)

def at_func_PLATFORM_1(s):
  ANYOF(s,[DOWN,CLIMB,NORTH,SOUTH,EAST,WEST,NORTHEAST ,NORTHWEST,SOUTHEAST,SOUTHWEST,JUMP ])
  opSAY(s,SIZZLE)
  opGOTO(s,YLEM)
  CALL(s,CORONER)
at_PLATFORM_1 = mkAT('PLATFORM', at_func_PLATFORM_1)

def at_func_CYLINDRICAL(s):
  ANYOF(s,[ZORTON,XYZZY,THURB,SNOEZE,SAMOHT,PLUGH,NOSIDE,MELENKURION ,KNERL,KLAETU,FOO,FOE,FIE,FEE,BLERBI,PHUGGG ])
  if  ((((((((((((((( KEYP(s,SAY) ))))))))))))))) :
    opSET(s,I,ARG2)
  else:
    if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
      opSET(s,I,ARG1)
    else:
      opSET(s,I,0)
  LDA(s,J,ZORTON)
  SUB(s,I,J)
  if  ((((((((((((((( EQP(s,I,ESCAPE) ))))))))))))))) :
    if  ((((((((((((((( KEYP(s,BLERBI) ))))))))))))))) :
      opSET(s,CLOSURE,4)
      opSAY(s,FOOF)
      opGOTO(s,ROAD)
    else:
      opSAY(s,OK_)
      ADD(s,ESCAPE,1)
  else:
    opSET(s,ESCAPE,0)
    opSAY(s,NOTHING)
  opQUIT(s)
at_CYLINDRICAL = mkAT('CYLINDRICAL', at_func_CYLINDRICAL)

def action_GET(s):
  if  ((((((((((((((( EQP(s,LAMP,0)  or   not  NEARP(s,LAMP) )  and   not  BITP(s,HERE,LIT) ) ))))))))))))) :
    CALL(s,GROPE_FOR_IT)
  DEFAULT(s,PORTABLE)
  ANYOF(s,[BIRD,CAGE,BOTTLE,OIL,WATER,CHAIN,BEAR,INVENTORY,CLAM ,SWORD,SCEPTRE,KNIFE ])
  if  ((((((((((((((( KEYP(s,BIRD) ))))))))))))))) :
    CALL(s,GETBIRD)
  else:
    if  ((((((((((((((( KEYP(s,CAGE) ))))))))))))))) :
      CALL(s,GETCAGE)
    else:
      if  ((((((((((((((( KEYP(s,BOTTLE) ))))))))))))))) :
        CALL(s,GETBOTTLE)
      else:
        if  ((((((((((((((( KEYP(s,OIL) ))))))))))))))) :
          CALL(s,GETOIL)
        else:
          if  ((((((((((((((( KEYP(s,WATER) ))))))))))))))) :
            CALL(s,GETWATER)
          else:
            if  ((((((((((((((( KEYP(s,CHAIN) ))))))))))))))) :
              CALL(s,GETCHAIN)
            else:
              if  ((((((((((((((( KEYP(s,BEAR) ))))))))))))))) :
                CALL(s,GETBEAR)
              else:
                if  ((((((((((((((( KEYP(s,INVENTORY) ))))))))))))))) :
                  CALL(s,INVENTORY)
                else:
                  if  ((((((((((((((( KEYP(s,SWORD) ))))))))))))))) :
                    CALL(s,GETSWORD)
                  else:
                    if  ((((((((((((((( KEYP(s,SCEPTRE) ))))))))))))))) :
                      CALL(s,GETSCEPTRE)
                    else:
                      if  ((((((((((((((( KEYP(s,KNIFE) ))))))))))))))) :
                        CALL(s,GETKNIFE)
GET = mkACTION('GET', action_GET)

def action_GET_2(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opPROCEED(s)
  if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
    pass
  else:
    opSAY(s,HAH_)
    opQUIT(s)
  if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
    opSAY(s,YOUHAVEIT)
    opQUIT(s)
  if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
    pass
  else:
    NAME(s,IDONTSEE,ARG2)
    opQUIT(s)
  if  ((((((((((((((( BITP(s,ARG2,PORTABLE) ))))))))))))))) :
    pass
  else:
    opSAY(s,HAH_)
    opQUIT(s)
  if  ((((((((((((((( LTP(s,INVCT,STRENGTH) ))))))))))))))) :
    opGET(s,ARG2)
    opSAY(s,OK)
    if  ((((((((((((((( BITP(s,ARG2,UNSTABLE) ))))))))))))))) :
      EVAL(s,J,ARG2)
      if  ((((((((((((((( EQP(s,J,0) ))))))))))))))) :
        DEPOSIT(s,ARG2,1)
  else:
    opSAY(s,ARMSAREFULL)
  opQUIT(s)
GET_2 = mkACTION('GET', action_GET_2)

def action_DROP(s):
  ANYOF(s,[BIRD,CAGE,BOTTLE,OIL,WATER,VASE,VIAL,DJINN,BEAR ])
  if  ((((((((((((((( KEYP(s,BIRD) ))))))))))))))) :
    CALL(s,DROPBIRD)
  else:
    if  ((((((((((((((( KEYP(s,CAGE) ))))))))))))))) :
      CALL(s,DROPCAGE)
    else:
      if  ((((((((((((((( KEYP(s,BOTTLE) ))))))))))))))) :
        CALL(s,DROPBOTTLE)
      else:
        if  ((((((((((((((( KEYP(s,OIL)  or  KEYP(s,WATER) ) )))))))))))))) :
          CALL(s,DROPLIQUID)
        else:
          if  ((((((((((((((( KEYP(s,VASE) ))))))))))))))) :
            CALL(s,DROPVASE)
          else:
            if  ((((((((((((((( KEYP(s,VIAL) ))))))))))))))) :
              CALL(s,DROPVIAL)
            else:
              if  ((((((((((((((( KEYP(s,DJINN) ))))))))))))))) :
                CALL(s,FREEDJINN)
              else:
                if  ((((((((((((((( KEYP(s,BEAR) ))))))))))))))) :
                  CALL(s,DROPBEAR)
  opPROCEED(s)
DROP = mkACTION('DROP', action_DROP)

def action_DROP_2(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opPROCEED(s)
  if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
    pass
  else:
    opSAY(s,HAH_)
    opQUIT(s)
  if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
    opDROP(s,ARG2)
    opSAY(s,OK)
  else:
    opSAY(s,NOTCARRYING)
  opQUIT(s)
DROP_2 = mkACTION('DROP', action_DROP_2)

def action_WALK(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    NAME(s,WHICHWAY,ARG1)
  else:
    if  ((((((((((((((( KEYP(s,NORTH)  or  KEYP(s,SOUTH) )  or  KEYP(s,EAST) )  or  KEYP(s,WEST) )  or  KEYP(s,NORTHEAST) )  or  KEYP(s,NORTHWEST) )  or  KEYP(s,SOUTHEAST) )  or  KEYP(s,SOUTHWEST) )  or  KEYP(s,UP) )  or  KEYP(s,DOWN) )  or  KEYP(s,BACK) )  or  KEYP(s,CAVE) )  or  KEYP(s,OUT) )  or  KEYP(s,IN) ) )) :
      CALL(s,ARG2)
    else:
      if  ((((((((((((((( BITP(s,ARG2,PLACE) ))))))))))))))) :
        if  ((((((((((((((( ATP(s,ARG2) ))))))))))))))) :
          opSAY(s,NEEDDETAIL)
        else:
          opSAY(s,NO_CAN_GO)
      else:
        opSAY(s,HUH__)
  opQUIT(s)
WALK = mkACTION('WALK', action_WALK)

def action_DIG(s):
  opSAY(s,NEEDSHOVEL)
  opQUIT(s)
DIG = mkACTION('DIG', action_DIG)

def action_CAVE(s):
  AT(s,VALLEY,FOREST,FOREST2,STREAM,ROAD,SLIT,DEPRESSION,BUILDING)
  opSAY(s,WHEREISCAVE)
  opQUIT(s)
CAVE = mkACTION('CAVE', action_CAVE)

def action_CAVE_2(s):
  opSAY(s,NEEDDETAIL)
  opQUIT(s)
CAVE_2 = mkACTION('CAVE', action_CAVE_2)

def action_WATER(s):
  KEYWORD(s,DOOR)
  if  ((((((((((((((( NEARP(s,DOOR) ))))))))))))))) :
    if  ((((((((((((((( HAVEP(s,WATER) ))))))))))))))) :
      APPORT(s,WATER,LIMBO)
      opSET(s,BOTTLE,1)
      opSAY(s,HINGES__RUST)
      opSET(s,DOOR,0)
    else:
      NAME(s,YOUDONTHAVE,ARG1)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
WATER = mkACTION('WATER', action_WATER)

def action_OIL(s):
  KEYWORD(s,DOOR)
  if  ((((((((((((((( NEARP(s,DOOR) ))))))))))))))) :
    if  ((((((((((((((( HAVEP(s,OIL) ))))))))))))))) :
      APPORT(s,OIL,LIMBO)
      opSET(s,BOTTLE,1)
      opSET(s,DOOR,1)
      opSAY(s,OIL__DOOR)
    else:
      NAME(s,YOUDONTHAVE,ARG1)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
OIL = mkACTION('OIL', action_OIL)

def action_WATER_2(s):
  KEYWORD(s,PLANT)
  if  ((((((((((((((( NEARP(s,PLANT) ))))))))))))))) :
    if  ((((((((((((((( HAVEP(s,WATER) ))))))))))))))) :
      APPORT(s,WATER,LIMBO)
      opSET(s,BOTTLE,1)
      ADD(s,PLANT,1)
      opSAY(s,PLANT)
      ADD(s,PLANT,1)
      if  ((((((((((((((( EQP(s,PLANT,6) ))))))))))))))) :
        opSET(s,PLANT,0)
        BIS(s,PLANT2,INVISIBLE)
      else:
        BIC(s,PLANT2,INVISIBLE)
      opGOTO(s,HERE)
      opSET(s,PLANT2,PLANT)
    else:
      NAME(s,YOUDONTHAVE,ARG1)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
WATER_2 = mkACTION('WATER', action_WATER_2)

def action_OIL_2(s):
  KEYWORD(s,PLANT)
  if  ((((((((((((((( NEARP(s,PLANT) ))))))))))))))) :
    if  ((((((((((((((( HAVEP(s,OIL) ))))))))))))))) :
      APPORT(s,OIL,LIMBO)
      opSET(s,BOTTLE,1)
      opSAY(s,OIL__PLANT)
    else:
      NAME(s,YOUDONTHAVE,ARG1)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
OIL_2 = mkACTION('OIL', action_OIL_2)

def action_OIL_3(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,BOTTLE)  and  EQP(s,BOTTLE,2) )  or  HAVEP(s,OIL) )  or  ATP(s,EASTPIT) ) )))))))))))) :
      NAME(s,WHAT_DO,ARG1)
    else:
      NAME(s,IDONTSEE,ARG1)
  else:
    opSAY(s,HAH_)
  opQUIT(s)
OIL_3 = mkACTION('OIL', action_OIL_3)

def action_WATER_3(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,BOTTLE)  and  EQP(s,BOTTLE,0) )  or  HAVEP(s,WATER) )  or  BITP(s,HERE,H20HERE) ) )))))))))))) :
      NAME(s,WHAT_DO,ARG1)
    else:
      NAME(s,IDONTSEE,ARG1)
  else:
    opSAY(s,HAH_)
  opQUIT(s)
WATER_3 = mkACTION('WATER', action_WATER_3)

def action_THROW(s):
  ANYOF(s,[AXE,SWORD ])
  CALL(s,WEAPONRY)
THROW = mkACTION('THROW', action_THROW)

def action_THROW_2(s):
  KEYWORD(s,FOOD)
  HAVE(s,FOOD)
  if  ((((((((((((((( NEARP(s,TROLL) ))))))))))))))) :
    opSAY(s,FEED__TROLL)
  else:
    if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
      opSAY(s,FED__DWARF)
      opDROP(s,FOOD)
      BIS(s,DWARF,SPECIAL2)
    else:
      if  ((((((((((((((( NEARP(s,BEAR) ))))))))))))))) :
        opSAY(s,BEAR__URRP)
        APPORT(s,FOOD,LIMBO)
        opSET(s,BEAR,1)
        if  ((((((((((((((( EQP(s,AXE,1) ))))))))))))))) :
          opSET(s,AXE,0)
      else:
        opPROCEED(s)
  opQUIT(s)
THROW_2 = mkACTION('THROW', action_THROW_2)

def action_THROW_3(s):
  KEYWORD(s,TEETH)
  HAVE(s,TEETH)
  opSET(s,TEETH,0)
  NEAR(s,GOBLINS)
  opSAY(s,WARRIORS)
  APPORT(s,TEETH,LIMBO)
  APPORT(s,GOBLINS,LIMBO)
  opQUIT(s)
THROW_3 = mkACTION('THROW', action_THROW_3)

def action_THROW_4(s):
  KEYWORD(s,VIAL)
  HAVE(s,VIAL)
  CALL(s,BREAK_VIAL)
THROW_4 = mkACTION('THROW', action_THROW_4)

def action_WAVE(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      pass
    else:
      opSAY(s,HAH_)
      opQUIT(s)
    if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
      pass
    else:
      opSAY(s,NOTCARRYING)
      opQUIT(s)
  if  ((((((((((((((( KEYP(s,ROD) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,FISSURE) ))))))))))))))) :
      if  ((((((((((((((( LTP(s,CLOSURE,2) ))))))))))))))) :
        ADD(s,FISSURE,1)
        opSAY(s,FISSURE)
        if  ((((((((((((((( EQP(s,FISSURE,2) ))))))))))))))) :
          opSET(s,FISSURE,0)
          BIS(s,FISSURE,INVISIBLE)
        else:
          BIC(s,FISSURE,INVISIBLE)
      else:
        opSAY(s,NOTHING)
    else:
      if  ((((((((((((((( NEARP(s,QUICKSAND) ))))))))))))))) :
        opSAY(s,NOTHING_OBVIOUS)
        opSET(s,QUICKSAND,1)
      else:
        if  ((((((((((((((( NEARP(s,GORGE)  and  LTP(s,CLOSURE,2) ) )))))))))))))) :
          ADD(s,GORGE,1)
          opSAY(s,GORGE)
          ADD(s,GORGE,1)
          if  ((((((((((((((( EQP(s,GORGE,4) ))))))))))))))) :
            opSET(s,GORGE,0)
            BIS(s,GORGE,INVISIBLE)
          else:
            BIC(s,GORGE,INVISIBLE)
        else:
          opSAY(s,NOTHING)
  else:
    if  ((((((((((((((( KEYP(s,AXE)  or  KEYP(s,SWORD) ) )))))))))))))) :
      CALL(s,WEAPONRY)
    else:
      opSAY(s,NOTHING)
  opQUIT(s)
WAVE = mkACTION('WAVE', action_WAVE)

def action_THROW_5(s):
  if  ((((((((((((((( EQP(s,STATUS,2) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( HAVEP(s,ARG2)  and  BITP(s,HERE,THROWER) ) )))))))))))))) :
        CALL(s,UPCHUCK)
  CALL(s,DROP)
THROW_5 = mkACTION('THROW', action_THROW_5)

def action_NORTH(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
NORTH = mkACTION('NORTH', action_NORTH)

def action_SOUTH(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
SOUTH = mkACTION('SOUTH', action_SOUTH)

def action_UP(s):
  opSAY(s,NOCANGO)
  opQUIT(s)
UP = mkACTION('UP', action_UP)

def action_DOWN(s):
  opSAY(s,NOCANGO)
  opQUIT(s)
DOWN = mkACTION('DOWN', action_DOWN)

def action_EAST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
EAST = mkACTION('EAST', action_EAST)

def action_WEST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
WEST = mkACTION('WEST', action_WEST)

def action_NORTHEAST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
NORTHEAST = mkACTION('NORTHEAST', action_NORTHEAST)

def action_NORTHWEST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
NORTHWEST = mkACTION('NORTHWEST', action_NORTHWEST)

def action_SOUTHEAST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
SOUTHEAST = mkACTION('SOUTHEAST', action_SOUTHEAST)

def action_SOUTHWEST(s):
  CALL(s,NO_MOVE_POSSIBLE)
  opQUIT(s)
SOUTHWEST = mkACTION('SOUTHWEST', action_SOUTHWEST)

def action_INVENTORY(s):
  opSET(s,J,0)
  for o in all_objects:
    LDA(s, I, o)
    if  ((((((((((((((( HAVEP(s,I) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,J,0) ))))))))))))))) :
        opSAY(s,YOUNOWHAVE)
        opSET(s,J,1)
      opSAY(s,I)
  if  ((((((((((((((( EQP(s,J,0) ))))))))))))))) :
    opSAY(s,ARMSAREEMPTY)
  opQUIT(s)
INVENTORY = mkACTION('INVENTORY', action_INVENTORY)

def action_LOOK(s):
  ANYOF(s,[MIST,TREES ])
  CALL(s,ARG2)
LOOK = mkACTION('LOOK', action_LOOK)

def action_LOOK_2(s):
  if  ((((((((((((((( NEARP(s,LAMP)  and  EQP(s,LAMP,1) )  or  BITP(s,HERE,LIT) ) ))))))))))))) :
    opSET(s,J,0)
    if  ((((((((((((((( BITP(s,STATUS,FASTMODE) ))))))))))))))) :
      pass
    else:
      BIS(s,STATUS,FULLDISP)
      opSET(s,J,1)
    opSAY(s,HERE)
    BIC(s,STATUS,FULLDISP)
    BIS(s,HERE,BEENHERE)
    for o in all_objects:
      if not NEARP(s, o): continue
      LDA(s, I, o)
      if  ((((((((((((((( NEARP(s,I)  and   not  HAVEP(s,I) ) )))))))))))))) :
        if  ((((((((((((((( EQP(s,J,1)  and   not  BITP(s,I,INVISIBLE) ) )))))))))))))) :
          opSET(s,J,0)
          opSAY(s,BLANK)
        BIS(s,I,SEEN)
        opSAY(s,I)
    if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,DWARROWS,1) ))))))))))))))) :
        opSAY(s,DWARFHERE)
      else:
        VALUE(s,DWARVESHERE,DWARROWS)
    if  ((((((((((((((( HAVEP(s,BEAR) ))))))))))))))) :
      opSAY(s,I_C_A_BEAR)
  else:
    opSAY(s,NOLIGHTHERE)
  opQUIT(s)
LOOK_2 = mkACTION('LOOK', action_LOOK_2)

def action_LIGHT(s):
  if  ((((((((((((((( KEYP(s,LAMP) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,LAMP) ))))))))))))))) :
      if  ((((((((((((((( LTP(s,LAMPLIFE,40) ))))))))))))))) :
        if  ((((((((((((((( NEARP(s,BATTERIES)  and  EQP(s,BATTERIES,0) ) )))))))))))))) :
          opSAY(s,NEW_BATTERIES)
          opSET(s,BATTERIES,1)
          ADD(s,LAMPLIFE,300)
          BIC(s,LAMP,SPECIAL1)
          BIC(s,LAMP,SPECIAL1)
      if  ((((((((((((((( GTP(s,LAMPLIFE,0) ))))))))))))))) :
        opSAY(s,LAMPNOWON)
        if  ((((((((((((((( LTP(s,LAMP,1) ))))))))))))))) :
          if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
            pass
          else:
            opSET(s,LAMP,1)
            CALL(s,LOOK)
        opSET(s,LAMP,1)
        CALL(s,PHOG)
      else:
        opSAY(s,LAMP_IS_DEAD)
    else:
      NAME(s,IDONTSEE,ARG2)
  else:
    if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
      opSAY(s,DUNNO_HOW)
    else:
      if  ((((((((((((((( NEARP(s,LAMP) ))))))))))))))) :
        if  ((((((((((((((( LTP(s,LAMPLIFE,40) ))))))))))))))) :
          if  ((((((((((((((( NEARP(s,BATTERIES) ))))))))))))))) :
            if  ((((((((((((((( EQP(s,BATTERIES,0) ))))))))))))))) :
              opSAY(s,NEW_BATTERIES)
              opSET(s,BATTERIES,1)
              ADD(s,LAMPLIFE,300)
              BIC(s,LAMP,SPECIAL1)
        if  ((((((((((((((( GTP(s,LAMPLIFE,0) ))))))))))))))) :
          opSAY(s,LAMPNOWON)
          opSET(s,I,LAMP)
          opSET(s,LAMP,1)
          CALL(s,PHOG)
          if  ((((((((((((((( LTP(s,I,1)  and   not  BITP(s,HERE,LIT) ) )))))))))))))) :
            CALL(s,LOOK)
        else:
          opSAY(s,LAMP_IS_DEAD)
      else:
        opSAY(s,NOLIGHTHERE)
  opQUIT(s)
LIGHT = mkACTION('LIGHT', action_LIGHT)

def action_EXTINGUISH(s):
  if  ((((((((((((((( KEYP(s,LAMP)  or  EQP(s,STATUS,1) ) )))))))))))))) :
    if  ((((((((((((((( NEARP(s,LAMP) ))))))))))))))) :
      opSET(s,LAMP,0)
      opSAY(s,LAMPNOWOFF)
      if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
        pass
      else:
        opSAY(s,ITISNOWDARK)
      CALL(s,PHOG)
    else:
      if  ((((((((((((((( KEYP(s,LAMP) ))))))))))))))) :
        NAME(s,IDONTSEE,ARG2)
      else:
        opPROCEED(s)
  else:
    opSAY(s,DUNNO_HOW)
  opQUIT(s)
EXTINGUISH = mkACTION('EXTINGUISH', action_EXTINGUISH)

def action_OPEN(s):
  DEFAULT(s,OPENABLE)
  KEYWORD(s,GRATE)
  NEAR(s,GRATE)
  if  ((((((((((((((( HAVEP(s,KEYS) ))))))))))))))) :
    if  ((((((((((((((( GTP(s,CLOSURE,1)  or  BITP(s,ADMIN,NOMAGIC) ) )))))))))))))) :
      opSAY(s,GRATE_STUCK)
      if  ((((((((((((((( GTP(s,CLOSURE,1) ))))))))))))))) :
        BIS(s,ADMIN,PANICED)
        if  ((((((((((((((( BITP(s,GRATE,SPECIAL1) ))))))))))))))) :
          pass
        else:
          BIS(s,GRATE,SPECIAL1)
          opSAY(s,GRATE_CLOSED)
    else:
      opSET(s,GRATE,1)
      opSAY(s,GRATEUNLOCKED)
      BIC(s,DEPRESSION,HINTABLE)
  else:
    opSAY(s,NEEDKEYS)
  opQUIT(s)
OPEN = mkACTION('OPEN', action_OPEN)

def action_OPEN_2(s):
  KEYWORD(s,CHAIN)
  NEAR(s,CHAIN)
  if  ((((((((((((((( HAVEP(s,KEYS) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,CHAIN,0) ))))))))))))))) :
      opSAY(s,CHAIN_UNLOCKED)
    else:
      if  ((((((((((((((( EQP(s,CHAIN,1) ))))))))))))))) :
        if  ((((((((((((((( EQP(s,BEAR,0) ))))))))))))))) :
          opSAY(s,BEAR__CHAIN)
        else:
          opSAY(s,CHAIN_UNLOCKED)
          opSET(s,CHAIN,0)
          opSET(s,BEAR,2)
      else:
        opSAY(s,CHAIN_UNLOCKED)
        opSET(s,CHAIN,0)
  else:
    opSAY(s,NEEDKEYS)
  opQUIT(s)
OPEN_2 = mkACTION('OPEN', action_OPEN_2)

def action_OPEN_3(s):
  KEYWORD(s,DOOR)
  NEAR(s,DOOR)
  opSAY(s,NOLOCK)
  opQUIT(s)
OPEN_3 = mkACTION('OPEN', action_OPEN_3)

def action_OPEN_4(s):
  KEYWORD(s,KEYS)
  opSAY(s,UNLOCKKEYS)
  opQUIT(s)
OPEN_4 = mkACTION('OPEN', action_OPEN_4)

def action_OPEN_5(s):
  KEYWORD(s,SAFE)
  NEAR(s,SAFE)
  if  ((((((((((((((( EQP(s,SAFE,0) ))))))))))))))) :
    opSAY(s,NO_KEYHOLE)
  else:
    if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
      NAME(s,ALREADY_OPEN,ARG2)
    else:
      opSAY(s,IT_IS_MELTED)
  opQUIT(s)
OPEN_5 = mkACTION('OPEN', action_OPEN_5)

def action_OPEN_6(s):
  KEYWORD(s,CLAM)
  NEAR(s,CLAM)
  if  ((((((((((((((( HAVEP(s,CLAM) ))))))))))))))) :
    opSAY(s,DROP_THE_CLAM)
  else:
    if  ((((((((((((((( HAVEP(s,TRIDENT) ))))))))))))))) :
      APPORT(s,CLAM,LIMBO)
      APPORT(s,OYSTER,HERE)
      APPORT(s,PEARL,CULDESAC)
      opSAY(s,CLAM__OPENED)
    else:
      opSAY(s,NEED_TRIDENT)
  opQUIT(s)
OPEN_6 = mkACTION('OPEN', action_OPEN_6)

def action_OPEN_7(s):
  KEYWORD(s,OYSTER)
  NEAR(s,OYSTER)
  if  ((((((((((((((( HAVEP(s,OYSTER) ))))))))))))))) :
    opSAY(s,DROP_THE_OYSTER)
  else:
    if  ((((((((((((((( HAVEP(s,TRIDENT) ))))))))))))))) :
      opSAY(s,OYSTER__OPENED)
    else:
      opSAY(s,NEED_TRIDNT2)
  opQUIT(s)
OPEN_7 = mkACTION('OPEN', action_OPEN_7)

def action_OPEN_8(s):
  KEYWORD(s,VIAL)
  NEAR(s,VIAL)
  CALL(s,BREAK_VIAL)
OPEN_8 = mkACTION('OPEN', action_OPEN_8)

def action_OPEN_9(s):
  KEYWORD(s,FLASK)
  NEAR(s,FLASK)
  if  ((((((((((((((( LTP(s,FLASK,2) ))))))))))))))) :
    if  ((((((((((((((( LOCP(s,FLASK,PENTAGRAM) ))))))))))))))) :
      APPORT(s,DJINN,PENTAGRAM)
      opSAY(s,POLITE_DJINN)
    else:
      opSAY(s,RUDE_DJINN)
    opSET(s,FLASK,2)
  else:
    NAME(s,ALREADY_OPEN,ARG2)
  opQUIT(s)
OPEN_9 = mkACTION('OPEN', action_OPEN_9)

def action_OPEN_10(s):
  KEYWORD(s,PENTAGRAM)
  if  ((((((((((((((( ATP(s,PENTAGRAM) ))))))))))))))) :
    if  ((((((((((((((( NEARP(s,DJINN) ))))))))))))))) :
      opSAY(s,DJINN_ADVICE)
      APPORT(s,DJINN,LIMBO)
      BIS(s,DJINN,SPECIAL1)
    else:
      opSAY(s,EMPTY_PENTA)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
OPEN_10 = mkACTION('OPEN', action_OPEN_10)

def action_CLOSE(s):
  DEFAULT(s,OPENABLE)
  KEYWORD(s,GRATE)
  NEAR(s,GRATE)
  opSET(s,GRATE,0)
  opSAY(s,GRATELOCKED)
  opQUIT(s)
CLOSE = mkACTION('CLOSE', action_CLOSE)

def action_CLOSE_2(s):
  KEYWORD(s,CHAIN)
  NEAR(s,CHAIN)
  if  ((((((((((((((( ATP(s,BEARHERE) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,CHAIN,0) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,BEAR) ))))))))))))))) :
        opDROP(s,BEAR)
        opSET(s,BEAR,1)
        opSET(s,CHAIN,1)
      else:
        opSET(s,CHAIN,2)
    opSAY(s,LOCK__CHAIN)
    if  ((((((((((((((( HAVEP(s,CHAIN) ))))))))))))))) :
      opDROP(s,CHAIN)
  else:
    opSAY(s,LOCK__CHAIN_)
  opQUIT(s)
CLOSE_2 = mkACTION('CLOSE', action_CLOSE_2)

def action_CLOSE_3(s):
  KEYWORD(s,DOOR)
  NEAR(s,DOOR)
  opSAY(s,NOLOCK)
  opQUIT(s)
CLOSE_3 = mkACTION('CLOSE', action_CLOSE_3)

def action_CLOSE_4(s):
  KEYWORD(s,SAFE)
  NEAR(s,SAFE)
  if  ((((((((((((((( EQP(s,SAFE,1) ))))))))))))))) :
    opSAY(s,SAFE_SHUTS)
    opSET(s,SAFE,0)
  else:
    NAME(s,ALREADY_SHUT,ARG2)
  opQUIT(s)
CLOSE_4 = mkACTION('CLOSE', action_CLOSE_4)

def action_CLOSE_5(s):
  KEYWORD(s,FLASK)
  NEAR(s,FLASK)
  if  ((((((((((((((( EQP(s,FLASK,0) ))))))))))))))) :
    NAME(s,ALREADY_SHUT,ARG2)
  else:
    NAME(s,DUNNO_HAO,ARG2)
  opQUIT(s)
CLOSE_5 = mkACTION('CLOSE', action_CLOSE_5)

def action_HELP(s):
  if  ((((((((((((((( BITP(s,HERE,HINTABLE) ))))))))))))))) :
    CALL(s,HINT_LOGIC)
  else:
    opSAY(s,HELPDATA)
  opQUIT(s)
HELP = mkACTION('HELP', action_HELP)

def action_INFO(s):
  opSAY(s,INFO_2)
  opQUIT(s)
INFO = mkACTION('INFO', action_INFO)

def action_BRIEF(s):
  opSAY(s,BRIEF_OK)
  BIS(s,STATUS,QUICKIE)
  BIC(s,STATUS,FASTMODE)
  LDA(s,OK,OK_)
  opQUIT(s)
BRIEF = mkACTION('BRIEF', action_BRIEF)

def action_LPSD(s):
  if  ((((((((((((((( EQP(s,STATUS,1)  or   not  BITP(s,ADMIN,OLORIN) ) )))))))))))))) :
    opSAY(s,WHAT_)
    opQUIT(s)
  if  ((((((((((((((( BITP(s,ARG2,PLACE) ))))))))))))))) :
    opGOTO(s,ARG2)
  else:
    opSAY(s,WHAT_)
  opQUIT(s)
LPSD = mkACTION('LPSD', action_LPSD)

def action_KILL(s):
  DEFAULT(s,MORTAL)
  ANYOF(s,[TROLL,DWARF,DRAGON,SNAKE,BIRD,BEAR,OYSTER,CLAM,OGRE,BLOB ,DJINN,GOBLINS,BASILISK,GONG ])
  NEAR(s,ARG2)
  if  ((((((((((((((( KEYP(s,TROLL) ))))))))))))))) :
    CALL(s,KILLTROLL)
  else:
    if  ((((((((((((((( KEYP(s,DWARF) ))))))))))))))) :
      CALL(s,KILLDWARF)
    else:
      if  ((((((((((((((( KEYP(s,DRAGON) ))))))))))))))) :
        CALL(s,KILLDRAGON)
      else:
        if  ((((((((((((((( KEYP(s,SNAKE) ))))))))))))))) :
          CALL(s,KILLSNAKE)
        else:
          if  ((((((((((((((( KEYP(s,BLOB) ))))))))))))))) :
            CALL(s,KILLBLOB)
          else:
            if  ((((((((((((((( KEYP(s,BEAR) ))))))))))))))) :
              CALL(s,KILLBEAR)
            else:
              if  ((((((((((((((( KEYP(s,CLAM)  or  KEYP(s,OYSTER) ) )))))))))))))) :
                CALL(s,KILLBIVALVE)
              else:
                if  ((((((((((((((( KEYP(s,OGRE) ))))))))))))))) :
                  CALL(s,KILLOGRE)
                else:
                  if  ((((((((((((((( KEYP(s,BIRD) ))))))))))))))) :
                    CALL(s,KILLBIRD)
                  else:
                    if  ((((((((((((((( KEYP(s,DJINN) ))))))))))))))) :
                      CALL(s,KILLDJINN)
                    else:
                      if  ((((((((((((((( KEYP(s,GOBLINS) ))))))))))))))) :
                        CALL(s,KILLGOBLINS)
                      else:
                        if  ((((((((((((((( KEYP(s,BASILISK) ))))))))))))))) :
                          CALL(s,KILLBASILISK)
                        else:
                          if  ((((((((((((((( KEYP(s,GONG) ))))))))))))))) :
                            CALL(s,HITGONG)
  opQUIT(s)
KILL = mkACTION('KILL', action_KILL)

def action_KILL_2(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opSAY(s,PACIFIST)
    opQUIT(s)
KILL_2 = mkACTION('KILL', action_KILL_2)

def action_FAST(s):
  BIC(s,STATUS,QUICKIE)
  BIS(s,STATUS,FASTMODE)
  opSAY(s,OK)
  LDA(s,OK,SOK_)
  opQUIT(s)
FAST = mkACTION('FAST', action_FAST)

def action_FULL(s):
  BIC(s,STATUS,QUICKIE)
  BIC(s,STATUS,FASTMODE)
  LDA(s,OK,OK_)
  opSAY(s,OK)
  opQUIT(s)
FULL = mkACTION('FULL', action_FULL)

def action_FEED(s):
  ANYOF(s,[BEAR,TROLL,BIRD,SNAKE,DWARF,DRAGON,BASILISK,GOBLINS ])
  if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
    if  ((((((((((((((( KEYP(s,BEAR) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,FOOD) ))))))))))))))) :
        opSAY(s,BEAR__URRP)
        opSET(s,BEAR,1)
        if  ((((((((((((((( HAVEP(s,FOOD) ))))))))))))))) :
          APPORT(s,FOOD,LIMBO)
        if  ((((((((((((((( EQP(s,AXE,1) ))))))))))))))) :
          opSET(s,AXE,0)
      else:
        opSAY(s,SNAKEWONTEAT)
    else:
      if  ((((((((((((((( KEYP(s,TROLL) ))))))))))))))) :
        opSAY(s,FEED__TROLL)
      else:
        if  ((((((((((((((( KEYP(s,SNAKE) ))))))))))))))) :
          if  ((((((((((((((( HAVEP(s,BIRD) ))))))))))))))) :
            opSAY(s,SNAKE__BIRD)
            APPORT(s,BIRD,LIMBO)
          else:
            opSAY(s,SNAKEWONTEAT)
        else:
          if  ((((((((((((((( KEYP(s,DWARF) ))))))))))))))) :
            opSAY(s,FED__DWARF)
            BIS(s,DWARF,SPECIAL2)
          else:
            if  ((((((((((((((( KEYP(s,BIRD) ))))))))))))))) :
              opSAY(s,BIRDSEED)
            else:
              if  ((((((((((((((( KEYP(s,DRAGON) ))))))))))))))) :
                if  ((((((((((((((( EQP(s,DRAGON,0) ))))))))))))))) :
                  opSAY(s,SNAKEWONTEAT)
                else:
                  opSAY(s,IT_IS_DEAD)
              else:
                if  ((((((((((((((( KEYP(s,BASILISK) ))))))))))))))) :
                  if  ((((((((((((((( LTP(s,BASILISK,2) ))))))))))))))) :
                    opSAY(s,SNAKEWONTEAT)
                  else:
                    opSAY(s,IT_IS_DEAD)
                else:
                  if  ((((((((((((((( KEYP(s,GOBLINS) ))))))))))))))) :
                    opSAY(s,GOBL_EAT_YOU)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
FEED = mkACTION('FEED', action_FEED)

def action_FEED_2(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opSAY(s,HUH__)
  else:
    opSAY(s,HAH_)
  opQUIT(s)
FEED_2 = mkACTION('FEED', action_FEED_2)

def action_SCORE(s):
  opSET(s,QUITTING,1)
  CALL(s,GETSCORE)
  VALUE(s,IFYOUQUIT,SCOREX)
  VALUE(s,IFYOUQUIT2,MAXSCORE)
  opQUIT(s)
SCORE = mkACTION('SCORE', action_SCORE)

def action_JUMP(s):
  opSAY(s,NOJUMPING)
  opQUIT(s)
JUMP = mkACTION('JUMP', action_JUMP)

def action_IN(s):
  opSAY(s,INFROMOUT)
  opQUIT(s)
IN = mkACTION('IN', action_IN)

def action_OUT(s):
  opSAY(s,INFROMOUT)
  opQUIT(s)
OUT = mkACTION('OUT', action_OUT)

def action_ABRA(s):
  opSAY(s,MAGICKWORD)
  opQUIT(s)
ABRA = mkACTION('ABRA', action_ABRA)

def action_FEE(s):
  ANYOF(s,[FIE,FOE,FOO,FUM ])
  opSET(s,FOOBAR,0)
  opSAY(s,NOTHING)
  opQUIT(s)
FEE = mkACTION('FEE', action_FEE)

def action_FEE_2(s):
  opSET(s,FOOBAR,1)
  opSAY(s,OK)
  opQUIT(s)
FEE_2 = mkACTION('FEE', action_FEE_2)

def action_FIE(s):
  if  ((((((((((((((( EQP(s,FOOBAR,0) ))))))))))))))) :
    opSET(s,FOOBAR,2)
    opSAY(s,OK)
  else:
    opSET(s,FOOBAR,0)
    opSAY(s,NOTHING)
  opQUIT(s)
FIE = mkACTION('FIE', action_FIE)

def action_FOE(s):
  if  ((((((((((((((( EQP(s,FOOBAR,1) ))))))))))))))) :
    opSET(s,FOOBAR,3)
    opSAY(s,OK)
  else:
    opSET(s,FOOBAR,0)
    opSAY(s,NOTHING)
  opQUIT(s)
FOE = mkACTION('FOE', action_FOE)

def action_FOO(s):
  if  ((((((((((((((( EQP(s,FOOBAR,2) ))))))))))))))) :
    if  ((((((((((((((( LOCP(s,EGGS,GIANT)  or  LOCP(s,EGGS,YLEM) ) )))))))))))))) :
      opSAY(s,NOTHING)
    else:
      if  ((((((((((((((( NEARP(s,EGGS) ))))))))))))))) :
        opSET(s,EGGS,1)
      else:
        if  ((((((((((((((( ATP(s,GIANT) ))))))))))))))) :
          opSET(s,EGGS,0)
        else:
          opSET(s,EGGS,2)
      if  ((((((((((((((( HAVEP(s,EGGS) ))))))))))))))) :
        opDROP(s,EGGS)
      opSAY(s,EGGS)
      opSET(s,EGGS,0)
      if  ((((((((((((((( LOCP(s,EGGS,LIMBO) ))))))))))))))) :
        BIS(s,TROLL,SPECIAL1)
        if  ((((((((((((((( EQP(s,TROLL,1)  or  EQP(s,TROLL,2) ) )))))))))))))) :
          if  ((((((((((((((( NEARP(s,TROLL2) ))))))))))))))) :
            opSET(s,TROLL,5)
            opSAY(s,TROLL)
          opSET(s,TROLL,0)
          APPORT(s,TROLL,SWOFCHASM)
          APPORT(s,TROLL2,LIMBO)
      APPORT(s,EGGS,GIANT)
  else:
    opSAY(s,NOTHING)
  opSET(s,FOOBAR,0)
  opQUIT(s)
FOO = mkACTION('FOO', action_FOO)

def action_FUM(s):
  opSET(s,FOOBAR,0)
  opSAY(s,NOTHING)
  opQUIT(s)
FUM = mkACTION('FUM', action_FUM)

def action_XYZZY(s):
  opSAY(s,NOTHING)
  opQUIT(s)
XYZZY = mkACTION('XYZZY', action_XYZZY)

def action_PLUGH(s):
  opSAY(s,NOTHING)
  opQUIT(s)
PLUGH = mkACTION('PLUGH', action_PLUGH)

def action_FIND(s):
  KEYWORD(s,CAVE)
  if  ((((((((((((((( BITP(s,HERE,NOTINCAVE)  and   not  BITP(s,INCAVE,BEENHERE) ) )))))))))))))) :
    opSAY(s,WHEREISCAVE)
  else:
    opSAY(s,NEEDDETAIL)
  opQUIT(s)
FIND = mkACTION('FIND', action_FIND)

def action_FIND_2(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        if  ((((((((((((((( HAVEP(s,ARG2) ))))))))))))))) :
          opSAY(s,ITISHERENOW)
        else:
          opSAY(s,HERESOMEWHERE)
      else:
        opSAY(s,CANTFIND)
      opQUIT(s)
    else:
      if  ((((((((((((((( BITP(s,ARG2,PLACE) ))))))))))))))) :
        if  ((((((((((((((( ATP(s,ARG2) ))))))))))))))) :
          opSAY(s,YOU_ARE_THERE)
        else:
          opSAY(s,CANTFIND)
      else:
        opSAY(s,WHAT_)
      opQUIT(s)
FIND_2 = mkACTION('FIND', action_FIND_2)

def action_SWIM(s):
  opSAY(s,DUNNO_HOW)
  opQUIT(s)
SWIM = mkACTION('SWIM', action_SWIM)

def action_BREAK(s):
  KEYWORD(s,VASE)
  NEAR(s,VASE)
  opSAY(s,THROW_VASE)
  if  ((((((((((((((( HAVEP(s,VASE) ))))))))))))))) :
    APPORT(s,VASE,LIMBO)
    APPORT(s,SHARDS,HERE)
  opQUIT(s)
BREAK = mkACTION('BREAK', action_BREAK)

def action_BREAK_2(s):
  KEYWORD(s,VIAL)
  NEAR(s,VIAL)
  CALL(s,BREAK_VIAL)
BREAK_2 = mkACTION('BREAK', action_BREAK_2)

def action_FIX(s):
  KEYWORD(s,VASE)
  NEAR(s,POTTERY)
  opSAY(s,NO_CAN_FIX)
  opQUIT(s)
FIX = mkACTION('FIX', action_FIX)

def action_FILL(s):
  KEYWORD(s,VASE)
  NEAR(s,VASE)
  if  ((((((((((((((( BITP(s,HERE,H20HERE)  or  ATP(s,EASTPIT) ) )))))))))))))) :
    opSAY(s,SHATTER_VASE)
    if  ((((((((((((((( HAVEP(s,VASE) ))))))))))))))) :
      APPORT(s,VASE,LIMBO)
      APPORT(s,SHARDS,HERE)
  else:
    opSAY(s,NOTHING_VASE)
  opQUIT(s)
FILL = mkACTION('FILL', action_FILL)

def action_FILL_2(s):
  KEYWORD(s,BOTTLE)
  NEAR(s,BOTTLE)
  if  ((((((((((((((( EQP(s,BOTTLE,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,HERE,H20HERE) ))))))))))))))) :
      opSAY(s,BOTTLE__H20)
      opSET(s,BOTTLE,0)
      if  ((((((((((((((( HAVEP(s,BOTTLE) ))))))))))))))) :
        opGET(s,WATER)
    else:
      if  ((((((((((((((( ATP(s,EASTPIT) ))))))))))))))) :
        opSAY(s,BOTTLE__OIL)
        opSET(s,BOTTLE,2)
        if  ((((((((((((((( HAVEP(s,BOTTLE) ))))))))))))))) :
          opGET(s,OIL)
      else:
        opSAY(s,NOTHING2FILL)
  else:
    opSAY(s,BOTTLEWASFULL)
  opQUIT(s)
FILL_2 = mkACTION('FILL', action_FILL_2)

def action_FILL_3(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    opSAY(s,CANTFILLTHAT)
    opQUIT(s)
FILL_3 = mkACTION('FILL', action_FILL_3)

def action_POUR(s):
  KEYWORD(s,WATER)
  if  ((((((((((((((( HAVEP(s,WATER) ))))))))))))))) :
    APPORT(s,WATER,LIMBO)
    opSET(s,BOTTLE,1)
    if  ((((((((((((((( NEARP(s,PLANT) ))))))))))))))) :
      ADD(s,PLANT,1)
      opSAY(s,PLANT)
      ADD(s,PLANT,1)
      if  ((((((((((((((( EQP(s,PLANT,6) ))))))))))))))) :
        opSET(s,PLANT,0)
        BIS(s,PLANT2,INVISIBLE)
      else:
        BIC(s,PLANT2,INVISIBLE)
      opGOTO(s,HERE)
      opSET(s,PLANT2,PLANT)
    else:
      if  ((((((((((((((( NEARP(s,DOOR) ))))))))))))))) :
        opSAY(s,HINGES__RUST)
        opSET(s,DOOR,0)
      else:
        opSAY(s,POURWATER)
  else:
    NAME(s,YOUDONTHAVE,WATER)
  opQUIT(s)
POUR = mkACTION('POUR', action_POUR)

def action_POUR_2(s):
  KEYWORD(s,OIL)
  if  ((((((((((((((( HAVEP(s,OIL) ))))))))))))))) :
    APPORT(s,OIL,LIMBO)
    opSET(s,BOTTLE,1)
    if  ((((((((((((((( NEARP(s,PLANT) ))))))))))))))) :
      opSAY(s,OIL__PLANT)
    else:
      if  ((((((((((((((( NEARP(s,DOOR) ))))))))))))))) :
        opSAY(s,OIL__DOOR)
        opSET(s,DOOR,1)
      else:
        opSAY(s,POURWATER)
  else:
    NAME(s,YOUDONTHAVE,ARG2)
  opQUIT(s)
POUR_2 = mkACTION('POUR', action_POUR_2)

def action_PLACATE(s):
  ANYOF(s,[DWARF,SNAKE,BIRD,DRAGON,TROLL,BEAR,PIRATE,OGRE,BASILISK,GOBLINS ])
  NEAR(s,ARG2)
  opSAY(s,IAMGAME)
  opQUIT(s)
PLACATE = mkACTION('PLACATE', action_PLACATE)

def action_EAT(s):
  DEFAULT(s,EDIBLE)
  NEAR(s,MUSHROOM)
  if  ((((((((((((((( EQP(s,STATUS,1)  or  KEYP(s,MUSHROOM) ) )))))))))))))) :
    if  ((((((((((((((( HAVEP(s,MUSHROOM) ))))))))))))))) :
      opDROP(s,MUSHROOM)
    opSET(s,MUSHROOM,2)
    opSAY(s,MUSHROOM)
    opSET(s,MUSHTIME,30)
    ADD(s,MUSHTIME,LASTCLOCK)
    APPORT(s,MUSHROOM,LIMBO)
    opSET(s,STRENGTH,12)
    opQUIT(s)
EAT = mkACTION('EAT', action_EAT)

def action_EAT_2(s):
  NEAR(s,FOOD)
  if  ((((((((((((((( EQP(s,STATUS,1)  or  KEYP(s,FOOD) ) )))))))))))))) :
    if  ((((((((((((((( HAVEP(s,FOOD) ))))))))))))))) :
      APPORT(s,FOOD,LIMBO)
    opSAY(s,URRP)
    opQUIT(s)
EAT_2 = mkACTION('EAT', action_EAT_2)

def action_EAT_3(s):
  ANYOF(s,[DWARF,DRAGON,BIRD,SNAKE,BEAR,TROLL,PLANT,OGRE ,BASILISK,GOBLINS ])
  if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
    opSAY(s,BLEAH)
  else:
    NAME(s,IDONTSEE,ARG2)
  opQUIT(s)
EAT_3 = mkACTION('EAT', action_EAT_3)

def action_EAT_4(s):
  if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
    opSAY(s,NO_FOOD)
    opQUIT(s)
  else:
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        opSAY(s,REPULSIVE)
        opQUIT(s)
EAT_4 = mkACTION('EAT', action_EAT_4)

def action_RUB(s):
  KEYWORD(s,LAMP)
  NEAR(s,LAMP)
  NAME(s,RUBLAMP,ARG2)
  opQUIT(s)
RUB = mkACTION('RUB', action_RUB)

def action_RUB_2(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        opSAY(s,PECULIAR)
        opQUIT(s)
RUB_2 = mkACTION('RUB', action_RUB_2)

def action_BACK(s):
  if  ((((((((((((((( BITP(s,HERE,NOBACK)  or  BITP(s,THERE,NOBACK) )  or  EQP(s,THERE,0) ) ))))))))))))) :
    opSAY(s,CANTGOBACK)
  else:
    opGOTO(s,THERE)
  opQUIT(s)
BACK = mkACTION('BACK', action_BACK)

def action_MIST(s):
  opSAY(s,THISISMIST)
  opQUIT(s)
MIST = mkACTION('MIST', action_MIST)

def action_TREES(s):
  if  ((((((((((((((( BITP(s,HERE,NOTINCAVE) ))))))))))))))) :
    opSAY(s,INFOREST)
  else:
    opSAY(s,NO_TREES_HERE)
  opQUIT(s)
TREES = mkACTION('TREES', action_TREES)

def action_SAY(s):
  ANYOF(s,[PLUGH,XYZZY,PLOVER,THURB,MELENKURION,NOSIDE,SAMOHT ,KNERL,ZORTON,KLAETU,SNOEZE,BLERBI,PHUGGG ])
  CALL(s,ARG2)
  opQUIT(s)
SAY = mkACTION('SAY', action_SAY)

def action_SAY_2(s):
  if  ((((((((((((((( EQP(s,STATUS,2) ))))))))))))))) :
    opQUIT(s)
SAY_2 = mkACTION('SAY', action_SAY_2)

def action_DRINK(s):
  if  ((((((((((((((( EQP(s,STATUS,1)  or  KEYP(s,WATER) ) )))))))))))))) :
    if  ((((((((((((((( BITP(s,HERE,H20HERE) ))))))))))))))) :
      opSAY(s,SLURP)
      opQUIT(s)
    else:
      if  ((((((((((((((( NEARP(s,BOTTLE)  and  EQP(s,BOTTLE,0) ) )))))))))))))) :
        opSAY(s,WATERGONE)
        APPORT(s,WATER,LIMBO)
        opSET(s,BOTTLE,1)
        opQUIT(s)
    if  ((((((((((((((( KEYP(s,WATER) ))))))))))))))) :
      NAME(s,IDONTSEE,ARG2)
    else:
      opSAY(s,CANTDRINK)
  else:
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        opSAY(s,HAH_)
      else:
        NAME(s,IDONTSEE,ARG2)
    else:
      opSAY(s,HAH_)
  opQUIT(s)
DRINK = mkACTION('DRINK', action_DRINK)

def action_NEWS(s):
  opSAY(s,NEWSDATA)
  opQUIT(s)
NEWS = mkACTION('NEWS', action_NEWS)

def action_READ(s):
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG2) ))))))))))))))) :
        if  ((((((((((((((( KEYP(s,MAGAZINES) ))))))))))))))) :
          CALL(s,READ_MAGAZINES)
        else:
          if  ((((((((((((((( KEYP(s,MESSAGE) ))))))))))))))) :
            CALL(s,READ_MESSAGE)
          else:
            if  ((((((((((((((( KEYP(s,TABLET) ))))))))))))))) :
              CALL(s,READ_TABLET)
            else:
              NAME(s,DUNNO_HAO,ARG1)
      else:
        NAME(s,IDONTSEE,ARG2)
    else:
      opSAY(s,HAH_)
  else:
    opPROCEED(s)
  opQUIT(s)
READ = mkACTION('READ', action_READ)

def action_HOURS(s):
  opSAY(s,HOURS_ARE)
  EXECUTIVE(s,6,I)
  opQUIT(s)
HOURS = mkACTION('HOURS', action_HOURS)

def action_CLIMB(s):
  opSAY(s,NOCANCLIMB)
  opQUIT(s)
CLIMB = mkACTION('CLIMB', action_CLIMB)

def action_LOST(s):
  opSAY(s,IMCONFUSED)
  opQUIT(s)
LOST = mkACTION('LOST', action_LOST)

def action_MELENKURION(s):
  if  ((((((((((((((( NEARP(s,STATUE)  and  EQP(s,STATUE,0) ) )))))))))))))) :
    opSET(s,STATUE,1)
    opSAY(s,CRUMBLE)
  else:
    opSAY(s,NOTHING)
  opQUIT(s)
MELENKURION = mkACTION('MELENKURION', action_MELENKURION)

def action_NOSIDE(s):
  KEYWORD(s,SAMOHT)
  if  ((((((((((((((( BITP(s,LAMP,SPECIAL1)  or  BITP(s,HERE,LIT) )  or   not  BITP(s,LAIR,BEENHERE) )  or   not  NEARP(s,LAMP) ) )))))))))))) :
    opSAY(s,NOTHING)
  else:
    if  ((((((((((((((( HAVEP(s,LAMP) ))))))))))))))) :
      opSAY(s,FZAP)
      CALL(s,CORONER)
    else:
      if  ((((((((((((((( GTP(s,LAMPLIFE,40) ))))))))))))))) :
        APPORT(s,LAMP,YLEM)
        opSET(s,BATTERIES,1)
        opSET(s,LAMP,0)
        opSET(s,LAMPLIFE,0)
        if  ((((((((((((((( CHANCEP(s,50) ))))))))))))))) :
          opSAY(s,LAMP_GOES_POOF)
          opSAY(s,ITISNOWDARK)
        else:
          opSAY(s,LAMP_EXPLODES)
          CALL(s,CORONER)
      else:
        opSAY(s,LAMP_RECHARGED)
        ADD(s,LAMPLIFE,150)
        opSET(s,LAMP,1)
        BIS(s,LAMP,SPECIAL1)
  opQUIT(s)
NOSIDE = mkACTION('NOSIDE', action_NOSIDE)

def action_NOSIDE_2(s):
  opSAY(s,NOTHING)
  opQUIT(s)
NOSIDE_2 = mkACTION('NOSIDE', action_NOSIDE_2)

def action_SAMOHT(s):
  opSAY(s,NOTHING)
  opQUIT(s)
SAMOHT = mkACTION('SAMOHT', action_SAMOHT)

def action_THURB(s):
  opSAY(s,NOTHING)
  opQUIT(s)
THURB = mkACTION('THURB', action_THURB)

def action_KNERL(s):
  CALL(s,PASSPHRASE)
KNERL = mkACTION('KNERL', action_KNERL)

def action_ZORTON(s):
  CALL(s,PASSPHRASE)
ZORTON = mkACTION('ZORTON', action_ZORTON)

def action_KLAETU(s):
  CALL(s,PASSPHRASE)
KLAETU = mkACTION('KLAETU', action_KLAETU)

def action_SNOEZE(s):
  CALL(s,PASSPHRASE)
SNOEZE = mkACTION('SNOEZE', action_SNOEZE)

def action_BLERBI(s):
  CALL(s,PASSPHRASE)
BLERBI = mkACTION('BLERBI', action_BLERBI)

def action_RIDE(s):
  if  ((((((((((((((( EQP(s,STATUS,1)  or  KEYP(s,TURTLE) )  and  NEARP(s,TURTLE) ) ))))))))))))) :
    opSAY(s,TURTLE_BACK)
    opGOTO(s,RESERVOIR)
    APPORT(s,TURTLE,LIMBO)
    opQUIT(s)
RIDE = mkACTION('RIDE', action_RIDE)

def action_PHUGGG(s):
  BIS(s,DJINN,SPECIAL2)
  if  ((((((((((((((( BITP(s,HERE,NOTINCAVE) ))))))))))))))) :
    opSAY(s,NOTHING)
  else:
    if  ((((((((((((((( NEARP(s,BOTTLE)  and  EQP(s,BOTTLE,0) )  or  BITP(s,HERE,H20HERE) ) ))))))))))))) :
      if  ((((((((((((((( CHANCEP(s,85) ))))))))))))))) :
        opSAY(s,NOTHING)
      else:
        if  ((((((((((((((( CHANCEP(s,95) ))))))))))))))) :
          opSAY(s,JELLYFISH)
          CALL(s,CORONER)
        else:
          opSAY(s,CAVE_DESTROYED)
          opSTOP(s)
    else:
      if  ((((((((((((((( NEARP(s,AXE)  or  NEARP(s,SWORD) ) )))))))))))))) :
        if  ((((((((((((((( NEARP(s,AXE) ))))))))))))))) :
          opSAY(s,ZOT_AXE)
          if  ((((((((((((((( HAVEP(s,AXE) ))))))))))))))) :
            APPORT(s,AXE,LIMBO)
        if  ((((((((((((((( NEARP(s,SWORD) ))))))))))))))) :
          opSAY(s,ZOT_SWORD)
          if  ((((((((((((((( HAVEP(s,SWORD) ))))))))))))))) :
            APPORT(s,SWORD,LIMBO)
      else:
        RANDOM(s,I,3)
        MULT(s,I,2)
        if  ((((((((((((((( GTP(s,DWARROWS,1) ))))))))))))))) :
          ADD(s,I,1)
        if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
          if  ((((((((((((((( CHANCEP(s,70) ))))))))))))))) :
            LDA(s,J,IT_WORKED)
            ADD(s,I,J)
            opSAY(s,I)
            APPORT(s,DWARF,LIMBO)
            SUB(s,DWARFCOUNT,DWARROWS)
            opSET(s,DWARROWS,0)
          else:
            LDA(s,J,IT_DIDNT_WORK)
            ADD(s,I,J)
            opSAY(s,I)
            CALL(s,CORONER)
        else:
          opSAY(s,NOTHING)
  opQUIT(s)
PHUGGG = mkACTION('PHUGGG', action_PHUGGG)

def label_INITIAL(s):
  opSAY(s,BLANK)
  RANDOM(s,I,100)
  for o in all_objects:
    LDA(s, I, o)
    APPORT(s,I,LIMBO)
  BIS(s,KEYS,PORTABLE)
  BIS(s,LAMP,PORTABLE)
  BIS(s,CAGE,PORTABLE)
  BIS(s,ROD,PORTABLE)
  BIS(s,DYNAMITE,PORTABLE)
  BIS(s,BIRD,PORTABLE)
  BIS(s,PILLOW,PORTABLE)
  BIS(s,CLAM,PORTABLE)
  BIS(s,OYSTER,PORTABLE)
  BIS(s,MAGAZINES,PORTABLE)
  BIS(s,KNIFE,PORTABLE)
  BIS(s,FOOD,PORTABLE)
  BIS(s,BOTTLE,PORTABLE)
  BIS(s,WATER,PORTABLE)
  BIS(s,OIL,PORTABLE)
  BIS(s,AXE,PORTABLE)
  BIS(s,BEAR,PORTABLE)
  BIS(s,BATTERIES,PORTABLE)
  BIS(s,GOLD,PORTABLE)
  BIS(s,DIAMONDS,PORTABLE)
  BIS(s,SILVER,PORTABLE)
  BIS(s,JEWELRY,PORTABLE)
  BIS(s,COINS,PORTABLE)
  BIS(s,CHEST,PORTABLE)
  BIS(s,EGGS,PORTABLE)
  BIS(s,TRIDENT,PORTABLE)
  BIS(s,VASE,PORTABLE)
  BIS(s,POTTERY,PORTABLE)
  BIS(s,EMERALD,PORTABLE)
  BIS(s,PYRAMID,PORTABLE)
  BIS(s,PEARL,PORTABLE)
  BIS(s,RUG,PORTABLE)
  BIS(s,SPICES,PORTABLE)
  BIS(s,CHAIN,PORTABLE)
  BIS(s,RING,PORTABLE)
  BIS(s,SPYGLASS,PORTABLE)
  BIS(s,BAG,PORTABLE)
  BIS(s,HELMET,PORTABLE)
  BIS(s,TEETH,PORTABLE)
  BIS(s,VIAL,PORTABLE)
  BIS(s,MUSHROOM,PORTABLE)
  BIS(s,SCULPTURE,PORTABLE)
  BIS(s,BRACELET,PORTABLE)
  BIS(s,CASKET,PORTABLE)
  BIS(s,SWORD,PORTABLE)
  BIS(s,CROWN,PORTABLE)
  BIS(s,SCEPTRE,PORTABLE)
  BIS(s,YACHT,PORTABLE)
  BIS(s,FLASK,PORTABLE)
  BIS(s,PLATE,PORTABLE)
  BIS(s,BEADS,PORTABLE)
  BIS(s,BIRD,FREEBIE)
  BIS(s,OIL,FREEBIE)
  BIS(s,WATER,FREEBIE)
  BIS(s,BEAR,FREEBIE)
  BIS(s,ROAD,LIT)
  BIS(s,HILL,LIT)
  BIS(s,BUILDING,LIT)
  BIS(s,VALLEY,LIT)
  BIS(s,FOREST,LIT)
  BIS(s,FOREST2,LIT)
  BIS(s,SLIT,LIT)
  BIS(s,FAKE_SLIT,LIT)
  BIS(s,DEPRESSION,LIT)
  BIS(s,INCAVE,LIT)
  BIS(s,COBBLES,LIT)
  BIS(s,PLOVER,LIT)
  BIS(s,BREATHTAKER,LIT)
  BIS(s,LAIR,LIT)
  BIS(s,SHELF,LIT)
  BIS(s,BEACH,LIT)
  BIS(s,PLAIN_2,LIT)
  BIS(s,PLAIN_3,LIT)
  BIS(s,FACES,LIT)
  BIS(s,BY_FIGURE,LIT)
  BIS(s,AUDIENCE,LIT)
  BIS(s,AUDIENCE_E,LIT)
  BIS(s,TRANSLUCENT,LIT)
  BIS(s,PLATFORM,LIT)
  BIS(s,CYLINDRICAL,LIT)
  BIS(s,TREASUREROOM,LIT)
  BIS(s,BALCONY,LIT)
  BIS(s,INCAVE,NODWARF)
  BIS(s,COBBLES,NODWARF)
  BIS(s,ALCOVE,NODWARF)
  BIS(s,PLOVER,NODWARF)
  BIS(s,DARK,NODWARF)
  BIS(s,SWOFCHASM,NODWARF)
  BIS(s,NEOFCHASM,NODWARF)
  BIS(s,CORRIDOR,NODWARF)
  BIS(s,FORK,NODWARF)
  BIS(s,WARMJUNCTN,NODWARF)
  BIS(s,BREATHTAKER,NODWARF)
  BIS(s,BOULDERS,NODWARF)
  BIS(s,LIMESTONE,NODWARF)
  BIS(s,BARREN,NODWARF)
  BIS(s,BEARHERE,NODWARF)
  BIS(s,MAZEA_114,NODWARF)
  BIS(s,EASTPIT,NODWARF)
  BIS(s,WESTPIT,NODWARF)
  BIS(s,STREAMPIT,NODWARF)
  BIS(s,FACES,NODWARF)
  BIS(s,BY_FIGURE,NODWARF)
  BIS(s,PLAIN_1,NODWARF)
  BIS(s,PLAIN_2,NODWARF)
  BIS(s,PLAIN_3,NODWARF)
  BIS(s,NONDESCRIPT,NODWARF)
  BIS(s,PENTAGRAM,NODWARF)
  BIS(s,CHIMNEY,NODWARF)
  BIS(s,TUBE,NODWARF)
  BIS(s,TUBE_SLIDE,NODWARF)
  BIS(s,BASQUE_1,NODWARF)
  BIS(s,BASQUE_2,NODWARF)
  BIS(s,BASQUE_FORK,NODWARF)
  BIS(s,PEELGRUNT,NODWARF)
  BIS(s,ON_STEPS,NODWARF)
  BIS(s,STEPS_EXIT,NODWARF)
  BIS(s,STORAGE,NODWARF)
  BIS(s,FAKE_Y2,NODWARF)
  BIS(s,FAKE_JUMBLE,NODWARF)
  BIS(s,CATACOMBS_1,NODWARF)
  BIS(s,CATACOMBS_2,NODWARF)
  BIS(s,CATACOMBS_3,NODWARF)
  BIS(s,CATACOMBS_4,NODWARF)
  BIS(s,CATACOMBS_5,NODWARF)
  BIS(s,CATACOMBS_6,NODWARF)
  BIS(s,CATACOMBS_7,NODWARF)
  BIS(s,CATACOMBS_8,NODWARF)
  BIS(s,CATACOMBS_9,NODWARF)
  BIS(s,CATACOMBS_10,NODWARF)
  BIS(s,CATACOMBS_11,NODWARF)
  BIS(s,CATACOMBS_12,NODWARF)
  BIS(s,CATACOMBS_13,NODWARF)
  BIS(s,CATACOMBS_14,NODWARF)
  BIS(s,CATACOMBS_15,NODWARF)
  BIS(s,CATACOMBS_16,NODWARF)
  BIS(s,CATACOMBS_17,NODWARF)
  BIS(s,CATACOMBS_18,NODWARF)
  BIS(s,CATACOMBS_19,NODWARF)
  BIS(s,AUDIENCE,NODWARF)
  BIS(s,AUDIENCE_E,NODWARF)
  BIS(s,BANSHEE_1,NODWARF)
  BIS(s,GOLDEN,NODWARF)
  BIS(s,ARABESQUE,NODWARF)
  BIS(s,TRANSLUCENT,NODWARF)
  BIS(s,RESERVOIR_N,NODWARF)
  BIS(s,WARM,NODWARF)
  BIS(s,BALCONY,NODWARF)
  BIS(s,INSAFE,NODWARF)
  BIS(s,ROAD,NOTINCAVE)
  BIS(s,HILL,NOTINCAVE)
  BIS(s,BUILDING,NOTINCAVE)
  BIS(s,VALLEY,NOTINCAVE)
  BIS(s,FOREST,NOTINCAVE)
  BIS(s,FOREST2,NOTINCAVE)
  BIS(s,SLIT,NOTINCAVE)
  BIS(s,DEPRESSION,NOTINCAVE)
  BIS(s,FAKE_SLIT,NOTINCAVE)
  BIS(s,MAZEA_43,NOBACK)
  BIS(s,MAZEA_44,NOBACK)
  BIS(s,MAZEA_45,NOBACK)
  BIS(s,MAZEA_46,NOBACK)
  BIS(s,MAZEA_47,NOBACK)
  BIS(s,MAZEA_48,NOBACK)
  BIS(s,MAZEA_49,NOBACK)
  BIS(s,MAZEA_50,NOBACK)
  BIS(s,MAZEA_51,NOBACK)
  BIS(s,MAZEA_52,NOBACK)
  BIS(s,MAZEA_53,NOBACK)
  BIS(s,MAZEA_54,NOBACK)
  BIS(s,MAZEA_55,NOBACK)
  BIS(s,MAZEA_56,NOBACK)
  BIS(s,MAZEA_57_PIT,NOBACK)
  BIS(s,MAZEA_58,NOBACK)
  BIS(s,MAZEA_80,NOBACK)
  BIS(s,MAZEA_81,NOBACK)
  BIS(s,MAZEA_82,NOBACK)
  BIS(s,MAZEA_83,NOBACK)
  BIS(s,MAZEA_84,NOBACK)
  BIS(s,MAZEA_85,NOBACK)
  BIS(s,MAZEA_86,NOBACK)
  BIS(s,MAZEA_87,NOBACK)
  BIS(s,MAZED_112,NOBACK)
  BIS(s,MAZEA_114,NOBACK)
  BIS(s,MAZED_131,NOBACK)
  BIS(s,MAZED_132,NOBACK)
  BIS(s,MAZED_133,NOBACK)
  BIS(s,MAZED_134,NOBACK)
  BIS(s,MAZED_135,NOBACK)
  BIS(s,MAZED_136,NOBACK)
  BIS(s,MAZED_137,NOBACK)
  BIS(s,MAZED_138,NOBACK)
  BIS(s,MAZED_139,NOBACK)
  BIS(s,MAZED_140,NOBACK)
  BIS(s,INCLINE,NOBACK)
  BIS(s,STALACT,NOBACK)
  BIS(s,SWOFCHASM,NOBACK)
  BIS(s,NEOFCHASM,NOBACK)
  BIS(s,WITTSEND,NOBACK)
  BIS(s,ALCOVE,NOBACK)
  BIS(s,PLOVER,NOBACK)
  BIS(s,DARK,NOBACK)
  BIS(s,NSCANYONWIDE,NOBACK)
  BIS(s,ICECAVE_1,NOBACK)
  BIS(s,ICECAVE_2,NOBACK)
  BIS(s,ICECAVE_3,NOBACK)
  BIS(s,ICECAVE_4,NOBACK)
  BIS(s,ICECAVE_5,NOBACK)
  BIS(s,ICECAVE_6,NOBACK)
  BIS(s,ICECAVE_7,NOBACK)
  BIS(s,ICECAVE_8,NOBACK)
  BIS(s,ICECAVE_9,NOBACK)
  BIS(s,ICECAVE_10,NOBACK)
  BIS(s,ICECAVE_11,NOBACK)
  BIS(s,ICECAVE_12,NOBACK)
  BIS(s,ICECAVE_13,NOBACK)
  BIS(s,ICECAVE_14,NOBACK)
  BIS(s,ICECAVE_15,NOBACK)
  BIS(s,ICECAVE_16,NOBACK)
  BIS(s,ICECAVE_17,NOBACK)
  BIS(s,ICECAVE_18,NOBACK)
  BIS(s,ICECAVE_19,NOBACK)
  BIS(s,ICECAVE_20,NOBACK)
  BIS(s,ICECAVE_21,NOBACK)
  BIS(s,SLIDE,NOBACK)
  BIS(s,ICE,NOBACK)
  BIS(s,CATACOMBS_1,NOBACK)
  BIS(s,CATACOMBS_2,NOBACK)
  BIS(s,CATACOMBS_3,NOBACK)
  BIS(s,CATACOMBS_4,NOBACK)
  BIS(s,CATACOMBS_5,NOBACK)
  BIS(s,CATACOMBS_6,NOBACK)
  BIS(s,CATACOMBS_7,NOBACK)
  BIS(s,CATACOMBS_8,NOBACK)
  BIS(s,CATACOMBS_9,NOBACK)
  BIS(s,CATACOMBS_10,NOBACK)
  BIS(s,CATACOMBS_11,NOBACK)
  BIS(s,CATACOMBS_12,NOBACK)
  BIS(s,CATACOMBS_13,NOBACK)
  BIS(s,CATACOMBS_14,NOBACK)
  BIS(s,CATACOMBS_15,NOBACK)
  BIS(s,CATACOMBS_16,NOBACK)
  BIS(s,CATACOMBS_17,NOBACK)
  BIS(s,CATACOMBS_18,NOBACK)
  BIS(s,CATACOMBS_19,NOBACK)
  BIS(s,FACES,NOBACK)
  BIS(s,PLAIN_1,NOBACK)
  BIS(s,PLAIN_2,NOBACK)
  BIS(s,BASQUE_1,NOBACK)
  BIS(s,CYLINDRICAL,NOBACK)
  BIS(s,PLATFORM,NOBACK)
  BIS(s,SHELL,NOBACK)
  BIS(s,ARCH_COR_1,NOBACK)
  BIS(s,ARCH_COR_2,NOBACK)
  BIS(s,MAZEA_42,INMAZE)
  BIS(s,MAZEA_43,INMAZE)
  BIS(s,MAZEA_44,INMAZE)
  BIS(s,MAZEA_45,INMAZE)
  BIS(s,MAZEA_46,INMAZE)
  BIS(s,MAZEA_47,INMAZE)
  BIS(s,MAZEA_48,INMAZE)
  BIS(s,MAZEA_49,INMAZE)
  BIS(s,MAZEA_50,INMAZE)
  BIS(s,MAZEA_51,INMAZE)
  BIS(s,MAZEA_52,INMAZE)
  BIS(s,MAZEA_53,INMAZE)
  BIS(s,MAZEA_54,INMAZE)
  BIS(s,MAZEA_55,INMAZE)
  BIS(s,MAZEA_56,INMAZE)
  BIS(s,MAZEA_57_PIT,INMAZE)
  BIS(s,MAZEA_58,INMAZE)
  BIS(s,MAZEA_80,INMAZE)
  BIS(s,MAZEA_81,INMAZE)
  BIS(s,MAZEA_82,INMAZE)
  BIS(s,MAZEA_83,INMAZE)
  BIS(s,MAZEA_84,INMAZE)
  BIS(s,MAZEA_85,INMAZE)
  BIS(s,MAZEA_86,INMAZE)
  BIS(s,MAZEA_87,INMAZE)
  BIS(s,MAZED_107,INMAZE)
  BIS(s,MAZED_112,INMAZE)
  BIS(s,MAZEA_114,INMAZE)
  BIS(s,MAZED_131,INMAZE)
  BIS(s,MAZED_132,INMAZE)
  BIS(s,MAZED_133,INMAZE)
  BIS(s,MAZED_134,INMAZE)
  BIS(s,MAZED_135,INMAZE)
  BIS(s,MAZED_136,INMAZE)
  BIS(s,MAZED_137,INMAZE)
  BIS(s,MAZED_138,INMAZE)
  BIS(s,MAZED_139,INMAZE)
  BIS(s,MAZED_140,INMAZE)
  BIS(s,SLIDE,INMAZE)
  BIS(s,ICECAVE_1,INMAZE)
  BIS(s,ICECAVE_1A,INMAZE)
  BIS(s,ICECAVE_2,INMAZE)
  BIS(s,ICECAVE_2A,INMAZE)
  BIS(s,ICECAVE_3,INMAZE)
  BIS(s,ICECAVE_3A,INMAZE)
  BIS(s,ICECAVE_4,INMAZE)
  BIS(s,ICECAVE_5,INMAZE)
  BIS(s,ICECAVE_6,INMAZE)
  BIS(s,ICECAVE_7,INMAZE)
  BIS(s,ICECAVE_8,INMAZE)
  BIS(s,ICECAVE_9,INMAZE)
  BIS(s,ICECAVE_10,INMAZE)
  BIS(s,ICECAVE_11,INMAZE)
  BIS(s,ICECAVE_12,INMAZE)
  BIS(s,ICECAVE_12A,INMAZE)
  BIS(s,ICECAVE_13,INMAZE)
  BIS(s,ICECAVE_14,INMAZE)
  BIS(s,ICECAVE_15,INMAZE)
  BIS(s,ICECAVE_15A,INMAZE)
  BIS(s,ICECAVE_16,INMAZE)
  BIS(s,ICECAVE_17,INMAZE)
  BIS(s,ICECAVE_18,INMAZE)
  BIS(s,ICECAVE_19,INMAZE)
  BIS(s,ICECAVE_20,INMAZE)
  BIS(s,ICECAVE_21,INMAZE)
  BIS(s,ICECAVE_22,INMAZE)
  BIS(s,ICECAVE_23,INMAZE)
  BIS(s,ICECAVE_24,INMAZE)
  BIS(s,ICECAVE_25,INMAZE)
  BIS(s,ICECAVE_26,INMAZE)
  BIS(s,ICECAVE_27,INMAZE)
  BIS(s,ICECAVE_28,INMAZE)
  BIS(s,ICECAVE_28A,INMAZE)
  BIS(s,ICECAVE_29,INMAZE)
  BIS(s,ICECAVE_30,INMAZE)
  BIS(s,GOLDROOM,ONE_EXIT)
  BIS(s,SOUTHSIDE,ONE_EXIT)
  BIS(s,SANDSTONE,ONE_EXIT)
  BIS(s,WINDOW,ONE_EXIT)
  BIS(s,WINDOW2,ONE_EXIT)
  BIS(s,MAZEA_46,ONE_EXIT)
  BIS(s,MAZEA_47,ONE_EXIT)
  BIS(s,MAZEA_48,ONE_EXIT)
  BIS(s,MAZEA_49,ONE_EXIT)
  BIS(s,MAZEA_54,ONE_EXIT)
  BIS(s,MAZEA_56,ONE_EXIT)
  BIS(s,MAZEA_58,ONE_EXIT)
  BIS(s,DEADEND1,ONE_EXIT)
  BIS(s,DEADEND2,ONE_EXIT)
  BIS(s,DEADEND3,ONE_EXIT)
  BIS(s,MAZEA_81,ONE_EXIT)
  BIS(s,MAZEA_82,ONE_EXIT)
  BIS(s,MAZEA_85,ONE_EXIT)
  BIS(s,MAZEA_86,ONE_EXIT)
  BIS(s,SOFT,ONE_EXIT)
  BIS(s,CULDESAC,ONE_EXIT)
  BIS(s,RESERVOIR,ONE_EXIT)
  BIS(s,BALCONY,ONE_EXIT)
  BIS(s,MAZED_140,ONE_EXIT)
  BIS(s,INSAFE,ONE_EXIT)
  BIS(s,TOOL,ONE_EXIT)
  BIS(s,CUBICLE,ONE_EXIT)
  BIS(s,SPHERICAL,ONE_EXIT)
  BIS(s,ICECAVE_1A,ONE_EXIT)
  BIS(s,ICECAVE_3A,ONE_EXIT)
  BIS(s,ICECAVE_7,ONE_EXIT)
  BIS(s,ICECAVE_8,ONE_EXIT)
  BIS(s,ICECAVE_13,ONE_EXIT)
  BIS(s,ICECAVE_14,ONE_EXIT)
  BIS(s,CRACK_4,ONE_EXIT)
  BIS(s,BEACH,ONE_EXIT)
  BIS(s,GRATE,OPENABLE)
  BIS(s,DOOR,OPENABLE)
  BIS(s,CLAM,OPENABLE)
  BIS(s,OYSTER,OPENABLE)
  BIS(s,FLASK,OPENABLE)
  BIS(s,CHAIN,OPENABLE)
  BIS(s,SAFE,OPENABLE)
  BIS(s,VIAL,OPENABLE)
  BIS(s,STEPS,INVISIBLE)
  BIS(s,FISSURE,INVISIBLE)
  BIS(s,MIRROR,INVISIBLE)
  BIS(s,STALACTITE,INVISIBLE)
  BIS(s,DRAWING,INVISIBLE)
  BIS(s,PIRATE,INVISIBLE)
  BIS(s,STATUE,INVISIBLE)
  BIS(s,VOLCANO,INVISIBLE)
  BIS(s,QUICKSAND,INVISIBLE)
  BIS(s,THRONE,INVISIBLE)
  BIS(s,CARPET,INVISIBLE)
  BIS(s,DWARF,INVISIBLE)
  BIS(s,KNIFE,INVISIBLE)
  BIS(s,FOG,INVISIBLE)
  BIS(s,PLANT2,INVISIBLE)
  BIS(s,MAZEA_42,HINTABLE)
  BIS(s,MAZEA_43,HINTABLE)
  BIS(s,MAZEA_44,HINTABLE)
  BIS(s,MAZEA_45,HINTABLE)
  BIS(s,MAZEA_46,HINTABLE)
  BIS(s,MAZEA_47,HINTABLE)
  BIS(s,MAZEA_48,HINTABLE)
  BIS(s,MAZEA_49,HINTABLE)
  BIS(s,MAZEA_50,HINTABLE)
  BIS(s,MAZEA_51,HINTABLE)
  BIS(s,MAZEA_52,HINTABLE)
  BIS(s,MAZEA_53,HINTABLE)
  BIS(s,MAZEA_54,HINTABLE)
  BIS(s,MAZEA_55,HINTABLE)
  BIS(s,MAZEA_56,HINTABLE)
  BIS(s,MAZEA_57_PIT,HINTABLE)
  BIS(s,MAZEA_58,HINTABLE)
  BIS(s,MAZEA_80,HINTABLE)
  BIS(s,MAZEA_81,HINTABLE)
  BIS(s,MAZEA_82,HINTABLE)
  BIS(s,MAZEA_83,HINTABLE)
  BIS(s,MAZEA_84,HINTABLE)
  BIS(s,MAZEA_85,HINTABLE)
  BIS(s,MAZEA_86,HINTABLE)
  BIS(s,MAZEA_87,HINTABLE)
  BIS(s,MAZED_107,HINTABLE)
  BIS(s,MAZED_112,HINTABLE)
  BIS(s,MAZEA_114,HINTABLE)
  BIS(s,MAZED_131,HINTABLE)
  BIS(s,MAZED_132,HINTABLE)
  BIS(s,MAZED_133,HINTABLE)
  BIS(s,MAZED_134,HINTABLE)
  BIS(s,MAZED_135,HINTABLE)
  BIS(s,MAZED_136,HINTABLE)
  BIS(s,MAZED_137,HINTABLE)
  BIS(s,MAZED_138,HINTABLE)
  BIS(s,MAZED_139,HINTABLE)
  BIS(s,MAZED_140,HINTABLE)
  BIS(s,BIRDCHAMBER,HINTABLE)
  BIS(s,DEPRESSION,HINTABLE)
  BIS(s,MTKING,HINTABLE)
  BIS(s,WITTSEND,HINTABLE)
  BIS(s,PLOVER,HINTABLE)
  BIS(s,ALCOVE,HINTABLE)
  BIS(s,DARK,HINTABLE)
  BIS(s,SLIDE,HINTABLE)
  BIS(s,ICECAVE_1,HINTABLE)
  BIS(s,ICECAVE_1A,HINTABLE)
  BIS(s,ICECAVE_2,HINTABLE)
  BIS(s,ICECAVE_2A,HINTABLE)
  BIS(s,ICECAVE_3,HINTABLE)
  BIS(s,ICECAVE_3A,HINTABLE)
  BIS(s,ICECAVE_4,HINTABLE)
  BIS(s,ICECAVE_5,HINTABLE)
  BIS(s,ICECAVE_6,HINTABLE)
  BIS(s,ICECAVE_7,HINTABLE)
  BIS(s,ICECAVE_8,HINTABLE)
  BIS(s,ICECAVE_9,HINTABLE)
  BIS(s,ICECAVE_10,HINTABLE)
  BIS(s,ICECAVE_11,HINTABLE)
  BIS(s,ICECAVE_12,HINTABLE)
  BIS(s,ICECAVE_12A,HINTABLE)
  BIS(s,ICECAVE_13,HINTABLE)
  BIS(s,ICECAVE_14,HINTABLE)
  BIS(s,ICECAVE_15,HINTABLE)
  BIS(s,ICECAVE_15A,HINTABLE)
  BIS(s,ICECAVE_16,HINTABLE)
  BIS(s,ICECAVE_17,HINTABLE)
  BIS(s,ICECAVE_18,HINTABLE)
  BIS(s,ICECAVE_19,HINTABLE)
  BIS(s,ICECAVE_20,HINTABLE)
  BIS(s,ICECAVE_21,HINTABLE)
  BIS(s,ICECAVE_22,HINTABLE)
  BIS(s,ICECAVE_23,HINTABLE)
  BIS(s,ICECAVE_24,HINTABLE)
  BIS(s,ICECAVE_25,HINTABLE)
  BIS(s,ICECAVE_26,HINTABLE)
  BIS(s,ICECAVE_27,HINTABLE)
  BIS(s,ICECAVE_28,HINTABLE)
  BIS(s,ICECAVE_28A,HINTABLE)
  BIS(s,ICECAVE_29,HINTABLE)
  BIS(s,ICECAVE_30,HINTABLE)
  BIS(s,PLAIN_2,HINTABLE)
  BIS(s,BUILDING,H20HERE)
  BIS(s,ROAD,H20HERE)
  BIS(s,VALLEY,H20HERE)
  BIS(s,SLIT,H20HERE)
  BIS(s,STREAMPIT,H20HERE)
  BIS(s,CAVERN,H20HERE)
  BIS(s,RESERVOIR,H20HERE)
  BIS(s,RESERVOIR_N,H20HERE)
  BIS(s,PIT,THROWER)
  BIS(s,EASTOFFISSURE,THROWER)
  BIS(s,WESTOFFISSURE,THROWER)
  BIS(s,WEND2PIT,THROWER)
  BIS(s,EEND2PIT,THROWER)
  BIS(s,LOWNSPASSAGE,THROWER)
  BIS(s,WINDOW,THROWER)
  BIS(s,WINDOW2,THROWER)
  BIS(s,BRINK,THROWER)
  BIS(s,DUSTY,THROWER)
  BIS(s,MAZEA_57_PIT,THROWER)
  BIS(s,SECRETNSCYN,THROWER)
  BIS(s,SECRETNSCPAS,THROWER)
  BIS(s,SECRETEW_TITE,THROWER)
  BIS(s,INCLINE,THROWER)
  BIS(s,CAVERN,THROWER)
  BIS(s,MISTY,THROWER)
  BIS(s,RESERVOIR,THROWER)
  BIS(s,RESERVOIR_N,THROWER)
  BIS(s,STALACT,THROWER)
  BIS(s,BALCONY,THROWER)
  BIS(s,SWOFCHASM,THROWER)
  BIS(s,NEOFCHASM,THROWER)
  BIS(s,BREATHTAKER,THROWER)
  BIS(s,FACES,THROWER)
  BIS(s,TUBE,THROWER)
  BIS(s,TUBE_SLIDE,THROWER)
  BIS(s,BASQUE_FORK,THROWER)
  BIS(s,ON_STEPS,THROWER)
  BIS(s,STEPS_EXIT,THROWER)
  BIS(s,BRINK_1,THROWER)
  BIS(s,BRINK_2,THROWER)
  BIS(s,ICE,THROWER)
  BIS(s,BRINK_3,THROWER)
  BIS(s,SHELF,THROWER)
  BIS(s,PLATFORM,THROWER)
  BIS(s,GOLD,VALUED)
  BIS(s,DIAMONDS,VALUED)
  BIS(s,SILVER,VALUED)
  BIS(s,JEWELRY,VALUED)
  BIS(s,COINS,VALUED)
  BIS(s,CHEST,VALUED)
  BIS(s,EGGS,VALUED)
  BIS(s,TRIDENT,VALUED)
  BIS(s,VASE,VALUED)
  BIS(s,EMERALD,VALUED)
  BIS(s,PYRAMID,VALUED)
  BIS(s,PEARL,VALUED)
  BIS(s,RUG,VALUED)
  BIS(s,SPICES,VALUED)
  BIS(s,CHAIN,VALUED)
  BIS(s,CASKET,VALUED)
  BIS(s,SCULPTURE,VALUED)
  BIS(s,BRACELET,VALUED)
  BIS(s,RING,VALUED)
  BIS(s,SPYGLASS,VALUED)
  BIS(s,BAG,VALUED)
  BIS(s,HELMET,VALUED)
  BIS(s,CROWN,VALUED)
  BIS(s,SCEPTRE,VALUED)
  BIS(s,YACHT,VALUED)
  BIS(s,BRACELET,VALUED)
  BIS(s,BEADS,VALUED)
  BIS(s,CHEST,UNSTABLE)
  BIS(s,SCULPTURE,UNSTABLE)
  BIS(s,CAGE,UNSTABLE)
  BIS(s,CASKET,UNSTABLE)
  BIS(s,TEETH,UNSTABLE)
  BIS(s,MUSHROOM,UNSTABLE)
  BIS(s,BAG,UNSTABLE)
  BIS(s,CROWN,UNSTABLE)
  BIS(s,YACHT,UNSTABLE)
  BIS(s,PLATE,UNSTABLE)
  BIS(s,BEADS,UNSTABLE)
  BIS(s,FLASK,UNSTABLE)
  BIS(s,TROLL,MORTAL)
  BIS(s,DWARF,MORTAL)
  BIS(s,DRAGON,MORTAL)
  BIS(s,SNAKE,MORTAL)
  BIS(s,BLOB,MORTAL)
  BIS(s,BEAR,MORTAL)
  BIS(s,CLAM,MORTAL)
  BIS(s,OYSTER,MORTAL)
  BIS(s,OGRE,MORTAL)
  BIS(s,BIRD,MORTAL)
  BIS(s,DJINN,MORTAL)
  BIS(s,GOBLINS,MORTAL)
  BIS(s,BASILISK,MORTAL)
  BIS(s,GONG,MORTAL)
  BIS(s,FOOD,EDIBLE)
  BIS(s,MUSHROOM,EDIBLE)
  APPORT(s,KEYS,BUILDING)
  APPORT(s,LAMP,BUILDING)
  APPORT(s,GRATE,DEPRESSION)
  APPORT(s,CAGE,COBBLES)
  APPORT(s,ROD,DEBRIS)
  APPORT(s,STEPS,PIT)
  APPORT(s,BIRD,BIRDCHAMBER)
  APPORT(s,DOOR,IMMENSENSPASS)
  APPORT(s,PILLOW,SOFT)
  APPORT(s,SNAKE,MTKING)
  APPORT(s,FISSURE,EASTOFFISSURE)
  APPORT(s,TABLET,DARK)
  APPORT(s,CLAM,SHELL)
  APPORT(s,MAGAZINES,ANTEROOM)
  APPORT(s,FOOD,BUILDING)
  APPORT(s,BOTTLE,BUILDING)
  APPORT(s,PLANT,WESTPIT)
  APPORT(s,PLANT2,WEND2PIT)
  APPORT(s,STALACTITE,STALACT)
  APPORT(s,SHADOW,WINDOW)
  APPORT(s,DRAWING,ORIENTAL)
  APPORT(s,DRAGON,SECRETCYNNE1)
  APPORT(s,CHASM,SWOFCHASM)
  APPORT(s,TROLL,SWOFCHASM)
  APPORT(s,BEAR,BEARHERE)
  APPORT(s,VOLCANO,BREATHTAKER)
  APPORT(s,MACHINE,MAZED_140)
  APPORT(s,CARPET,SOFT)
  APPORT(s,GOLD,GOLDROOM)
  APPORT(s,DIAMONDS,WESTOFFISSURE)
  APPORT(s,SILVER,LOWNSPASSAGE)
  APPORT(s,JEWELRY,SOUTHSIDE)
  APPORT(s,COINS,WESTSIDE)
  APPORT(s,EGGS,GIANT)
  APPORT(s,TRIDENT,CAVERN)
  APPORT(s,VASE,ORIENTAL)
  APPORT(s,EMERALD,PLOVER)
  APPORT(s,PYRAMID,DARK)
  APPORT(s,SPICES,BOULDERS)
  APPORT(s,CHAIN,BEARHERE)
  APPORT(s,SPYGLASS,IN_JONAH)
  APPORT(s,BAG,BEACH)
  APPORT(s,DINGHY,BEACH)
  APPORT(s,HELMET,MORION)
  APPORT(s,VIAL,SPHERICAL)
  APPORT(s,MUSHROOM,CUBICLE)
  APPORT(s,SCULPTURE,ICECAVE_14)
  APPORT(s,CASKET,CRACK_4)
  APPORT(s,SAFE,VAULT)
  APPORT(s,QUICKSAND,ARCH_COR_1)
  APPORT(s,SLIME,CRACK_2)
  APPORT(s,SWORD,SANDSTONE)
  APPORT(s,OGRE,GLASSY)
  APPORT(s,THRONE,AUDIENCE_E)
  APPORT(s,SKELETON,AUDIENCE_E)
  APPORT(s,SCEPTRE,AUDIENCE_E)
  APPORT(s,CROWN,INSAFE)
  APPORT(s,STATUE,BY_FIGURE)
  APPORT(s,FOG,PLAIN_2)
  APPORT(s,YACHT,NONDESCRIPT)
  APPORT(s,BRACELET,TRANSLUCENT)
  APPORT(s,FLASK,ARABESQUE)
  APPORT(s,BASILISK,BASQUE_1)
  APPORT(s,PLATE,STORAGE)
  APPORT(s,BEADS,BALCONY)
  APPORT(s,GONG,RESERVOIR_N)
  BIS(s,GRATE,SCHIZOID)
  BIS(s,STEPS,SCHIZOID)
  BIS(s,FISSURE,SCHIZOID)
  BIS(s,PLANT2,SCHIZOID)
  BIS(s,SHADOW,SCHIZOID)
  BIS(s,DRAGON,SCHIZOID)
  BIS(s,CHASM,SCHIZOID)
  BIS(s,TROLL,SCHIZOID)
  BIS(s,TROLL2,SCHIZOID)
  BIS(s,QUICKSAND,SCHIZOID)
  BIS(s,SAFE,SCHIZOID)
  BIS(s,FOG,SCHIZOID)
  BIS(s,GORGE,SCHIZOID)
  BIS(s,BASILISK,SCHIZOID)
  RANDOM(s,I,100)
  opGOTO(s,ROAD)
  LDA(s,OK,OK_)
  RANDOM(s,CLOCK,10)
  ADD(s,CLOCK,15)
  opSET(s,LAMPLIFE,300)
  RANDOM(s,DWARFCOUNT,3)
  ADD(s,DWARFCOUNT,3)
  if  ((((((((((((((( CHANCEP(s,10) ))))))))))))))) :
    RANDOM(s,CAMEO_TIME,400)
    ADD(s,CAMEO_TIME,100)
  else:
    opSET(s,CAMEO_TIME,0)
  opSET(s,CHAIN,1)
  opSET(s,FOG,8)
  opSET(s,FLASK,1)
  opSET(s,INVCT,0)
  opSET(s,STRENGTH,7)
  opSAY(s,LOGON)
  QUERY(s,HITHERE,INITIAL2)
INITIAL = mkLABEL('INITIAL', label_INITIAL)

def label_INITIAL2(s):
  if  ((((((((((((((( REPLYP(s,QUERY_REPLY) ))))))))))))))) :
    opSAY(s,INTRO)
  opSAY(s,BLANK)
  CALL(s,REPEAT)
INITIAL2 = mkLABEL('INITIAL2', label_INITIAL2)

def label_REPEAT(s):
  if  ((((((((((((((( BITP(s,ADMIN,TICKER) ))))))))))))))) :
    CALL(s,TICK)
  if  ((((((((((((((( BITP(s,STATUS,MOVED) ))))))))))))))) :
    pass
  else:
    opPROCEED(s)
  if  ((((((((((((((( BITP(s,THERE,ONE_EXIT)  and  LOCP(s,DWARF,THERE) ) )))))))))))))) :
    opGOTO(s,THERE)
    BIC(s,STATUS,MOVED)
    opSAY(s,DWARFBLOCK)
    opPROCEED(s)
  if  ((((((((((((((( NEARP(s,FOG) ))))))))))))))) :
    CALL(s,PHOG)
  BIC(s,STATUS,MOVED)
  ADD(s,MOVES,1)
  if  ((((((((((((((( BITP(s,ADMIN,DEMO) ))))))))))))))) :
    opSET(s,I,MAX_DEMO)
  else:
    opSET(s,I,MAX_GAME)
  if  ((((((((((((((( EQP(s,MOVES,I) ))))))))))))))) :
    opSAY(s,WIZARD_ENDS)
    CALL(s,FINIS)
  if  ((((((((((((((( NEARP(s,LAMP) ))))))))))))))) :
    if  ((((((((((((((( EQP(s,LAMP,1) ))))))))))))))) :
      SUB(s,LAMPLIFE,1)
      if  ((((((((((((((( EQP(s,LAMPLIFE,40)  or  EQP(s,LAMPLIFE,0) ) )))))))))))))) :
        CALL(s,LAMPREY)
  if  ((((((((((((((( LOCP(s,GOBLINS,LIMBO) ))))))))))))))) :
    pass
  else:
    APPORT(s,GOBLINS,HERE)
    if  ((((((((((((((( GTP(s,GOBLINS,-1) ))))))))))))))) :
      opSAY(s,GOBLIN_CHASE)
    ADD(s,GOBLINS,1)
  opSET(s,K,0)
  if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
    opSET(s,K,1)
  else:
    if  ((((((((((((((( NEARP(s,LAMP) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,LAMP,1) ))))))))))))))) :
        opSET(s,K,1)
  if  ((((((((((((((( BITP(s,HERE,BEENHERE)  and  BITP(s,STATUS,QUICKIE) )  or  BITP(s,STATUS,FASTMODE) ) ))))))))))))) :
    opSET(s,J,0)
  else:
    opSET(s,J,1)
  if  ((((((((((((((( EQP(s,K,1) ))))))))))))))) :
    opSAY(s,HERE)
    if  ((((((((((((((( BITP(s,HERE,BEENHERE) ))))))))))))))) :
      opSET(s,K,0)
    BIS(s,HERE,BEENHERE)
    for o in all_objects:
      if not NEARP(s, o): continue
      LDA(s, I, o)
      if  ((((((((((((((( NEARP(s,I)  and   not  HAVEP(s,I) ) )))))))))))))) :
        BIS(s,I,SEEN)
        if  ((((((((((((((( EQP(s,J,1)  and   not  BITP(s,I,INVISIBLE) ) )))))))))))))) :
          opSAY(s,BLANK)
          opSET(s,J,0)
        opSAY(s,I)
    if  ((((((((((((((( HAVEP(s,BEAR) ))))))))))))))) :
      opSAY(s,I_C_A_BEAR)
  else:
    if  ((((((((((((((( BITP(s,THERE,LIT)  or  CHANCEP(s,75) )  or  BITP(s,ADMIN,RANOUT) ) ))))))))))))) :
      opSAY(s,ITISNOWDARK)
    else:
      opSAY(s,CRUNCH)
      CALL(s,CORONER)
  BIC(s,ADMIN,RANOUT)
  if  ((((((((((((((( ATP(s,Y2) ))))))))))))))) :
    if  ((((((((((((((( CHANCEP(s,35) ))))))))))))))) :
      opSAY(s,SAYSPLUGH)
  if  ((((((((((((((( NEARP(s,GOBLINS) ))))))))))))))) :
    ADD(s,GOBLINS,1)
    if  ((((((((((((((( GTP(s,GOBLINS,6) ))))))))))))))) :
      CALL(s,CORONER)
  if  ((((((((((((((( LOCP(s,DWARF,LIMBO) ))))))))))))))) :
    pass
  else:
    if  ((((((((((((((( BITP(s,HERE,NOTINCAVE)  or  BITP(s,HERE,NODWARF) ) )))))))))))))) :
      pass
    else:
      APPORT(s,DWARF,HERE)
  if  ((((((((((((((( BITP(s,HERE,NOTINCAVE) ))))))))))))))) :
    pass
  else:
    SUB(s,CLOCK,2)
    SUB(s,CLOCK,K)
    if  ((((((((((((((( LTP(s,CLOCK,1) ))))))))))))))) :
      CALL(s,CLOCK4)
  if  ((((((((((((((( NEARP(s,DWARF) ))))))))))))))) :
    BIC(s,PIRATE,SPECIAL1)
    if  ((((((((((((((( GTP(s,DWARFCOUNT,0) ))))))))))))))) :
      if  ((((((((((((((( EQP(s,DWARROWS,1) ))))))))))))))) :
        opSAY(s,DWARFHERE)
      else:
        VALUE(s,DWARVESHERE,DWARROWS)
      opSET(s,J,DWARROWS)
      ADD(s,J,4)
      RANDOM(s,J,J)
      SUB(s,J,3)
      if  ((((((((((((((( GTP(s,J,0) ))))))))))))))) :
        if  ((((((((((((((( EQP(s,J,1) ))))))))))))))) :
          opSAY(s,KNIFETHROWN)
        else:
          VALUE(s,KNIVESTHROWN,J)
        opSET(s,I,INVCT)
        MULT(s,I,-5)
        ADD(s,I,95)
        if  ((((((((((((((( BITP(s,DWARF,SPECIAL2) ))))))))))))))) :
          SUB(s,I,20)
        if  ((((((((((((((( EQP(s,MUSHROOM,2) ))))))))))))))) :
          ADD(s,I,25)
        DIVIDE(s,I,J)
        if  ((((((((((((((( CHANCEP(s,I)  or  BITP(s,DWARF,SPECIAL1) ) )))))))))))))) :
          if  ((((((((((((((( EQP(s,J,1) ))))))))))))))) :
            opSAY(s,MISSES)
          else:
            opSAY(s,KNIVESMISS)
          BIC(s,DWARF,SPECIAL1)
        else:
          if  ((((((((((((((( EQP(s,J,1) ))))))))))))))) :
            opSAY(s,GETSYOU)
          else:
            opSAY(s,KNIFEGOTYOU)
          CALL(s,CORONER)
  if  ((((((((((((((( LOCP(s,LAMP,YLEM)  and  ATP(s,ROAD) )  and  LTP(s,CLOSURE,4) ) ))))))))))))) :
    opSAY(s,LAMP_DEAD_)
    opSET(s,QUITTING,1)
    CALL(s,FINIS)
REPEAT = mkLABEL('REPEAT', label_REPEAT)

def labels_REPEAT_2(s):
  if  ((((((((((((((( BITP(s,HERE,HINTABLE) ))))))))))))))) :
    ADD(s,HINT_TIME,1)
    if  ((((((((((((((( GTP(s,HINT_TIME,30)  and   not  BITP(s,HERE,INMAZE) )  or  GTP(s,HINT_TIME,50) ) ))))))))))))) :
      CALL(s,HINT_LOGIC)
  else:
    opSET(s,HINT_TIME,0)
  if  ((((((((((((((( EQP(s,BLOB,16) ))))))))))))))) :
    APPORT(s,BLOB,HERE)
  opSET(s,INVCT,0)
  for o in all_objects:
    LDA(s, I, o)
    if  ((((((((((((((( HAVEP(s,I)  and   not  BITP(s,I,FREEBIE) ) )))))))))))))) :
      ADD(s,INVCT,1)
  INPUT(s,INPUT_IS_READY)
REPEAT_2 = mkLABEL('REPEAT', labels_REPEAT_2)

def label_INPUT_IS_READY(s):
  SUB(s,FOOBAR,1)
  ADD(s,TURNS,1)
  if  ((((((((((((((( EQP(s,STATUS,0) ))))))))))))))) :
    opQUIT(s)
  if  ((((((((((((((( BITP(s,ARG1,BADWORD) ))))))))))))))) :
    opSAY(s,WHAT_)
    opQUIT(s)
  if  ((((((((((((((( KEYP(s,SAY) ))))))))))))))) :
    CALL(s,PRESAY)
  if  ((((((((((((((( GTP(s,STATUS,1) ))))))))))))))) :
    if  ((((((((((((((( BITP(s,ARG2,BADWORD) ))))))))))))))) :
      LDA(s,I,RESTORE)
      if  ((((((((((((((( GTP(s,ARG1,I) ))))))))))))))) :
        NAME(s,NOCOMPRENDE,ARG2)
        opQUIT(s)
  CALL(s,HERE)
  if  ((((((((((((((( BITP(s,ARG1,PLACE) ))))))))))))))) :
    if  ((((((((((((((( ATP(s,ARG1) ))))))))))))))) :
      opSAY(s,YOU_ARE_THERE)
    else:
      opSAY(s,NO_CAN_GO)
  else:
    CALL(s,ARG1)
    if  ((((((((((((((( BITP(s,ARG1,OBJECT) ))))))))))))))) :
      if  ((((((((((((((( NEARP(s,ARG1) ))))))))))))))) :
        NAME(s,WHAT_DO,ARG1)
      else:
        NAME(s,IDONTSEE,ARG1)
    else:
      CALL(s,BAILOUT)
INPUT_IS_READY = mkLABEL('INPUT_IS_READY', label_INPUT_IS_READY)

def label_TEST_SET_VAR(s):
  opSET(s,I,0)
  PRINT(s,"0",I)
  opSET(s,I,12)
  PRINT(s,"12",I)
  opSET(s,J,I)
  PRINT(s,"12",J)
TEST_SET_VAR = mkLABEL('TEST_SET_VAR', label_TEST_SET_VAR)

def label_TEST_SET_OBJ(s):
  opSET(s,AXE,0)
  PRINT(s,"AXE0",AXE)
  opSET(s,AXE,1)
  PRINT(s,"AXE1",AXE)
TEST_SET_OBJ = mkLABEL('TEST_SET_OBJ', label_TEST_SET_OBJ)

def label_TEST_LDA(s):
  opSET(s,I,0)
  PRINT(s,"0",I)
  LDA(s,I,WESTOFFISSURE)
  PRINT(s,"WESTOFFISSURE",I)
  LDA(s,J,EAST)
  PRINT(s,"EAST",J)
  LDA(s,J,SNIDELEY-1)
  PRINT(s,"SNIDELEY",SNIDELEY)
  PRINT(s,"SNIDELEY-1",J)
  PRINT(s,"SLIDE",SLIDE.rank)
  LDA(s,J,SLIDE.rank-1)
  PRINT(s,"SLIDE-1",J)
TEST_LDA = mkLABEL('TEST_LDA', label_TEST_LDA)

def label_TEST_DEPOSIT(s):
  LDA(s,I,AXE)
  PRINT(s,"IAXE",I)
  opSET(s,AXE,1)
  PRINT(s,"AXE1",AXE)
  DEPOSIT(s,I,2)
  PRINT(s,"AXE2",AXE)
TEST_DEPOSIT = mkLABEL('TEST_DEPOSIT', label_TEST_DEPOSIT)

def label_TEST_EVAL(s):
  opSET(s,AXE,2)
  PRINT(s,"AXE2",AXE)
  LDA(s,J,AXE)
  EVAL(s,I,J)
  PRINT(s,"I2",I)
TEST_EVAL = mkLABEL('TEST_EVAL', label_TEST_EVAL)

def label_TEST_RANDOM(s):
  RANDOM(s,I,10)
  PRINT(s,"RANDI",I)
  RANDOM(s,I,10)
  PRINT(s,"RANDI",I)
  RANDOM(s,J,LAST_CAMEO-CAMEO+1)
  PRINT(s,"RANDCAMEO",J)
  RANDOM(s,J,LAST_CAMEO-CAMEO+1)
  PRINT(s,"RANDCAMEO",J)
  opSET(s,SCULPTURE,12)
  RANDOM(s,SCULPTURE,get_value(s, SCULPTURE)-1)
  PRINT(s,"RANDSCUL",SCULPTURE)
  opSET(s,SCULPTURE,12)
  RANDOM(s,SCULPTURE,get_value(s, SCULPTURE)-1)
  PRINT(s,"RANDSCUL",SCULPTURE)
TEST_RANDOM = mkLABEL('TEST_RANDOM', label_TEST_RANDOM)

def label_TEST_ARITHMETICS(s):
  opSET(s,I,0)
  PRINT(s,"I0",I)
  ADD(s,I,12)
  PRINT(s,"I12",I)
  SUB(s,I,3)
  PRINT(s,"I9",I)
  DIVIDE(s,I,3)
  PRINT(s,"I3",I)
  MULT(s,I,2)
  PRINT(s,"I6",I)
  opSET(s,J,4)
  ADD(s,I,J)
  PRINT(s,"I10",I)
TEST_ARITHMETICS = mkLABEL('TEST_ARITHMETICS', label_TEST_ARITHMETICS)

def label_TEST_BITS(s):
  BIC(s,BEAR,LIT)
  BIS(s,BEAR,FREEBIE)
  PRINT(s,"BEARFREE",BEAR)
  if  ((((((((((((((( BITP(s,BEAR,FREEBIE) ))))))))))))))) :
    pass
  else:
    PRINT(s,"FAIL",0)
  if  ((((((((((((((( BITP(s,BEAR,LIT) ))))))))))))))) :
    PRINT(s,"FAIL",0)
  BIC(s,BEAR,FREEBIE)
  PRINT(s,"BEARFREE",BEAR)
  if  ((((((((((((((( BITP(s,BEAR,FREEBIE) ))))))))))))))) :
    PRINT(s,"FAIL",0)
  if  ((((((((((((((( BITP(s,BEAR,LIT) ))))))))))))))) :
    PRINT(s,"FAIL",0)
  LDA(s,I,BEAR)
  BIS(s,I,LIT)
  PRINT(s,"BEARLIT",BEAR)
  PRINT(s,"ILIT",I)
  if  ((((((((((((((( BITP(s,I,LIT) ))))))))))))))) :
    pass
  else:
    PRINT(s,"FAIL",0)
  BIS(s,I,FREEBIE)
  PRINT(s,"BEARLITFREE",BEAR)
  PRINT(s,"ILITFREE",I)
  BIC(s,I,LIT)
  if  ((((((((((((((( BITP(s,I,LIT) ))))))))))))))) :
    PRINT(s,"FAIL",0)
  if  ((((((((((((((( BITP(s,I,FREEBIE) ))))))))))))))) :
    pass
  else:
    PRINT(s,"FAIL",0)
  PRINT(s,"BEARFREE",BEAR)
  PRINT(s,"IFREE",I)
def label_TEST_STATUS(s):
    LDA(s,STATUS,1)
    if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
      pass
    else:
      PRINT(s,"FAIL",1)
    opSET(s,STATUS,2)
    if  ((((((((((((((( EQP(s,STATUS,2) ))))))))))))))) :
      pass
    else:
      PRINT(s,"FAIL",2)
    BIS(s,STATUS,FASTMODE)
    if  ((((((((((((((( BITP(s,STATUS,FASTMODE) ))))))))))))))) :
      pass
    else:
      PRINT(s,"FAIL",3)
    LDA(s,STATUS,1)
    if  ((((((((((((((( EQP(s,STATUS,1) ))))))))))))))) :
      pass
    else:
      PRINT(s,"FAIL",4)
    if  ((((((((((((((( BITP(s,STATUS,FASTMODE) ))))))))))))))) :
      pass
    else:
      PRINT(s,"FAIL",5)
def label_TEST_GOTO(s):
      opGOTO(s,SWOFCHASM)
      PRINT(s,"HERE",HERE)
      if  ((((((((((((((( ATP(s,SWOFCHASM) ))))))))))))))) :
        pass
      else:
        PRINT(s,"FAIL",1)
      if  ((((((((((((((( BITP(s,STATUS,MOVED) ))))))))))))))) :
        pass
      else:
        PRINT(s,"FAIL",2)
      BIC(s,STATUS,MOVED)
      opGOTO(s,SLOPING)
      if  ((((((((((((((( ATP(s,SLOPING) ))))))))))))))) :
        pass
      else:
        PRINT(s,"FAIL",3)
      LDA(s,I,SWOFCHASM)
      if  ((((((((((((((( EQP(s,I,THERE) ))))))))))))))) :
        pass
      else:
        PRINT(s,"FAIL",4)
      if  ((((((((((((((( BITP(s,STATUS,MOVED) ))))))))))))))) :
        pass
      else:
        PRINT(s,"FAIL",5)
def label_TEST_GOTO_BITS(s):
        BIS(s,ROAD,LIT)
        BIC(s,SLOPING,LIT)
        opGOTO(s,ROAD)
        if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
          pass
        else:
          PRINT(s,"FAIL",1)
        opGOTO(s,SLOPING)
        if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
          PRINT(s,"FAIL",1)
        opGOTO(s,ROAD)
        if  ((((((((((((((( BITP(s,HERE,LIT) ))))))))))))))) :
          pass
        else:
          PRINT(s,"FAIL",1)
def label_TEST_APPORT(s):
          APPORT(s,STALACTITE,STALACT)
          if  ((((((((((((((( LOCP(s,STALACTITE,STALACT) ))))))))))))))) :
            pass
          else:
            PRINT(s,"FAIL",1)
          APPORT(s,STALACTITE,ROAD)
          if  ((((((((((((((( LOCP(s,STALACTITE,STALACT) ))))))))))))))) :
            PRINT(s,"FAIL",2)
          if  ((((((((((((((( LOCP(s,STALACTITE,ROAD) ))))))))))))))) :
            pass
          else:
            PRINT(s,"FAIL",3)
          LDA(s,I,STALACTITE)
          if  ((((((((((((((( LOCP(s,STALACTITE,STALACT) ))))))))))))))) :
            PRINT(s,"FAIL",4)
          if  ((((((((((((((( LOCP(s,STALACTITE,ROAD) ))))))))))))))) :
            pass
          else:
            PRINT(s,"FAIL",5)
          APPORT(s,I,STALACT)
          if  ((((((((((((((( LOCP(s,STALACTITE,STALACT) ))))))))))))))) :
            pass
          else:
            PRINT(s,"FAIL",6)
          if  ((((((((((((((( LOCP(s,STALACTITE,ROAD) ))))))))))))))) :
            PRINT(s,"FAIL",7)
def label_TEST_ITOBJ(s):
            APPORT(s,SWORD,ROAD)
            if  ((((((((((((((( LOCP(s,SWORD,ROAD) ))))))))))))))) :
              pass
            else:
              PRINT(s,"FAIL",1)
            for o in all_objects:
              LDA(s, I, o)
              APPORT(s,I,LIMBO)
            if  ((((((((((((((( LOCP(s,SWORD,ROAD) ))))))))))))))) :
              PRINT(s,"FAIL",1)
            if  ((((((((((((((( LOCP(s,SWORD,LIMBO) ))))))))))))))) :
              pass
            else:
              PRINT(s,"FAIL",1)
def label_TEST_COND(s):
              LDA(s,I,1)
              if  ((((((((((((((( EQP(s,I,1) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",1)
              if  ((((((((((((((( GTP(s,I,0) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",2)
              if  ((((((((((((((( GEP(s,I,1) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",3)
              if  ((((((((((((((( GEP(s,I,2) ))))))))))))))) :
                PRINT(s,"FAIL",4)
              if  ((((((((((((((( LTP(s,I,2) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",5)
              if  ((((((((((((((( LEP(s,I,2) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",6)
              if  ((((((((((((((( LEP(s,I,1) ))))))))))))))) :
                pass
              else:
                PRINT(s,"FAIL",7)
              if  ((((((((((((((( LEP(s,I,0) ))))))))))))))) :
                PRINT(s,"FAIL",8)
TEST_COND = mkLABEL('TEST_COND', label_TEST_COND)

TEST_ITOBJ = mkLABEL('TEST_ITOBJ', label_TEST_ITOBJ)

TEST_APPORT = mkLABEL('TEST_APPORT', label_TEST_APPORT)

TEST_GOTO_BITS = mkLABEL('TEST_GOTO_BITS', label_TEST_GOTO_BITS)

TEST_GOTO = mkLABEL('TEST_GOTO', label_TEST_GOTO)

TEST_STATUS = mkLABEL('TEST_STATUS', label_TEST_STATUS)

TEST_BITS = mkLABEL('TEST_BITS', label_TEST_BITS)

