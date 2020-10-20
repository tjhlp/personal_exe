# -*- coding: utf-8 -*-
# File              : test5.py
# Author            : tjh
# Create Date       : 2020/07/16
# Last Modified Date: 2020/07/16
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import requests


res = requests.post('http://192.168.1.166:8080/job/v1/pipeline/job/stop/', json={"job_id": "2020071508031387750518",
                                                                        "party_id": "10005",
                                                                        "role": "guest"})
rsp = requests.post('http://192.168.1.166:9380/v1/job/clean/queue')

print(rsp.text)
