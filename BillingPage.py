
# Billing Page of eik-B

from tkinter import Frame, Canvas, Text, PhotoImage, StringVar, font, END, Scrollbar, ALL, IntVar
from tkinter import ttk
from os import getcwd, listdir, startfile
import sqlite3 as sql
from MemberShow import MemberShow
import datetime
from fpdf import FPDF

position = getcwd()

class Billing(Frame):
    def __init__(self, master, **kwarks):
        Frame.__init__(self, master, **kwarks)
        self.font = font.Font(family="Roboto", size=33)

    def billingPage(self, event=None):
        self.stframe = Frame(self, width=1286,
                             height=841, background="#FDFEFE")
        self.stframe.pack()
        self.billing_txt = ttk.Label(self.stframe, text="BILLING",
                              background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.billing_txt.place(x=35, y=5)
        self.CustomerName = ttk.Label(
            self.stframe, text="Customer Name", background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.CustomerName.place(x = 75, y = 100)
        self.DealerName = ttk.Label(self.stframe, text="Company Name", background="#FDFEFE", foreground="#0077FF", font=self.font)
        self.DealerName.place(x = 570, y = 100)

        self.CustomerGet = StringVar()
        self.DealerGet = StringVar()
        CustomerValues = []
        DealerValues = []
        vegetables = ["Amaranth","Arugula","Beet","Bok choy","Borage greens","Broccoli","Brooklime","Brussels sprouts","Cabbage","Catsear","Celery","Celtuce","Chaya","Chickweed","Chicory",
        "Chinese mallow","Garland Chrysanthemum","Collard greens","Common purslane","Corn salad","Cress","Dandelion","Dill","Endive","Fat hen","Fiddlehead","Athyrium","Fluted pumpkin","Garden rocket","Golden samphire","Good King Henry","Grape","Greater plantain","Kai-lan","Kale","Komatsuna","Kuka","Lagos bologi","Lamb's lettuce","Lamb's quarters","Land cress","Lettuce Lactuca","Lizard's tail","Malabar","Mallow","Melokhia","Corchorus","Miner's","Mizuna greens","Mustard","Napa cabbage"]


        with sql.connect(position + "/Pass/veg.db") as veg:
            Veg = veg.cursor()
            Veg.execute(''' CREATE TABLE IF NOT EXISTS Veg(NUM INT, NAMES TEXT NOT NULL PRIMARY KEY)''')
            for i, j in enumerate(vegetables):
                try:
                    Veg.execute('''INSERT INTO Veg(NUM, NAMES) VALUES(?, ?)''', (i+1, j))
                except: pass
            veg.commit()

        with sql.connect(position+"/Pass/"+"Customer-data.db") as CustomerData:
            CD = CustomerData.cursor()
            CD.execute(''' CREATE TABLE IF NOT EXISTS Customer(NUM INT, CUSTOMERNAME TEXT NOT NULL PRIMARY KEY, COMPANYNAME TEXT, COMPANYADDRESS TEXT, PHONENUMBER TEXT) ''')
            CustomerData.commit()

        with sql.connect(position+"/Pass/"+"Dealer-data.db") as DealerData:
            DD = DealerData.cursor()
            DD.execute(
                ''' CREATE TABLE IF NOT EXISTS Dealer(NUM INT, COMPANYNAME TEXT NOT NULL PRIMARY KEY, DEALERNAME TEXT, COMPANYADDRESS TEXT, PHONENUMBER TEXT) ''')
            DealerData.commit()

        def getName(getName):
            if getName == "Dealer":
                textvar = self.DealerGet
                databaseName = "Dealer-data.db"
                table = "Dealer"
                column = "COMPANYNAME"
                ArrayofData = DealerValues
                boxName = self.ComboFroSelectDealer
            elif getName == "Customer":
                textvar = self.CustomerGet
                databaseName = "Customer-data.db"
                table = "Customer"
                column = "CUSTOMERNAME"
                ArrayofData = CustomerValues
                boxName = self.ComboFroSelect
            cusName = textvar.get()
            lencus = len(cusName)
            with sql.connect(position + "/Pass/%s"%databaseName) as Data:
                DD = Data.cursor()
                DD.execute('''SELECT %s FROM %s'''%(column, table))
                DataSelect = DD.fetchall()
                for lentch in DataSelect:
                    if lencus > 0:
                        if lentch[0][0:lencus] == cusName.capitalize():
                            ArrayofData.append(lentch[0])
                            ArrayofData.sort()
                        if lentch[0][0:lencus] == cusName.lower():
                            ArrayofData.append(lentch[0])
                            ArrayofData.sort()
                    else:
                        ArrayofData.clear()
                Data.commit()
            boxName.config(values=list(set(ArrayofData)))
            ArrayofData.clear()

        self.ComboFroSelect = ttk.Combobox(
            self.stframe, values=CustomerValues, textvar=self.CustomerGet, font=("Helvetica", 20))
        self.bigfont = font.Font(family="Helvetica", size=20)
        self.option_add("*TCombobox*Listbox*Font", self.bigfont)
        self.ComboFroSelect.place(x = 65, y = 180)
        self.ComboFroSelect.bind("<KeyPress>", lambda event: getName("Customer"))

        self.ComboFroSelectDealer = ttk.Combobox(
            self.stframe, values=DealerValues, textvar=self.DealerGet, font=("Helvetica", 20))
        self.bigfont = font.Font(family="Helvetica", size=20)
        self.option_add("*TCombobox*Listbox*Font", self.bigfont)
        self.ComboFroSelectDealer.place(x = 565, y = 180)
        self.ComboFroSelectDealer.bind("<KeyPress>", lambda event: getName("Dealer"))

        def BillChange(event, buttonNum):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/BillUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Bill.png"
            self.BillImageChange = PhotoImage(file=position+ImageName)
            if buttonNum == 1:
                self.Bill.configure(image=self.BillImageChange)
                self.Bill.image = self.BillImageChange
            elif buttonNum == 2:
                self.BillForDeal.configure(image=self.BillImageChange)
                self.BillForDeal.image = self.BillImageChange

        self.BillImage = PhotoImage(file=position+"/Requirements/Bill.png")
        self.Bill = ttk.Label(
            self.stframe, image=self.BillImage, background="white")
        self.Bill.image = self.BillImage
        self.Bill.place(x=140, y=245)

        self.BillForDeal = ttk.Label(
            self.stframe, image=self.BillImage, background="white")
        self.BillForDeal.image = self.BillImage
        self.BillForDeal.place(x=650, y=245)

        self.Bill.bind("<Enter>", lambda event:BillChange(event, 1))
        self.Bill.bind("<Leave>", lambda event:BillChange(event, 1))
        self.Bill.bind("<Button-1>", lambda event :self.BillingSys("Customer"))

        self.BillForDeal.bind("<Enter>", lambda event:BillChange(event, 2))
        self.BillForDeal.bind("<Leave>", lambda event: BillChange(event, 2))
        self.BillForDeal.bind("<Button-1>", lambda event: self.BillingSys("Dealer"))

    def BillingSys(self, DRC):
        self.DRC = DRC
        self.CustomerName.destroy()
        self.DealerName.destroy()
        self.ComboFroSelect.destroy()
        self.ComboFroSelectDealer.destroy()
        self.Bill.destroy()
        self.BillForDeal.destroy()
        self.billing_txt.destroy()
        
        Customer = PhotoImage(file = position + "/Requirements/contacts.png")
        self.CustomerShowImage = ttk.Label(self.stframe, image = Customer, background = "white")
        self.CustomerShowImage.image = Customer
        self.CustomerShowImage.place(x=35, y=5)

        def smallup(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/Updatesmallup.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Updatesmall.png"
            self.updatesmall = PhotoImage(file=position+ImageName)
            self.upsmallShowImage.configure(image=self.updatesmall)
            self.upsmallShowImage.image = self.updatesmall

        upsmall = PhotoImage(file = position + "/Requirements/Updatesmall.png")
        self.upsmallShowImage = ttk.Label(self.stframe, image = upsmall, background = "white")
        self.upsmallShowImage.image = upsmall
        self.upsmallShowImage.place(x=1000, y=95)

        self.upsmallShowImage.bind("<Enter>", smallup)
        self.upsmallShowImage.bind("<Leave>", smallup)

        global BillingName
        if self.DRC == "Customer":
            self.CusBill = self.CustomerGet.get()
            BillingName = self.CusBill
        elif self.DRC == "Dealer":
            self.CusBill = self.DealerGet.get()
            BillingName = self.CusBill

        self.CustomerNameBill = ttk.Label(
            self.stframe, text=self.CusBill, font=self.font, foreground="#0077FF", background="white")
        self.CustomerNameBill.place(x = 210, y = 5)

        self.DateVar = StringVar()
        self.DateEntry = ttk.Entry(self.stframe, font=(
            "Helvetica", 20), width=10, foreground="black", textvar = self.DateVar)
        self.DateEntry.insert(END, str(datetime.date.today()))
        self.DateEntry.place(x = 225, y = 80)

        image_names = ["ExNo.png", "Date.png", "Rs.png", "Product.png",
                       "NOM.png", "Net.png", "Total.png"]
        listHead = []

        for li in range(7):
            listHead.insert(li, PhotoImage(file = position + "/Requirements/" + image_names[li]))
        
        Heading = ttk.Label(self.stframe, image = listHead[0], background = "#0077FF")
        Heading.image = listHead[0]
        Heading.place(x = 0, y = 170)

        Heading1 = ttk.Label(
            self.stframe, image=listHead[1], background="#0077FF")
        Heading1.image = listHead[1]
        Heading1.place(x = 25, y = 170)

        Heading2 = ttk.Label(
            self.stframe, image=listHead[2], background="#0077FF")
        Heading2.image = listHead[2]
        Heading2.place(x = 180, y = 170)

        Heading3 = ttk.Label(
            self.stframe, image=listHead[3], background="#0077FF")
        Heading3.image = listHead[3]
        Heading3.place(x = 350, y = 170)

        Heading4 = ttk.Label(
            self.stframe, image=listHead[4], background="#0077FF")
        Heading4.image = listHead[4]
        Heading4.place(x = 600, y = 170)

        Heading5 = ttk.Label(
            self.stframe, image=listHead[5], background="#0077FF")
        Heading5.image = listHead[5]
        Heading5.place(x = 800, y = 170)

        Heading6 = ttk.Label(
            self.stframe, image=listHead[6], background="#0077FF")
        Heading6.image = listHead[6]
        Heading6.place(x = 1010, y = 170)

        self.BillingFrame = Frame(self.stframe, background = "white", width = 1230, height = 523)
        self.BillingFrame.place(x = 0, y = 227)

        self.BillingCanvas = Canvas(
            self.BillingFrame, background="white", width=1230, height=523)
        
        self.BillingCanvas.yview_moveto(0)

        self.BillingInsideFrame = Frame(
            self.BillingCanvas, background="#0077FF", width=1230, height=523)
        
        self.ScrollBillView = ttk.Scrollbar(self.BillingFrame)

        def myfunction(event):
            self.BillingCanvas.configure(scrollregion=self.BillingCanvas.bbox(ALL))
 
        self.ScrollBillView.place(x=1215, y=2, height=523)
        self.BillingCanvas.place(x = 0, y = 0)
        self.ScrollBillView.config(
            orient="vertical", command=self.BillingCanvas.yview)
        self.BillingCanvas.create_window((700, 523), window = self.BillingInsideFrame)
        self.fontDe = font.Font(family="Adobe Fan Heiti Std", size=25)

        self.Debit = ttk.Label(self.stframe, text="Debit",
                               background="white", foreground="#0077FF", font=self.fontDe)
        self.Debit.place(x = 20, y = 760)

        self.DebitVar = IntVar()
        self.TotalVar = IntVar()
        self.PayVar = IntVar()
        self.CoolieVar = IntVar()

        self.DebitEntry = ttk.Entry(
            self.stframe, textvar=self.DebitVar, font=("Helvetica", 20), width=8)
        self.DebitEntry.place(x = 120, y = 763)
        self.DebitEntry.bind("<FocusIn>", lambda event : self.DebitEntry.select_range(0, END))

        try:
            with sql.connect(position + "/Pass/%s"%(str(self.DRC)+"-data.db")) as debitdata:
                DD = debitdata.cursor()
                DD.execute('''SELECT DEBIT FROM %s ORDER BY NUM DESC'''%(self.CusBill+"MONEY"))
                debit = DD.fetchall()
                self.DebitEntry.delete(0, END)
                self.DebitEntry.insert(END, int(debit[0][0]))
        except:
            self.DebitEntry.insert(END, 0)
        
        global det
        det = self.DebitVar.get()

        self.Total = ttk.Label(self.stframe, text="Total",
                               background="white", foreground="#0077FF", font=self.fontDe)
        self.Total.place(x = 250, y = 765)

        self.TotalBox = ttk.Entry(
            self.stframe, textvar=self.TotalVar, font=("Helvetica", 20), width=8)
        self.TotalBox.place(x = 350, y = 770)
        self.TotalBox.bind("<FocusIn>", lambda event : self.TotalBox.select_range(0, END))

        self.Pay = ttk.Label(self.stframe, text="Pay",
                               background="white", foreground="#0077FF", font=self.fontDe)
        self.Pay.place(x = 480, y = 765)

        self.PayBox = ttk.Entry(
            self.stframe, textvar=self.PayVar, font=("Helvetica", 20), width=8)
        self.PayBox.place(x = 560, y = 765)
        self.PayBox.bind("<FocusIn>", lambda event : self.PayBox.select_range(0, END))

        self.Coolie = ttk.Label(self.stframe, text="Fright",
                               background="white", foreground="#0077FF", font=self.fontDe)
        self.Coolie.place(x = 690, y = 765)

        self.CoolieBox = ttk.Entry(
            self.stframe, textvar=self.CoolieVar, font=("Helvetica", 20), width=8)
        self.CoolieBox.place(x = 810, y = 770)
        self.CoolieBox.bind(
            "<FocusIn>", lambda event: self.CoolieBox.select_range(0, END))

        def debitGet(event):
            try:
                tot = self.TotalVar.get()
                pay = self.PayVar.get()
                fright = self.CoolieVar.get()
                debit = (tot + fright - pay) + det
                if debit > 0:
                    self.DebitEntry.delete(0, END)
                    self.DebitEntry.insert(END, debit)
                else:
                    self.DebitEntry.delete(0, END)
                    self.DebitEntry.insert(END, 0)
            except: pass

        def Forfright(event):
            try:
                tot = self.TotalVar.get()
                fright = self.CoolieVar.get()
                debit = tot + fright + det
                self.DebitEntry.delete(0, END)
                self.DebitEntry.insert(END, debit)
            except: pass

        self.PayBox.bind("<KeyRelease>", debitGet)
        self.CoolieBox.bind("<KeyRelease>", Forfright)

        self.BillingCanvas.configure(yscrollcommand=self.ScrollBillView.set)
        self.BillingInsideFrame.bind("<Configure>", myfunction)

        for num in range(50):
            self.Num = ttk.Label(self.BillingInsideFrame, text=str(
                num + 1), background="#0077FF", foreground="white", font=("Helvetica", 15))
            self.Num.grid(row = num, column = 0)

        self.RsName = []
        self.DateName = []
        self.ProductName = []
        self.NomName = []
        self.NetName  = []
        self.TotName = []
        self.MainTotal = {}

        def CalculateTotal(markvalue):
            self.Boundary = markvalue
            pay = self.PayVar.get()
            self.Print.bind("<Button-1>", lambda event : self.PrintAndUpdate(self.DRC, self.Boundary))
            self.upsmallShowImage.bind("<Button-1>", lambda event : self.PrintAndUpdate(self.DRC, self.Boundary, "onlyup"))
            get_money = self.NetName[markvalue].get()
            if get_money != "":
                try:
                    self.TotEntry[markvalue].delete(0, END)
                    money = float(self.RsName[markvalue].get())
                    total = float(get_money) * money
                    if self.TotName[markvalue].get() != str(total):
                        self.TotEntry[markvalue].insert(END, str(total))
                        self.MainTotal[markvalue] = total
                        self.TotalBox.delete(0, END)
                        self.TotalBox.insert(END, sum(self.MainTotal.values()))
                        devalue = sum(self.MainTotal.values())+det-pay
                        self.DebitEntry.delete(0, END)
                        self.DebitEntry.insert(END, devalue)
                    else:   pass

                except:
                    pass
            else:
                try:
                    self.TotEntry[markvalue].delete(0, END)
                    money = float(self.RsName[markvalue].get())
                    non = float(self.NomName[markvalue].get())
                    total = money * non
                    if self.TotName[markvalue].get() != str(total):
                        self.TotEntry[markvalue].insert(END, str(total))
                        self.MainTotal[markvalue] = total
                        self.TotalBox.delete(0, END)
                        self.TotalBox.insert(END, sum(self.MainTotal.values()))
                        devalue = sum(self.MainTotal.values())+det-pay
                        self.DebitEntry.delete(0, END)
                        self.DebitEntry.insert(END, devalue) 
                    else:
                        pass

                except: pass

        VEGNAMES = []

        def getVegName(value):
            vegName = self.ProductName[value].get()
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
            self.ProEntry[value].config(values=list(set(VEGNAMES)))
            VEGNAMES.clear()

        def eval_link(x): return (lambda p: CalculateTotal(x))

        def eval_veg(x): return (lambda p: getVegName(x))

        def dateform(var):
            self.DateEntry[var].delete(0, END)
            self.DateEntry[var].insert(END, str(datetime.date.today()))

        def focusDate(x): 
            return (lambda event: dateform(x))

        def switchingEntry(box, x):
            if box == "rs":
                self.ProEntry[x].focus()
            elif box == "pro":
                self.NomEntry[x].focus()
            elif box == "nom":
                self.NetEntry[x].focus()
            elif box == "net":
                self.TotEntry[x].focus()
            elif box == "tot":
                self.DateEntry[x+1].focus()
            elif box == "Date":
                self.RsEntry[x].focus()

        def eval_switch(box, x): return (lambda p: switchingEntry(box, x))

        self.DateEntry = {}

        for Date in range(50):
            self.DateName.insert(Date, StringVar())
            self.DateEntry[Date] = ttk.Entry(
                self.BillingInsideFrame, font=("Helvetica", 20), width = 10, textvar = self.DateName[Date], foreground="black")
            self.DateEntry[Date].grid(row=Date, column=2)
            self.DateEntry[Date].bind("<Return>", eval_switch("Date", Date))
            self.DateEntry[Date].bind("<FocusIn>", focusDate(Date))
        
        self.DateEntry[0].focus()

        self.RsEntry = {}

        for Rs in range(50):
            self.RsName.insert(Rs, StringVar())
            self.RsEntry[Rs] = ttk.Entry(
                self.BillingInsideFrame, font=("Helvetica", 20), width = 11, textvar = self.RsName[Rs], foreground="black")
            self.RsEntry[Rs].grid(row=Rs, column=3)
            self.RsEntry[Rs].bind("<Return>", eval_switch("rs", Rs))
        

        self.ProEntry = {}

        for Pro in range(50):
            self.ProductName.insert(Pro, StringVar())
            self.ProEntry[Pro] = ttk.Combobox(
                self.BillingInsideFrame, font=("Helvetica", 20), width = 17, textvar = self.ProductName[Pro], foreground="black", values = VEGNAMES)
            self.ProEntry[Pro].grid(row=Pro, column=4)
            self.ProEntry[Pro].bind("<KeyPress>", eval_veg(Pro))
            self.ProEntry[Pro].bind("<Return>", eval_switch("pro", Pro))

        self.NomEntry = {}

        for Nom in range(50):
            self.NomName.insert(Nom, StringVar())
            self.NomEntry[Nom] = ttk.Entry(
                self.BillingInsideFrame, font=("Helvetica", 20), width=12, textvar=self.NomName[Nom], foreground="black")
            self.NomEntry[Nom].grid(row=Nom, column=5)
            self.NomEntry[Nom].bind("<Return>", eval_switch("nom", Nom))

        self.NetEntry = {}

        for Net in range(50):
            self.NetName.insert(Net, StringVar())
            self.NetEntry[Net] = ttk.Entry(
                self.BillingInsideFrame, font=("Helvetica", 20), width = 14, textvar = self.NetName[Net], foreground="black")
            self.NetEntry[Net].grid(row=Net, column=6)
            self.NetEntry[Net].bind("<Return>", eval_switch("net", Net))

        self.TotEntry = {}

        for Tot in range(50):
            self.TotName.insert(Tot, StringVar())
            self.TotEntry[Tot] = ttk.Entry(
                self.BillingInsideFrame, font=("Helvetica", 20), width=13, textvar=self.TotName[Tot], foreground="black")
            self.TotEntry[Tot].grid(row=Tot, column=7)
            self.TotEntry[Tot].bind("<FocusIn>", eval_link(Tot))
            self.TotEntry[Tot].bind("<Return>", eval_switch("tot", Tot))

        def PrintChange(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/PrintUp.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/Print.png"
            self.PrintImageChange = PhotoImage(file=position+ImageName)
            self.Print.configure(image=self.PrintImageChange)
            self.Print.image = self.PrintImageChange

        self.PrintImage = PhotoImage(file=position+"/Requirements/Print.png")
        self.Print = ttk.Label(
            self.stframe, image=self.PrintImage, background="white")
        self.Print.image = self.PrintImage
        self.Print.place(x=1050, y=770)

        self.Print.bind("<Enter>", PrintChange)
        self.Print.bind("<Leave>", PrintChange)
        try:
            bound = self.Boundary
            #, self.DRC))
        except: pass

    def PrintAndUpdate(self, DRC, Boundary, poru=None):
        todayDate = datetime.date.today()
        if DRC == "Customer":
            cusname = self.CustomerGet.get()
            databaseName = "Customer-data.db"
        elif DRC == "Dealer":
            cusname = self.DealerGet.get()
            databaseName = "Dealer-data.db"
        #today = self.DateVar.get()
        pdfdata = []
        CoolieEN = self.CoolieVar.get()
        try:
            with sql.connect(position + "/Pass/%s"%databaseName) as CustomerData:
                CD = CustomerData.cursor()
                for up in range(Boundary + 1):
                    today = self.DateName[up].get()
                    rupee = self.RsName[up].get()
                    product = self.ProductName[up].get()
                    nom = self.NomName[up].get()
                    net = self.NetName[up].get()
                    tot = self.TotName[up].get()
                    pdfdata.append([today, rupee, product, net, nom, tot])
                    CD.execute(''' INSERT INTO %s(NUM, DateData, RS, PRODUCT, NOM, NET, TOTAL) VALUES(?, ?, ?, ?, ?, ?, ?)''' % cusname,(up+1, today, rupee, product, nom, net, tot))
                CustomerData.commit()
        except: pass
        
        try:
            with sql.connect(position + "/Pass/%s"%databaseName) as Money:
                MD = Money.cursor()
                MD.execute('''SELECT * FROM %s'''%(self.CusBill + "MONEY"))
                MoneyData = len(MD.fetchall())
                moneydebit = self.DebitVar.get()
                moneytotal = self.TotalVar.get()
                moneypay = self.PayVar.get()
                fright = self.CoolieVar.get()
                MD.execute('''INSERT INTO %s(NUM, DateData, TOTAL, DEBIT, CREDITED) VALUES(?, ?, ?, ?, ?)'''%(self.CusBill + "MONEY"), (MoneyData+1, today, int(moneytotal)+int(CoolieEN), int(moneydebit), moneypay))
                Money.commit()
        except: pass
        
        if poru != "onlyup":
            datepa = self.DateVar.get()
            pdf = FPDF(format='A5', unit='mm')
            pdf.add_page()
            pdf.image(position + '/Requirements/ABNBill.jpg', x=4, y=2, w=140)
            pdf.set_font('Times','B',10.0)
            pdf.ln(30)
            HEADERS = ["Date", "Rs", "Product", "Net.Wt (Kg)", "NUM", "Total"]
            epw = pdf.w - 2*pdf.l_margin
            col_width = epw/6
            th = pdf.font_size
            pdf.ln(2*th)
            pdf.cell(10, 10, str(DRC + " : " + self.CusBill + "                                                                            Date : %s" % str(datepa)))
            pdf.ln(2*th)
            for head in HEADERS:
                pdf.cell(col_width, 2*th, str(head), border=1)
            pdf.ln(2*th)
            pdf.set_font('Times','',10.0)
            pdf.ln(0.5)
            for inr, row in enumerate(pdfdata):
                for datum in row:
                    pdf.cell(col_width, 2*th, str(datum), border=1)
                if (inr + 1)%19 == 0:
                    pdf.image(position + '/Requirements/ABNBill.jpg', x=4, y=2, w=140)
                    pdf.set_font('Times','B',10.0)
                    pdf.ln(30)
                    pdf.ln(2*th)
                    pdf.cell(10, 10, str(DRC + " : " + self.CusBill + "                                                                            Date : %s" % str(todayDate)))
                    pdf.ln(2*th)
                    for head in HEADERS:
                        pdf.cell(col_width, 2*th, str(head), border=1)
                    pdf.ln(2*th)
                    pdf.set_font('Times', '', 10.0)
                    pdf.ln(0.5)
                    for nineteen in pdfdata[inr]:
                        pdf.cell(col_width, 2*th, str(nineteen), border=1)

                pdf.ln(2*th)
            
            col_widthForFright = epw - epw/6
            
            pdf.cell(col_widthForFright, 2*th, "Fright : ", border=1)
            pdf.cell(col_width, 2*th, str(CoolieEN), border=1)
            
            pdf.ln(2*th)
            totalEn = self.TotalVar.get()
            pdf.set_font('Times', 'B', 16.0)
            pdf.cell(10, 10,str(59*" ")+"Today : %s" % str(int(moneytotal)+int(CoolieEN)))
            pdf.ln(2*th)
            pdf.cell(10, 10,str(59*" ")+"MunBill : %s" % str(det))
            pdf.ln(2*th)
            pdf.cell(10, 10, str(59*" ")+"Total : %s" % str(totalEn + CoolieEN + int(det)))

            filecheck = listdir(position + "/Pass")
            NameOF = str(BillingName) + str(datepa)  + "(1)"

            if NameOF + ".pdf" not in filecheck:
                printerPDF = str(NameOF) + ".pdf"
                pdf.output(position + '/Pass/' + printerPDF,'F')
            else:            
                temp = []
                for ins in filecheck:
                    if str(BillingName) + str(datepa) in ins:
                        temp.append(ins[-6])
                        maxval = max(temp)
                add = int(maxval) + 1
                printerPDF = NameOF.replace(NameOF[-2:], "%s)"%str(add)) + ".pdf"
                pdf.output(position + '/Pass/' + printerPDF ,'F')

            try:
                pdffile = position + "\\Pass\\" + printerPDF
                startfile(str(pdffile),'print')
            except:
                pass
        else:   pass
