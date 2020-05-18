
# eiK-B Software

from tkinter import Tk, Frame, BOTH, YES
from os import getcwd, listdir
from LoginPage import LoginPage
from StartNew import StartNew

# Get the current location 
position = getcwd()

# main function of eiK-B
class eiK_B(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title_name = "EIK-B"
        self.title(self.title_name)
        self.wm_state('zoomed')
        self.minsize(width=894, height=649)
        self.resizable(0, 0)
        self.iconbitmap(position + "/Requirements/eiK-B.ico")

    def check(self):
        try:
            file = listdir(position + "\\Pass")

            for infile in file:
                if "password.ec" in file:
                    if ".ec" == infile[-3:]:
                        self.thevai = infile  # if u have account then call login_page function
                        login = LoginPage(self, self.thevai)
                        login.pack(fill=BOTH, expand=YES)
                        login.loginComponentsSet()
                        break
                    else:
                        if len(file) - file.index(infile) == 1:
                            # else create new account
                            newAccount = StartNew(self)
                            newAccount.pack(fill=BOTH, expand=True)
                            newAccount.start_new()
                            break
                        else:
                            pass
                else:
                    newAccount = StartNew(self)  # else create new account
                    newAccount.pack(fill=BOTH, expand=True)
                    newAccount.start_new()

        except:
            newAccount = StartNew(self)  # else create new account
            newAccount.pack(fill=BOTH, expand=True)
            newAccount.start_new()

if __name__ == "__main__":
    firstSoft = eiK_B()
    firstSoft.check()
    firstSoft.mainloop()
