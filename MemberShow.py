# Show the members in eiK-B

from PIL import ImageTk, ImageDraw, Image, ImageFont
import sqlite3 as sql
from os import getcwd
from InsideMemberShow import MemberView
from tkinter import Text, ALL
position = getcwd()

class MemberShow:
    def __init__(self, frame):
        #print(dir(frame))
        self.frame = frame
        self.showFrame = self.frame.showFrame

    def ShowThat(self, name):
        self.ConImage = []
        DealerContact = []
        PositionX = 90
        PositionY = 100
        VarForX = 0
        VarForY = 0
        
        if name == "Dealer":
            database = "Dealer-data.db"
            table = name
            column = "COMPANYNAME"
        elif name == "Customer":
            database = 'Customer-data.db'
            table = name
            column = "CUSTOMERNAME"

        with sql.connect(position + "/Pass/%s" % database) as DealerDb:
            DD = DealerDb.cursor()
            DD.execute('''SELECT %s FROM %s ORDER BY %s ASC'''%(column, table, column))
            self.data = DD.fetchall()
            ShowImage = []
            throw = {}

            for comindex, company in enumerate(self.data):
                DealerContact.insert(comindex, Image.open(position + "/Requirements/contacts.png"))
                font_type = ImageFont.truetype("arial.ttf", 18)
                draw = ImageDraw.Draw(DealerContact[comindex])
                draw.text(xy=(58, 157), text=str(
                    company[0]), fill=(0, 119, 255), font=font_type)
                self.ConImage.insert(comindex, ImageTk.PhotoImage(DealerContact[comindex]))
                if VarForY >= 3:
                    PositionY += 200
                    VarForY = 0
                else:
                    pass
                if VarForX >= 3:
                    PositionX = 90
                    VarForX = 0
                elif 0 < VarForX < 3:
                    PositionX += 180
                else:
                    pass

                ShowImage.insert(comindex, self.showFrame.create_image(PositionX, PositionY, image=self.ConImage[comindex]))
                self.showFrame.image = self.ConImage
                throw["a[%s]" % str(comindex)] = company[0]

                def eval_link(x): return (
                    lambda p: MemberView(frame = self.frame, DorC = str(name)).InsideOfShowMember(throw["a[%s]" % str(x)]))
                self.showFrame.tag_bind(ShowImage[comindex], "<Button-1>", eval_link(comindex))
    
                VarForX += 1
                VarForY += 1

            DealerDb.commit()
