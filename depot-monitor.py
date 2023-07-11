#!/usr/bin/python3
import PyNUT

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
    allUpsVars = {y.decode('ascii'): upsVars.get(y).decode('ascii') for y in upsVars.keys()}
    for variable in toMonitor:
        upsVars[variable] = allUpsVars[variable]
    if upsVars !=upsVarsLast:
        print(upsVars)
    return

def main():
    setup()
    while True:
        loop()
    return

if __name__ == "__main__":
    main()