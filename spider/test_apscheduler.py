# -*- coding: utf-8 -*-
# File              : test_apscheduler.py
# Author            : tjh
# Create Date       : 2021/01/04
# Last Modified Date: 2021/01/04
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import random
# import requests

params = {
    "user_id": "1"

}


def run():
    try:
        # a = requests.post(url='http://129.211.77.253:8000/amazon/spider/', json=params)
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        # print(a.text)
    except Exception as e:
        print(str(e))


scheduler = BlockingScheduler()
run()

scheduler.add_job(func=run, trigger='interval', seconds=random.randint(1,10))

scheduler.start()






