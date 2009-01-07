#!/bin/bash -eu
compile() {
  echo "from classes import *"
  echo "from adv import *"
  cat $* | python compile.py
}

d=../ADV_DB

compile $d/PLACE.D $d/OBJECTS.D $d/OBJSYN.D $d/VERBS.D $d/TEXT.D $d/LABELS.D \
        $d/MOVES.D $d/ACTION.D $d/INIT.D $d/REPEAT.D $d/TEST.D > data.py

compile $d/BITS.D $d/VARS.D > vars.py
