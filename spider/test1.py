# -*- coding: utf-8 -*-
# File              : test1.py
# Author            : tjh
# Create Date       : 2020/12/26
# Last Modified Date: 2020/12/26
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import pandas as pd

s_str = '1000+ answered questions'
print(s_str[:s_str.rfind('answered')-1])
