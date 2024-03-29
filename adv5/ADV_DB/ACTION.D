*
*	This module defines the actions to be taken when certain
*	verb, verb/object, or object/object word sequences are
*	spoken.  BEWARE:  When defining a set of alternate actions
*	to be taken for different uses of a word, you must ALWAYS
*	use the same definition of the word - do NOT define ANY
*	actions for the word's synonyms if any, or you will lose
*	some of your action controls!
*
ACTION	GET
	IFEQ  LAMP,0   {off? 
	   OR
	   NOT
	IFNEAR   LAMP  {missing the lamp?}
	   AND
	   NOT
	BIT   HERE,LIT {place is not illuminated}
	   CALL  GROPE.FOR.IT   {have to grope around for it}
	FIN
	DEFAULT   PORTABLE {hope this works!}
	ANYOF BIRD,CAGE,BOTTLE,OIL,WATER,CHAIN,BEAR,INVENTORY,CLAM
	ANYOF SWORD,SCEPTRE,KNIFE
	IFKEY BIRD
	   CALL GETBIRD
	ELSE
	   IFKEY CAGE
	      CALL  GETCAGE
	   ELSE
	      IFKEY BOTTLE
		 CALL  GETBOTTLE
	      ELSE
		 IFKEY OIL
		    CALL GETOIL
		 ELSE
		    IFKEY WATER
			CALL  GETWATER
		    ELSE
			IFKEY CHAIN
			  CALL  GETCHAIN
			ELSE
			  IFKEY BEAR
			     CALL  GETBEAR
			  ELSE
			     IFKEY INVENTORY
				CALL  INVENTORY
			     ELSE
				IFKEY SWORD
				   CALL  GETSWORD
				ELSE
				   IFKEY SCEPTRE
				      CALL  GETSCEPTRE
				   ELSE
				      IFKEY KNIFE
					 CALL  GETKNIFE
				      FIN
				   FIN
				FIN
			     FIN
			  FIN
			FIN
		    FIN
		 FIN
	      FIN
	   FIN
	FIN
* Generalized last-case "get" routine
ACTION	GET
	IFEQ  STATUS,1
	   PROCEED
	FIN
	BIT   ARG2,OBJECT
	ELSE
	   SAY   HAH!
	   QUIT
	FIN
	IFHAVE   ARG2
	   SAY   YOUHAVEIT
	   QUIT
	FIN
	IFNEAR   ARG2
	ELSE
	   NAME  IDONTSEE,ARG2
	   QUIT
	FIN
	BIT   ARG2,PORTABLE
	ELSE
	   SAY   HAH!
	   QUIT
	FIN
	IFLT  INVCT,STRENGTH
	   GET   ARG2
	   SAY   OK
	   BIT ARG2,UNSTABLE
	      EVAL  J,ARG2
	      IFEQ  J,0
		 DEPOSIT  ARG2,1
	      FIN
	   FIN
	ELSE
	   SAY   ARMSAREFULL
	FIN
	QUIT
ACTION	DROP
	ANYOF BIRD,CAGE,BOTTLE,OIL,WATER,VASE,VIAL,DJINN,BEAR
	IFKEY BIRD
	   CALL DROPBIRD
	ELSE
	   IFKEY CAGE
	      CALL  DROPCAGE
	   ELSE
	      IFKEY BOTTLE
		 CALL  DROPBOTTLE
	      ELSE
		 IFKEY OIL
		    OR
		 IFKEY WATER
		    CALL DROPLIQUID
		 ELSE
		    IFKEY VASE
			CALL  DROPVASE
		    ELSE
			IFKEY VIAL
			  CALL  DROPVIAL
			ELSE
			  IFKEY DJINN
			     CALL  FREEDJINN
			  ELSE
			     IFKEY BEAR
				CALL  DROPBEAR
			     FIN
			  FIN
			FIN
		    FIN
		 FIN
	      FIN
	   FIN
	FIN
	PROCEED
* Generalized "drop" control
ACTION	DROP
	IFEQ  STATUS,1
	   PROCEED
	FIN
	BIT   ARG2,OBJECT
	ELSE
	   SAY   HAH!
	   QUIT
	FIN
	IFHAVE   ARG2
	   DROP  ARG2
	   SAY   OK
	ELSE
	   SAY   NOTCARRYING
	FIN
	QUIT
ACTION	WALK
	IFEQ  STATUS,1
	   NAME  WHICHWAY,ARG1
	ELSE
	   IFKEY NORTH
	      OR
	   IFKEY SOUTH
	      OR
	   IFKEY EAST
	      OR
	   IFKEY WEST
	      OR
	   IFKEY NORTHEAST
	      OR
	   IFKEY NORTHWEST
	      OR
	   IFKEY SOUTHEAST
	      OR
	   IFKEY SOUTHWEST
	      OR
	   IFKEY UP
	      OR
	   IFKEY DOWN
	      OR
	   IFKEY BACK
	      OR
	   IFKEY CAVE
	      OR
	   IFKEY OUT
	      OR
	   IFKEY IN
	      CALL  ARG2
	   ELSE
	      BIT   ARG2,PLACE
		 IFAT  ARG2
		    SAY   NEEDDETAIL
		 ELSE
		    SAY   NO.CAN.GO
		 FIN
	      ELSE
		 SAY   HUH??
	      FIN
	   FIN
	FIN
	QUIT
ACTION	DIG
	SAY   NEEDSHOVEL
	QUIT
ACTION	CAVE
	AT VALLEY
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT FOREST
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT FOREST2
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT STREAM
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT ROAD
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT SLIT
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT DEPRESSION
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	AT BUILDING
	SAY   WHEREISCAVE
	QUIT
ACTION	CAVE
	SAY   NEEDDETAIL
	QUIT
ACTION	WATER DOOR
	IFNEAR   DOOR
	   IFHAVE   WATER
	      APPORT   WATER,LIMBO
	      SET   BOTTLE,1
	      SAY   HINGES..RUST
	      SET   DOOR,0
	   ELSE
	      NAME  YOUDONTHAVE,ARG1
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	OIL   DOOR
	IFNEAR   DOOR
	   IFHAVE   OIL
	      APPORT   OIL,LIMBO
	      SET   BOTTLE,1
	      SET   DOOR,1
	      SAY   OIL..DOOR
	   ELSE
	      NAME  YOUDONTHAVE,ARG1
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	WATER PLANT
	IFNEAR   PLANT
	   IFHAVE   WATER
	      APPORT   WATER,LIMBO
	      SET   BOTTLE,1
	      ADD   PLANT,1
	      SAY   PLANT
	      ADD   PLANT,1
	      IFEQ  PLANT,6
		 SET   PLANT,0
		 BIS   PLANT2,INVISIBLE
	      ELSE
		 BIC   PLANT2,INVISIBLE
	      FIN
	      GOTO  HERE
	      SET   PLANT2,PLANT
	   ELSE
	      NAME  YOUDONTHAVE,ARG1
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	OIL PLANT
	IFNEAR   PLANT
	   IFHAVE   OIL
	      APPORT   OIL,LIMBO
	      SET   BOTTLE,1
	      SAY   OIL..PLANT
	   ELSE
	      NAME  YOUDONTHAVE,ARG1
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	OIL
	IFEQ  STATUS,1
	   IFNEAR   BOTTLE
	      AND
	   IFEQ  BOTTLE,2
	      OR
	   IFHAVE   OIL
	      OR
	   IFAT  EASTPIT
	      NAME  WHAT.DO,ARG1
	   ELSE
	      NAME  IDONTSEE,ARG1
	   FIN
	ELSE
	   SAY   HAH!
	FIN
	QUIT
ACTION	WATER
	IFEQ  STATUS,1
	   IFNEAR   BOTTLE
	      AND
	   IFEQ  BOTTLE,0
	      OR
	   IFHAVE   WATER
	      OR
	   BIT   HERE,H20HERE
	      NAME  WHAT.DO,ARG1
	   ELSE
	      NAME  IDONTSEE,ARG1
	   FIN
	ELSE
	   SAY   HAH!
	FIN
	QUIT
ACTION	THROW
	ANYOF AXE,SWORD
	CALL  WEAPONRY
ACTION	THROW FOOD
	HAVE  FOOD
	IFNEAR   TROLL
	   SAY   FEED..TROLL
	ELSE
	   IFNEAR   DWARF
	      SAY   FED..DWARF
	      DROP  FOOD
	      BIS   DWARF,SPECIAL2 {enrage the dwarf}
	   ELSE
	      IFNEAR   BEAR
		 SAY   BEAR..URRP
		 APPORT   FOOD,LIMBO
		 SET   BEAR,1
		 IFEQ  AXE,1
		    SET   AXE,0
		 FIN
	      ELSE
		 PROCEED
	      FIN
	   FIN
	FIN
	QUIT
ACTION	THROW TEETH
	HAVE  TEETH
	SET   TEETH,0
	NEAR   GOBLINS
	SAY   WARRIORS
	APPORT   TEETH,LIMBO
	APPORT   GOBLINS,LIMBO
	QUIT
ACTION	THROW VIAL
	HAVE  VIAL
	CALL  BREAK.VIAL
ACTION	WAVE
	IFGT  STATUS,1
	   BIT   ARG2,OBJECT
	   ELSE
	      SAY   HAH!
	      QUIT
	   FIN
	   IFHAVE   ARG2
	   ELSE
	      SAY   NOTCARRYING
	      QUIT
	   FIN
	FIN
	IFKEY ROD
	   IFNEAR   FISSURE
	      IFLT  CLOSURE,2
		 ADD   FISSURE,1
		 SAY   FISSURE
		 IFEQ  FISSURE,2
		    SET   FISSURE,0
		    BIS   FISSURE,INVISIBLE
		 ELSE
		    BIC   FISSURE,INVISIBLE
		 FIN
	      ELSE
		 SAY   NOTHING
	      FIN
	   ELSE
	      IFNEAR   QUICKSAND
		 SAY   NOTHING.OBVIOUS
		 SET   QUICKSAND,1    {harden the quicksand for a while}
	      ELSE
		 IFNEAR   GORGE
		    AND
		 IFLT  CLOSURE,2
		    ADD   GORGE,1
		    SAY   GORGE
		    ADD   GORGE,1
		    IFEQ  GORGE,4
			SET   GORGE,0
			BIS   GORGE,INVISIBLE
		    ELSE
			BIC   GORGE,INVISIBLE
		    FIN
		 ELSE
		    SAY   NOTHING
		 FIN
	      FIN
	   FIN
	ELSE
	   IFKEY AXE
	      OR
	   IFKEY SWORD
	      CALL  WEAPONRY
	   ELSE
	      SAY   NOTHING
	   FIN
	FIN
	QUIT
* Generalized "throw" control
ACTION	THROW
	IFEQ  STATUS,2
	   BIT   ARG2,OBJECT {throwing objects}
	      IFHAVE   ARG2  {that you happen to be carrying}
		 AND         {in a place that things can be}
	      BIT   HERE,THROWER {thrown from, to someplace else}
		 CALL  UPCHUCK     {find the destination and print the message}
	      FIN
	   FIN
	FIN
	CALL  DROP
ACTION	NORTH
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	SOUTH
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	UP
	SAY   NOCANGO
	QUIT
ACTION	DOWN
	SAY   NOCANGO
	QUIT
ACTION	EAST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	WEST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	NORTHEAST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	NORTHWEST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	SOUTHEAST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	SOUTHWEST
	CALL  NO.MOVE.POSSIBLE
	QUIT
ACTION	INVENTORY
	SET   J,0
	ITOBJ I
	   IFHAVE   I
	      IFEQ  J,0
		 SAY   YOUNOWHAVE
		 SET   J,1
	      FIN
	      SAY   I
	   FIN
	EOI
	IFEQ  J,0
	   SAY   ARMSAREEMPTY
	FIN
	QUIT
ACTION	LOOK
	ANYOF MIST,TREES
	CALL  ARG2
ACTION	LOOK
	IFNEAR   LAMP
	   AND
	IFEQ  LAMP,1
	   OR
	BIT   HERE,LIT
	   SET   J,0
	   BIT   STATUS,FASTMODE
	   ELSE
	      BIS   STATUS,FULLDISP
	      SET   J,1
	   FIN
	   SAY   HERE
	   BIC   STATUS,FULLDISP
	   BIS   HERE,BEENHERE
	   ITLIST I
	      IFNEAR   I
		 AND
		 NOT
	      IFHAVE   I
		 IFEQ  J,1
		    AND
		    NOT
		 BIT   I,INVISIBLE
		    SET   J,0
		    SAY   BLANK
		 FIN
		 BIS   I,SEEN
		 SAY   I
	      FIN
	   EOI
	   IFNEAR   DWARF
	      IFEQ  DWARROWS,1
		 SAY   DWARFHERE
	      ELSE
		 VALUE DWARVESHERE,DWARROWS
	      FIN
	   FIN
	   IFHAVE   BEAR
	      SAY   I.C.A.BEAR
	   FIN
	ELSE
	   SAY   NOLIGHTHERE
	FIN
	QUIT
ACTION	LIGHT
	IFKEY LAMP
	   IFNEAR   LAMP
	      IFLT  LAMPLIFE,40
		 IFNEAR   BATTERIES
		    AND
		 IFEQ  BATTERIES,0
		    SAY   NEW.BATTERIES
		    SET   BATTERIES,1
		    ADD   LAMPLIFE,300
		    BIC   LAMP,SPECIAL1  {clear "recharged" flag}
		    BIC   LAMP,SPECIAL1  {clear "recharged already" flag}
		 FIN
	      FIN
	      IFGT  LAMPLIFE,0
		 SAY   LAMPNOWON
		 IFLT  LAMP,1
		    BIT   HERE,LIT
		    ELSE
			SET   LAMP,1
			CALL  LOOK
		    FIN
		 FIN
		 SET   LAMP,1
		 CALL  PHOG
	      ELSE
		 SAY   LAMP.IS.DEAD
	      FIN
	   ELSE
	      NAME  IDONTSEE,ARG2 { (is this right?) }
	   FIN
	ELSE
	   IFGT  STATUS,1
	      SAY   DUNNO.HOW
	   ELSE
	      IFNEAR   LAMP
	      IFLT  LAMPLIFE,40
		 IFNEAR   BATTERIES
		    IFEQ  BATTERIES,0
			SAY   NEW.BATTERIES
			SET   BATTERIES,1
			ADD   LAMPLIFE,300
			BIC   LAMP,SPECIAL1   {clear "recharged already" flag}
		    FIN
		 FIN
	      FIN
		 IFGT  LAMPLIFE,0
		    SAY   LAMPNOWON
		    SET   I,LAMP
		    SET   LAMP,1
		    CALL  PHOG
		    IFLT  I,1
			AND
			NOT
		    BIT   HERE,LIT
			CALL  LOOK
		    FIN
		 ELSE
		    SAY   LAMP.IS.DEAD
		 FIN
	      ELSE
		 SAY   NOLIGHTHERE
	      FIN
	   FIN
	FIN
	QUIT
ACTION	EXTINGUISH
	IFKEY LAMP
	   OR
	IFEQ  STATUS,1
	   IFNEAR   LAMP
	      SET   LAMP,0
	      SAY   LAMPNOWOFF
	      BIT   HERE,LIT
	      ELSE
		 SAY   ITISNOWDARK
	      FIN
	      CALL  PHOG
	   ELSE
	      IFKEY LAMP
		 NAME  IDONTSEE,ARG2
	      ELSE
		 PROCEED
	      FIN
	   FIN
	ELSE
	   SAY   DUNNO.HOW
	FIN
	QUIT
ACTION	OPEN
	DEFAULT  OPENABLE
	KEYWORD  GRATE
	NEAR   GRATE
	IFHAVE   KEYS
	   IFGT  CLOSURE,1
	      OR
	   BIT   ADMIN,NOMAGIC
	      SAY   GRATE.STUCK
	      IFGT  CLOSURE,1
		 BIS   ADMIN,PANICED
		 BIT   GRATE,SPECIAL1
		 ELSE
		    BIS   GRATE,SPECIAL1
		    SAY   GRATE.CLOSED
		 FIN
	      FIN
	   ELSE
	      SET   GRATE,1
	      SAY   GRATEUNLOCKED
	      BIC   DEPRESSION,HINTABLE
	   FIN
	ELSE
	   SAY   NEEDKEYS
	FIN
	QUIT
ACTION	OPEN  CHAIN
	NEAR   CHAIN
	IFHAVE   KEYS
	   IFEQ  CHAIN,0
	      SAY   CHAIN.UNLOCKED
	   ELSE
	      IFEQ  CHAIN,1
		 IFEQ  BEAR,0
		    SAY   BEAR..CHAIN
		 ELSE
		    SAY   CHAIN.UNLOCKED
		    SET   CHAIN,0
		    SET   BEAR,2
		 FIN
	      ELSE
		 SAY   CHAIN.UNLOCKED
		 SET   CHAIN,0
	      FIN
	   FIN
	ELSE
	   SAY   NEEDKEYS
	FIN
	QUIT
ACTION	OPEN DOOR
	NEAR   DOOR
	SAY   NOLOCK
	QUIT
ACTION	OPEN  KEYS
	SAY   UNLOCKKEYS
	QUIT
ACTION	OPEN  SAFE
	NEAR  SAFE
	IFEQ  SAFE,0
	   SAY   NO.KEYHOLE
	ELSE
	   IFEQ  SAFE,1
	      NAME  ALREADY.OPEN,ARG2
	   ELSE
	      SAY   IT.IS.MELTED
	   FIN
	FIN
	QUIT
ACTION	OPEN CLAM
	NEAR   CLAM
	IFHAVE   CLAM
	   SAY   DROP.THE.CLAM
	ELSE
	   IFHAVE   TRIDENT
	      APPORT   CLAM,LIMBO
	      APPORT   OYSTER,HERE
	      APPORT   PEARL,CULDESAC
	      SAY   CLAM..OPENED
	   ELSE
	      SAY   NEED.TRIDENT
	   FIN
	FIN
	QUIT
ACTION	OPEN OYSTER
	NEAR   OYSTER
	IFHAVE   OYSTER
	   SAY   DROP.THE.OYSTER
	ELSE
	   IFHAVE   TRIDENT
	      SAY   OYSTER..OPENED
	   ELSE
	      SAY   NEED.TRIDNT2
	   FIN
	FIN
	QUIT
ACTION	OPEN VIAL
	NEAR  VIAL
	CALL  BREAK.VIAL
ACTION	OPEN FLASK
	NEAR  FLASK
	IFLT  FLASK,2
	   IFLOC FLASK,PENTAGRAM
	      APPORT   DJINN,PENTAGRAM
	      SAY   POLITE.DJINN
	   ELSE
	      SAY   RUDE.DJINN
	   FIN
	   SET   FLASK,2
	ELSE
	   NAME  ALREADY.OPEN,ARG2
	FIN
	QUIT
* {weird case - opening a place!}
ACTION	OPEN PENTAGRAM
	IFAT  PENTAGRAM
	   IFNEAR   DJINN
	      SAY   DJINN.ADVICE
	      APPORT   DJINN,LIMBO
	      BIS   DJINN,SPECIAL1
	   ELSE
	      SAY   EMPTY.PENTA
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	CLOSE
	DEFAULT  OPENABLE
	KEYWORD  GRATE
	NEAR GRATE
	SET   GRATE,0
	SAY   GRATELOCKED
	QUIT
ACTION	CLOSE CHAIN
	NEAR   CHAIN
	IFAT  BEARHERE
	   IFEQ  CHAIN,0
	      IFNEAR   BEAR
		 DROP BEAR
		 SET   BEAR,1
		 SET   CHAIN,1
	      ELSE
		 SET   CHAIN,2
	      FIN
	   FIN
	   SAY   LOCK..CHAIN
	   IFHAVE   CHAIN
	      DROP  CHAIN
	   FIN
	ELSE
	   SAY   LOCK..CHAIN?
	FIN
	QUIT
ACTION	CLOSE DOOR
	NEAR   DOOR
	SAY   NOLOCK
	QUIT
ACTION	CLOSE SAFE
	NEAR  SAFE
	IFEQ  SAFE,1
	   SAY   SAFE.SHUTS
	   SET   SAFE,0
	ELSE
	   NAME  ALREADY.SHUT,ARG2
	FIN
	QUIT
ACTION	CLOSE FLASK
	NEAR  FLASK
	IFEQ  FLASK,0
	   NAME  ALREADY.SHUT,ARG2
	ELSE
	   NAME  DUNNO.HAO,ARG2
	FIN
	QUIT
ACTION	HELP
	BIT   HERE,HINTABLE	 { modification by K.C.W next 5 lines }
	   CALL HINT.LOGIC
	ELSE
	   SAY HELPDATA
	FIN
	QUIT
ACTION	INFO
	SAY   INFO.2
	QUIT
* ACTION	QUIT
* 	QUERY WANTTOQUIT
* 	   SET   QUITTING,1
* 	   CALL  FINIS
* 	FIN
* 	SAY   OK
* 	QUIT
ACTION	BRIEF
	SAY   BRIEF.OK
	BIS   STATUS,QUICKIE
	BIC   STATUS,FASTMODE
	LDA   OK,OK!
	QUIT
ACTION	LPSD
	IFEQ  STATUS,1
	   OR
	NOT
	BIT   ADMIN,OLORIN
	   SAY   WHAT?
	   QUIT
	FIN
	BIT   ARG2,PLACE
	   GOTO  ARG2
	ELSE
	   SAY   WHAT?
	FIN
	QUIT
ACTION	KILL
	DEFAULT  MORTAL      {find default enemy in one exists}
	ANYOF TROLL,DWARF,DRAGON,SNAKE,BIRD,BEAR,OYSTER,CLAM,OGRE,BLOB
	ANYOF DJINN,GOBLINS,BASILISK,GONG
	NEAR   ARG2
	IFKEY TROLL
	   CALL  KILLTROLL
	ELSE
	   IFKEY DWARF
	      CALL  KILLDWARF
	   ELSE
	      IFKEY DRAGON
		 CALL  KILLDRAGON
	      ELSE
		 IFKEY SNAKE
		    CALL  KILLSNAKE
		 ELSE
		    IFKEY BLOB
			CALL  KILLBLOB
		    ELSE
			IFKEY BEAR
			  CALL KILLBEAR
			ELSE
			  IFKEY CLAM
			     OR
			  IFKEY OYSTER
			     CALL  KILLBIVALVE
			  ELSE
			     IFKEY OGRE
				CALL  KILLOGRE
			     ELSE
				IFKEY BIRD
				   CALL  KILLBIRD
				ELSE
				   IFKEY DJINN
				      CALL  KILLDJINN
				   ELSE
				      IFKEY GOBLINS
					 CALL  KILLGOBLINS
				      ELSE
					 IFKEY BASILISK
					    CALL  KILLBASILISK
					 ELSE
					    IFKEY GONG
						CALL  HITGONG
					    FIN
					 FIN
				      FIN
				   FIN
				FIN
			     FIN
			  FIN
			FIN
		    FIN
		 FIN
	      FIN
	   FIN
	FIN
	QUIT
ACTION	KILL
	IFEQ  STATUS,1
	   SAY   PACIFIST
	   QUIT
	FIN
ACTION	FAST
	BIC   STATUS,QUICKIE
	BIS   STATUS,FASTMODE
	SAY   OK
	LDA   OK,SOK!
	QUIT
ACTION	FULL
	BIC   STATUS,QUICKIE
	BIC   STATUS,FASTMODE
	LDA   OK,OK!
	SAY   OK
	QUIT
ACTION	FEED
	ANYOF BEAR,TROLL,BIRD,SNAKE,DWARF,DRAGON,BASILISK,GOBLINS
	IFNEAR   ARG2
	   IFKEY BEAR
	      IFNEAR   FOOD
		 SAY   BEAR..URRP
		 SET   BEAR,1
		 IFHAVE   FOOD
		    APPORT   FOOD,LIMBO
		 FIN
		 IFEQ  AXE,1
		    SET   AXE,0
		 FIN
	      ELSE
		 SAY   SNAKEWONTEAT
	      FIN
	   ELSE
	      IFKEY TROLL
		 SAY   FEED..TROLL
	      ELSE
		 IFKEY SNAKE
		    IFHAVE   BIRD
			SAY   SNAKE..BIRD
			APPORT   BIRD,LIMBO
		    ELSE
			SAY   SNAKEWONTEAT
		    FIN
		 ELSE
		    IFKEY DWARF
			SAY   FED..DWARF
			BIS   DWARF,SPECIAL2 {makes him mad}
		    ELSE
			IFKEY BIRD
			  SAY   BIRDSEED
			ELSE
			  IFKEY DRAGON
			     IFEQ  DRAGON,0
				SAY   SNAKEWONTEAT
			     ELSE
				SAY   IT.IS.DEAD
			     FIN
			  ELSE
			     IFKEY BASILISK
				IFLT  BASILISK,2
				   SAY   SNAKEWONTEAT
				ELSE
				   SAY   IT.IS.DEAD
				FIN
			     ELSE
				IFKEY GOBLINS
				   SAY   GOBL.EAT.YOU
				FIN
			     FIN
			  FIN
			FIN
		    FIN
		 FIN
	      FIN
	   FIN
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	FEED
	IFEQ  STATUS,1
	   SAY   HUH??
	ELSE
	   SAY   HAH!
	FIN
	QUIT
ACTION	SCORE
	SET   QUITTING,1
	CALL  GETSCORE
	VALUE IFYOUQUIT,SCOREX
	VALUE IFYOUQUIT2,MAXSCORE
* 	QUERY WANTTOQUIT
* 	   SAY   OK
* 	   CALL  FINIS
* 	ELSE
* 	   SAY   OK
* 	FIN
	QUIT
ACTION	JUMP
	SAY   NOJUMPING
	QUIT
ACTION	IN
	SAY   INFROMOUT
	QUIT
ACTION	OUT
	SAY   INFROMOUT
	QUIT
ACTION	ABRA
	SAY   MAGICKWORD
	QUIT
ACTION	FEE
	ANYOF FIE,FOE,FOO,FUM
	SET   FOOBAR,0
	SAY   NOTHING
	QUIT
ACTION	FEE
	SET   FOOBAR,1
	SAY   OK
	QUIT
ACTION	FIE
	IFEQ  FOOBAR,0
	   SET   FOOBAR,2
	   SAY   OK
	ELSE
	   SET   FOOBAR,0
	   SAY   NOTHING
	FIN
	QUIT
ACTION	FOE
	IFEQ  FOOBAR,1
	   SET   FOOBAR,3
	   SAY   OK
	ELSE
	   SET   FOOBAR,0
	   SAY   NOTHING
	FIN
	QUIT
ACTION	FOO
	IFEQ  FOOBAR,2
	   IFLOC EGGS,GIANT
	      OR
	   IFLOC EGGS,YLEM   {threw 'em into the chasm}
	      SAY   NOTHING
	   ELSE
	      IFNEAR   EGGS
		 SET   EGGS,1
	      ELSE
		 IFAT  GIANT
		    SET   EGGS,0
		 ELSE
		    SET   EGGS,2
		 FIN
	      FIN
	      IFHAVE   EGGS
		 DROP  EGGS
	      FIN
	      SAY   EGGS
	      SET   EGGS,0
	      IFLOC EGGS,LIMBO  {if the eggs were given in toll}
		 BIS   TROLL,SPECIAL1    {can't be fooled twice}
		 IFEQ  TROLL,1  {bought off, not crossed}
		    OR
		 IFEQ  TROLL,2  {bought off, crossed}
		    IFNEAR   TROLL2   {at the chasm with a good bridge}
			SET   TROLL,5  {irate}
			SAY   TROLL    {bitch, bitch!}
		    FIN
		    SET   TROLL,0     {normal troll mode}
		    APPORT   TROLL,SWOFCHASM   {fetch him back}
		    APPORT   TROLL2,LIMBO      {discard fake troll}
		 FIN
	      FIN
	      APPORT   EGGS,GIANT
	   FIN
	ELSE
	   SAY   NOTHING
	FIN
	SET   FOOBAR,0
	QUIT
ACTION	FUM
	SET   FOOBAR,0
	SAY   NOTHING
	QUIT
ACTION	XYZZY
	SAY   NOTHING
	QUIT
ACTION	PLUGH
	SAY   NOTHING
	QUIT
ACTION	FIND  CAVE
	BIT   HERE,NOTINCAVE
	   AND
	   NOT
	BIT   INCAVE,BEENHERE
	   SAY   WHEREISCAVE
	ELSE
	   SAY   NEEDDETAIL
	FIN
	QUIT
ACTION	FIND
	IFGT  STATUS,1
	   BIT   ARG2,OBJECT
	      IFNEAR   ARG2
		 IFHAVE   ARG2
		    SAY   ITISHERENOW
		 ELSE
		    SAY   HERESOMEWHERE
		 FIN
	      ELSE
		 SAY   CANTFIND
	      FIN
	      QUIT
	   ELSE
	      BIT   ARG2,PLACE
		 IFAT  ARG2
		    SAY   YOU.ARE.THERE
		 ELSE
		    SAY   CANTFIND
		 FIN
	      ELSE
		 SAY   WHAT?
	      FIN
	      QUIT
	   FIN
	FIN
ACTION	SWIM
	SAY   DUNNO.HOW
	QUIT
ACTION	BREAK VASE
	NEAR  VASE
	SAY   THROW.VASE
	IFHAVE   VASE
	   APPORT   VASE,LIMBO
	   APPORT   SHARDS,HERE
	FIN
	QUIT
ACTION	BREAK VIAL
	NEAR  VIAL
	CALL  BREAK.VIAL
ACTION	FIX   VASE
	NEAR  POTTERY
	SAY   NO.CAN.FIX
	QUIT
ACTION	FILL VASE
	NEAR  VASE
	BIT   HERE,H20HERE
	   OR
	IFAT  EASTPIT
	   SAY   SHATTER.VASE
	   IFHAVE   VASE
	     APPORT   VASE,LIMBO
	     APPORT   SHARDS,HERE
	   FIN
	ELSE
	   SAY   NOTHING.VASE
	FIN
	QUIT
ACTION	FILL BOTTLE
	NEAR  BOTTLE
	IFEQ  BOTTLE,1
	   BIT   HERE,H20HERE
	      SAY   BOTTLE..H20
	      SET   BOTTLE,0
	      IFHAVE   BOTTLE
		 GET   WATER
	      FIN
	   ELSE
	      IFAT  EASTPIT
		 SAY   BOTTLE..OIL
		 SET   BOTTLE,2
		 IFHAVE   BOTTLE
		    GET   OIL
		 FIN
	      ELSE
		 SAY   NOTHING2FILL
	      FIN
	   FIN
	ELSE
	   SAY   BOTTLEWASFULL
	FIN
	QUIT
ACTION	FILL
	IFGT  STATUS,1
	   SAY   CANTFILLTHAT
	   QUIT
	FIN
ACTION	POUR WATER
	IFHAVE   WATER
	   APPORT   WATER,LIMBO
	   SET   BOTTLE,1
	   IFNEAR   PLANT
	      ADD   PLANT,1
	      SAY   PLANT
	      ADD   PLANT,1
	      IFEQ  PLANT,6
		 SET   PLANT,0
		 BIS   PLANT2,INVISIBLE
	      ELSE
		 BIC   PLANT2,INVISIBLE
	      FIN
	      GOTO  HERE
	      SET   PLANT2,PLANT
	   ELSE
	      IFNEAR   DOOR
		 SAY   HINGES..RUST
		 SET   DOOR,0
	      ELSE
		 SAY   POURWATER
	      FIN
	   FIN
	ELSE
	   NAME  YOUDONTHAVE,WATER
	FIN
	QUIT
ACTION	POUR OIL
	IFHAVE   OIL
	   APPORT   OIL,LIMBO
	   SET   BOTTLE,1
	   IFNEAR   PLANT
	      SAY   OIL..PLANT
	   ELSE
	      IFNEAR   DOOR
		 SAY   OIL..DOOR
		 SET   DOOR,1
	      ELSE
		 SAY   POURWATER
	      FIN
	   FIN
	ELSE
	   NAME  YOUDONTHAVE,ARG2
	FIN
	QUIT
ACTION	PLACATE
	ANYOF DWARF,SNAKE,BIRD,DRAGON,TROLL,BEAR,PIRATE,OGRE,BASILISK,GOBLINS
	NEAR  ARG2
	SAY   IAMGAME
	QUIT
ACTION	EAT
	DEFAULT  EDIBLE
	NEAR  MUSHROOM
	IFEQ  STATUS,1
	   OR
	IFKEY MUSHROOM
	   IFHAVE   MUSHROOM
	      DROP  MUSHROOM
	   FIN
	   SET   MUSHROOM,2
	   SAY   MUSHROOM
	   SET   MUSHTIME,30
	   ADD   MUSHTIME,LASTCLOCK
	   APPORT   MUSHROOM,LIMBO
	   SET   STRENGTH,12
	   QUIT
	FIN
ACTION	EAT
	NEAR   FOOD
	IFEQ  STATUS,1
	   OR
	IFKEY FOOD
	   IFHAVE   FOOD
	     APPORT   FOOD,LIMBO
	   FIN
	   SAY   URRP
	   QUIT
	FIN
ACTION	EAT
	ANYOF DWARF,DRAGON,BIRD,SNAKE,BEAR,TROLL,PLANT,OGRE
	ANYOF BASILISK,GOBLINS
	IFNEAR   ARG2
	   SAY   BLEAH
	ELSE
	   NAME  IDONTSEE,ARG2
	FIN
	QUIT
ACTION	EAT
	IFEQ  STATUS,1
	   SAY   NO.FOOD
	   QUIT
	ELSE
	   BIT   ARG2,OBJECT
	      IFNEAR   ARG2
		 SAY   REPULSIVE
		 QUIT
	      FIN
	   FIN
	FIN
ACTION	RUB   LAMP
	NEAR  LAMP
	NAME  RUBLAMP,ARG2
	QUIT
ACTION	RUB
	IFGT  STATUS,1
	   BIT   ARG2,OBJECT
	      IFNEAR   ARG2
		 SAY   PECULIAR
		 QUIT
	      FIN
	   FIN
	FIN
ACTION	BACK
	BIT   HERE,NOBACK
	   OR
	BIT   THERE,NOBACK
	   OR
	IFEQ  THERE,0
	   SAY   CANTGOBACK
	ELSE
	   GOTO  THERE
	FIN
	QUIT
ACTION	MIST
	SAY   THISISMIST
	QUIT
ACTION	TREES	{ Bug fix. Add TREES routine Jim 6/12/85 }
	BIT HERE,NOTINCAVE	{ Can see trees anywhere above ground }
	   SAY INFOREST
	ELSE
	   SAY NO.TREES.HERE
	FIN
	QUIT
ACTION	SAY
	ANYOF PLUGH,XYZZY,PLOVER,THURB,MELENKURION,NOSIDE,SAMOHT
	ANYOF KNERL,ZORTON,KLAETU,SNOEZE,BLERBI,PHUGGG
	CALL  ARG2
	QUIT
ACTION	SAY
	IFEQ  STATUS,2
	   QUIT
	FIN
* ACTION	SAVE
* 	BIT   ADMIN,DEMO
* 	   SAY   SUSP.DEMO
* 	ELSE
* 	   SET   I,1
* 	   BIT   ADMIN,OLORIN
* 	   ELSE
* 	      VALUE MUSTWAIT,MINTIME
* 	      QUERY IS.THIS.OK?
* 	      ELSE
* 		 SET   I,0
* 	      FIN
* 	   FIN
* 	   IFGT  I,0
* 	      SVAR  4,TIME
* 	      MULT  TIME,60
* 	      SVAR  5,I
* 	      ADD   TIME,I
* 	      EXECUTIVE   1,I      {save program image}
* 	      IFEQ  I,0
* 		 BIT   ADMIN,OLORIN
* 		    QUERY CONTINUE.NOW?
* 			SAY   OK
* 			SAY   BLANK
* 			QUIT
* 		    FIN
* 		 FIN
* 		 SAY   OK
* 		 SAY   BLANK
* 		 STOP
* 	      ELSE
* 		 SAY   CANT.SAVE
* 	      FIN
* 	   ELSE
* 	      SAY   OK
* 	   FIN
* 	FIN
* 	QUIT
* ACTION	RESTORE
* 	EXECUTE  5,I      {get prime-time factor}
* 	IFGT  I,0      {if something forbids adventures}
* 	   BIT   ADMIN,OLORIN
* 	   ELSE
* 	      LDA   J,RESTORE.PRIME-1
* 	      ADD   J,I
* 	      SAY   J
* 	      QUIT
* 	   FIN
* 	FIN
* 	BIT   ADMIN,OLORIN
* 	   SET   I,1
* 	ELSE
* 	   SET   I,0
* 	FIN
* 	EXECUTIVE 7,I  {save value of I over RESTORE attempt}
* 	EXECUTE  2,I      {attempt to restore image}
* 	IFEQ  I,0         {all well}
* 	   SVAR  4,I      {get hours}
* 	   SVAR  5,J      {get minutes}
* 	   MULT  I,60
* 	   ADD   I,J
* 	   IFLT  I,TIME
* 	      ADD   I,720
* 	      ADD   I,720    {1440 is too big}
* 	   FIN
* 	   SUB   I,TIME
* 	   EXECUTIVE   8,J   {restore pushed value}
* 	   IFEQ  J,1
* 	      BIS   ADMIN,OLORIN
* 	   ELSE
* 	      BIC   ADMIN,OLORIN
* 	   FIN
* 	   BIT   ADMIN,OLORIN {if he's a wizard}
* 	      OR
* 	   IFGT  I,MINTIME
* 	      IFEQ  LAMP,1   {if the lamp is on}
* 		 ADD   LAMPLIFE,1  {compensate for following move}
* 	      FIN
* 	      BIT   ADMIN,OLORIN  {if we're a wizard}
* 		 QUERY SAVE.THE.IMAGE
* 		 ELSE
* 		    EXECUTIVE   3,I   {flush the image}
* 		 FIN
* 	      ELSE
* 		 EXECUTIVE   3,I      {flush user-mode image}
* 	      FIN
* 	      EXECUTIVE   4,I   {flush the cache out}
* 	      GOTO  HERE
* 	      SAY   OK
* 	      SAY   BLANK
* 	   ELSE
* 	      VALUE TOO.SOON,MINTIME
* 	      SAY   BLANK
* 	      STOP     {must stop - we already did the restore!}
* 	   FIN
* 	ELSE
* 	   IFEQ  I,1   {no file, or no image}
* 	      SAY   NO.IMAGE
* 	      SUB   TURNS,1  {let him try again}
* 	   ELSE     {response 2 = checksum failed!}
* 	      SAY   EXPLOSION   {well-house blew up}
* 	      EXECUTE  3,I      {delete the record}
* 	   FIN
* 	FIN
* 	QUIT
ACTION	DRINK
	IFEQ  STATUS,1
	   OR
	IFKEY WATER
	   BIT   HERE,H20HERE
	      SAY   SLURP
	      QUIT
	   ELSE
	      IFNEAR   BOTTLE
		 AND
	      IFEQ  BOTTLE,0
		 SAY   WATERGONE
		 APPORT   WATER,LIMBO
		 SET   BOTTLE,1
		 QUIT
	      FIN
	   FIN
	   IFKEY WATER
	      NAME  IDONTSEE,ARG2
	   ELSE
	      SAY   CANTDRINK
	   FIN
	ELSE
	   BIT   ARG2,OBJECT
	      IFNEAR   ARG2
		 SAY   HAH!
	      ELSE
		 NAME  IDONTSEE,ARG2
	      FIN
	   ELSE
	      SAY   HAH!
	   FIN
	FIN
	QUIT
ACTION	NEWS
	SAY   NEWSDATA
	QUIT
ACTION	READ
	IFGT  STATUS,1
	   BIT   ARG2,OBJECT
	      IFNEAR   ARG2
		 IFKEY    MAGAZINES
		    CALL  READ.MAGAZINES
		 ELSE
		    IFKEY    MESSAGE
			CALL  READ.MESSAGE
		    ELSE
			IFKEY    TABLET
			  CALL  READ.TABLET
			ELSE
			  NAME  DUNNO.HAO,ARG1
			FIN
		    FIN
		 FIN
	      ELSE
		 NAME  IDONTSEE,ARG2
	      FIN
	   ELSE
	      SAY   HAH!
	   FIN
	ELSE
	   PROCEED
	FIN
	QUIT
ACTION	HOURS
	SAY   HOURS.ARE
	EXECUTIVE   6,I
	QUIT
* ACTION	WIZARD
* 	QUERY R.U.A.WIZARD?
* 	   SAY   PROVE.IT
* 	   INPUT
* 	   SET   I,1      {sense switch number}
* 	   SVAR  8,I      {read sense switch 1}
* 	   IFEQ  I,1
* 	      AND
* 	   IFKEY SLIME
* 	      SAY   SO.YOU.ARE
* 	      BIC   ADMIN,DEMO
* 	      BIS   ADMIN,OLORIN
* 	   ELSE
* 	      SAY   OH.POOH
* 	      ADD   PENALTIES,10
* 	   FIN
* 	ELSE
* 	   SAY   OK
* 	FIN
* 	QUIT
ACTION	CLIMB
	SAY   NOCANCLIMB
	QUIT
ACTION	LOST
	SAY   IMCONFUSED
	QUIT
ACTION	MELENKURION
	IFNEAR   STATUE
	   AND
	IFEQ  STATUE,0
	   SET   STATUE,1
	   SAY   CRUMBLE
	ELSE
	   SAY   NOTHING
	FIN
	QUIT
ACTION	NOSIDE SAMOHT
	BIT   LAMP,SPECIAL1
	   OR
	BIT   HERE,LIT
	   OR
	   NOT
	BIT   LAIR,BEENHERE
	   OR
	   NOT
	IFNEAR   LAMP
	   SAY   NOTHING
	ELSE
	   IFHAVE   LAMP
	      SAY   FZAP
	      CALL  CORONER
	   ELSE
	      IFGT  LAMPLIFE,40
		 APPORT   LAMP,YLEM
		 SET   BATTERIES,1    {so lamp doesn't come back}
		 SET   LAMP,0
		 SET   LAMPLIFE,0
		 CHANCE   50
		    SAY   LAMP.GOES.POOF
		    SAY   ITISNOWDARK
		 ELSE
		    SAY   LAMP.EXPLODES
		    CALL  CORONER
		 FIN
	      ELSE
		 SAY   LAMP.RECHARGED
		 ADD   LAMPLIFE,150
		 SET   LAMP,1
		 BIS   LAMP,SPECIAL1
	      FIN
	   FIN
	FIN
	QUIT
ACTION	NOSIDE
	SAY   NOTHING
	QUIT
ACTION	SAMOHT
	SAY   NOTHING
	QUIT
ACTION	THURB
	SAY   NOTHING
	QUIT
ACTION	KNERL
	CALL  PASSPHRASE
ACTION	ZORTON
	CALL  PASSPHRASE
ACTION	KLAETU
	CALL  PASSPHRASE
ACTION	SNOEZE
	CALL  PASSPHRASE
ACTION	BLERBI
	CALL  PASSPHRASE
ACTION	RIDE
	IFEQ  STATUS,1
	   OR
	IFKEY TURTLE
	   AND
	IFNEAR   TURTLE
	   SAY   TURTLE.BACK
	   GOTO  RESERVOIR
	   APPORT   TURTLE,LIMBO
	   QUIT
	FIN
ACTION	PHUGGG
	BIS   DJINN,SPECIAL2    {he needn't tell us about it}
	BIT   HERE,NOTINCAVE
	   SAY   NOTHING
	ELSE
	   IFNEAR   BOTTLE
	      AND
	   IFEQ  BOTTLE,0
	      OR
	   BIT   HERE,H20HERE
	      CHANCE   85
		 SAY   NOTHING
	      ELSE
		 CHANCE   95
		    SAY   JELLYFISH
		    CALL  CORONER
		 ELSE
		    SAY   CAVE.DESTROYED
		    STOP
		 FIN
	      FIN
	   ELSE
	      IFNEAR   AXE
		 OR
	      IFNEAR   SWORD
		 IFNEAR   AXE
		    SAY   ZOT.AXE
		    IFHAVE   AXE
		       APPORT   AXE,LIMBO
		    FIN
		 FIN
		 IFNEAR   SWORD
		    SAY   ZOT.SWORD
		    IFHAVE   SWORD
		       APPORT   SWORD,LIMBO
		    FIN
		 FIN
	      ELSE
		 RANDOM   I,3
		 MULT  I,2
		 IFGT  DWARROWS,1
		    ADD   I,1
		 FIN
		 IFNEAR   DWARF
		    CHANCE   70
			LDA   J,IT.WORKED
			ADD   I,J
			SAY   I
			APPORT   DWARF,LIMBO
			SUB   DWARFCOUNT,DWARROWS
			SET   DWARROWS,0
		    ELSE
			LDA   J,IT.DIDNT.WORK
			ADD   I,J
			SAY   I
			CALL  CORONER
		    FIN
		 ELSE
		    SAY   NOTHING
		 FIN
	      FIN
	   FIN
	FIN
	QUIT
