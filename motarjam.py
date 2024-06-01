from collections import OrderedDict 
# hala mikhaim yek motarjam online besazim :) komakam konid.
dicshenery=OrderedDict()
dicshenery={'hello': 'salam','goodbye': 'khodafez','say': 'goftan','we': 'ma','you': 'shoma'}
# hala jomlato vared kon
jomle=input('khobb  ')
c=[]
jomle=jomle.split()
for item in jomle:
    c.append(dicshenery.get(item,item))
    b=' '.join(c)
print(b)