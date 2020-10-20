# -*- coding: utf-8 -*-
# File              : test13_job_log.py
# Author            : tjh
# Create Date       : 2020/07/24
# Last Modified Date: 2020/07/24
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import json
import requests
import tarfile
import os

# http://192.168.1.166:8081/#/dashboard?job_id=20200724074945138267151&role=host&party_id=10005
url1 = 'http://192.168.1.166:9380/v1/job/log'
url2 = 'http://192.168.1.122:9380/v1/job/log'
params1 = {"job_id": "20200724074945138267151"}
rsp = requests.get(url2, json=params1, stream=True)

with open('output_log.tar.gz', "wb") as f:
    for chunk in rsp.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)

# tar = tarfile.open('output_log.tar.gz', "r:gz")
# file_names = tar.getnames()
# print(file_names)
# dir1 = r'D:\personal\exercise\personal_exe\test_ex\log'
# for file_name in file_names:
#     tar.extract(file_name, dir1)
#
# tar.close()
# import os
# for root, dirs, files in os.walk(dir1):
#     if 'ERROR.log' in files:
#
#         z = os.path.join(root, 'ERROR.log')
#         print(z)


# list_dir(dir1)
