
from fpdf import FPDF
import sqlite3 as sql
from os import getcwd, listdir, startfile
import datetime

position = getcwd()

class Debit:
    def TotDeb(database):
        if database == "Dealer":
            database = "Dealer-data.db"
            table = "Dealer"
            column = "COMPANYNAME"
            heads = "Company Name"
            deb = "CompanyDebit"

        elif database == "Customer":
            database = "Customer-data.db"
            table = "Customer"
            column = "CUSTOMERNAME"
            heads = "Customer Name"
            deb = "CustomerDebit"

        pdfOFDebit = []
        todayDate = datetime.date.today()
        allDealerDebit = []

        with sql.connect(position + "/Pass/%s"%database) as DealerDb:
            DD = DealerDb.cursor()
            DD.execute(
                '''SELECT %s FROM %s ORDER BY %s ASC'''%(column, table, column))
            data = DD.fetchall()
            for inCase in data:
                DD.execute('''SELECT DEBIT FROM %s ORDER BY NUM DESC LIMIT 1''' % (inCase[0] + "MONEY"))
                debitdata = DD.fetchall()
                try:
                    pdfOFDebit.append([inCase[0], debitdata[0][0]])
                    allDealerDebit.append(int(debitdata[0][0]))
                except:
                    pass
            DealerDb.commit()

        TOTAL_DEBIT = sum(allDealerDebit)
        pdfdeal = FPDF(format='A5', unit='mm')
        pdfdeal.add_page()
        pdfdeal.image(position + '/Requirements/ABNBill.jpg', x=4, y=2, w=140)
        pdfdeal.set_font('Times', 'B', 10.0)
        pdfdeal.ln(30)
        HEADERS = [heads, "Debit"]
        epw = pdfdeal.w - 2*pdfdeal.l_margin
        col_width = epw/2
        th = pdfdeal.font_size
        pdfdeal.ln(2*th)
        pdfdeal.cell(10, 10, "Date : " + str(todayDate))
        pdfdeal.ln(2*th)
        for head in HEADERS:
            pdfdeal.cell(col_width, 2*th, str(head), border=1)
        pdfdeal.ln(2*th)
        pdfdeal.set_font('Times', '', 8.0)
        pdfdeal.ln(0.5)
        for inr, row in enumerate(pdfOFDebit):
            for datum in row:
                pdfdeal.cell(col_width, 2*th, str(datum), border=1)
            if (inr + 1) % 19 == 0:
                pdfdeal.image(
                    position + '/Requirements/ABNBill.jpg', x=4, y=2, w=140)
                pdfdeal.set_font('Times', 'B', 10.0)
                pdfdeal.ln(30)
                pdfdeal.ln(2*th)
                pdfdeal.cell(10, 10, "Date : " + str(todayDate))
                pdfdeal.ln(2*th)
                for head in HEADERS:
                    pdfdeal.cell(col_width, 2*th, str(head), border=1)
                pdfdeal.ln(2*th)
                pdfdeal.set_font('Times', '', 8.0)
                pdfdeal.ln(0.5)
                for nineteen in pdfOFDebit[inr]:
                    pdfdeal.cell(col_width, 2*th, str(nineteen), border=1)

            pdfdeal.ln(2*th)
        pdfdeal.set_font('Times', 'B', 16.0)
        pdfdeal.cell(
            10, 10, "                                                           Total : %s" % str(TOTAL_DEBIT))

        filecheck = listdir(position + "/Pass")
        NameOF = deb + str(todayDate) + "(1)"

        if NameOF + ".pdf" not in filecheck:
            printerPDF = str(NameOF) + ".pdf"
            pdfdeal.output(position + '/Pass/' + printerPDF, 'F')
        else:
            temp = []
            for ins in filecheck:
                if deb + str(todayDate) in ins:
                    temp.append(ins[-6])
                    maxval = max(temp)
            add = int(maxval) + 1
            printerPDF = NameOF.replace(NameOF[-2:], "%s)" % str(add)) + ".pdf"
            pdfdeal.output(position + '/Pass/' + printerPDF, 'F')

        try:
            pdffile = position + "\\Pass\\" + printerPDF
            startfile(str(pdffile), 'print')

        except:
            pass
