# -*- coding: utf-8 -*-
# File              : test30_cut_model_id.py
# Author            : tjh
# Create Date       : 2020/12/07
# Last Modified Date: 2020/12/07
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import re

model_id = 'arbiter-16899#guest-16800#host-16899#model'
arbiter, guest, host = re.findall('arbiter-(.*?)#guest-(.*)#host-(.*)#model', model_id)[0]
print(guest)

