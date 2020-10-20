# -*- coding: utf-8 -*-
# File              : test2.py
# Author            : tjh
# Create Date       : 2020/07/08
# Last Modified Date: 2020/07/08
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import os

post_data = {'job_dsl':
                 {'components':
                      {'dataio_0': {'module': 'DataIO', 'input': {'data': {'data': ['args.train_data']}},
                                    'output': {'data': ['train_data'], 'model': ['dataio']}},
                       'dataio_1': {'module': 'DataIO',
                                    'input': {'data': {'data': ['args.eval_data']}, 'model': ['dataio_0.dataio']},
                                    'output': {'data': ['eval_data'], 'model': ['dataio']}},
                       'intersection_0': {'module': 'Intersection',
                                          'input': {'data': {'data': ['dataio_0.train_data']}},
                                          'output': {'data': ['train']}},
                       'intersection_1': {'module': 'Intersection', 'input': {'data': {'data': ['dataio_1.eval_data']}},
                                          'output': {'data': ['eval_data']}}, 'hetero_lr_0': {'module': 'HeteroLR',
                                                                                              'input': {'data': {
                                                                                                  'train_data': [
                                                                                                      'intersection_0.train'],
                                                                                                  'eval_data': [
                                                                                                      'intersection_1.eval_data']}},
                                                                                              'output': {'data': [
                                                                                                  'hetero_lr_data'],
                                                                                                  'model': [
                                                                                                      'hetero_lr_model']}},
                       'evaluation_0': {'module': 'Evaluation',
                                        'input': {'data': {'data': ['hetero_lr_0.hetero_lr_data']}}}}},
             'job_runtime_conf': {'initiator': {'role': 'guest', 'party_id': 10000}, 'job_parameters': {'work_mode': 1},
                                  'role': {'guest': [10000], 'host': [10002], 'arbiter': [10000]}, 'role_parameters': {
                     'guest': {'args': {'data': {'train_data': [{'name': 'gov_ind_credit', 'namespace': 'gov2gov'}],
                                                 'eval_data': [{'name': 'gov_ind_credit', 'namespace': 'gov2gov'}]}},
                               'dataio_0': {'with_label': [True], 'label_name': ['y'], 'label_type': ['int'],
                                            'output_format': ['dense'], 'missing_fill': [True],
                                            'outlier_replace': [True]},
                               'evaluation_0': {'eval_type': ['binary'], 'pos_label': [1]}}, 'host': {'args': {
                         'data': {'train_data': [{'name': 'gov_second_try', 'namespace': 'gov2cmb'}],
                                  'eval_data': [{'name': 'gov_second_try', 'namespace': 'gov2cmb'}]}}, 'dataio_0': {
                         'with_label': [False], 'output_format': ['dense'], 'outlier_replace': [True]},
                         'evaluation_0': {
                             'need_run': [
                                 False]}}},
                                  'algorithm_parameters': {
                                      'hetero_lr_0': {'penalty': 'L2', 'optimizer': 'nesterov_momentum_sgd',
                                                      'tol': 0.0001, 'alpha': 0.01, 'max_iter': 30,
                                                      'early_stop': 'weight_diff', 'batch_size': -1,
                                                      'learning_rate': 0.15, 'validation_freqs': 3,
                                                      'early_stopping_rounds': 3,
                                                      'init_param': {'init_method': 'random_uniform'},
                                                      'cv_param': {'n_splits': 5, 'shuffle': False, 'random_seed': 103,
                                                                   'need_cv': False,
                                                                   'evaluate_param': {'eval_type': 'binary'}}},
                                      'intersect_0': {'intersect_method': 'rsa', 'sync_intersect_ids': True,
                                                      'only_output_key': False}},
                                  'config': '/data/projects/fate/python/fate_flow/examples/test_hetero_lr_job_conf_0702.json',
                                  'dsl': 'examples/test_hetero_lr_job_dsl_0702.json', 'function': 'submit_job'}}

import requests
import pprint
import json

url = "http://192.168.1.166:9380/v1/job/submit"
# response = requests.post(url=url, json=post_data)
# print(response.content)
# url1 = "http://192.168.1.166:9380/v1/job/query"


t = 'fasldfksj{}'.format('121213')
# print(t)

# params = {
#     "job_id": "2020070903410794466326"
# }

# response = requests.post(url=url1, json=params)
# rsp = json.loads(response.content.decode())
# pprint.pprint(rsp)

# import sys

# print(sys.modules[__name__])
# data = b'{"data":{"board_url":"http://fateboard:8080/index.html#/dashboard?job_id=202007100813362127359&role=guest&party_id=10006","job_dsl_path":"/data/projects/fate/python/jobs/202007100813362127359/job_dsl.json","job_runtime_conf_path":"/data/projects/fate/python/jobs/202007100813362127359/job_runtime_conf.json","logs_directory":"/data/projects/fate/python/logs/202007100813362127359","model_info":{"model_id":"arbiter-10006#guest-10006#host-10005#model","model_version":"202007100813362127359"}},"jobId":"202007100813362127359","retcode":0,"retmsg":"success"}\n'
# d1 = data.decode()
# print(d1)
# data2 = {"data": {
#     "board_url": "http://fateboard:8080/index.html#/dashboard?job_id=202007100813362127359&role=guest&party_id=10006",
#     "job_dsl_path": "/data/projects/fate/python/jobs/202007100813362127359/job_dsl.json",
#     "job_runtime_conf_path": "/data/projects/fate/python/jobs/202007100813362127359/job_runtime_conf.json",
#     "logs_directory": "/data/projects/fate/python/logs/202007100813362127359",
#     "model_info": {"model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "202007100813362127359"}},
#          "jobId": "202007100813362127359", "retcode": 0, "retmsg": "success"}
#
# print(data2['jobId'])
data = {"job_id": "2020071010021979129155", "role": "arbiter", "party_id": "10006"}

rsp = requests.post("http://192.168.1.122:9380/job/v1/pipeline/job/stop", json.dumps(data))
print(rsp.content)