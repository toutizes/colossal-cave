import re, sys
param_re = re.compile("^\s+[A-Z0-9]+\s*(\S+)")

params = {}

for line in sys.stdin.readlines():
  m =  param_re.match(line)
  if m:
    for p in m.group(1).split(',')[:1]:
      if params.has_key(p):
        params[p] = params[p] + 1
      else:
        params[p] = 1

keys = params.keys()
keys.sort()
for k in keys:
  print k, params[k]
