# -*- coding: utf-8 -*-
# File              : test_19_thread.py
# Author            : tjh
# Create Date       : 2020/08/05
# Last Modified Date: 2020/08/05
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
from concurrent.futures.thread import ThreadPoolExecutor

executor = ThreadPoolExecutor()


def thread_pool_run(func, call_back, args):
    executor.submit(lambda p: func(*p), args).add_done_callback(call_back)


def demo1(x, y, z):
    print(x+y)
    print(z)

def demo2(res):
    print('call_back')

str1 = "id 11 id "
print(str1.replace('id','ID'))

thread_pool_run(func=demo1, call_back=demo2, args=[1, 2, 53])