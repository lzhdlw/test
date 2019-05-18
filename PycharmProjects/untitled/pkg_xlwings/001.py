# _*_ coding:utf-8 _*_


import xlwings as xw
import sys
import time

fullname = r"D:\temp\last5000.xlsx"


def test_001():
    app = xw.App(visible=True, add_book=False)
    wb = app.books.add()
    sht = wb.sheets(1)
    sht.name = "test"

    row_heading = [i for i in range(1, 21)]
    column_header = ["number", "name", "age", "sex", "height", "weight"]

    sht.range("A1").value = column_header
    sht.range("A2").options(transpose=True).value = row_heading

    # close the workbook and quit the app
    while True:
        close_or_not = input("是否关闭工作簿(yes/no):\n")
        if close_or_not == "yes":
            wb.close()
            app.quit()
            break


def test_002():
    # open a workbook and get the particular worksheet(optionally the first worksheet):
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(fullname)
    sht = wb.sheets(1)

    # get some information of the worksheet:
    print(sht.name)  # name
    print(sht.index)  # index
    sum_rows = sht.shapes
    print(sum_rows)

    # close the workbook and quit the app
    while True:
        close_or_not = input("是否关闭工作簿(yes/no):\n")
        if close_or_not == "yes":
            wb.close()
            app.quit()
            break


def test_003():
    app = xw.App(visible=True, add_book=False)
    wb = app.books.open(fullname)
    sht = wb.sheets(1)
    print(sht.name)
    print(sht.index)
    print(sht.range("A1").value)
    print(dir(sht.range("A1")))
    print(sht.range("A1").shape)
    print(dir(sht.range("A1").options(expand=True)))
    print(dir(wb))
    print(sht.range("A1").expand().rows.count)
    print(sht.range("A1").expand().columns.count)
    wb.close()
    app.quit()


if __name__ == "__main__":
    test_003()
