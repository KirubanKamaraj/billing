
from tkinter import ttk
from tkinter import StringVar, PhotoImage, NO, CENTER, font, Tk, END, Text
from os import getcwd
import sqlite3 as sql
import datetime


position = getcwd()

class MemberView:
    def __init__(self, frame, DorC):
        self.mainframe = frame
        self.DorC = DorC
        self.ChangingDictDeal = {"Pos": "Money"}
        self.database = self.DorC+"-data.db"
        if self.DorC == "Dealer":
            self.CNorCN = "COMPANYNAME"
            self.nameName = "DEALERNAME"
            self.frame_ce = self.mainframe.frame_ce

        elif self.DorC == "Customer":
            self.CNorCN = "CUSTOMERNAME"
            self.nameName = "CUSTOMERNAME"
            self.frame_ce = self.mainframe.CustomerFrame

    def InsideOfShowMember(self, Name):
        self.Name = Name
        self.mainframe.showFrame.destroy()
        self.mainframe.distributor_con.destroy()
        self.mainframe.Scrollshow.destroy()
        self.mainframe.distributor_txt.destroy()
        self.mainframe.NameEntry.destroy()
        self.mainframe.AddressEntry.destroy()
        self.mainframe.CompanyEntry.destroy()
        self.mainframe.PhoneEntry.destroy()
        self.mainframe.updateCustomer.destroy()
        self.mainframe.TotDebCustomer.destroy()
        try:
            self.HoleViewForMoney.destroy()
            self.DateEntryForMoneyUpdate.destroy()
            self.TotalEntryForMoneyUpdate.destroy()
            self.CreditEntryForMoneyUpdate.destroy()
            self.DebitEntryForMoneyUpdate.destroy()
            self.ScrollHoleMoneyView.destroy()
            self.DealerShowImage.destroy()
            self.ChangeDealer.destroy()
            self.updateDealer.destroy()
            self.AddDealer.destroy()
            self.DealerName.destroy()
            self.AddressLabel1.destroy()
            self.AddressLabel2.destroy()
            self.PhoneLabel.destroy()
        except: pass

        Deal = PhotoImage(file = position + "/Requirements/contacts1.png")
        self.DealerShowImage = ttk.Label(
            self.frame_ce, image=Deal, background="white")
        self.DealerShowImage.image = Deal
        self.DealerShowImage.place(x=35, y=5)

        self.ChangingDictDeal = {"Pos":"Money"}

        def ChangeBill(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/ChangeUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Change.png"
            self.DealerImageBill = PhotoImage(file=position+ImageName)
            self.ChangeDealer.configure(image=self.DealerImageBill)
            self.ChangeDealer.image = self.DealerImageBill

        self.DealerImage = PhotoImage(file=position+"/Requirements/Change.png")
        self.ChangeDealer = ttk.Label(
            self.frame_ce, image=self.DealerImage, background="white")
        self.ChangeDealer.image = self.DealerImage
        self.ChangeDealer.place(x=1000, y=100)

        self.ChangeDealer.bind("<Enter>", ChangeBill)
        self.ChangeDealer.bind("<Leave>", ChangeBill)
        self.ChangeDealer.bind("<Button-1>", lambda event: self.ChangeWindow())
        
        self.HoleView = ttk.Treeview(self.frame_ce, selectmode='browse')
        self.HoleView["columns"]=("Rs", "Product","NOM", "Net.Wt", "Total")
        self.HoleView.column("#0", stretch = NO, minwidth = 210, width = 210, anchor = CENTER)
        self.HoleView.column("#1", stretch = NO, minwidth = 180, width = 210, anchor = CENTER)
        self.HoleView.column("#2", stretch = NO, minwidth = 180, width = 210, anchor = CENTER)
        self.HoleView.column("#3", stretch = NO, minwidth = 180, width = 210, anchor = CENTER)
        self.HoleView.column("#4", stretch = NO, minwidth = 180, width = 210, anchor = CENTER)
        self.HoleView.column("#5", stretch=NO, minwidth=180,
                             width=180, anchor=CENTER)
        self.HoleView.heading("#0", text = "Date")
        self.HoleView.heading("#1", text = "Rs")
        self.HoleView.heading("#2", text = "Product")
        self.HoleView.heading("#3", text = "NOM")
        self.HoleView.heading("#4", text = "Net.Wt")
        self.HoleView.heading("#5", text = "Total")
        self.HoleView.place(x = 0, y = 150, width = 1230, height = 560)

        style = ttk.Style()
        style.configure("Treeview", font=(
            "Arial", 12), background="#0077FF", foreground="white", rowheight = 30)
        style.configure("Treeview.Heading", font=(
            "Arial", 12), background="blue")

        self.DateDeal = StringVar()
        self.RsDeal = StringVar()
        self.ProDeal = StringVar()
        self.NOMDeal = StringVar()
        self.NetDeal = StringVar()
        self.TotDeal = StringVar()

        self.DealerName = ttk.Label(self.frame_ce, text = self.Name, font = self.mainframe.font, foreground = "#0077FF", background = "white")
        self.DealerName.place(x = 180, y = 30)

        self.DateEntryForUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar = self.DateDeal)
        self.DateEntryForUpdate.place(x = 20, y = 750)

        self.RsEntryForUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar = self.RsDeal)
        self.RsEntryForUpdate.place(x = 200, y = 750)

        VEGNAMES = []
        def getVegName(event):
            vegName = self.ProDeal.get()
            lenveg = len(vegName)
            with sql.connect(position + "/Pass/Veg.db") as vegetable:
                vg = vegetable.cursor()
                vg.execute('''SELECT NAMES FROM Veg''')
                vegetableSelect = vg.fetchall()
                for lentch in vegetableSelect:
                    if lenveg > 0:
                        if lentch[0][0:lenveg] == vegName.capitalize():
                            VEGNAMES.append(lentch[0])
                            VEGNAMES.sort()
                        elif lentch[0][0:lenveg] == vegName.lower():
                            VEGNAMES.append(lentch[0])
                            VEGNAMES.sort()
                    else:
                        VEGNAMES.clear()
                vegetable.commit()
            self.ProductEntryForUpdate.config(values=list(set(VEGNAMES)))
            VEGNAMES.clear()
                
        self.ProductEntryForUpdate = ttk.Combobox(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar=self.ProDeal)
        self.ProductEntryForUpdate.place(x = 380, y = 750)
        self.bigfont = font.Font(family="Helvetica", size=20)
        Tk.option_add(self.mainframe,"*TCombobox*Listbox*Font", self.bigfont)
        self.ProductEntryForUpdate.bind("<KeyPress>", getVegName)

        self.NOMEntryForUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar = self.NOMDeal)
        self.NOMEntryForUpdate.place(x = 560, y = 750)

        self.NetEntryForUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar = self.NetDeal)
        self.NetEntryForUpdate.place(x = 720, y = 750)

        self.TotalEntryForUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 18), width=10, textvar=self.TotDeal)
        self.TotalEntryForUpdate.place(x = 880, y = 750)

        def updateBill(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/UpdateRoUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/UpdateRo.png"
            self.DealerImageBill = PhotoImage(file=position+ImageName)
            self.updateDealer.configure(image=self.DealerImageBill)
            self.updateDealer.image = self.DealerImageBill

        self.DealerImage = PhotoImage(file=position+"/Requirements/UpdateRo.png")
        self.updateDealer = ttk.Label(
            self.frame_ce, image=self.DealerImage, background="white")
        self.updateDealer.image = self.DealerImage
        self.updateDealer.place(x=1155, y=730)

        self.updateDealer.bind("<Enter>", updateBill)
        self.updateDealer.bind("<Leave>", updateBill)
        self.updateDealer.bind("<Button-1>", lambda event: self.ChangeUpdateRoundForDeal())

        with sql.connect(position + "/Pass/%s"%self.database) as DealerData:
            DD = DealerData.cursor()
            DD.execute(''' SELECT * FROM %s'''%self.Name)
            data = DD.fetchall()
            DealerData.commit()
            DDeatil = DealerData.cursor()
            DDeatil.execute(
                ''' SELECT * FROM %s WHERE %s = (?)'''%(self.DorC, self.CNorCN), (self.Name, ))
            dataDeatil = DDeatil.fetchall()
            DealerData.commit()
        try:
            self.AddressLabel1 = ttk.Label(
                self.frame_ce, text=dataDeatil[0][3][0:33], font=("Helvetica", 20), foreground="#0077FF", background="white")
            self.AddressLabel1.place(x = 600, y = 5)

            self.AddressLabel2 = ttk.Label(
                self.frame_ce, text=dataDeatil[0][3][33:67], font=("Helvetica", 20), foreground="#0077FF", background="white")
            self.AddressLabel2.place(x = 600, y = 55)

            self.PhoneLabel = ttk.Label(
                self.frame_ce, text=dataDeatil[0][4], font=("Helvetica", 20), foreground="#0077FF", background = "white")
            self.PhoneLabel.place(x = 170, y = 100)
        except: pass


        def getFromTree(event):
            self.DateEntryForUpdate.delete(0, END)
            self.RsEntryForUpdate.delete(0, END)
            self.ProductEntryForUpdate.delete(0, END)
            self.NOMEntryForUpdate.delete(0, END)
            self.NetEntryForUpdate.delete(0, END)
            self.TotalEntryForUpdate.delete(0, END)
            try:
                item = self.HoleView.selection()[0]
                self.DATEde = self.HoleView.item(item, "text")
                valueOfData = self.HoleView.item(item, "values")
                self.DateEntryForUpdate.insert(END, self.DATEde)
                self.RUPEEDEL = valueOfData[0]
                self.PRODUCTDEL = valueOfData[1]
                self.NOMDEL = valueOfData[2]
                self.NETDEL = valueOfData[3]
                self.TOTALDEL = valueOfData[4]
                self.RsEntryForUpdate.insert(END, self.RUPEEDEL)
                self.ProductEntryForUpdate.insert(END, self.PRODUCTDEL)
                self.NOMEntryForUpdate.insert(END, self.NOMDEL)
                self.NetEntryForUpdate.insert(END, self.NETDEL)
                self.TotalEntryForUpdate.insert(END, self.TOTALDEL)
            except: pass

        for index, row in enumerate(data):
            self.HoleView.insert("", "end",text = row[1], values = (row[2], row[3], row[4], row[5], row[6]))

        def deleteCol(event):
            item = self.HoleView.selection()[0]
            self.DATEde = self.HoleView.item(item, "text")
            valueOfData = self.HoleView.item(item, "values")

            with sql.connect(position + "/Pass/%s"%self.database) as DealerUpdate:
                CD = DealerUpdate.cursor()
                CD.execute('''DELETE FROM %s WHERE DateData = ? AND RS = ? AND PRODUCT = ? AND NOM = ? AND NET = ? AND TOTAL = ?'''%Name, (self.DATEde, valueOfData[0], valueOfData[1], valueOfData[2], valueOfData[3], valueOfData[4]))
                DealerUpdate.commit()
            self.HoleView.delete(item)
        
        self.HoleView.bind("<Double-1>", getFromTree)
        self.HoleView.bind("<Delete>", deleteCol)

        self.ScrollHoleView = ttk.Scrollbar(self.frame_ce, orient="vertical", command=self.HoleView.yview)
        self.HoleView.configure(yscrollcommand=self.ScrollHoleView.set)
        self.ScrollHoleView.place(x=1215, y=150, height=560)
        self.DealerShowImage.bind(
            "<Button-1>", lambda event: self.DealerDeatiles(self.Name))

    def UpdateFirstForDeal(self, Name):
        try:
            inDate = self.DateDeal.get()
            inRupee = self.RsDeal.get()
            inProduct = self.ProDeal.get()
            inNOM = self.NOMDeal.get()
            inNet = self.NetDeal.get()
            inTotal = self.TotDeal.get()
            with sql.connect(position + "/Pass/%s"%self.database) as DealerUpdate:
                CD = DealerUpdate.cursor()
                CD.execute(''' SELECT * FROM %s'''%Name)
                CD.execute('''UPDATE %s SET DateData = ?, RS = ?, PRODUCT = ?, NOM = ?, NET = ?, TOTAL = ? WHERE DateData = ? AND RS = ? AND PRODUCT = ? AND NOM = ? AND NET = ? AND TOTAL = ?'''%Name, (inDate, inRupee, inProduct, inNOM, inNet, inTotal, self.DATEde, self.RUPEEDEL, self.PRODUCTDEL, self.NOMDEL, self.NETDEL, self.TOTALDEL))
                DealerUpdate.commit()
            self.HoleView.delete(*self.HoleView.get_children())
            with sql.connect(position + "/Pass/%s"%self.database) as DealerUpdate:
                CD = DealerUpdate.cursor()
                CD.execute(''' SELECT * FROM %s''' % Name)
                data = CD.fetchall()
                for rowNext in data:
                    self.HoleView.insert("", "end",text = rowNext[1], values = (rowNext[2], rowNext[3], rowNext[4], rowNext[5], rowNext[6]))
                DealerUpdate.commit()
            self.DateEntryForUpdate.delete(0, END)
            self.RsEntryForUpdate.delete(0, END)
            self.ProductEntryForUpdate.delete(0, END)
            self.NetEntryForUpdate.delete(0, END)
            self.NOMEntryForUpdate.delete(0, END)
            self.TotalEntryForUpdate.delete(0, END)
            
        except:
            pass

    def DealerMoney(self, Name):
        self.Name = Name
        self.ChangingDictDeal["Pos"] = "Pro"
        self.HoleView.destroy()
        self.ScrollHoleView.destroy()
        self.DateEntryForUpdate.destroy()
        self.RsEntryForUpdate.destroy()
        self.ProductEntryForUpdate.destroy()
        self.NOMEntryForUpdate.destroy()
        self.NetEntryForUpdate.destroy()
        self.TotalEntryForUpdate.destroy()

        self.HoleViewForMoney = ttk.Treeview(self.frame_ce, selectmode='browse')
        self.HoleViewForMoney["columns"]=("Rs", "Product","NOM", "Net.Wt", "Total")
        self.HoleViewForMoney.column("#0", stretch = NO, minwidth = 300, width = 300, anchor = CENTER)
        self.HoleViewForMoney.column("#1", stretch = NO, minwidth = 300, width = 300, anchor = CENTER)
        self.HoleViewForMoney.column("#2", stretch = NO, minwidth = 300, width = 300, anchor = CENTER)
        self.HoleViewForMoney.column("#3", stretch = NO, minwidth = 300, width = 300, anchor = CENTER)

        self.HoleViewForMoney.heading("#0", text = "Date")
        self.HoleViewForMoney.heading("#1", text = "Today")
        self.HoleViewForMoney.heading("#2", text = "Credited")
        self.HoleViewForMoney.heading("#3", text = "Debit")

        self.HoleViewForMoney.place(x = 0, y = 150, width = 1230, height = 560)

        self.DE = StringVar()
        self.TEM = StringVar()
        self.CEM = StringVar()
        self.DEM = StringVar()

        self.DateEntryForMoneyUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 20), width=10, textvar = self.DE)
        self.DateEntryForMoneyUpdate.place(x = 20, y = 750)
        self.DateEntryForMoneyUpdate.insert(END, datetime.date.today())

        self.TotalEntryForMoneyUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 20), width=10, textvar = self.TEM)
        self.TotalEntryForMoneyUpdate.place(x = 250, y = 750)

        self.CreditEntryForMoneyUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 20), width=10, textvar = self.CEM)
        self.CreditEntryForMoneyUpdate.place(x = 500, y = 750)

        self.DebitEntryForMoneyUpdate = ttk.Entry(
            self.frame_ce, font=("Helvetica", 20), width=10, textvar = self.DEM)
        self.DebitEntryForMoneyUpdate.place(x=750, y=750)
        self.DebitEntryForMoneyUpdate.bind(
            "<FocusIn>", lambda event: self.CollectingDebit(self.Name))

        def AddBill(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/AddRoUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/AddRo.png"
            self.DealerImageBill = PhotoImage(file=position+ImageName)
            self.AddDealer.configure(image=self.DealerImageBill)
            self.AddDealer.image = self.DealerImageBill

        self.DealerImage = PhotoImage(file=position+"/Requirements/AddRo.png")
        self.AddDealer = ttk.Label(
            self.frame_ce, image=self.DealerImage, background="white")
        self.AddDealer.image = self.DealerImage
        self.AddDealer.place(x=1050, y=732)

        self.AddDealer.bind("<Enter>", AddBill)
        self.AddDealer.bind("<Leave>", AddBill)
        self.AddDealer.bind("<Button-1>", lambda event: self.AddMoney(self.Name))

        with sql.connect(position + "/Pass/%s"%self.database) as DealerMoney:
            DM = DealerMoney.cursor()
            DM.execute(''' SELECT * FROM %s'''%(self.Name + "MONEY"))
            MoneyData = DM.fetchall()
            DealerMoney.commit()
        

        def getFromMoneyTree(event):
            self.DateEntryForMoneyUpdate.delete(0, END)
            self.TotalEntryForMoneyUpdate.delete(0, END)
            self.CreditEntryForMoneyUpdate.delete(0, END)
            self.DebitEntryForMoneyUpdate.delete(0, END)

            item = self.HoleViewForMoney.selection()[0]
            self.DATEm = self.HoleViewForMoney.item(item, "text")
            valueOfData = self.HoleViewForMoney.item(item, "values")
            self.DateEntryForMoneyUpdate.insert(END, self.DATEm)
            self.TOTALm = valueOfData[0]
            self.CREDITm = valueOfData[1]
            self.DEBITm = valueOfData[2]
            self.TotalEntryForMoneyUpdate.insert(END, self.TOTALm)
            self.CreditEntryForMoneyUpdate.insert(END, self.CREDITm)
            self.DebitEntryForMoneyUpdate.insert(END, self.DEBITm)

        for money in MoneyData:
            self.HoleViewForMoney.insert("", "end",text = money[1], values = (money[2], money[4], money[3]))

        def deleteColMon(event):
            item = self.HoleViewForMoney.selection()[0]
            self.DATEde = self.HoleViewForMoney.item(item, "text")
            valueOfData = self.HoleViewForMoney.item(item, "values")

            with sql.connect(position + "/Pass/%s"%self.database) as DealerMoney:
                CD = DealerMoney.cursor()
                CD.execute('''DELETE FROM %s WHERE DateData = ? AND TOTAL = ? AND DEBIT = ? AND CREDITED = ?'''%str(self.Name+"Money"), (self.DATEde, valueOfData[0], valueOfData[1], valueOfData[2]))
                DealerMoney.commit()
            self.HoleViewForMoney.delete(item)

        self.HoleViewForMoney.bind("<Double-1>", getFromMoneyTree)
        self.HoleViewForMoney.bind("<Delete>", deleteColMon)

        self.ScrollHoleMoneyView = ttk.Scrollbar(
            self.frame_ce, orient="vertical", command=self.HoleViewForMoney.yview)
        self.HoleViewForMoney.configure(yscrollcommand=self.ScrollHoleMoneyView.set)
        self.ScrollHoleMoneyView.place(x=1215, y=150, height=560)

    def CollectingDebit(self, name):
        with sql.connect(position + "/Pass/%s"%self.database) as DealerMoney:
            DM = DealerMoney.cursor()
            DM.execute(
                '''SELECT DEBIT FROM %s ORDER BY NUM DESC LIMIT 1''' % (name+"MONEY"))
            lastDebt = DM.fetchall()
            DealerMoney.commit()
        credit = self.CEM.get()

        try:
            nowDebit = int(lastDebt[0][0]) + int(self.TEM.get()) - int(credit)
            self.DebitEntryForMoneyUpdate.delete(0, END)
            self.DebitEntryForMoneyUpdate.insert(END, str(nowDebit))
        except:
            pass


    def AddMoney(self, name):
        date = self.DE.get()
        tot = self.TEM.get()
        credit = self.CEM.get()
        debit = self.DEM.get()
        with sql.connect(position + "/Pass/%s"%self.database) as DealerMoney:
            DM = DealerMoney.cursor()
            DM.execute(
                '''SELECT NUM FROM %s ORDER BY NUM DESC LIMIT 1''' % (name+"MONEY"))
            num = DM.fetchall()
            try:
                num = int(num[0][0]) + 1
            except:
                num = 1
            DM.execute('''INSERT INTO %s(NUM, DateData, TOTAL, DEBIT, CREDITED) VALUES(?, ?, ?, ?, ?)''' %(name+"MONEY"), (num, date, tot, debit, credit))
            DM.execute(''' SELECT * FROM %s'''%(self.Name + "MONEY"))
            MoneyData = DM.fetchall()
            DealerMoney.commit()
        self.HoleViewForMoney.delete(*self.HoleViewForMoney.get_children())
        for money in MoneyData:
            self.HoleViewForMoney.insert("", "end",text = money[1], values = (money[2], money[4], money[3]))
        self.TotalEntryForMoneyUpdate.delete(0, END)
        self.CreditEntryForMoneyUpdate.delete(0, END)
        self.DebitEntryForMoneyUpdate.delete(0, END)


    def UpdateMoneyFirstForDeal(self, Name):
        try:
            inDateMoney = self.DE.get()
            inTotalMoney = self.TEM.get()
            inCreditMoney = self.CEM.get()
            inDebitMoney = self.DEM.get()
            with sql.connect(position + "/Pass/%s"%self.database) as DealerMoneyUpdate:
                CDM = DealerMoneyUpdate.cursor()
                CDM.execute(''' SELECT * FROM %s'''%(Name + "MONEY"))
                CDM.execute('''UPDATE %s SET DateData = ?, TOTAL = ?, DEBIT = ?, CREDITED = ? WHERE DateData = ? AND TOTAL = ? AND DEBIT = ? AND CREDITED = ?''' %(Name + "MONEY"), (inDateMoney, inTotalMoney, inDebitMoney, inCreditMoney, self.DATEm, self.TOTALm, self.DEBITm, self.CREDITm))  
                DealerMoneyUpdate.commit()
            self.HoleViewForMoney.delete(*self.HoleViewForMoney.get_children())
            with sql.connect(position + "/Pass/%s"%self.database) as DealerMoneyUpdate:
                CDM = DealerMoneyUpdate.cursor()
                CDM.execute(''' SELECT * FROM %s''' % (Name + "MONEY"))
                data = CDM.fetchall()
                for moneyNext in data:
                    self.HoleViewForMoney.insert("", "end", text=moneyNext[1], values=(
                        moneyNext[2], moneyNext[4], moneyNext[3]))
                DealerMoneyUpdate.commit()
            self.DateEntryForMoneyUpdate.delete(0, END)
            self.TotalEntryForMoneyUpdate.delete(0, END)
            self.CreditEntryForMoneyUpdate.delete(0, END)
            self.DebitEntryForMoneyUpdate.delete(0, END)

        except: pass


    def DealerDeatiles(self, Name):
        self.Name = Name
        self.DateEntryForUpdate.destroy()
        self.RsEntryForUpdate.destroy()
        self.ProductEntryForUpdate.destroy()
        self.NOMEntryForUpdate.destroy()
        self.NetEntryForUpdate.destroy()
        self.TotalEntryForUpdate.destroy()
        self.updateDealer.destroy()
        self.DealerShowImage.destroy()
        try:
            self.AddDealer.destroy()
        except:
            pass
        self.ChangeDealer.destroy()
        self.HoleView.destroy()
        self.ScrollHoleView.destroy()
        self.AddressLabel1.destroy()
        self.AddressLabel2.destroy()
        self.PhoneLabel.destroy()
        Deal = PhotoImage(file = position + "/Requirements/contacts.png")
        self.DealerShowImageDL = ttk.Label(
            self.frame_ce, image=Deal, background="white")
        self.DealerShowImageDL.image = Deal
        self.DealerShowImageDL.place(x = 450, y = 20)
        self.DealerName.place(x = 470, y = 220)

        try:
            self.HoleViewForMoney.destroy()
            self.DateEntryForMoneyUpdate.destroy()
            self.TotalEntryForMoneyUpdate.destroy()
            self.CreditEntryForMoneyUpdate.destroy()
            self.DebitEntryForMoneyUpdate.destroy()
            self.ScrollHoleMoneyView.destroy()
        except:
            pass


        self.DistributorNameReUpdate = StringVar()
        self.CompanyNameReUpdate = StringVar()
        self.PhoneNameForDisReUpdate = StringVar()

        with sql.connect(position + "/Pass/%s"%self.database) as DealerData:
            DD = DealerData.cursor()
            DD.execute(''' SELECT * FROM %s WHERE %s = (?)'''%(self.DorC, self.CNorCN), (self.Name, ))
            self.dataForReUp = DD.fetchall()
            DealerData.commit()
        self.NameEntryForDisReUpdate = ttk.Entry(
            self.frame_ce, textvar=self.DistributorNameReUpdate, foreground="black", width=25, font=("Helvetica", 20))
        self.NameEntryForDisReUpdate.place(x=360, y=300, height=50)
        self.NameEntryForDisReUpdate.insert(0, str(self.dataForReUp[0][2]))

        self.AddressEntryReUpdate = Text(
            self.frame_ce, foreground="black", width=25, font=("Helvetica", 20), relief="ridge")
        self.AddressEntryReUpdate.place(x=360, y=375, height=100)
        self.AddressEntryReUpdate.insert(END, str(self.dataForReUp[0][3]))

        self.PhoneEntryReUpdate = ttk.Entry(
            self.frame_ce, textvar=self.PhoneNameForDisReUpdate, foreground="black", width=25, font=("Helvetica", 20))
        self.PhoneEntryReUpdate.place(x=360, y=495, height=50)
        self.PhoneEntryReUpdate.insert(0, str(self.dataForReUp[0][4]))

        def updateChangeReUp(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/UpdateUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Update.png"
            self.CustomerImageChangeReUp = PhotoImage(file=position+ImageName)
            self.updateCustomerReUp.configure(image=self.CustomerImageChangeReUp)
            self.updateCustomerReUp.image = self.CustomerImageChangeReUp

        self.CustomerImageReUp = PhotoImage(file=position+"/Requirements/Update.png")
        self.updateCustomerReUp = ttk.Label(
            self.frame_ce, image=self.CustomerImageReUp, background="white")
        self.updateCustomerReUp.image = self.CustomerImageReUp
        self.updateCustomerReUp.place(x=460, y=570)

        self.updateCustomerReUp.bind("<Enter>", updateChangeReUp)
        self.updateCustomerReUp.bind("<Leave>", updateChangeReUp)
        self.updateCustomerReUp.bind("<Button-1>", lambda event : self.ReUpdate(self.Name))

    def ReUpdate(self, Name):
        DisNameUp = self.DistributorNameReUpdate.get()
        address = self.AddressEntryReUpdate.get("1.0", "end-1c")
        phone = self.PhoneNameForDisReUpdate.get()
        try:
            with sql.connect(position + "/Pass/%s"%self.database) as DealerUp:
                DU = DealerUp.cursor()
                DU.execute(''' UPDATE %s SET %s = ?, COMPANYADDRESS = ?, PHONENUMBER = ? WHERE %s = ?'''%(self.DorC, self.nameName, self.CNorCN),(DisNameUp, address, phone, Name))
                DealerUp.commit()
            self.add()
        except: pass

    
    def ChangeWindow(self):
        if self.ChangingDictDeal["Pos"] == "Pro":
            self.InsideOfShowMember(self.Name)
        elif self.ChangingDictDeal["Pos"] == "Money":
            self.DealerMoney(self.Name)

    def ChangeUpdateRoundForDeal(self):
        if self.ChangingDictDeal["Pos"] == "Pro":
            self.UpdateMoneyFirstForDeal(self.Name)
        elif self.ChangingDictDeal["Pos"] == "Money":
            self.UpdateFirstForDeal(self.Name)
