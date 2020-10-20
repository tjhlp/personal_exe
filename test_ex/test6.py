# -*- coding: utf-8 -*-
# File              : test6.py
# Author            : tjh
# Create Date       : 2020/07/16
# Last Modified Date: 2020/07/16
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

model_name = '太子路交通拥挤模型'
model_target = '交通拥挤指数'
model_object = ['蛇口太子路18号', '2020-05-28 18:00', '2020-05-28 21:00']

source_rule = {
    'source_1': {
        'tab_online_order': {'p1': ['speed', 'avg'], 'p2': ['track_record', 'max'], 'p3': ['number_of_lights', 'sum']},
        'tab_traffic_light': {'p4': ['road', 'max'], 'p5': ['traffic_light', 'min']}
    },
    'source_2': {}

}
source_unrule = {
    'source_1':{
        'tab_finance_risk'
    }
}
# constant = {'cp1': '10'}
relation = {'source_1': '10 * p1 +p2/(p3*200+4) + 0.4 *p4'}
ret = {
    'web_data':  {
        ''
    }
}