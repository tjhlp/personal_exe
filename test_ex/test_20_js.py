# -*- coding: utf-8 -*-
# File              : test_20_js.py
# Author            : tjh
# Create Date       : 2020/08/10
# Last Modified Date: 2020/08/10
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import datetime

data1 = (('tab_model_info',
          "CREATE TABLE `tab_model_info` (\n  `model_id` int unsigned NOT NULL AUTO_INCREMENT,\n  `node_id` char(8) NOT NULL DEFAULT '' COMMENT '所属节点',\n  `model_name` varchar(120) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '模型名称',\n  `model_desc` varchar(600) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '模型描述',\n  `model_target` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL DEFAULT '' COMMENT '模型目的',\n  `model_type` char(1) NOT NULL COMMENT '0: 非参数 1：参数',\n  `object_param` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '对象参数',\n  `source` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '数据源表及相应的字段',\n  `model_relation` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '模型公式',\n  `model_result` longtext COMMENT '模型结果',\n  `front_data` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '前端数据',\n  `Crt_Time` datetime DEFAULT NULL COMMENT '创建时间',\n  `Upd_Time` datetime DEFAULT NULL COMMENT '更新时间',\n  PRIMARY KEY (`model_id`) USING BTREE\n) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8"),)
print(data1[0][1])
z = data1[0][1]
c = z.replace('tab_model_info', '1_tab_model_info')
print(c)


test1 = {"errCod": 0, "errMsg": "\u6210\u529f", "data": {"tableName": "1_tab_financial_info", "sourceID": 69}}
print(test1)
