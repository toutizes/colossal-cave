from classes import *
from vars import *
import random
import traceback
import sys

# Runtime

INHAND = mkPLACE("INHAND", ["In hand.", "In your steady hand."])
QUERY_REPLY = None

# These variable are special re: bits.  
# The bits are attached to the variable itself, not to its value.
STATUS = Special('STATUS')
# HERE = Special('HERE')
# THERE = Special('THERE')
ARG1 = Special('ARG1')
ARG2 = Special('ARG2')

rev_all_stuff = {}


class SavedState:
  def __init__(self, state, clear_output=True):
    if len(rev_all_stuff) == 0:
      for i in xrange(0, len(all_stuff)):
        rev_all_stuff[all_stuff[i]] = i
    self.continuation = self.o2k(state.continuation)
    self.values = self.o2kdict(state.values)
    self.locations = self.o2kdict(state.locations)
    self.bits = self.o2kdict(state.bits)
    self.exited = state.exited
    if clear_output:
      self.output = ''
    else:
      self.output = state.output

  def state(self):
    state = State(self.k2o(self.continuation))
    state.values = self.k2odict(self.values)
    state.locations = self.k2odict(self.locations)
    state.bits = self.k2odict(self.bits)
    state.exited = self.exited
    state.output = self.output
    return state

  def o2kdict(self, od):
    kd = {}
    for (k,v) in od.iteritems():
      kd[self.o2k(k)] = self.o2k(v)
    return kd

  def k2odict(self, kd):
    od = {}
    for (k,v) in kd.iteritems():
#      print self.k2o(k), self.k2o(v)
      od[self.k2o(k)] = self.k2o(v)
    return od

  def o2k(self, o):
    if type(o) == int:
      return (0, o)
    elif type(o) == str or type(o) == unicode:
      return (1, o)
    else:
      return (2, rev_all_stuff[o])

  def k2o(self, k):
    if k[0] == 0 or k[0] == 1:
      return k[1]
    else:
      return all_stuff[k[1]]

class State(object):
  def __init__(self, continuation):
    self.interactive = False
    self.continuation = continuation
    self.values = {}
    self.locations = {}
    self.input = ""
    self.input_words = []
    self.input_strings = []
    self.output = ""
    self.bits = {}
    self.exited = False

  def emit(self, text):
    if self.interactive:
      sys.stdout.write(text)
      sys.stdout.write("\n")
    else:
      self.output += text + "\n"

class Proceed(Exception):
  pass

class Quit(Exception):
  def __init__(self, continuation=None):
    self.continuation = continuation

class Stop(Exception):
  pass

def var_value(s, x):
  if type(x) == Variable or type(x) == Special:
    return s.values.get(x, 0)
  else:
    return x

def get_value(s, x):
  if type(x) == int:
    return x
  elif type(x) == Place:
    return x.rank
  elif type(x) == Object or type(x) == Special or type(x) == Action:
    return s.values.get(x, 0)
  elif type(x) == Variable:
    return get_value(s, s.values.get(x, 0))
  else:
    return x

def set_value(s, x, v):
  if type(x) == Object or type(x) == Place or \
     type(x) == Variable or type (x) == Special or \
     type(x) == Action:
    s.values[x] = v
  else:
    raise Exception(x)

def get_location(s, x):
  return s.locations.get(x, None)

def set_location(s, x, y):
  s.locations[x] = y

def special_value(s, x):
  if type(x) == Variable:
    return var_value(s, x)
  else:
    return x

def get_bits(s, x):
  return s.bits.get(special_value(s, x), 0)

def set_bits(s, x, y):
  s.bits[special_value(s, x)] = y

def get_text(s, v):
  if v == OK:
    return "OK"
  o = var_value(s, v)
  if type(o) == str or type(o) == unicode:
    return o
  if type(o) == int:
    return all_text[o].value
  elif type(o) == Object:
    if get_location(s, o) != INHAND:
      # Man, this is tricky!
      if v == ARG1:
        return s.input_strings[0]
      elif v == ARG2:
        return s.input_strings[1]
      else:
        val = get_value(s, o)
        if val + 1 < len(o.states):
          return o.states[val + 1]
        else:
          return ''
    else:
      return o.states[0]
  elif type(o) == Place:
    if BITP(s, STATUS, FULLDISP):
      return o.long
    elif BITP(s, STATUS, QUICKIE) and BITP(s, o, BEENHERE):
      return o.short
    elif BITP(s, STATUS, FASTMODE):
      return o.short
    else:
      return o.long
  elif type(o) == Verb:
    return o.name
  elif type(o) == Action:
    return o.name
  else:
    return "Unknown entry %s" % o
  
