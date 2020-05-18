
from tkinter import Frame, Canvas, Text, PhotoImage, StringVar, font, END, Scrollbar, ALL
from tkinter import ttk
from os import getcwd
import sqlite3 as sql
from MemberShow import MemberShow
from TotalDebit import Debit

position = getcwd()

class customer(Frame):
    def __init__(self, master, **kwarks):
        Frame.__init__(self, master, **kwarks)
        self.font = font.Font(family="Roboto", size=33)

    def customerPage(self, event=None):
        self.CustomerFrame = Frame(self, width=1286, height=841, background="#FDFEFE")
        self.CustomerFrame.pack()
        self.distributor_txt = ttk.Label(self.CustomerFrame, text="ADD CUSTOMER",
                               background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.distributor_txt.place(x=35, y=5)

        self.CustomerName = StringVar()
        self.ShopName = StringVar()
        self.PhoneName = StringVar()

        self.NameEntry = ttk.Entry(
            self.CustomerFrame, textvar=self.CustomerName, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.NameEntry.place(x=60, y=100, height=50)
        self.NameEntry.insert(0, " Customer Name")

        self.CompanyEntry = ttk.Entry(
            self.CustomerFrame, textvar=self.ShopName, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.CompanyEntry.place(x=60, y=175, height=50)
        self.CompanyEntry.insert(0, " Company Name")

        self.AddressEntry = Text(
            self.CustomerFrame, foreground="#7f8c8d", width=23, font=("Helvetica", 20), relief="ridge")
        self.AddressEntry.place(x=60, y=250, height=100)
        self.AddressEntry.insert(END, " Address")

        self.PhoneEntry = ttk.Entry(
            self.CustomerFrame, textvar=self.PhoneName, foreground="#7f8c8d", width=23, font=("Helvetica", 20))
        self.PhoneEntry.place(x=60, y=370, height=50)
        self.PhoneEntry.insert(0, " Phone Number")

        self.distributor_con = ttk.Label(self.CustomerFrame, text="CUSTOMER",
                                    background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.distributor_con.place(x=530, y=8)
        #self.showFrame = Text(self.CustomerFrame, height = 37, width = 69, background = "white", state = DISABLED)
        self.showFrame = Canvas(self.CustomerFrame, height = 595, width = 550, background = "white")
        self.showFrame.place(x = 530, y = 99)
        self.Scrollshow = Scrollbar(self.CustomerFrame)
        self.Scrollshow.place(x = 1075, y = 99, height = 600)

        self.NameEntry.bind("<FocusIn>", lambda idc: self.RemovePlace("Name"))
        self.NameEntry.bind("<FocusOut>", lambda idc: self.InsertPlace("Name"))
        self.NameEntry.bind(
            "<Return>", lambda idc: self.FocusEntryForCus("Name"))

        self.CompanyEntry.bind("<FocusIn>", lambda idc: self.RemovePlace("Company"))
        self.CompanyEntry.bind("<FocusOut>", lambda idc: self.InsertPlace("Company"))
        self.CompanyEntry.bind(
            "<Return>", lambda idc: self.FocusEntryForCus("Company"))

        self.PhoneEntry.bind(
            "<FocusIn>", lambda idc: self.RemovePlace("Phone"))
        self.PhoneEntry.bind(
            "<FocusOut>", lambda idc: self.InsertPlace("Phone"))

        self.AddressEntry.bind(
            "<FocusIn>", lambda idc: self.RemovePlace("Address"))
        self.AddressEntry.bind(
            "<FocusOut>", lambda idc: self.InsertPlace("Address"))
        self.AddressEntry.bind(
            "<Return>", lambda idc: self.FocusEntryForCus("Address"))

        with sql.connect(position+"/Pass/"+"Customer-data.db") as CustomerData:
            CD = CustomerData.cursor()
            CD.execute(''' CREATE TABLE IF NOT EXISTS Customer(NUM INT, CUSTOMERNAME TEXT NOT NULL PRIMARY KEY, COMPANYNAME TEXT, COMPANYADDRESS TEXT, PHONENUMBER TEXT) ''')
            CustomerData.commit()
        
        MemberShow(self).ShowThat(name="Customer")

        def updateChange(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/UpdateUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/UpdateUp.png"
                ImageName = "/Requirements/Update.png"
            self.CustomerImageChange = PhotoImage(file=position+ImageName)
            self.updateCustomer.configure(image=self.CustomerImageChange)
            self.updateCustomer.image = self.CustomerImageChange

        self.CustomerImage = PhotoImage(file=position+"/Requirements/Update.png")
        self.updateCustomer = ttk.Label(
            self.CustomerFrame, image=self.CustomerImage, background="white")
        self.updateCustomer.image = self.CustomerImage
        self.updateCustomer.place(x=60, y=470)

        self.updateCustomer.bind("<Enter>", updateChange)
        self.updateCustomer.bind("<Leave>", updateChange)
        self.updateCustomer.bind("<Button-1>", self.CustomerUpdate)

        def TotDeb(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/TotDebUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/TotDeb.png"
            self.CustomerImageChange = PhotoImage(file=position+ImageName)
            self.TotDebCustomer.configure(image=self.CustomerImageChange)
            self.TotDebCustomer.image = self.CustomerImageChange

        self.CustomerImage = PhotoImage(
            file=position+"/Requirements/TotDeb.png")
        self.TotDebCustomer = ttk.Label(
            self.CustomerFrame, image=self.CustomerImage, background="white")
        self.TotDebCustomer.image = self.CustomerImage
        self.TotDebCustomer.place(x=60, y=570)

        self.TotDebCustomer.bind("<Enter>", TotDeb)
        self.TotDebCustomer.bind("<Leave>", TotDeb)
        self.TotDebCustomer.bind("<Button-1>", self.CustomerTotDeb)

    def FocusEntryForCus(self, EntryBox):
        if EntryBox == "Company":
            self.AddressEntry.focus()
        elif EntryBox == "Name":
            self.CompanyEntry.focus()
        elif EntryBox == "Address":
            self.PhoneEntry.focus()


    def RemovePlace(self, IdCheck):
        self.NamePer = self.CustomerName.get()
        self.NameSh = self.ShopName.get()
        self.NamePho = self.PhoneName.get()
        self.NameAddress = self.AddressEntry.get("1.0", "end-1c")

        if IdCheck == "Name":
            if self.NamePer == " Customer Name":
                self.NameEntry.delete(0, END)
                self.NameEntry.config(foreground="black")
        elif IdCheck == "Company":
            if self.NameSh == " Company Name":
                self.CompanyEntry.delete(0, END)
                self.CompanyEntry.config(foreground="black")
        elif IdCheck == "Phone":
            if self.NamePho == " Phone Number":
                self.PhoneEntry.delete(0, END)
                self.PhoneEntry.config(foreground="black")
        elif IdCheck == "Address":
            if self.NameAddress == " Address":
                self.AddressEntry.delete("1.0", END)
                self.AddressEntry.config(foreground = "black")

    def InsertPlace(self, IdCheck):
        self.NamePer = self.CustomerName.get()
        self.NameSh = self.ShopName.get()
        self.NamePho = self.PhoneName.get()
        self.NameAddress = self.AddressEntry.get("1.0", "end-1c")

        if IdCheck == "Name":
            if self.NamePer == '':
                self.NameEntry.config(foreground="#7f8c8d")
                self.NameEntry.insert(0, " Customer Name")
        elif IdCheck == "Company":
            if self.NameSh == '':
                self.CompanyEntry.config(foreground="#7f8c8d")
                self.CompanyEntry.insert(0, " Company Name")
        elif IdCheck == "Phone":
            if self.NamePho == '':
                self.PhoneEntry.config(foreground="#7f8c8d")
                self.PhoneEntry.insert(0, " Phone Number")
        elif IdCheck == "Address":
            if self.NameAddress == "":
                self.AddressEntry.config(foreground="#7f8c8d")
                self.AddressEntry.insert(END, " Address")

    def CustomerUpdate(self, event):
        self.NamePer = self.CustomerName.get()
        if self.NamePer == " Customer Name":
            self.NamePer = ' '
        self.NameSh = self.ShopName.get()
        if self.NameSh == " Company Name":
            self.NameSh = ' '
        self.AddressNameForCus = self.AddressEntry.get("1.0", "end-1c")
        if self.AddressNameForCus == " Address":
            self.AddressNameForCus = ' '
        self.NamePho = self.PhoneName.get()
        if self.NamePho == " Phone Number":
            self.NamePho = ' '
        with sql.connect(position+"/Pass/"+"Customer-data.db") as CustomerData:
            try:
                CD = CustomerData.cursor()
                CD.execute(''' CREATE TABLE IF NOT EXISTS %s(NUM INT, DateData DATE, RS TEXT, PRODUCT TEXT, NOM TEXT, NET TEXT, TOTAL TEXT)'''%self.NamePer)
                CD.execute(
                    ''' CREATE TABLE IF NOT EXISTS %s(NUM INT, DateData DATE, TOTAL TEXT, DEBIT TEXT, CREDITED TEXT)''' % (self.NamePer + "MONEY"))
                CD.execute('''SELECT * FROM Customer''')
                CustomerNumdata = len(CD.fetchall())
                
                CD.execute(''' INSERT INTO Customer(NUM, CUSTOMERNAME, COMPANYNAME, COMPANYADDRESS, PHONENUMBER)
                            VALUES(?, ?, ?, ?, ?)''',
                            (CustomerNumdata + 1, self.NamePer, self.NameSh, self.AddressNameForCus, self.NamePho))
                CustomerData.commit()
                self.NameEntry.delete(0, END)
                self.CompanyEntry.delete(0, END)
                self.AddressEntry.delete("1.0", END)
                self.PhoneEntry.delete(0, END)
                self.CompanyEntry.config(foreground="#7f8c8d")
                self.PhoneEntry.config(foreground="#7f8c8d")
                self.AddressEntry.config(foreground="#7f8c8d")
                self.CompanyEntry.insert(0, " Company Name")
                self.PhoneEntry.insert(0, " Phone Number")
                self.AddressEntry.insert(END, " Address")
                self.NameEntry.focus()
                MemberShow(self).ShowThat(name="Customer")

            except:
                self.bell()

    def CustomerTotDeb(self, event):
        Debit.TotDeb("Customer")

    def ChangeWindow(self):
        if self.ChangingDict["Pos"] == "Pro":
            self.InsideOfShowCustomer(self.Name)
        elif self.ChangingDict["Pos"] == "Money":
            self.CustomerMoney(self.Name)

    def ChangeUpdateRound(self):
        if self.ChangingDict["Pos"] == "Pro":
            self.UpdateMoneyFirst(self.Name)
        elif self.ChangingDict["Pos"] == "Money":
            self.UpdateFirst(self.Name)
