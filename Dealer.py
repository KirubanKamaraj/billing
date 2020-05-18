
# Dealer Page of eik-B

from tkinter import Frame, Canvas, Text, PhotoImage, StringVar, font, END, Scrollbar, ALL
from tkinter import ttk
from os import getcwd
import sqlite3 as sql
from MemberShow import MemberShow
from TotalDebit import Debit

position = getcwd()

class DealerPage(Frame):
    def __init__(self, master, **kwarks):
        Frame.__init__(self, master, **kwarks)
        self.font = font.Font(family="Roboto", size=33)
        #self.ChangingDictDeal = {"Pos": "Money"}
        
    def PullComponents(self, event=None):
        self.frame_ce = Frame(self, width=1286,
                              height=416, background="#FDFEFE")
        self.frame_ce.pack(fill='both', expand=True, anchor='n')
        
        self.distributor_txt = ttk.Label(self.frame_ce, text="ADD DEALER", background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.distributor_txt.place(x=35, y=5)

        self.DistributorName = StringVar()
        self.CompanyName = StringVar()
        self.PhoneNameForDis = StringVar()

        self.NameEntry = ttk.Entry(
            self.frame_ce, textvar=self.DistributorName, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.NameEntry.place(x=60, y=175, height=50)
        self.NameEntry.insert(0, " Dealer Name")

        self.CompanyEntry = ttk.Entry(
            self.frame_ce, textvar=self.CompanyName, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.CompanyEntry.place(x=60, y=100, height=50)
        self.CompanyEntry.insert(0, " Company Name")

        self.AddressEntry = Text(
            self.frame_ce, foreground="#7f8c8d", width=23, font=("Helvetica", 20), relief="ridge")
        self.AddressEntry.place(x=60, y=250, height=100)
        self.AddressEntry.insert(END, " Address")

        self.PhoneEntry = ttk.Entry(
            self.frame_ce, textvar=self.PhoneNameForDis, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.PhoneEntry.place(x=60, y=370, height=50)
        self.PhoneEntry.insert(0, " Phone Number")

        self.distributor_con = ttk.Label(self.frame_ce, text="DEALER",
                                    background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.distributor_con.place(x=530, y=8)

        self.showFrame = Canvas(self.frame_ce, height = 595, width = 550, background = "white")
        self.showFrame.place(x = 530, y = 99)
        self.Scrollshow = Scrollbar(self.frame_ce)
        self.Scrollshow.place(x = 1075, y = 99, height = 600)

        self.NameEntry.bind("<FocusIn>", lambda idc: self.RemovePlaceForDis("Name"))
        self.NameEntry.bind("<FocusOut>", lambda idc: self.InsertPlaceForDis("Name"))
        self.NameEntry.bind("<Return>", lambda idc: self.FocusEntry("Name"))

        self.CompanyEntry.bind("<FocusIn>", lambda idc: self.RemovePlaceForDis("Company"))
        self.CompanyEntry.bind("<FocusOut>", lambda idc: self.InsertPlaceForDis("Company"))
        self.CompanyEntry.bind("<Return>", lambda idc: self.FocusEntry("Company"))

        self.PhoneEntry.bind(
            "<FocusIn>", lambda idc: self.RemovePlaceForDis("Phone"))
        self.PhoneEntry.bind(
            "<FocusOut>", lambda idc: self.InsertPlaceForDis("Phone"))

        self.AddressEntry.bind("<FocusIn>", lambda idc: self.RemovePlaceForDis("Address"))
        self.AddressEntry.bind("<FocusOut>", lambda idc: self.InsertPlaceForDis("Address"))
        self.AddressEntry.bind("<Return>", lambda idc: self.FocusEntry("Address"))

        with sql.connect(position+"/Pass/"+"Dealer-data.db") as DealerData:
            DD = DealerData.cursor()
            DD.execute(''' CREATE TABLE IF NOT EXISTS Dealer(NUM INT, COMPANYNAME TEXT NOT NULL PRIMARY KEY, DEALERNAME TEXT, COMPANYADDRESS TEXT, PHONENUMBER TEXT) ''')
            DealerData.commit()
        MemberShow(self).ShowThat(name="Dealer")
        self.showFrame.config(
            scrollregion=self.showFrame.bbox(ALL))
        self.showFrame.config(yscrollcommand=self.Scrollshow.set)
        self.Scrollshow.config(command=self.showFrame.yview)

        def updateChange(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/UpdateUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Update.png"
            self.CustomerImageChange = PhotoImage(file=position+ImageName)
            self.updateCustomer.configure(image=self.CustomerImageChange)
            self.updateCustomer.image = self.CustomerImageChange

        self.CustomerImage = PhotoImage(file=position+"/Requirements/Update.png")
        self.updateCustomer = ttk.Label(
            self.frame_ce, image=self.CustomerImage, background="white")
        self.updateCustomer.image = self.CustomerImage
        self.updateCustomer.place(x=60, y=470)

        self.updateCustomer.bind("<Enter>", updateChange)
        self.updateCustomer.bind("<Leave>", updateChange)
        self.updateCustomer.bind("<Button-1>", self.DistributorUpdate)

        def TotDeb(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/TotDebUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/TotDeb.png"
            self.CustomerImageChange = PhotoImage(file=position+ImageName)
            self.TotDebCustomer.configure(image=self.CustomerImageChange)
            self.TotDebCustomer.image = self.CustomerImageChange

        self.CustomerImage = PhotoImage(file=position+"/Requirements/TotDeb.png")
        self.TotDebCustomer = ttk.Label(
            self.frame_ce, image=self.CustomerImage, background="white")
        self.TotDebCustomer.image = self.CustomerImage
        self.TotDebCustomer.place(x=60, y=570)

        self.TotDebCustomer.bind("<Enter>", TotDeb)
        self.TotDebCustomer.bind("<Leave>", TotDeb)
        self.TotDebCustomer.bind("<Button-1>", self.DistributorTotDeb)
    
    def FocusEntry(self, EntryBox):
        if EntryBox == "Company":
            self.NameEntry.focus()
        elif EntryBox == "Name":
            self.AddressEntry.focus()
        elif EntryBox == "Address":
            self.PhoneEntry.focus()

    def RemovePlaceForDis(self, IdCheck):
        self.NamePerForDis = self.DistributorName.get()
        self.NameShForDis = self.CompanyName.get()
        self.NamePhoForDis = self.PhoneNameForDis.get()
        self.NameAddressForDis = self.AddressEntry.get("1.0", "end-1c")

        if IdCheck == "Name":
            if self.NamePerForDis == " Dealer Name":
                self.NameEntry.delete(0, END)
                self.NameEntry.config(foreground="black")
        elif IdCheck == "Company":
            if self.NameShForDis == " Company Name":
                self.CompanyEntry.delete(0, END)
                self.CompanyEntry.config(foreground="black")
        elif IdCheck == "Phone":
            if self.NamePhoForDis == " Phone Number":
                self.PhoneEntry.delete(0, END)
                self.PhoneEntry.config(foreground="black")
        elif IdCheck == "Address":
            if self.NameAddressForDis == " Address":
                self.AddressEntry.delete("1.0", END)
                self.AddressEntry.config(foreground="black")

    def InsertPlaceForDis(self, IdCheck):
        self.NamePerForDis = self.DistributorName.get()
        self.NameShForDis = self.CompanyName.get()
        self.NamePhoForDis = self.PhoneNameForDis.get()
        self.AddressNameForDis = self.AddressEntry.get("1.0", "end-1c")

        if IdCheck == "Name":
            if self.NamePerForDis == '':
                self.NameEntry.config(foreground="#7f8c8d")
                self.NameEntry.insert(0, " Dealer Name")
        elif IdCheck == "Company":
            if self.NameShForDis == '':
                self.CompanyEntry.config(foreground="#7f8c8d")
                self.CompanyEntry.insert(0, " Company Name")
        elif IdCheck == "Phone":
            if self.NamePhoForDis == '':
                self.PhoneEntry.config(foreground="#7f8c8d")
                self.PhoneEntry.insert(0, " Phone Number")
        elif IdCheck == "Address":
            if self.AddressNameForDis == '':
                self.AddressEntry.config(foreground="#7f8c8d")
                self.AddressEntry.insert(END, " Address")

    def DistributorUpdate(self, event = None):
        self.NamePerForDis = self.DistributorName.get()
        if self.NamePerForDis == " Dealer Name":
            self.NamePerForDis = ' '
        self.NameShForDis = self.CompanyName.get()
        if self.NameShForDis == " Company Name":
            self.NameShForDis = ' '
        self.NamePhoForDis = self.PhoneNameForDis.get()
        if self.NamePhoForDis == " Phone Number":
            self.NamePhoForDis = ' '
        self.NameAddressForDis = self.AddressEntry.get("1.0", "end-1c")
        if self.NameAddressForDis == " Address":
            self.NameAddressForDis = ' '
        with sql.connect(position+"/Pass/"+"Dealer-data.db") as DealerData:
            DD = DealerData.cursor()

            try:
                DD.execute(
                    ''' CREATE TABLE IF NOT EXISTS %s(NUM INT, DateData DATE, RS TEXT, PRODUCT TEXT, NOM TEXT, NET TEXT, TOTAL TEXT)''' %self.NameShForDis)

                DD.execute(''' CREATE TABLE IF NOT EXISTS %s(NUM INT, DateData DATE, TOTAL TEXT, DEBIT TEXT, CREDITED TEXT)''' % (self.NameShForDis + "MONEY"))
                DD.execute('''SELECT * FROM Dealer''')
                DealerNumdata = DD.fetchall()
                numData = len(DealerNumdata)
                DD.execute(''' INSERT INTO Dealer(NUM , COMPANYNAME, DEALERNAME, COMPANYADDRESS, PHONENUMBER) VALUES(?, ?, ?, ?, ?)''', (numData + 1, self.NameShForDis,
                                                                                self.NamePerForDis, self.NameAddressForDis, self.NamePhoForDis))
                DealerData.commit()
                self.NameEntry.delete(0, END)
                self.CompanyEntry.delete(0, END)
                self.PhoneEntry.delete(0, END)
                self.AddressEntry.delete("1.0", END)
                self.NameEntry.config(foreground="#7f8c8d")
                self.PhoneEntry.config(foreground="#7f8c8d")
                self.NameEntry.insert(0, " Dealer Name")
                self.PhoneEntry.insert(0, " Phone Number")
                self.AddressEntry.config(foreground="#7f8c8d")
                self.AddressEntry.insert(END, " Address")
                self.CompanyEntry.focus()
                MemberShow(self).ShowThat(name="Dealer")
                self.showFrame.config(scrollregion=self.showFrame.bbox(ALL))
                self.showFrame.config(yscrollcommand=self.Scrollshow.set)
                self.Scrollshow.config(command=self.showFrame.yview)

            except:
                self.bell()

    def DistributorTotDeb(self, event):
        Debit.TotDeb("Dealer")

