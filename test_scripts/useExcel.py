import openpyxl
import xlrd
import xlwt
import glob
import sys
import os

excel_file_path = os.path.dirname(os.path.abspath(__file__))
excel_file_names = glob.glob(excel_file_path + os.sep + "*.xls*")
print(excel_file_path)
print(excel_file_names)
wb = openpyxl.load_workbook(excel_file_names[0])
# sheet1为Excel文件的第一张表
sheet1 = wb.worksheets[1]
sheet_names= wb.sheetnames
# 打印第一张表的表名
print(sheet1)
print(sheet_names)
# 取第一张表中的A1单元格的文本
# print(sheet1["A1"].value)

# for row in sheet1.iter_rows(min_col=1, max_col=3, min_row=1, max_row=1):
#     for cell in row:
#         print(cell.coordinate, cell.value)
