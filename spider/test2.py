# -*- coding: utf-8 -*-
# File              : test2.py
# Author            : tjh
# Create Date       : 2020/12/31
# Last Modified Date: 2020/12/31
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import pandas as pd

train = pd.read_csv('None.tsv', sep='\t', header=None)
train.to_csv('test.csv', header=None)