# Control flow
def opQUIT(s):
  raise Quit()

# Conditions
def BITP(s, x, y):
#  print 'bitp', x, y, (get_bits(s, x) & (1 << y)) != 0
  return (get_bits(s, x) & (1 << y)) != 0

def CHANCEP(s, chance):
  return get_value(s, chance) >= random.randint(0, 100)

def ATP(s, location):
#  print HERE, var_value(s, HERE), location, var_value(s, location)
  return var_value(s, location) == var_value(s, HERE)

def EQP(s, x, y):
  return get_value(s, x) == get_value(s, y)

def GEP(s, x, y):
  return get_value(s, x) >= get_value(s, y)

def GTP(s, x, y):
  return get_value(s, x) > get_value(s, y)

def HAVEP(s, x):
#  print 'havep', var_value(s, x), get_location(s, var_value(s, x))
  return get_location(s, var_value(s, x)) == INHAND

def KEYP(s, x):
  if type(x) == str:
    what = x
  else:
    what = x.name
  return what in s.input_strings

def LEP(s, x, y):
  return get_value(s, x) <= get_value(s, y)

def LOCP(s, x, y):
#  print 'LOCP', x, y, get_location(s, var_value(s, x)) == y
  return get_location(s, var_value(s, x)) == y

def LTP(s, x, y):
  return get_value(s, x) < get_value(s, y)

def NEARP(s, x):
  if HAVEP(s, x):
    return True
  return nearp(s, x)

def nearp(s, x):
  what = var_value(s, x)
  where = var_value(s, HERE)
  if get_location(s, what) == where:
    return True
  if BITP(s, what, SCHIZOID) and get_location(s, what).rank == where.rank - 1:
    return True
  return False

def QUERY(s, text, label):
#  print 'query', text, label.name
  opSAY(s, text)
  raise Quit(label)

# Opcodes
def ADD(s, x, y):
  set_value(s, x, get_value(s, x) + get_value(s, y))

def ANYOF(s, any_key):
  for key in any_key:
    if KEYP(s, key): return
  opPROCEED(s)

def APPORT(s, obj, location):
#  print 'APPORT', obj, var_value(s, obj), var_value(s, location)
  set_location(s, var_value(s, obj), var_value(s, location))

def AT(s, loc):
  if ATP(s, loc): return
  opPROCEED(s)

def BIC(s, x, y):
#  print 'bic', x, y, get_bits(s, x) & (~ (1 << y))
  set_bits(s, x, get_bits(s, x) & (~ (1 << y)))

def BIS(s, x, y):
  # print 'bis', x, y, get_bits(s, x) | (1 << y)
  set_bits(s, x, get_bits(s, x) | (1 << y))

def get_callable(x):
  if type(x) == Action or type(x) == At or type(x) == Label:
    return x
  if type(x) == Verb:
    for n in x.synonyms:
      what = callables.get(n, None)
      if what:
        return what
  if type(x) == Object:
    return callables.get(x.name, None)
  if type(x) == Place:
    return callables.get(x.name, None)
    

# Objects and verbs can has an action.
# Places can have a move.
def CALL(s, c):
#  print 'CALL', c, var_value(s, c), var_value(s, c).name, get_callable(var_value(s, c))
  what = get_callable(var_value(s, c))
  if not what:
    return
#  print "CALL", what.name
  for f in what.functions:
    try:
#      print 'CALLING', f
      f(s)
    except Proceed:
#      print 'PROCEED'
      continue

def DEFAULT(s, x):
  if len(s.input_words) != 1: return
  for o in all_objects:
    if nearp(s, o) and BITP(s, o, x):
      set_input_value(s, ARG1, o)
      LDA(s, STATUS, 2)
      s.input_words.append(o)
      s.input_strings.append(o.name)
      return

def DEPOSIT(s, x, y):
  set_value(s, var_value(s, x), get_value(s, y))

def DIVIDE(s, x, y):
  set_value(s, x, int(get_value(s, x) / get_value(s, y)))

def opDROP(s, x):
#  print x, get_location(s, var_value(s, x))
  set_location(s, var_value(s, x), var_value(s, HERE))
#  print x, get_location(s, var_value(s, x))

def EVAL(s, x, y):
  set_value(s, x, get_value(s, var_value(s, y)))

def opGET(s, x):
  set_location(s, var_value(s, x), INHAND)
  # Bit about negative values???

def opGOTO(s, location):
  where = var_value(s, location)
  LDA(s, THERE, HERE)
  LDA(s, HERE, where)
  BIS(s, STATUS, MOVED)
