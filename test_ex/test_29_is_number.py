# -*- coding: utf-8 -*-
# File              : test_29_is_number.py
# Author            : tjh
# Create Date       : 2020/11/16
# Last Modified Date: 2020/11/16
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


def is_number(s):
    try:
        import unicodedata
        s = unicodedata.numeric(s)
        return s
    except (TypeError, ValueError):
        pass

    try:
        s = float(s)
        return s
    except ValueError:
        return s


i = '123.1'
print(i.isnumeric())
print(i.isdigit())
print(i.isdecimal())
t = is_number(i)
print(type(t))
print(t)


