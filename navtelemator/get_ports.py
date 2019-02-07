import tmlookup
import json

dev = {}
for p in tmlookup.get_ports_all(''):
    if not p.Label:
        continue
    if p.End not in dev:
        dev[p.End] = {}
    if p.Card not in dev[p.End]:
        dev[p.End][p.Card] = {}
    if p.Label not in dev[p.End][p.Card]:
        dev[p.End][p.Card][p.Label] = {'ID': int(p.Port), 'Remark': p.Remark or ''}
    #print("{} {} {} {} {}".format(p.End, p.Card, p.Label, p.Remark or '', p.Port))
print(json.dumps(dev))
