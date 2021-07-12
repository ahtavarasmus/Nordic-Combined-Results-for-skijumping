#! python3
# jumpingresults.py - nordic combined skijumping results program

# TODO: find out users home dictionary and save the resultsfile to users desktop
import datetime
import pyinputplus as pyip
from collections import OrderedDict





# Takes the hill size
print('Syötä mäen k-piste:')
kpoint = pyip.inputNum(min=20, max=240)
if 20<= kpoint <= 24:
    metervalue = 4.8
elif 25<= kpoint <= 29:
    metervalue = 4.4
elif 30<= kpoint <= 34:
    metervalue = 4.0
elif 35<= kpoint <= 39:
    metervalue = 3.6
elif 40<= kpoint <= 49:
    metervalue = 3.2
elif 50<= kpoint <= 59:
    metervalue = 2.8
elif 60<= kpoint <= 69:
    metervalue = 2.4
elif 70<= kpoint <= 79:
    metervalue = 2.2
elif 80<= kpoint <= 99:
    metervalue = 2.0
elif 100<= kpoint:
    metervalue = 1.8

names =[]
while True:
    name = input('Syötä nimi: ')
    if not name:   # jos nimi == enter, se lopettaa
        break
    names.append(name)
tulokset = {} # includes {'otto':{'pituus':130,'tp':50,...}}

for name in names:
    tulokset.setdefault(name,{})

    print(f'{name} hypyn pituus:')
    pituus = pyip.inputNum()
    tulokset[name].setdefault('pituus',pituus)

    if pituus < kpoint:
        pp = 60 - metervalue * (kpoint - pituus)
    else:
        pp = 60 + metervalue * (pituus - kpoint)
    tulokset[name].setdefault('pp',pp)

    tyylit_raw = []
    tuomarit = ['a','b','c','d','e']
    for letter in tuomarit:
        print(f'Tuomari {letter}:')
        t = pyip.inputNum(min=10,max=20)
        tyylit_raw.append(t)

    tyylit_raw.sort()
    tp = tyylit_raw[1] + tyylit_raw[2] + tyylit_raw[3]
    tulokset[name].setdefault('tp',tp)

    tyylit3 = [tyylit_raw[1], tyylit_raw[2], tyylit_raw[3]]
    tulokset[name].setdefault('tyylit',tyylit3)

    yhtp = pp + tp
    tulokset[name].setdefault('yht',yhtp)


    print(tulokset,'\n')

# Making a new dict sorted by the yht points
res = OrderedDict(sorted(tulokset.items(),key=lambda kv: kv[1]['yht'], reverse=True))

# calculating the timedifferences
nollamies = list(res.keys())[0] # nollamies nimi
nollamiespp = res[nollamies]['yht'] # nollamiehen yhtpisteet

times = [] # aikaerot hiihtoon
for name in res:
    for yht in res[name]:
        if yht == 'yht':
            time = str(datetime.timedelta(seconds=((nollamiespp - res[name]['yht']) * 60 / 15))) # lasketaan kaavalla 15p = 1min
            times.append(time)

# Printing the results
p = 1
for name,time in zip(res,times):
    print(p,'{:<10s}'.format(name),res[name],time) # en tiedä mikä {:<10s} on mutta se laittaa tasasen välin nimien jälkeen
    p += 1
# TODO: HOW TO ROUND DATETIME TO THE NEAREST SECOND!!! IDK!
# TODO: write results to file on a desktop
