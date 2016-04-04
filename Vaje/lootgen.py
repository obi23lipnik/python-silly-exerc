__author__ = 'obi'

import random

meds =["Povoj"]*30 + ["Prva pomoc"]*5 + ["Antibiotik"]*5

goods =["Plastenka vode"]*10 + ["Plocevinka kole"]*20 + ["Snickers"]*30 \
       + ["Prebranec in klobasa"]*10 + ["Vlozeno sadje"]*10
"""
       + ["Prazna plastenka 0,5L"]*20 + ["Prazna steklenica 0,25L"]*10 \
       + ["Prazna plastenka 1,5L"]*4
"""
weapons = ["Hokejska palica"]*25 + ["Lovski noz"]*25 + ["Motorka"]*5 \
       + ["Samostrel"]*25 + ["Pistola"]*10  + ["Puska"]*5

scavange = ["Borovnice"]*10 + ["Robide"]*10 + ["Jurcki"]*10 \
       + ["Vir pitne vode"]*30 + ["Lisicke"]*10

crap = ["Prebit gros"] + ["Strgan cevelj"] + ["Plasticna vrecka"] \
    + ["WC Papir"] + ["Zarjavela vilica"] + ["Prazna skatla za pice"] \
    + ["Prazna skatlica cigaret"] + ["Popisan zvezek"] + ["Clovesko stopalo"] \
    + ["Cloveski prst"] + ["Zob"] + ["Polomljen svincnik"] + ["Pokvarjen telefon"] \
    + ["Mrtva podgana"] + ["Mrtev pes"] + ["Pregorela zarnica"] + ["Uporabljen WC Papir"]

sefcrap = ["50.000 evrov"] + ["100 zlatih palic"] + ["Ponarejeni dokumenti"] + ["Fotografije"] + ["Dokumenti"] + ["Trdi disk"]
medcrap = ["Injekcije"] + ["Lesena noga"] + ["Respirator"] + ["Kateter"] + ["Viagra"] + ["Lateks rokavice"]

mevents = ["Horda zombijev!"] + ["Tujec"]*10 + ["2 Zombija"]*5 + ["Zombi"]*10 + ["Konec poti"]*10
gevents = ["Horda zombi krav!"] + ["Loputa"] + ["Zombi"]*10 + ["Konec poti"]
bevents = ["Horda zombi ovc!"] + ["Konec poti"]

def medbox(mod):
    if random.randint(10,30) > mod*2+10:
        return random.choice(medcrap), 0
    return random.choice(meds), 5

def sef(mod):
    if random.randint(10,30) > mod*2+10:
        return random.choice(sefcrap), 0
    if random.randint(1,100) > 80:
        return "Antibiotik", 5
    return random.choice(weapons), 2

def mesto(mod):
    if random.randint(1,100) >= 90:
        return random.choice(mevents),3
    if random.randint(1,100) <= 10 and random.randint(10,30) < mod*2+10:
        return random.choice(meds), 5
    if random.randint(1,100) <= 5 and random.randint(10,30) < mod*2+10:
        return random.choice(weapons), 2
    if random.randint(1,100) <= 4 and random.randint(10,30) < mod*2+10:
        return "Sef", 4
    if random.randint(10,30) > mod*2+10 :
        return random.choice(crap), 0
    return random.choice(goods), 1

def gozd(mod):
    if random.randint(1,100) >= 90:
        return random.choice(gevents), 3
    if random.randint(10,30) > mod*2+9 :
        return random.choice(crap), 0
    return random.choice(scavange), 1

def brune(mod):
    if random.randint(1,100) >= 90:
        return random.choice(bevents), 3
    if random.randint(1,100) <= 20 and random.randint(10,30) < mod*2+10:
        return random.choice(meds), 5
    if random.randint(1,100) <= 10 and random.randint(10,30) < mod*2+10:
        return random.choice(weapons), 2
    if random.randint(1,100) <= 5 and random.randint(10,30) < mod*2+10:
        return "Medbox", 4
    if random.randint(10,30) > mod*2+9 :
        return random.choice(crap), 0
    return random.choice(goods), 1

for a in range(1,100):
    print(mesto(5))