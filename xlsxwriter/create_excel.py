import xlsxwriter

# Crear excel

workbook = xlsxwriter.Workbook('nombre.xlsx')
worksheet = workbook.add_worksheet('Hoja 1')
headers = ['Columna 1', 'Columna 2']

# Escribir headers
# write(fila, columna, contenido)
for h, header in enumerate(headers):
    worksheet.write(0, h, header)

# Escribir contenido
worksheet.write(1, 0, "Hola")
worksheet.write(1, 1, "Que tal")

# Guardarlo
workbook.close()