#!/usr/bin/python

import pickle, random, sys
from data import *
from adv import *

def step(s, input):
  if s.continuation != INITIAL:
    HAS_INPUT(s, input)
  while True:
#    print 'Step', s.continuation.name
    try:
      CALL(s, s.continuation)
    except Quit, e:
      if e.continuation:
        s.continuation = e.continuation
        return
      else:
        s.continuation = REPEAT
    else:
      return

def show_output(s):
  print s.output
  s.output = ''

def main():
  if len(sys.argv) > 1:
    ss = pickle.load(open(sys.argv[1]))
    s = ss.state()
#    print s.continuation
  else:
    s = State(INITIAL)
    step(s, None)
  try:
    while True:
#      print 'at:', var_value(s, HERE)
      show_output(s)
      if s.continuation == INPUT_IS_READY:
        print "> ",
      else:
        print "yes or no> ",
      step(s, sys.stdin.readline()[:-1])
      ss = SavedState(s)
      out = open("tmp.adv", "w")
      pickle.dump(ss, out)
      out.close()
  except Stop, e:
    show_output(s)

main()
