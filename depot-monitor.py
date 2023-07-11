#!/usr/bin/python3
import PyNUT
from pprint import pprint
import datetime
import csv

def setup():
    global ups
    ups = PyNUT.PyNUTClient(host='localhost', timeout=300)
    global upsVarsLast
    global toMonitor
    upsVarsLast = {}
    toMonitor = ['input.voltage', 'ups.status']

def loop():
    global ups
    global upsVarsLast
    global toMonitor
    allUpsVars = {}
    upsVars = {}
    allUpsVars= ups.GetUPSVars(ups='chsl-depot-rack')
    allUpsVars = {y.decode('ascii'): allUpsVars.get(y).decode('ascii') for y in allUpsVars.keys()}
    now = datetime.datetime.now()
    for variable in toMonitor:
        upsVars[variable] = allUpsVars[variable]
    if upsVars !=upsVarsLast:
        dataPoint = {'date':now.strftime('%Y-%m-%d'), 'time':now.strftime('%H:%M:%S')}
        dataPoint.update(upsVars)
        with open('/home/pi/depotacdata.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(dataPoint)
    upsVarsLast = upsVars
    return

def main():
    setup()
    while True:
        loop()
    return

if __name__ == "__main__":
    main()