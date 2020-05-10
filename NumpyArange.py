#-*- coding:utf-8 -*-
# @Time    :2020/5/8 20:17
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyArange.py

import numpy as np
# 创建arange
r1 = np.arange(1,11,1)
print(r1)
print(type(r1))#<class 'numpy.ndarray'>
# 改变arange形状
r1.shape = 2,5
print(r1)
print(np.arange(10).reshape(2, 5))