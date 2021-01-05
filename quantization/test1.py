# -*- coding: utf-8 -*-
# File              : test1.py
# Author            : tjh
# Create Date       : 2020/11/23
# Last Modified Date: 2020/11/23
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import datetime

from sklearn.datasets import load_iris
# iris =load_iris()
#
# print(iris)
# t = iris.keys()
# print(t)
# print(datetime.datetime.now().strftime('%Y%m%d%H'))
with open('./test.txt', 'w')as w:
    w.write(str(9999))

for i in range(2):
    with open('./test.txt', 'a')as w:
        w.write(str(i))



