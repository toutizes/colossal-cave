import sys
import re

op_map = {
  'SAY': 'opSAY',
  'QUIT': 'opQUIT',
  'SET': 'opSET',
  'DROP': 'opDROP',
  'GOTO': 'opGOTO',
  'PROCEED': 'opPROCEED',
  'GET': 'opGET',
  'STOP': 'opSTOP',
}
def func_op(op):
  return op_map.get(op, op)

class Done(Exception):
  pass

class State:
  input = sys.stdin
  depth = 0
  back = None

  def _no_comment(s, line):
    x = line.find("*")
    if x != -1:
      line = line[0:x]
    x = line.find("{")
    if x != -1:
      line = line[0:x]
    line = line.replace('.', '_')
    line = line.replace('!', '_')
    line = line.replace('?', '_')
    line = line.replace('&', '_')
    return line

  def raw_line(self):
    if self.back != None:
      line = self.back
      self.back = None
    else:
      line = self.input.readline()[:-1]
      if not line:
        raise Done()
    return line.replace("\r", "")

  def next_line(self):
    return self._no_comment(self.raw_line())

  def peek_line(self, re_x, raw=False):
    try:
      line = self.raw_line()
      self.back = line
      if raw:
        return re_x.match(line)
      else:
        return re_x.match(self._no_comment(line))
    except Done:
      return False

def prin_py(d, py):
  print " " * d + py,

def print_py(d, py):
  prin_py(d, py)
  print

def prin_cond(cond, param):
  if cond[0:2] == "IF":
    cond = cond[2:]
  print "%sP(s,%s)" % (cond, mkparams(param)),

comment_pattern = "\s*((\*|{).*)?$"
itobj_re = re.compile("\s*ITOBJ\s*(\S+)\s*" + comment_pattern)
itlist_re = re.compile("\s*ITLIST\s*(\S+)\s*" + comment_pattern)
itplace_re = re.compile("\s*ITPLACE\s*(\S+)\s*" + comment_pattern)
eoi_re = re.compile("\s*EOI\s*" + comment_pattern)
if_re = re.compile("\s*(IF\S*|BIT|CHANCE)\s*(\S+)"  + comment_pattern)
else_re = re.compile("\s*ELSE\s*" + comment_pattern)
cond_re = re.compile("\s*(AND|OR|EOR|NOT)\s*" + comment_pattern)
fin_re = re.compile("\s*FIN\s*" + comment_pattern)
anyof_re = re.compile("\s*ANYOF\s+(\S+)\s*" + comment_pattern)
op0_re = re.compile("\s*(\S+)\s*" + comment_pattern)
op1_re = re.compile("\s*(\S+)\s+(\S+)\s*" + comment_pattern)

at_param_re = re.compile("@([A-Z][A-Z0-9_]*)")
hat_param_re = re.compile("\\^([A-Z][A-Z0-9_]*)")
def mkparams(x):
  x = at_param_re.sub(r"get_value(s, \1)", x)
  x = hat_param_re.sub(r"\1.rank", x)
  return x

action_re = re.compile("^ACTION\s+(\S+)(\s+(\S+))?\s*" + comment_pattern)
label_re = re.compile("^LABEL\s+(\S+)\s*" + comment_pattern)
at_re = re.compile("^AT\s+(\S+)\s*" + comment_pattern)
text_re = re.compile("^TEXT(\s+(\S+)\s*)?" + comment_pattern)
object_re = re.compile("^OBJECT\s+(\S+)\s*" + comment_pattern)
place_re = re.compile("^PLACE\s+(\S+)\s*" + comment_pattern)
synon_re = re.compile("^SYNON\s+(\S+)\s*" + comment_pattern)
variable_re = re.compile("^VARIABLE\s+(\S+)\s*" + comment_pattern)
verb_re = re.compile("^VERB\s+(\S+)\s*" + comment_pattern)

next_re = re.compile("^[A-Z0-9.!]")

def compile_line(s):
  line = s.next_line()
  m = action_re.match(line)
  if m:
    compile_action(s, m.group(1), m.group(3))
    return
  m = label_re.match(line)
  if m:
    compile_label(s, m.group(1))
    return
  m = at_re.match(line)
  if m:
    compile_at(s, m.group(1))
    return
  m = text_re.match(line)
  if m:
    compile_text(s, m.group(2))
    return
  m = object_re.match(line)
  if m:
    compile_object(s, m.group(1))
    return
  m = place_re.match(line)
  if m:
    compile_place(s, m.group(1))
    return
  m = synon_re.match(line)
  if m:
    compile_synon(s, m.group(1))
    return
  m = variable_re.match(line)
  if m:
    compile_variable(s, m.group(1))
    return
  m = verb_re.match(line)
  if m:
    compile_verb(s, m.group(1))
    return
  m = itobj_re.match(line)
  if m:
    compile_itobj(s, m.group(1))
    return
  m = itlist_re.match(line)
  if m:
    compile_itlist(s, m.group(1))
    return
  m = itplace_re.match(line)
  if m:
    compile_itplace(s, m.group(1))
    return
  m = if_re.match(line)
  if m:
    prin_py(s.depth, "if ")
    print "("*15,
    prin_cond(m.group(1), m.group(2))
    compile_if(s)
    return
  m = anyof_re.match(line)
  if m:
    prin_py(s.depth, "ANYOF(s,[%s" % m.group(1))
    while True:
      m = s.peek_line(anyof_re)
      if m:
        print("," + m.group(1)),
        s.next_line()
      else:
        print "])"
        return
  m = op0_re.match(line)
  if m:
    print_py(s.depth, "%s(s)" % func_op(m.group(1)))
    return
  m = op1_re.match(line)
  if m:
    print_py(s.depth, "%s(s,%s)" % (func_op(m.group(1)), mkparams(m.group(2))))
    return
  if line:
    print_py(s.depth, "**** " + line)
    
