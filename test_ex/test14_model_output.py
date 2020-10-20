# -*- coding: utf-8 -*-
# File              : test14_model_output.py
# Author            : tjh
# Create Date       : 2020/07/24
# Last Modified Date: 2020/07/24
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import requests
import json

url = "http://192.168.1.122:9380/v1/tracking/component/output/model"
params = {
    "job_id": "20200724091012741656154",
    "party_id": "10006",
    "role": "guest",
    "component_name": "hetero_lr_0",
}
rsp = requests.post(url, json=params)
# jr_rsp = json.loads(rsp.text)
z = {'data': {'bestIteration': -1, 'header': ['SX_GRD', 'GM', 'INF1', 'ADDRESS'], 'intercept': 0.07134794502597169,
              'isConverged': False, 'iters': 30, 'lossHistory': [], 'needOneVsRest': False,
              'weight': {'ADDRESS': 0.0018833126574553443, 'GM': 0.6472840744366855, 'INF1': 0.1352584100391512,
                         'SX_GRD': -0.1913269176011355}},
     'meta': {'meta_data': {'alpha': 0.01, 'batchSize': '-1', 'earlyStop': 'weight_diff', 'fitIntercept': True,
                            'learningRate': 0.15, 'maxIter': '30', 'needOneVsRest': False, 'optimizer': 'sgd',
                            'partyWeight': 0.0,
                            'penalty': 'L2', 'reEncryptBatches': '0', 'tol': 0.0001}, 'module_name': 'HeteroLR'},
     'retcode': 0,
     'retmsg': 'success'}

import logging


def json_decode(js_str):
    """
    将json字符串解码为成python对象
    :param js_str: json字符串
    :return: python对象
    """

    try:
        return json.loads(js_str)
    except Exception as e:
        logging.debug('json_decode got exception: %s, js_str:%s' % (str(e), js_str))
        return 'error'


CODE_FATE_TASK_ERROR = (1002, '访问fate平台失败', 0)
CODE_PROF_MODEL_FILE_ERROR = (10056, '文件删除失败', 0)
CODE_SUCCESS = (0, '成功', 0)


def request_fate_post(url, params):
    try:
        rsp = requests.post(url, json=params)
        jr_rsp = json_decode(rsp.text)
    except Exception as e:
        logging.error('FATE requests post got exception :%s' % str(e))
        print(e)
        return False, CODE_PROF_MODEL_FILE_ERROR

    return jr_rsp, CODE_SUCCESS


jr_rsp, code = request_fate_post(url=url, params=params)

print(jr_rsp['data'])
print(jr_rsp['data']['header'])
print(jr_rsp['data']['weight'])

header = jr_rsp['data']['header']
data = [jr_rsp['data']['weight'][i] for i in header]
print(data)