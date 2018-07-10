import os
import openpyxl

os.chdir('C:\Python37')
wb = openpyxl.load_workbook('Example.xlsx')
sheet = wb.sheetnames
print(sheet)
mysh = wb['Sheet1']
ce = mysh['C1']
print(ce.value)

