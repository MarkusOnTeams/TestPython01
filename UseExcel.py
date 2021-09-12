import openpyxl

book = openpyxl.load_workbook(r'C:\Daten\_GitHub\Repos\Test Python01\marks.xlsx')
sheet = book["Class101"]

print(sheet["A3"].value)
