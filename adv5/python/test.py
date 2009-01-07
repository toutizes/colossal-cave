import random, sys
from data import *
from adv import *

def main():
  s = State()
  keys = callables.keys()
  keys.sort()
  for k in keys:
    if k.startswith("TEST"):
      print k
      CALL(s, callables[k])
      print 
main()
