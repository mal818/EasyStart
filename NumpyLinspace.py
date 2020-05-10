#-*- coding:utf-8 -*-
# @Time    :2020/5/8 20:35
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyLinspace.py

import numpy as np
# 等差数列
lin = np.linspace(1,10,num=10,endpoint=False)
print(lin)
print(type(lin))#<class 'numpy.ndarray'>
# 等比数列
log = np.logspace(2,8,4,base=2)
print(log)
print(type(log))#<class 'numpy.ndarray'>