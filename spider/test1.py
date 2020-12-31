# -*- coding: utf-8 -*-
# File              : test1.py
# Author            : tjh
# Create Date       : 2020/12/26
# Last Modified Date: 2020/12/26
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import requests

params = {
    "user_id": "1"

}


def run():
    try:
        a = requests.post(url='http://129.211.77.253:8000/amazon/spider/', json=params)
        print(a.text)
    except Exception as e:
        print(str(e))


scheduler = BlockingScheduler()
scheduler.add_job(func=run, args=('循环任务',), trigger='interval', seconds=3)

scheduler.start()
