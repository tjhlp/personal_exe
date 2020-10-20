# -*- coding: utf-8 -*-
# File              : db.py
# Author            : tjh
# Create Date       : 2020/08/12
# Last Modified Date: 2020/08/12
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import pymysql

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
# con = pymysql.connect(**DB_BASIC)

data1 = [{'columns': [{'name': 'cycle', 'param': 'p1', 'rel': 'count'}],
          'conditions': [{'condition_param': '2020-01-01 09:00:00', 'condition_rel': '>', 'name': 'time'},
                         {'condition_param': '太子路', 'condition_rel': '=', 'name': 'road'}],
          'table_ID': 'tab_cycle_track'}]

data2 = [
    {'columns': [{'name': 'speed', 'param': 'p1', 'rel': 'avg'}, {'name': 'track_record', 'param': 'p2', 'rel': 'max'}],
     'conditions': [{'condition_param': '2020-01-01 09:00:00', 'condition_rel': '>', 'name': 'time'},
                    {'condition_param': '太子路', 'condition_rel': '=', 'name': 'road'}], 'table_ID': 'tab_online_order'},
    {'columns': [{'name': 'number_of_road', 'param': 'p3', 'rel': 'max'},
                 {'name': 'traffic_light', 'param': 'p4', 'rel': 'min'}],
     'conditions': [{'condition_param': '2020-01-01 09:00:00', 'condition_rel': '>', 'name': 'time'}],
     'table_ID': 'tab_traffic_light'}]

for tab in data2:
    print(tab['table_ID'])
