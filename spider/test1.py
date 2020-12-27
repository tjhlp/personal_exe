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

total_res = [{"goods_code": "['$29.99', '$61.95']",
            "goods_name": "https://www.amazon.com/Fire-TV-Stick-4K-with-Alexa-Voice-Remote/dp/B079QHML21/ref=zg_bs_electronics_2/136-1134223-2942050?_encoding=UTF8&psc=1&refRID=RTH9TXGG3ZMXZR83N4YB"}]
df = pd.DataFrame(total_res,
                  columns=["goods_code", "goods_name"])
df.to_csv('./test.csv', encoding='utf-8', index=False)
