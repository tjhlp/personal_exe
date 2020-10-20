# -*- coding: utf-8 -*-
# File              : db_test.py
# Author            : tjh
# Create Date       : 2020/07/23
# Last Modified Date: 2020/07/23
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import pymysql
import decimal
import datetime
import re
mdb = {
    'host': '192.168.1.122',
    'port': 9306,
    'user': 'root',
    'password': 'ZZfwq@2020',
    'database': 'prof_model_set',
    'charset': 'utf8',
    'autocommit': True,
    'connect_timeout': 3,
    'read_timeout': 10,
    'write_timeout': 5
}

conn = pymysql.connect(**mdb)
db = conn.cursor()

sql_count = "select count(*) from TAB_PROF_MODEL_INFO"
db.execute(sql_count)
r = db.fetchall()
print(r)
db.close()
