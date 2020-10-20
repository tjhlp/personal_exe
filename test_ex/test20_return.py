# -*- coding: utf-8 -*-
# File              : test20_return.py
# Author            : tjh
# Create Date       : 2020/08/06
# Last Modified Date: 2020/08/06
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


def demo(x):
    y = x+1
    z = x-1
    return y,z

a = demo(3)
print(isinstance(a, tuple))
print(type(a))

for i in range(1, 3):
    print(i)
    for j in range(5, 10):
        if j == 6:
            print(j)
            break

