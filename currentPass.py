from array import array
from os import getcwd


pas = "password" # put your password here
username = "username" # put your username here
pathForPass = getcwd()
pathForPass = str(pathForPass).replace("\\", "55")
pathForPass = str(pathForPass).replace(":", "k")
pasg = array('i')
dipa = {'1': '#', '2': '~', '3': '.', '4': '/', '5': '$', '6': '?',
                '7': '^', '8': '&', '9': '%', '0': '!', ',': 'z', '{': 'x', '}': 'u', ' ': 'i'}
usa = list(map(lambda i: pas[i]+'usa'+'g@me0<e^'+str(pathForPass)+str(username), [i for i in range(len(pas))]))
for ithu in range(0, len(usa)):
    for athu in range(len(usa[ithu])):
        hod = ord(usa[ithu][athu])
        pasg.append(hod)
        paas = str(set(pasg))

paass = 0
try:
    for ulla in paas:
        m = dipa[str(ulla)]
        paass = str(paass) + m
        paass = paass
except:
    pass
print(paass)
