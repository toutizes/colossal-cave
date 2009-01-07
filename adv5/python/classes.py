import re

names = {}
callables = {}
all_objects = []
all_places = []
all_text = []

all_stuff = []

class Callable(object):
  def __init__(self, name, func):
    self.name = name
    self.functions = [func]
    all_stuff.append(self)

  def append(self, callable):
    self.functions += callable.functions

def record_callable(c):
  if callables.has_key(c.name):
    callables[c.name].append(c)
  else:
    callables[c.name] = c
  return c

def record_name(name, o):
  if names.has_key(name):
    raise Exception("Name already in use: %s" % name)
  names[name] = o

class Action(Callable):
  def __init__(self, name, func):
    Callable.__init__(self, name, func)
  def __str__(self):
    return "Action{%s}" %(self.name)

def mkACTION(name, func):
  return record_callable(Action(name, func))

class Label(Callable):
  def __init__(self, name, func):
    Callable.__init__(self, name, func)
  def __str__(self):
    return "Label{%s}" %(self.name)

def mkLABEL(name, func):
  return record_callable(Label(name, func))

class At(Callable):
  def __init__(self, name, func):
    Callable.__init__(self, name, func)
  def __str__(self):
    return "At{%s}" %(self.name)

def mkAT(name, func):
  return record_callable(At(name, func))

class Object(object):
  def __init__(self, name, states):
    self.name = name
    self.states = []
    for s in states:
      if s.startswith(">$<"):
        s = ""
      self.states.append(s)
    all_stuff.append(self)
  def __str__(self):
    return "Object{%s}" %(self.name)

def mkOBJECT(name, states):
  o = Object(name, [x.strip() for x in states])
  all_objects.append(o)
  record_name(name, o)
  return o

class Text(object):
  def __init__(self, value):
    self.value = value
    all_stuff.append(self)
  def __str__(self):
    return "Text{%s}" %(self.values[:12])

def mkTEXT(value):
  all_text.append(Text(value.strip()))
  return len(all_text) - 1

class Variable(object):
  def __init__(self, name):
    self.name = name
    all_stuff.append(self)
  def __str__(self):
    return "Variable{%s}" %(self.name)

def VARIABLE(name):
  return Variable(name)

class Special(object):
  def __init__(self, name):
    self.name = name
    all_stuff.append(self)
  def __str__(self):
    return "Special{%s}" %(self.name)

class Verb(object):
  def __init__(self, name, synonyms):
    self.name = name
    self.synonyms = synonyms
    all_stuff.append(self)
  def __str__(self):
    return "Verb{%s}" %(self.name)

def mkVERB(name, synonyms):
  v = Verb(name, [name] + synonyms)
  for s in v.synonyms:
    record_name(s, v)
  return v

class Badword(object):
  def __init__(self, name):
    self.name = name

def BADWORD(x):
  return Badword(x)

class Place(object):
  def __init__(self, name, short, long):
    self.name = name
    self.short = short
    self.long = long
    self.rank = len(all_stuff)
    all_stuff.append(self)
  def __str__(self):
    return "Place{%s}" %(self.name)

short_re = re.compile("\s*\>\*\< (short|ditto)\s*(\S+)?")
def get_place_desc(d, default):
  m = short_re.match(d)
  if not m:
    return d
  t = m.group(1)
  if t == "ditto":
    return default
  else:
    other_place_name = m.group(2).replace('.', '_')
    return names[other_place_name].short

def mkPLACE(name, descs):
  if len(descs) == 2:
    short = get_place_desc(descs[0], descs[0])
    long = get_place_desc(descs[1], descs[0])
    p = Place(name, short, long)
  else:
    p = Place(name, "", "")
  p.rank = len(all_places)
  all_places.append(p)
  record_name(name, p)
  return p

def mkSYNON(x, names):
  for n in names:
    record_name(n, x)

