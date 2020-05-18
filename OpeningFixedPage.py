# This page was always fixed for left side bar

from tkinter import Frame, PhotoImage, Canvas, BOTH, YES
from os import getcwd
from tkinter import ttk
from tkinter import Tk
from PassAndVegUpdate import UpdateWindow
from Dealer import DealerPage
from Customer import customer
from BillingPage import Billing

pnges = ['ABN.png', 'Space.png',
         "Dealer.png", "Billing.png", "Customer.png", "SpaceFill.png"]

change_pnges = ['ABN.png', 'Space1.png',
           "DealerUp.png", "BillingUp.png", "CustomerUp.png", "SpaceFillUp.png"]

founationButtons = []
upperButtons = []
switching_func = []

position = getcwd()

# Fixed Opening Page
class FixedPage(Frame):
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.parent.resizable(894, 649)
        self.parent.geometry("894x649+200+200")

    def LeftSideFixedPage(self):
        self.FrameLeft = Frame(self, width=200, height=841)
        self.FrameLeft.pack(side='left', anchor='w', fill='both')
        self.CanvasLeft = Canvas(self.FrameLeft, width=200, height=850, borderwidth=10, background="#8E44AD")
        self.CanvasLeft.pack(side='left', anchor='w', fill='both')
        self.MenuOutLayout = PhotoImage(file=position + "/Requirements/MenuOut.png")
        self.MenuOut = ttk.Label(self.CanvasLeft, image=self.MenuOutLayout)
        self.MenuOut.image = self.MenuOutLayout
        self.MenuOut.pack(side='left', anchor='w', fill='both')

        self.FrameRight = Frame(self, width=1286,
                              height=841, background="#FDFEFE")
        self.FrameRight.pack(fill='both', expand=True, anchor='n')
        self.listlabel = []
        self.ImageButtonPull()

    def ImageButtonPull(self):
        for first in range(len(pnges)):
            for second in range(len(change_pnges)):
                if first == second:
                    sidebarImages = PhotoImage(file=position+'/Requirements/'+pnges[first])
                    foundationLabels = ttk.Label(self.MenuOut, image=sidebarImages, background='#0077FF')
                    founationButtons.append(foundationLabels)
                    foundationLabels.image = sidebarImages

                    row = first
                    if founationButtons.index(foundationLabels) < 6:
                        foundationLabels.grid(row=row, column=0)
                    else:
                        pass

                    upperSidebarImages = PhotoImage(
                        file=position + "/Requirements/" + change_pnges[second])
                    upperLabels = ttk.Label(
                        self.MenuOut, image=upperSidebarImages, background='#64ACFE')
                    upperButtons.append(upperLabels)
                    upperLabels.image = upperSidebarImages
                else:
                    pass
        self.design()

    def design(self):
        def call_2(event):
            upperButtons[2].grid_forget()
            founationButtons[2].grid(row=2, column=0)

        def call_3(event):
            upperButtons[3].grid_forget()
            founationButtons[3].grid(row=3, column=0)

        def call_4(event):
            upperButtons[4].grid_forget()
            founationButtons[4].grid(row=4, column=0)

        founationButtons[2].bind("<Enter>", lambda v: upperButtons[2].grid(row=2, column=0))
        upperButtons[2].bind("<Leave>", call_2)
        founationButtons[3].bind(
            "<Enter>", lambda v: upperButtons[3].grid(row=3, column=0))
        upperButtons[3].bind("<Leave>", call_3)
        founationButtons[4].bind(
            "<Enter>", lambda v: upperButtons[4].grid(row=4, column=0))
        upperButtons[4].bind("<Leave>", call_4)
#        upperButtons[3].bind("<Button-1>", self.stock_page)
        upperButtons[2].bind("<Button-1>", self.DealerOpenFunc)
        upperButtons[4].bind("<Button-1>", self.CustomerOpenFunc)
        upperButtons[3].bind("<Button-1>", self.BillingOpenFunc)
        founationButtons[0].bind("<Double-1>", self.PassAndVegUpdateFunc)
        self.parent.protocol("WM_DELETE_WINDOW",
                             lambda: self.PassAndVegUpdateFunc("destroy"))
    
    def PassAndVegUpdateFunc(self, event):
        global anotherWindowForUpdate
        if event != "destroy":
            anotherWindowForUpdate = UpdateWindow()
            anotherWindowForUpdate.WindowOfUpdate()
            anotherWindowForUpdate.mainloop()

        elif event == "destroy":
            try:
                self.parent.destroy()
                anotherWindowForUpdate.destroy()
            except: pass

    def DealerOpenFunc(self, event):
        self.design()
        upperButtons[2].bind(
            "<Leave>", lambda b: upperButtons[2].grid(in_=founationButtons[2]))
        upperButtons[3].grid_forget()
        upperButtons[4].grid_forget()

        if 'add' in switching_func:
            switching_func.remove("add")
            self.connectDealer.destroy()

        else:   
            pass

        switching_func.append('add')

        if "stock" in switching_func:
            self.connectBilling.destroy()
            switching_func.remove("stock")

        elif "customer" in switching_func:
            self.connectCustomer.destroy()
            switching_func.remove("customer")

        else:
            pass

        self.connectDealer = DealerPage(self.FrameRight)
        self.connectDealer.pack(fill=BOTH, expand=YES)
        self.connectDealer.PullComponents()

    def CustomerOpenFunc(self, event):
        self.design()
        upperButtons[2].grid_forget()
        upperButtons[3].grid_forget()
        upperButtons[4].bind(
            "<Leave>", lambda b: upperButtons[4].grid(in_=founationButtons[4]))
        if 'customer' in switching_func:
            switching_func.remove("customer")
            self.connectCustomer.destroy()
        else:
            pass

        switching_func.append("customer")

        if "add" in switching_func:
            switching_func.remove("add")
            self.connectDealer.destroy()

        elif "stock" in switching_func:
            switching_func.remove("stock")
            self.connectBilling.destroy()

        else:
            pass

        self.connectCustomer = customer(self.FrameRight)
        self.connectCustomer.pack(fill=BOTH, expand=YES)
        self.connectCustomer.customerPage()

    def BillingOpenFunc(self, event):
        self.design()
        upperButtons[2].grid_forget()
        upperButtons[4].grid_forget()
        upperButtons[3].bind(
            "<Leave>", lambda b: upperButtons[4].grid(in_=founationButtons[4]))
        if 'stock' in switching_func:
            self.connectBilling.destroy()
            switching_func.remove('stock')
        else:
            pass

        switching_func.append("stock")

        if "add" in switching_func:
            switching_func.remove("add")
            self.connectDealer.destroy()

        elif "customer" in switching_func:
            switching_func.remove("customer")
            self.connectCustomer.destroy()

        else:
            pass

        self.connectBilling = Billing(self.FrameRight)
        self.connectBilling.pack(fill=BOTH, expand=YES)
        self.connectBilling.billingPage()
