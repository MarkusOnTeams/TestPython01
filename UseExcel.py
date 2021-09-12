import openpyxl

book = openpyxl.load_workbook(r'C:\Daten\_GitHub\Repos\Test Python01\marks.xlsx')
sheet = book["Class101"]

# Read from Cell A3
#print(sheet["A3"].value)

# Write to Cell A8
sheet["a8"] = "Hello There!"
book.safe(r'C:\Daten\_GitHub\Repos\Test Python01\marks.xlsx')