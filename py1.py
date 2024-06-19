import openpyxl

new_xls = openpyxl.workbook.Workbook()
sheet1  = new_xls.create_sheet('Лист 1')

sheet1['A1'] = 1111
sheet1['A2'] = 2222
sheet1['A3'] = 3333

print(sheet1['A1'].value )
print(sheet1['A2'].value )
print(sheet1['A3'].value )


new_xls.save('MyExcel.xlsx')
