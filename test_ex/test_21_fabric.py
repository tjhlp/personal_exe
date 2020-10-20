# -*- coding: utf-8 -*-
# File              : test_21_fabric.py
# Author            : tjh
# Create Date       : 2020/08/18
# Last Modified Date: 2020/08/18
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

from concurrent.futures.thread import ThreadPoolExecutor


class AsyncTask(object):

    def __init__(self, nums=5):
        # 默认开启5个线程
        self.executor = ThreadPoolExecutor(nums)

    def submit_call_back(self, func, call_back, args):
        self.executor.submit(lambda p: func(*p), args).add_done_callback(call_back)

    def submit(self, func, args):
        self.executor.submit(lambda p: func(*p), args)

    def query_pool(self):
        # 参看线程池
        pass

    def shutdown_pool(self):
        # 关闭线程池
        pass


import time


def hello1():
    print(11111111)
    time.sleep(5)
    print(222222)


def hello2():
    print(333333)
    time.sleep(10)
    print(44444)


def res(result):
    print('ddd')


# a1 = AsyncTask()
# a1.submit(hello1, [])
# a1.submit_call_back(hello2, res, [])
data1 = {'a1': '1', 'a2': '1', 'a3': '1'}
for v in data1.values():
    if not v:
        print(111)
# print(data1)
# print("0" in data1.values())

a = {1}
b = True
if not (a and b):
    print(111)

import requests

param = {
    "channelName": "elfchannel",
    "chaincodeName": "cmb2LongHua",
    "fcn": "set",
    "args": ["key",
             "value13243242333333333333333333335555555555555555555555555555555555555fytfytftyfytfyfyfufifdsfawefqfqwefqwefweqfw3333333333333333333333333333222222222222222"],
    "businessOrgName": "招商银行",
    "userName": "test1"
}
import time
import functools

t = 0
for i in range(6):
    time1 = time.time()
    rsp = requests.post('http://192.168.0.130:8001/fabric/api/invoker/invoke', json=param)
    time2 = time.time()
    t += time2 - time1
    print(time2 - time1)
    print(rsp.text)

print(t / 6)
