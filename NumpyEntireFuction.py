#-*- coding:utf-8 -*-
# @Time    :2020/5/8 20:47
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyEntireFuction.py

import numpy as np

randn = np.random.randn(2, 3)
print('-' * 100, '\n', '原始：')
print(randn)
print('-' * 100, '\n', '向上取整：')
print(np.ceil(randn))
print('-' * 100, '\n', '向下取整：')
print(np.floor(randn))
print('-' * 100, '\n', '四舍五入：')
print(np.rint(randn))
print('-' * 100, '\n', '判断元素是否为NaN')
print(np.isnan(randn))
print('-' * 100, '\n', '元素相乘')
mat1 = np.mat([[-1,2],[3,-4]])
mat2 = np.mat([[5,6],[7,8]])
print(np.multiply(mat1, mat2))
print('-' * 100, '\n', '元素相除')
print(np.divide(mat2, mat1))
print('-' * 100, '\n', '取绝对值')
print(np.abs(mat1))
print('-' * 100, '\n', '三元运算符')
print(np.where(mat1>0,1,-1))