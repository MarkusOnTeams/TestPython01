import openpyxl 

wb = openpyxl.load_workbook("C:\\Daten\\_GitHub\\Repos\\Test Python01\\marks.xlsx")
sheet1 = wb['Class101']
sheet1['C10'].value = "Zustandsbeschreibung"

wb.save("C:\\Daten\\_GitHub\\Repos\\Test Python01\\marks.xlsx")
print ("Vorgang abgeschlossen")