def compile_if(s):
  connector = False
  to_close = 15
  while True:
    m = s.peek_line(cond_re)
    if m:
      connector = True
      print " %s " % m.group(1).lower(),
      s.next_line()
      continue
    m = s.peek_line(if_re)
    if not m:
      if connector:
        raise Exception("boolean cond without second if")
      else:
        break
    else:
      if not connector:
        break
      connector = False
      prin_cond(m.group(1), m.group(2))
      print ")",
      to_close -= 1
      s.next_line()
  print ")" * to_close,
  print ":"
  s.depth += 2
  m = s.peek_line(else_re)
  if m:
    print_py(s.depth, "pass")
  while True:
    m = s.peek_line(fin_re)
    if m:
      s.depth -= 2
      s.next_line()
      return
    m = s.peek_line(else_re)
    if m:
      print_py(s.depth - 2, "else:")
      s.next_line()
    compile_line(s)

actions = {}
def compile_action(s, name, filter):
  count = actions.get(name, 0)
  if count == 0:
    func = "action_%s" % name
    var = name
  else:
    func = "action_%s_%d" % (name, count + 1)
    var = "%s_%d" % (name, count + 1)
  actions[name] = count + 1
  print "def %s(s):" % func
  s.depth = s.depth + 2
  if filter:
    print_py(s.depth, "KEYWORD(s,%s)" % filter)
  try:
    while True:
      m = s.peek_line(next_re)
      if m:
        break
      compile_line(s)
  finally:
    s.depth = s.depth - 2
    print "%s = mkACTION('%s', %s)" % (var, name, func)
    print

labels = {}
def compile_label(s, name):
  count = labels.get(name, 0)
  if count == 0:
    func = "label_%s" % name
    var = name
  else:
    func = "labels_%s_%d" % (name, count + 1)
    var = "%s_%d" % (name, count + 1)
  labels[name] = count + 1
  print "def %s(s):" % func
  s.depth = s.depth + 2
  try:
    while True:
      m = s.peek_line(next_re)
      if m:
        break
      compile_line(s)
  finally:
    s.depth = s.depth - 2
    print "%s = mkLABEL('%s', %s)" % (var, name, func)
    print

ats = {}
def compile_at(s, name):
  count = ats.get(name, 0)
  func = "at_func_%s" % name
  var = "at_%s" % name
  if count > 0:
    func += "_%d" % count
    var += "_%d" % count
  ats[name] = count + 1
  print "def %s(s):" % func
  s.depth = s.depth + 2
  try:
    while True:
      m = s.peek_line(next_re)
      if m:
        break
      compile_line(s)
  finally:
    s.depth = s.depth - 2
    print "%s = mkAT('%s', %s)" % (var, name, func)
    print

def p(x):
  sys.stdout.write(x)

def compile_text_lines(s):
  lines = [[]]
  try:
    while True:
      m = s.peek_line(next_re, raw=True)
      if m:
        break
      line = s.raw_line()
      if line.startswith('*'):
        continue
      line = line[1:].replace("\"", "\\\"")
      if line.startswith('/'):
        line = line[1:]
      if line.startswith('%'):
        lines.append([line[1:]])
        continue
      lines[len(lines) - 1].append(line.strip())
  finally:
    for ll in lines:
      p("\"\"\"%s\"\"\",\n" % "\n".join(ll))

def compile_text(s, name):
  if name:
    p("%s = " % name)
  p("mkTEXT(")
  compile_text_lines(s)
  p(")\n")

def compile_object(s, name):
  p("%s = mkOBJECT(\"%s\", [" % (name, name))
  compile_text_lines(s)
  p("])\n")

def compile_place(s, name):
  p("%s = mkPLACE(\"%s\", [" % (name, name))
  compile_text_lines(s)
  p("])\n")

def compile_synon(s, args):
  x = args.split(',')
  print "mkSYNON(%s, %s)" %(x[0], x[1:])
  for s in x[1:]:
    print "%s = %s" % (s, x[0])

def compile_variable(s, args):
  for v in args.split(','):
    print "%s = VARIABLE('%s')" % (v, v)

def compile_verb(s, args):
  x = args.split(',')
  print "%s = mkVERB('%s', %s)" %(x[0], x[0], x[1:])
  for s in x[1:]:
    print "%s = %s" % (s, x[0])

def compile_itobj(s, var):
  print_py(s.depth, "for o in all_objects:")
  s.depth += 2
  print_py(s.depth, "LDA(s, %s, o)" % var)
  while True:
    m = s.peek_line(eoi_re)
    if m:
      s.next_line()
      s.depth -= 2
      return
    compile_line(s)

def compile_itlist(s, var):
  print_py(s.depth, "for o in all_objects:")
  s.depth += 2
  print_py(s.depth, "if not NEARP(s, o): continue")
  print_py(s.depth, "LDA(s, %s, o)" % var)
  while True:
    m = s.peek_line(eoi_re)
    if m:
      s.next_line()
      s.depth -= 2
      return
    compile_line(s)

def compile_itplace(s, var):
  print_py(s.depth, "for p in all_places:")
  s.depth += 2
  print_py(s.depth, "LDA(s, %s, p)" % var)
  while True:
    m = s.peek_line(eoi_re)
    if m:
      s.next_line()
      s.depth -= 2
      return
    compile_line(s)

def compile():
  s = State()
  try:
    while True:
      compile_line(s)
  except Done:
    pass

compile()
