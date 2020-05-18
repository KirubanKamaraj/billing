# Password and veg updates
from tkinter import Tk, Frame, font, StringVar, END
from tkinter import ttk
from os import getcwd
from passEncrypt import Encrypt
import sqlite3 as sql

position = getcwd()

class UpdateWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.my2font = font.Font(family="Arialblack bold", size=15)

    def WindowOfUpdate(self, ass=None):
        self.configure(background="white")
        self.minsize(width=650, height=300)
        self.resizable(0, 0)
        self.title("eiK-B")
        self.iconbitmap(position + "/Requirements/eiK-B.ico")
        self.newFrame = Frame(
            self, background="white", width=650, height=400)
        self.newFrame.pack(fill="both")
        self.passname = ttk.Label(self.newFrame, text="Change Password",
                                  background="white", foreground="#0077FF", font=("Helvetica", 20))
        self.passname.place(x=200, y=10)
        self.passin = StringVar()
        self.passEntry = ttk.Entry(
            self.newFrame, textvar=self.passin, font=self.my2font)
        self.passEntry.place(x=200, y=70)

        self.passBut = ttk.Button(
            self.newFrame, text="Update", command=self.UpPass)
        self.passBut.place(x=270, y=120)

        self.vegname = ttk.Label(self.newFrame, text="Update Product",
                                 background="white", foreground="#0077FF", font=("Helvetica", 20))
        self.vegname.place(x=215, y=200)

        self.vegin = StringVar()
        self.vegEntry = ttk.Entry(
            self.newFrame, textvar=self.vegin, font=self.my2font)
        self.vegEntry.place(x=200, y=260)
        self.vegBut = ttk.Button(
            self.newFrame, text="Update", command=self.UpVeg)
        self.vegBut.place(x=270, y=310)

    def UpVeg(self):
        veg = self.vegEntry.get()

        try:
            with sql.connect(position + "\Pass\Veg.db") as Veg:
                vd = Veg.cursor()
                vd.execute('''SELECT NUM FROM Veg ORDER BY NUM DESC LIMIT 1''')
                lastnum = vd.fetchall()
                try:
                    vd.execute(
                        '''INSERT INTO Veg(NUM, NAMES) VALUES(?, ?)''', (lastnum[0][0] + 1, veg))
                except:
                    pass
            Veg.commit()
            self.vegEntry.delete(0, END)
        except:
            self.bell()

    def UpPass(self):
        pas = self.passEntry.get()
        password = Encrypt().passwordLogin(pas)

        if len(pas) >= 6:
            try:
                with open(position + "/Pass/password.ec", "w+") as work_file:
                    work_file.truncate(0)
                    work_file.write(password)

                self.passEntry.delete(0, END)
            except:
                self.bell()
