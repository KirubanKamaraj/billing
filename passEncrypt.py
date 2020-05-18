from os import getcwd, getenv
from array import array

position = getcwd()
username = getenv('username')
pathForPass = getcwd()
pathForPass = str(pathForPass).replace("\\", "55")
pathForPass = str(pathForPass).replace(":", "k")

class Encrypt:
    def __init__(self, pas=None, passWordfile=None):
        self.pas = pas
        self.passWordfile = passWordfile

    def passwordLogin(self, event=None):
        self.pasg = array('i')
        self.dipa = {'1': '#', '2': '~', '3': '.', '4': '/', '5': '$', '6': '?',
                        '7': '^', '8': '&', '9': '%', '0': '!', ',': 'z', '{': 'x', '}': 'u', ' ': 'i'}

        # self.dipa for encrypte the password

        if type(event) == type("a"):
            self.pas = event
            #print(event)
        else:
            #self.pas = self.passwordGet.get()
            if self.pas == "":
                self.pas = "0"
            else:   pass

        self.usa = list(
            map(lambda i: self.pas[i]+'usa'+'g@me0<e^'+str(pathForPass)+str(username), [i for i in range(len(self.pas))]))
        for ithu in range(0, len(self.usa)):
            for athu in range(len(self.usa[ithu])):
                self.hod = ord(self.usa[ithu][athu])
                self.pasg.append(self.hod)
                self.paas = str(set(self.pasg))
        
        self.paass = 0
        try:
            for ulla in self.paas:
                m = self.dipa[str(ulla)]
                self.paass = str(self.paass) + m
                paass = self.paass

        except:
            self.paas = '0'
            self.bell()

        try:
            pda = open(position + "/Pass/" + self.passWordfile, 'r')
            password = pda.read()

            if self.paass == password:
                for dei in self.pasg:
                    self.pasg.remove(dei)
                pda.close()
                del self.paass
                del self.paas
                del self.pasg
                return 'Done'

            else:
                for poda in self.pasg:
                    self.pasg.remove(poda)
                pda.close()
                del self.paass
                del self.paas
                del self.pasg
                pass
        except:
            if self.paass:
                return paass

