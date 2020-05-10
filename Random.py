#-*- coding:utf-8 -*-
# @Time    :2020/5/7 23:36
# @Author  :MaLiang
# @Email   :mal818@126.com
# @File    :Random.py

import random
import numpy as np

print('Get the next random number in the range [0.0, 1.0).\n',str(random.random()))
print('-'*100)
print('Return random integer in range [a, b], including both end points.包头包尾。\n',str(random.randint(10,20)))
print('-'*100)
print('Choose a random item from range(start, stop[, step]).包头不包尾。\n',str(random.randrange(3,5,2)))
print('-'*100)
print('Draw samples from a chi-square distribution.\n',np.random.chisquare(10,size=(3,5)))

print('-'*100,'\n Return a sample (or samples) from the "standard normal" distribution.')
print(np.random.randn(2,4))
print('-'*100,'\n Draw random samples from a normal (Gaussian) distribution.')
print(np.random.normal(0,1,size=(2,4)))
print('-'*100,'\n Draw samples from a binomial distribution.')
print(np.random.binomial(10,0.5,size=(2,4)))