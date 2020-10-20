# -*- coding: utf-8 -*-
# File              : test12_clean_job.py
# Author            : tjh
# Create Date       : 2020/07/22
# Last Modified Date: 2020/07/22
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import requests
import json


def kill_job(kill_job_id):
    params = {
        "job_id": kill_job_id

    }
    try:
        url = 'http://192.168.1.122:9380/v1/job/clean'
        rsp = requests.post(url, json=params)
        rsp = rsp.text
    except Exception as e:
        rsp = {
            'error_msg': e
        }

    return rsp


def get_job_id():
    url1 = 'http://192.168.1.166:8081/job/query/page'
    job_lists = []
    count = 0
    for i in range(1, 20):
        params1 = {"page_num": i, "page_size": 20, "role": [], "status": [], "job_id": "", "party_id": "",
                   "start_time": "desc"}
        rsp = requests.post(url1, json=params1)
        jr_rsp = json.loads(rsp.text)

        if not jr_rsp['data']['list']:
            continue
        job_list = jr_rsp['data']['list']
        job_lists.append(job_list)
        count += len(job_list)

    return job_lists, count


def main():
    kill_count = 0
    job_lists, count = get_job_id()
    for job_list in job_lists:
        for job_info in job_list:
            job_id = job_info['job']['fJobId']
            kill_job(job_id)
            kill_count += 1
            print('当前：{},进度：%{:.2f}'.format(job_id, kill_count / count * 100))


if __name__ == '__main__':
    main()
