#-*- coding:utf-8 -*-
# @Time    :2020/5/8 20:25
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyMatrix.py

import numpy as np
# 正常的创建方式
mat1 = np.mat([[1,2,3],[4,5,6]])
print(mat1,'\n','-'*100)
# 一维的序列会被转换成二维
mat = np.matrix([1,2,3,4])
print(mat)
print(mat.ndim)
print(mat.shape)
print(mat.size,'\n','-'*100)
# 一种奇怪的构建方式
a = np.matrix('1 2; 3 4')
print(a)