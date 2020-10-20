# -*- coding: utf-8 -*-
# File              : test18_testdb.py
# Author            : tjh
# Create Date       : 2020/07/30
# Last Modified Date: 2020/07/30
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

DB_PROF = {
    'host': '192.168.1.116',
    'port': 7306,
    'user': 'cloud',
    'password': 'Cloud@2020',
    'database': 'prof_model_set',
    'charset': 'utf8',
    'autocommit': True,
    'connect_timeout': 3,
    'read_timeout': 10,
    'write_timeout': 5
}


DB_BASIC = {
    'host': '192.168.1.122',
    'port': 9306,
    'user': 'root',
    'password': 'ZZfwq@2020',
    'database': 'model_set',
    'charset': 'utf8',
    'autocommit': True,
    'connect_timeout': 3,
    'read_timeout': 10,
    'write_timeout': 5
}

import pymysql

conn1 = pymysql.connect(**DB_PROF)
cur1 = conn1.cursor()
sql1 = 'select * from TAB_PROF_MODEL_INFO where Model_ID=1'
cur1.execute(sql1)
print(cur1.fetchall())
cur1.close()

#
# conn2 = pymysql.connect(**DB_BASIC)
# cur2 = conn2.cursor()
# sql2 = 'select * from tab_model_info'
# cur2.execute(sql2)
# print(cur2.fetchall())
# cur2.close()

