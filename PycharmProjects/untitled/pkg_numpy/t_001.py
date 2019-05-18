# _*_ coding:utf-8 _*_


import numpy as np
import xlwings as xw

# path = r"D:\temp\last5000.xlsx"
# app = xw.App(visible=False,add_book=False)
# wb = app.books.open(path)
# sht = wb.sheets(1)
# original_data = sht.range("A1").expand().value
# wb.close()
# app.quit()

# array = np.array([[1, 2, 3],
#                   [2, 3, 4],
#                   [3, 4, 5],
#                   ["a", "b", "c"]])
array = np.arange(1, 28).reshape(3, 3, 3)
print(array)
print("dimension:", array.ndim)
print("shape:", array.shape)
print("size:", array.size)
print(array[0][0])