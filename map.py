#!/usr/bin/python2.4
# Copyright 2008 Google Inc.
# Author: mdevin@google.com
#
# Dump the adventure map for dot.
import re, sys

int_string_re = re.compile('(-?\d+) *(.*)\n')
def read_int_string(input):
  line = input.readline()
  m = int_string_re.match(line)
  if not m:
    raise Exception, line
  return (int(m.group(1)), m.group(2))

def read_ints(input):
  l = input.readline()[:-1].split()
  return [int(x) for x in l]

def read_multilines(input):
  lines = {}
  while True:
    (index, line) = read_int_string(input)
    if index == -1:
      return lines
    if lines.has_key(index):
      lines[index] = lines[index] + ' ' + line
    else:
      lines[index] = line

def read_multiwords(input):
  words = {}
  while True:
    (index, word) = read_int_string(input)
    if index == -1:
      return words
    if words.has_key(index):
      words[index].append(word)
    else:
      words[index] = [word]

def read_paths(input):
  paths = {}
  while True:
    numbers = read_ints(input)
    if numbers[0] == -1:
      return paths
    start = numbers[0]
    path = numbers[1:]
    if paths.has_key(start):
      paths[start].append(path)
    else:
      paths[start] = [path]

rand_dests = [[6, 5], [9], [9, 8], [20, 15], [22, 14], [1000], [31], [32], [32], [32], [8, 9], [9, 8], [22, 13], [66, 71, 72], [66]]

class Room:
  def __init__(self, index, long, short, paths):
    self.index = index
    self.long = long
    if short:
      self.short = short
    else:
      self.short = long
    self.paths = paths

  def connect(self, rooms, verbs):
    paths = []
    if self.paths:
      for x in self.paths:
        if x[0] < 300:
          dests = [x[0]]
        else:
          dests = rand_dests[x[0]-300]
        paths.append([[rooms[d] for d in dests], [verbs[y] for y in x[1:]]])
    self.paths = paths
               
  def dump(self):
    print self.short
    print ' - ', self.long
    for p in self.paths:
      verbs = [x[0][0] for x in p[1:]]
      for dest in p[0]:
        print ', '.join(verbs), '->', dest.short
    print

class Map:
  def __init__(self, long, short, paths, verbs):
    rooms = {}
    for i,l in long.iteritems():
      if short.has_key(i):
        s = short[i]
      else:
        s = None
      if paths.has_key(i):
        p = paths[i]
      else:
        p = None
      rooms[i] = Room(i, l, s, p)
    for i,r in rooms.iteritems():
      r.connect(rooms, verbs)
    self.rooms = rooms

  def dump(self):
    for i,r in self.rooms.iteritems():
      r.dump()
    
def load():
  input = open('advdat31.dat')
  while True:
    kind = read_ints(input)[0]
    if kind == 1:
      long_descriptions = read_multilines(input)
      long_descriptions[1000] = 'THE END'
      long_descriptions[26] = 'ROOM 26'
    elif kind == 2:
      short_descriptions = read_multilines(input)
    elif kind == 3:
      paths = read_paths(input)
    elif kind == 4:
      verbs = read_multiwords(input)
      verbs[305] = ['ve305']
      verbs[1] = ['ve001']
    else:
      break
  map = Map(long_descriptions, short_descriptions, paths, verbs)
  map.dump()

load()
