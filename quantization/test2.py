# -*- coding: utf-8 -*-
# File              : test2.py
# Author            : tjh
# Create Date       : 2020/12/10
# Last Modified Date: 2020/12/10
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
"""

利用http://tushare.org/index.html 中介绍的api，爬取
http://tushare.org/trading.html 页面中的所有交易数据存入本地数
据库（或csv文件夹）。
hint: 参考 http://tushare.org/storing.html
Due date：Next Week
Bottom Line：会使用api

"""

import tushare as ts

hs_stock = ts.get_hs300s()

print(hs_stock)
print(type(hs_stock))

