# -*- coding: utf-8 -*-
# File              : test_datetime.py
# Author            : tjh
# Create Date       : 2020/08/03
# Last Modified Date: 2020/08/03
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import re

# date = "2020-01-01 09:32:22"
# date1 = "2020-01-01"
# com = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
# char3 = re.findall(com, date)
# if char3:
#     print(char3)
input_dict = {'source_1': 1445.0, 'source_2': 4}
rel = "source_1 + source_2"

for k, v in input_dict.items():
    rel = rel.replace(k, v)

print(rel)