#  print "GOTO", var_value(s, location)
#  PRINT(s, "STATUS", STATUS)

def HAVE(s, x):
  if get_location(s, x) == INHAND:
    return
  opPROCEED(s)

nul_inputs = ["THE", "A", "IT", "AN", "THAT", "THIS", "TO"]
def INPUT(s, continuation):
  raise Quit(continuation)

def input_to_things(input):
  things = []
  for w in input.split():
    w = w.upper()
#    print 'w', names.has_key(w)
    if w in nul_inputs:
      continue
    if names.has_key(w):
      things.append(names[w])
    else:
      things.append(w)
    if len(things) == 2:
      break
  return things

def set_input_value(s, x, v):
  set_value(s, x, v)
#  PRINT(s,"x",x)
#  PRINT(s,"v",v)
  set_bits(s, x, get_bits(s, v))
#  PRINT(s,"x",x)
#  PRINT(s,"v",v)
  if type(v) == Object:
    BIS(s, x, OBJECT)
  elif type(v) == Place:
    BIS(s, x, PLACE)
  elif type(v) == Verb:
    BIS(s, x, VERB)
  else:
    BIS(s, x, BADWORD)
#  PRINT(s,"x",x)

def input_strings(input_words):
  strings = []
  for word in input_words:
    if type(word) == str or type(word) == unicode:
      strings.append(word)
    else:
      strings.append(word.name)
  return strings

def HAS_INPUT(s, input):
  things = input_to_things(input)
  LDA(s, STATUS, len(things))
  if len(things) == 0:
    return
  if len(things) >= 1:
    set_input_value(s, ARG1, things[0])
  if len(things) >= 2:
    set_input_value(s, ARG2, things[1])
  if type(things[0]) == Object:
    BIS(s, STATUS, OBJECT)
  elif type(things[0]) == Place:
    BIS(s, STATUS, PLACE)
  elif type(things[0]) == Verb:
    BIS(s, STATUS, VERB)
  else:
    BIS(s, STATUS, BADWORD)
  s.input_words = things
  s.input_strings = input_strings(things)
#  print things

def clear_input(s):
  LDA(s, STATUS, 0)
  set_input_value(s, ARG1, 0)
  set_input_value(s, ARG2, 0)
  BIC(s, STATUS, OBJECT)
  BIC(s, STATUS, PLACE)
  BIC(s, STATUS, VERB)
  BIC(s, STATUS, BADWORD)
  s.input_words = []
  s.input_strings = []

def KEYWORD(s, *words):
  for w in words:
    if not KEYP(s, w):
      opPROCEED(s)

def LDA(s, x, y):
  set_value(s, x, var_value(s, y))
  if type(x) == Special and type(y) != int:
    set_bits(s, x, get_bits(s, var_value(s, y)))

def LOCATE(s, x, y):
  set_value(s, x, get_location(s, var_value(y)))

def MOVE(s, command, location):
  if KEYP(s, command):
    opGOTO(s, location)
    QUIT(s)

def MULT(s, x, y):
  set_value(s, x, get_value(s, x) * get_value(s, y))

def NAME(s, x, y):
  # stuff about using the original word??
  s.emit(get_text(s, x).replace('#', '%(x)s') % {'x':get_text(s, y)})

def NEAR(s, x):
  if NEARP(s, x): return
  opPROCEED(s)

def opPROCEED(s):
#  traceback.print_stack()
  raise Proceed()

def QUIT(s):
#  traceback.print_stack()
  raise Quit()

def RANDOM(s, x, mod):
  mod_val = get_value(s, mod)
  if mod_val > 0:
    set_value(s, x, random.randint(0, 2000000000) % get_value(s, mod))

def REPLYP(s, ignore):
  if "Y" in s.input_words or "YES" in s.input_words:
    return True
  else:
    return False

def opSAY(s, x):
  s.emit(get_text(s, x))

def opSET(s, x, y):
  set_value(s, x, get_value(s, y))

def SMOVE(s, command, location, text):
  if KEYP(s, command):
    opGOTO(s, location)
    opSAY(s, text)
    opQUIT(s)

def opSTOP(s):
  s.exited = True
  raise Stop()

def SUB(s, x, y):
  set_value(s, x, get_value(s, x) - get_value(s, y))

def VALUE(s, x, y):
  s.emit(get_text(s, x).replace('#', '%(x)s') % {'x':get_value(s,y)})

def PRINT(s, t, x):
  print t,
  if type(x) == str or type(x) == unicode or type(x) == int:
    print x
  else:
    print "%s: var=%s, val=%s, bits=0x%04x" %(x, var_value(s, x), get_value(s, x), get_bits(s, x))

