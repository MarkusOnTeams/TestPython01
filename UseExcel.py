import openpyxl

wb = openpyxl.load_workbook(r'C:\Daten\_GitHub\Repos\Test Python01\marks.xlsx')
ws = wb['Class101']
ws['a10'].value   = "Hello There!"

wb.save(r'C:\Daten\_GitHub\Repos\Test Python01\marks.xlsx')
print ("Vorgang abgeschlossen")