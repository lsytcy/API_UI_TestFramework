import openpyxl
import xlrd
import xlwt
import glob
import sys
import os

wb = openpyxl.load_workbook("D:\\python-project\\python-func\\merge_all.xlsx")
# sheet1为Excel文件的第一张表
sheet1 = wb.worksheets[1]
# 打印第一张表的表名
# print(sheet1)
print(sheet1.values)
# 取第一张表中的A1单元格的文本
# print(sheet1["A1"].value)

filenames = glob.glob(sys.path[0])
print(filenames)

# for row in sheet1.iter_rows(min_col=1, max_col=3, min_row=1, max_row=1):
#     for cell in row:
#         print(cell.coordinate, cell.value)
