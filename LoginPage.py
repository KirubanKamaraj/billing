# Login page of eiK-B

from tkinter import Frame, YES, BOTH, StringVar, PhotoImage, font
from tkinter import ttk
from PIL import ImageTk, Image
from os import getcwd, getenv
from array import array
from OpeningFixedPage import FixedPage
from passEncrypt import Encrypt

position = getcwd()

class LoginPage(Frame):
    def __init__(self, parent=None, passWordfile=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.passWordfile = passWordfile
        self.config(background="black")

    def loginComponentsSet(self):
        self.my2font = font.Font(family="Arialblack bold", size=15)
        photo = ImageTk.PhotoImage(Image.open(
            position + "/Requirements/VegLog.png"))
        self.backgroundLabel = ttk.Label(self, image=photo, background="#FDFEFE")
        self.backgroundLabel.image = photo
        self.backgroundLabel.pack(fill=BOTH, expand=True)
        self.passwordGet = StringVar()
        self.passwordEntry = ttk.Entry(self, width=23,
                               show='*', textvar=self.passwordGet, font=self.my2font)
        self.passwordEntry.place(x=640, y=350)
        self.passwordEntry.focus()
        self.font = font.Font(family="Adobe Garamond Pro Bold", size=33)

        def LoginButtonChange(changeEvent):
            if str(changeEvent)[1:6] == "Enter":
                ImageName = "/Requirements/LoginUp.png"
            elif str(changeEvent)[1:6] == "Leave":
                ImageName = "/Requirements/Login.png"
            self.LoginChange = PhotoImage(file=position+ImageName)
            self.updateLogin.configure(image=self.LoginChange)
            self.updateLogin.image = self.LoginChange

        self.Login = PhotoImage(file=position+"/Requirements/Login.png")
        self.updateLogin = ttk.Label(self, image=self.Login, background="white")
        self.updateLogin.image = self.Login
        self.updateLogin.place(x=720, y=420)
        self.updateLogin.bind("<Enter>", LoginButtonChange)
        self.updateLogin.bind("<Leave>", LoginButtonChange)

        self.passwordEntry.bind("<Return>", self.EncryptPasswordAndLogin)
        self.updateLogin.bind("<Button-1>", self.EncryptPasswordAndLogin)

    def EncryptPasswordAndLogin(self, event):
        self.pas = self.passwordGet.get()
        password = Encrypt(self.pas, self.passWordfile).passwordLogin()
        if password == "Done":
            self.backgroundLabel.pack_forget()
            self.pack_forget()
            fixedPage = FixedPage(self.parent)
            fixedPage.pack(fill=BOTH, expand=YES)
            fixedPage.LeftSideFixedPage()
        else:
            self.bell()
            myfont = font.Font(family="Comic Sans MS", size=12)
            label_not = ttk.Label(self.backgroundLabel, text='Wrong Password!', foreground='Red',
                                    background='#BB8FCE', font=myfont)


