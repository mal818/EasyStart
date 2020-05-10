#-*- coding:utf-8 -*-
# @Time    :2020/5/8 7:34
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyArray.py

import numpy as np

print('\n','Numpy-array的创建','\n','-'*100)
mtr1 = [[1,2,3],[4,5,6]]
# 嵌套序列转换为ndarray
mtr2 = [range(5),range(5)]
arr1 = np.array(mtr2) #<class 'numpy.ndarray'>
print(arr1)

print('\n', 'array的属性', '\n', '-' * 100)
print('shape:',arr1.shape)#shape: (2, 3)
print('ndim:', arr1.ndim)#ndim: 2
print('dtype:', arr1.dtype)#dtype: int32
print('size:', arr1.size)#size: 6

print('\n', '特殊矩阵的创建', '\n', '-' * 100)
print('零矩阵')
print(np.zeros(shape=(2, 3)))
print('一矩阵')
print(np.ones(shape=(2,3)))
print('对角阵')
print(np.diag([1, 2, 3]))
print('单位矩阵')
print(np.eye(3))
