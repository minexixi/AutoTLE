import requests

allTle = open('allTLE.txt', 'r')
Tles = str(allTle.read())
allTle.close()
if '<' in Tles:
    print('get tles error.')
    sys.exit(1)
Tle = open('BH7AHSAutoTLE.txt', 'w')
Tles = Tles.splitlines()
Tles = [i for i in Tles if i != '']


satelistNumber = [
    '25544U', '27607U', '43678U', '44909U'
    ,'24278U' , '42017U', '44354U', 
    '44881U' , '43937U',  '50466U','40908U'
]
satelistName = [
    'ISS', 'SO-50', 'PO-101(DIWATA-2B)', 'RS-44', 
    'FO-29', 'EO-88', 'PSAT-2(NO-104)',
    'UVSQ-SAT', 'FO-99', 'XW-3(HO-113)', 'CAS-3H(LilacSat-2)'
]
for i in range(len(satelistNumber)):
    temp = [temp for temp in Tles if satelistNumber[i] in temp]
    print(satelistName[i])
    getTles = satelistName[i] + '\n' + Tles[Tles.index(temp[0])] + '\n' + Tles[Tles.index(temp[0]) + 1] + '\n'
    Tle.write(getTles)

Tle.close()
