import openpyxl
path = "/home/halovivek/Documents/welcome.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active
for i in range(1,10):
    for c in range(1,5):
        sheet.cell(row=i, column=c).value="OmVimVijayalakshmiNamah"

workbook.save(path)
