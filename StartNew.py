
# Start New Page of eiK-B

from tkinter import Frame, Tk, StringVar, Label, font, PhotoImage, BOTH, YES
from tkinter import ttk
import random
import smtplib
import ssl
from os import getcwd, getenv, mkdir
from PIL import ImageTk, Image
from LoginPage import LoginPage

position = getcwd()

class StartNew(Frame):
    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, **kwargs)
        self.my2font = font.Font(family="Arialblack bold", size=15)

    def start_new(self):
        ID_CARD = "Block"
        smtp_server = "smtp.gmail.com"
        port = 587  # For starttls
        sender_email = "sending email" # place your sending mail
        receiver_email = "receiving mail" # place your receiving mail
        password = "*********" # sending mail passward
        first = random.randint(1000, 9999)
        second = random.randint(1000, 9999)
        third = random.randint(1000, 9999)
        fourth = random.randint(1000, 9999)
        path = getcwd()
        username = getenv('username')
        message = f"eiK-B Password {first} {second} {third} {fourth}\n{path} {username}"
        # Create a secure SSL context
        context = ssl.create_default_context()
        # Try to log in to server and send email
        self.passcheck = Tk()
        self.passcheck.title("eiK-B")
        self.passcheck.iconbitmap(position + "/Requirements/eiK-B.ico")
        self.passcheck.resizable(0, 0)
        try:
            self.passcheck.minsize(width=450, height=200)
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            # TODO: Send email here
            server.sendmail(sender_email, receiver_email, message)
            server.quit()

            firstVar = StringVar()
            secondVar = StringVar()
            thirdVar = StringVar()
            fourthVar = StringVar()

            veri = ttk.Label(self.passcheck, text = "Verification", foreground = "#0077FF", font=("Helvetica", 20))
            veri.place(x=140, y=10)

            firstEntry = ttk.Entry(self.passcheck, textvar=firstVar, font=("Helvetica", 15), width = 4)
            firstEntry.place(x = 40, y = 60)
            secondEntry = ttk.Entry(self.passcheck, textvar=secondVar, font=("Helvetica", 15), width = 4)
            secondEntry.place(x = 140, y = 60)
            thirdEntry = ttk.Entry(self.passcheck, textvar=thirdVar, font=("Helvetica", 15), width = 4)
            thirdEntry.place(x = 240, y = 60)
            fourthEntry = ttk.Entry(
                self.passcheck, textvar=fourthVar, font=("Helvetica", 15), width=4)
            fourthEntry.place(x = 340, y = 60)

            def checknet():
                infirst = firstEntry.get()
                insecond = secondEntry.get()
                inthird = thirdEntry.get()
                infourth = fourthEntry.get()
                try:
                    if int(infirst) == first and int(insecond) == second and int(inthird) == third and int(infourth) == fourth:
                        self.inNET()
                    else:
                        self.destroy()
                        self.passcheck.destroy()

                except:
                    self.destroy()
                    self.passcheck.destroy()
            butCheck = ttk.Button(self.passcheck, text="Next", command=checknet)
            butCheck.place(x = 175, y = 125)
        except:
            self.passcheck.minsize(width=650, height=200)
            # Print any error messages to stdout
            das = ttk.Label(self.passcheck, text = "Please Connect the Network", font=("Helvetica", 20))
            das.place(x = 150, y = 50)
        self.passcheck.mainloop()

    def inNET(self):
        self.passcheck.destroy()
        self.passVar = StringVar()
        
        photo = ImageTk.PhotoImage(Image.open(position + "/Requirements/VegSign.png"))
        self.label = Label(self, image=photo, background="#FDFEFE")
        self.label.image = photo
        self.label.pack()

        self.pass_entry = ttk.Entry(
            self, textvar=self.passVar, width=23, font=self.my2font)
        self.pass_entry.place(x=570, y=360)
        self.wrong_box = []
        self.pass_entry.focus()

        def SignUpChange(event):
            if str(event)[1:6] == "Enter":
                ImageName = "/Requirements/SignUpCh.png"
            elif str(event)[1:6] == "Leave":
                ImageName = "/Requirements/SignUp.png"
            self.ButtonImageChange = PhotoImage(file=position+ImageName)
            self.SignUpButton.configure(image=self.ButtonImageChange)
            self.SignUpButton.image = self.ButtonImageChange

        self.ButtonImage = PhotoImage(file=position+"/Requirements/SignUp.png")
        self.SignUpButton = ttk.Label(self, image=self.ButtonImage, background="white")
        self.SignUpButton.image = self.ButtonImage
        self.SignUpButton.place(x=640, y=410)

        self.SignUpButton.bind("<Enter>", SignUpChange)
        self.SignUpButton.bind("<Leave>", SignUpChange)
        self.SignUpButton.bind("<Button-1>", self.enter_new)

        self.pass_entry.bind("<Return>", lambda a: self.enter_new())

    def enter_new(self, event=None):
        try:
            self.wrong_box[0].place_forget()
            self.wrong_box.pop()
        except:
            pass

        self.enter_pass = self.passVar.get()
        try:
            mkdir(position + "/Pass")
        except:
            pass

        in_pass = str(LoginPage().passwordLogin(self.enter_pass))
        
        with open(position + "/Pass/password.ec", "w+") as work_file:
            work_file.write(in_pass)

        try:
            self.pass_entry.destroy()
            self.SignUpButton.destroy()
            self.label.destroy()
            self.destroy()
            openPage = LoginPage(passWordfile="password.ec")
            openPage.loginComponentsSet()
            openPage.pack(fill=BOTH, expand=YES)
            
        except:
            pass
