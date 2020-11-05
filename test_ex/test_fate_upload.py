# -*- coding: utf-8 -*-
# File              : test_fate_upload.py
# Author            : tjh
# Create Date       : 2020/09/11
# Last Modified Date: 2020/09/11
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import requests

#
url = "http://{}/v1/data/upload".format('192.168.1.122:9380')
upload_param = {
    "file": "examples/data/longhua_company_penalty.csv",
    "head": 1,
    "partition": 2,
    "work_mode": 1,
    "table_name": "test",
    "namespace": "test_namespace",
    "use_local_data": "0",
    "drop": "1"
}
files = {'file': open(r'D:\personal\exercise\personal_exe\test_ex\longhua_company_penalty.csv', 'r', encoding='utf-8')}

"breast_hetero_mini_host.csv"
rsp = requests.post(url, files=files, params=upload_param)


print(rsp.text)
