import re,sys

decl_re = re.compile("^([A-Z]\S*)\s+(\S+)")

decls = {}
def add_decl(name, type):
    decl = decls.get(name, [])
    if not type in decl:
        decls[name] = decl + [type]

for l in sys.stdin.readlines():
    m = decl_re.match(l[:-1])
    if not m:
        continue
    type = m.group(1)
    names = m.group(2).split(',')
    for name in names:
        add_decl(name, type)


multis = {}

names = decls.keys()
names.sort()
for name in names:
    decl = decls[name]
    if len(decl) == 1:
        continue
    decl.sort()
    decl = ' '.join(decl)
    multis[decl] = multis.get(decl, []) + [name]

for (key, value) in multis.iteritems():
    print "%s: %d, %s" % (key, len(value), ' '.join(value))
