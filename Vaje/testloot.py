__author__ = 'obi'
import lootgen, math

gozd = []
mesto = []
brune = []
sef = []
medbox = []

def procenti(list):
    crap = list.count(0)
    print crap
    goods = list.count(1)
    print goods
    weapons = list.count(2)
    print weapons
    events = list.count(3)
    print events
    aid = list.count(5)
    print aid
    sumall = crap + goods + weapons + events + aid
    prcrap = (100 / float(sumall)) * float(crap)
    prgoods = (100 / sumall) * float(goods)
    prweapons = (100 / sumall) * float(weapons)
    prevents = (100 / sumall) * float(events)
    praid = (100 / sumall) * float(aid)
    return prcrap, prgoods, prweapons, prevents, praid

mod = input("Mod: ")
for a in range(0,10000):
    gitem = lootgen.gozd(mod)
    mitem = lootgen.mesto(mod)
    bitem = lootgen.brune(mod)
    mbitem = lootgen.medbox(mod)
    sitem = lootgen.sef(mod)
    gozd.append(gitem[1])
    mesto.append(mitem[1])
    brune.append(bitem[1])
    medbox.append(mbitem[1])
    sef.append(sitem[1])

print
print("Gozd: "+str(gozd.count(0))+" crap,\n"+str(gozd.count(1))+" goods, ")
print(str(gozd.count(2))+" weapons,\n"+str(gozd.count(4))+" lootbox, ")
print(str(gozd.count(3))+" events.")
print

print("Mesto: "+str(mesto.count(0))+" crap,\n"+str(mesto.count(1))+" goods, ")
print(str(mesto.count(2))+" weapons,\n"+str(mesto.count(5))+" zdravila,\n"+str(mesto.count(4))+" lootbox, ")
print(str(mesto.count(3))+" events.")
print

print("Brune: "+str(brune.count(0))+" crap,\n"+str(brune.count(1))+" goods, ")
print(str(brune.count(2))+" weapons,\n"+str(brune.count(5))+" zdravila,\n"+str(brune.count(4))+" lootbox, ")
print(str(brune.count(3))+" events.")
print

print("Sef: "+str(sef.count(0))+" crap,\n"+str(sef.count(2))+" weapons,\n"+str(sef.count(5))+" meds.")
print

print("Medbox: "+str(medbox.count(0))+" crap, \n"+str(medbox.count(5))+" meds.")



