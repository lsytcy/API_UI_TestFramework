# -*-coding:uft-8-*-
import xlrd
import xlwt
import glob
import sys
import os

""""
读取Excel文件需要的参数：
1、Excel文件的路径
2、指定数据的表名
3、指定单元格
"""



# 获取指定表的数据
def get_excel_data(file_path, sheet_name):
    # formatting_info=True --保持原样式
    work_book = xlrd.open_workbook(file_path)
    # 获取所有的表名
    sheet_names = work_book.sheet_names()
    print(sheet_names)
    print(sheet_names[1])
    sheet_data = work_book.sheet_by_name(sheet_name)
    print(sheet_data["A1"].value)


# 获取sheet表中指定行的数据
def get_excel_row_data(file_path, sheet_name, row_num):
    # formatting_info=True --保持原样式
    work_book = openpyxl.load_workbook(file_path)
    # 获取所有的表名
    sheet_names = work_book.sheetnames
    # 获取指定表名的数据
    sheet_data = work_book[sheet_name]
    # 获取指定行的数据
    sheet_row_data = list(sheet_data[row_num])
    print(sheet_row_data)
    for cell_data in sheet_row_data:
        print(cell_data)

# 获取sheet表中指定列的数据
def get_excel_col_data(file_path, sheet_name, col_num):
    # formatting_info=True --保持原样式
    work_book = openpyxl.load_workbook(file_path)
    # 获取所有的表名
    sheet_names = work_book.sheetnames
    # 获取指定表名的数据
    sheet_data = work_book[sheet_name]
    # 获取指定列的数据
    sheet_col_data = list(sheet_data[col_num])
    print(sheet_col_data)


if __name__ == "__main__":
    # get_excel_data('../test_data/testexcel.xlsx', 'parking_zx')
    # get_excel_row_data('../test_data/testexcel.xlsx', 'parking_zx', 1)
    get_excel_col_data('../test_data/testexcel.xlsx', 'parking_zx', "B")
