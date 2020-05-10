#-*- coding:utf-8 -*-
# @Time    :2020/5/9 7:37
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :NumpyOrientFuction.py

import numpy as np
mat1 = np.array([[1,2,3],[4,5,9],[0,8,9]])
print('_'*100,'\n','行方向求平均',np.mean(mat1,axis=1))
print('_'*100,'\n','列方向求和',np.sum(mat1,axis=0))
print('_'*100,'\n','列方向求最大值',np.max(mat1,axis=0))
print('_'*100,'\n','列方向求最小值',np.min(mat1,axis=0))
print('_'*100,'\n','列方向求标准差',np.std(mat1,axis=0))
print('_'*100,'\n','列方向求方差',np.var(mat1,axis=0))
print('_'*100,'\n','列方向最大值坐标',np.argmax(mat1,axis=0))
print('_'*100,'\n','列方向最小值坐标',np.argmin(mat1,axis=0))
print('_'*100,'\n','列方向累加','\n',np.cumsum(mat1,axis=0))
print('_'*100,'\n','列方向累加','\n',np.cumsum(mat1,axis=0))
print('_'*100,'\n','列方向累乘','\n',np.cumprod(mat1,axis=0))
print('_'*100,'\n','列方向去重并排序','\n',np.unique(mat1,axis=0))
