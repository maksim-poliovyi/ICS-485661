# Польовий Максим


import markets_data
import xlsxwriter

title_list = ['Код ринку',
              'Найменування ринку',
              'Дата',
              'Ціна',
              'Середня ціна']

workbook = xlsxwriter.Workbook('table_markets_analysis.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True, })
bold.set_text_wrap()
bold.set_align('center')
bold.set_align('top')
bold.set_border()
border = workbook.add_format()
border.set_border()

worksheet.write(0, 0, title_list[0], bold)
worksheet.write(0, 1, title_list[1], bold)
worksheet.write(0, 2, title_list[2], bold)
worksheet.write(0, 3, "", bold)
worksheet.write(0, 4, title_list[3], bold)
worksheet.write(0, 5, "", bold)
worksheet.write(0, 6, title_list[4], bold)

worksheet.write(1, 0, "", bold)
worksheet.write(1, 1, "", bold)
worksheet.write(1, 2, "", bold)
worksheet.write(1, 3, "Картопля", bold)
worksheet.write(1, 4, "Капуста", bold)
worksheet.write(1, 5, "Цибуля", bold)
worksheet.write(1, 6, "", bold)

for index in range(0, 7):
    worksheet.set_column(0, index, 15)

for i in range(1, len(markets_data.sorted_by_code)):

    column = 0

    for attr, value in vars(markets_data.sorted_by_code[i - 1]).items():
        worksheet.write(i + 1, column, value, border)
        column += 1

for i in range(0, 6):
    column = 0
    for attr, value in vars(markets_data.sorted_by_code[len(markets_data.sorted_by_code) - 1]).items():
        worksheet.write(10, column, value, border)
        column += 1

workbook.close()
