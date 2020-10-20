# -*- coding: utf-8 -*-
# File              : test4.py
# Author            : tjh
# Create Date       : 2020/07/15
# Last Modified Date: 2020/07/15
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


# data1 = {'data': {
#     'board_url': 'http://fateboard:8080/index.html#/dashboard?job_id=2020071506512075914390&role=guest&party_id=10006',
#     'job_dsl_path': '/data/projects/fate/python/jobs/2020071506512075914390/job_dsl.json',
#     'job_runtime_conf_path': '/data/projects/fate/python/jobs/2020071506512075914390/job_runtime_conf.json',
#     'logs_directory': '/data/projects/fate/python/logs/2020071506512075914390',
#     'model_info': {'model_id': 'arbiter-10006#guest-10006#host-10005#model',
#                    'model_version': '2020071506512075914390'}},
#                   'jobId': '2020071506512075914390', 'retcode': 0,
#     'retmsg': 'success'}
# print(data1['data']['board_url'])
# a = data1['data']['model_info']['model_id']
# import requests
# params = {
#     "job_id": "2020071702325350322834",
#     "role": "guest",
#     "party_id": "10006"
# }
# rsp = requests.post('http://192.168.1.122:9380/v1/job/query', json=params)
#
# print(rsp.text)
# url = "http://192.168.1.122:8080/index.html#/dashboard?job_id=20200715092512514998111&role=guest&party_id=10006"
# import re
# z = re.findall('&role=(.*?)&party_id=(.*)', url)
# print(z)
# import re
# print(a)
# z = re.findall("arbiter-(.*?)#guest-(.*?)#host-(.*?)#model", a)
# print(z)
import json
import requests

# rsp = requests.get('http://192.168.1.122:8080/job/query/2020071508015330636094/guest/10006')
# z = json.loads(rsp.text)
# print(z)
data2 = {'code': 0, 'msg': 'OK', 'data': {
    'job': {'fJobId': '2020071508015330636094', 'fRole': 'guest', 'fPartyId': '10006', 'fName': '', 'fTag': '',
            'fInitiatorPartyId': '10006', 'fStatus': 'failed', 'fCurrentSteps': None,
            'fCurrentTasks': '["2020071508015330636094_hetero_lr_0"]', 'fProgress': 60, 'fCreateTime': 1594800113307,
            'fUpdateTime': 1594800454825, 'fStartTime': 1594800116524, 'fEndTime': 1594800454825, 'fElapsed': 338301,
            'fRunIp': '192.167.0.6:9380', 'fDescription': '',
            'fRoles': '{"guest": [10006], "host": [10005], "arbiter": [10006]}',
            'fDsl': '{"components": {"dataio_0": {"module": "DataIO", "input": {"data": {"data": ["args.train_data"]}}, "output": {"data": ["train"], "model": ["dataio"]}, "need_deploy": true}, "hetero_feature_binning_0": {"module": "HeteroFeatureBinning", "input": {"data": {"data": ["dataio_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_feature_binning"]}}, "hetero_feature_selection_0": {"module": "HeteroFeatureSelection", "input": {"data": {"data": ["hetero_feature_binning_0.train"]}, "isometric_model": ["hetero_feature_binning_0.hetero_feature_binning"]}, "output": {"data": ["train"], "model": ["selected"]}}, "hetero_lr_0": {"module": "HeteroLR", "input": {"data": {"train_data": ["hetero_feature_selection_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_lr"]}}, "evaluation_0": {"module": "Evaluation", "input": {"data": {"data": ["hetero_lr_0.train"]}}, "output": {"data": ["evaluate"]}}}}',
            'fRuntimeConf': '{"initiator": {"role": "guest", "party_id": 10006}, "job_parameters": {"work_mode": 1, "processors_per_node": 1, "model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "2020071508015330636094"}, "role": {"guest": [10006], "host": [10005], "arbiter": [10006]}, "role_parameters": {"guest": {"args": {"data": {"train_data": [{"name": "default_prediction_bank", "namespace": "cmb2gov"}]}}, "dataio_0": {"with_label": [true], "label_name": ["y"], "label_type": ["int"], "output_format": ["dense"]}}, "host": {"args": {"data": {"train_data": [{"name": "default_prediction_gov", "namespace": "gov2cmb"}]}}, "dataio_0": {"with_label": [false], "output_format": ["dense"]}}}, "algorithm_parameters": {"hetero_lr_0": {"penalty": "L2", "optimizer": "nesterov_momentum_sgd", "tol": 0.0001, "alpha": 0.01, "max_iter": 30, "early_stop": "weight_diff", "batch_size": -1, "learning_rate": 0.15, "init_param": {"init_method": "random_uniform"}, "sqn_param": {"update_interval_L": 3, "memory_M": 5, "sample_size": 5000, "random_seed": null}, "cv_param": {"n_splits": 5, "shuffle": false, "random_seed": 103, "need_cv": false, "evaluate_param": {"eval_type": "binary"}}}}}'},
    'dataset': {'partner': {'arbiter': [10006], 'host': [10005]}, 'model_summary': {'job': {'job_view': {}}},
                'roles': {'arbiter': [10006], 'host': [10005], 'guest': [10006]},
                'dataset': {'host': {'10005': {'train_data': 'gov2cmb.default_prediction_gov'}},
                            'guest': {'10006': {'train_data': 'cmb2gov.default_prediction_bank'}}}}}}

# t = ['Model_ID', 'Calc_Role', "Calc_Job_ID", "Calc_Party_ID", "Calc_Start_Time", "Calc_End_Time",
#      "Calc_ Time", "Calc_Status", "Calc_Note", "Calc_Result", "Result_Checker", 'Crt_Time', 'Upd_Time']
# import time
# from datetime import datetime
print(data2['data']['job']['fStartTime'])
print(data2['data']['dataset']['dataset'])
#
# stamp = 1594800116524
# 1559896210
# 1594800116524
# datatime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(str(stamp)[0:10])))
# datatime = datatime + '.' + str(stamp)[10:]
# print(datatime)
# d2 = time.strftime(f, time.localtime(ut))
data1 = {'f_create_time': 1595316715375, 'f_current_steps': None,
         'f_current_tasks': '["2020072107315537203973_evaluation_0"]', 'f_description': '',
         'f_dsl': '{"components": {"dataio_0": {"module": "DataIO", "input": {"data": {"data": ["args.train_data"]}}, "output": {"data": ["train"], "model": ["dataio"]}, "need_deploy": true}, "hetero_feature_binning_0": {"module": "HeteroFeatureBinning", "input": {"data": {"data": ["dataio_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_feature_binning"]}}, "hetero_feature_selection_0": {"module": "HeteroFeatureSelection", "input": {"data": {"data": ["hetero_feature_binning_0.train"]}, "isometric_model": ["hetero_feature_binning_0.hetero_feature_binning"]}, "output": {"data": ["train"], "model": ["selected"]}}, "hetero_lr_0": {"module": "HeteroLR", "input": {"data": {"train_data": ["hetero_feature_selection_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_lr"]}}, "evaluation_0": {"module": "Evaluation", "input": {"data": {"data": ["hetero_lr_0.train"]}}, "output": {"data": ["evaluate"]}}}}',
         'f_elapsed': 4545547, 'f_end_time': 1595321262438, 'f_initiator_party_id': '10006', 'f_is_initiator': 1,
         'f_job_id': '2020072107315537203973', 'f_name': '', 'f_party_id': '10006', 'f_progress': 100,
         'f_role': 'guest', 'f_roles': '{"guest": [10006], "host": [10005], "arbiter": [10006]}',
         'f_run_ip': '192.167.0.6:9380',
         'f_runtime_conf': '{"initiator": {"role": "guest", "party_id": 10006}, "job_parameters": {"work_mode": 1, "processors_per_node": 1, "model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "2020072107315537203973"}, "role": {"guest": [10006], "host": [10005], "arbiter": [10006]}, "role_parameters": {"guest": {"args": {"data": {"train_data": [{"name": "default_prediction_bank", "namespace": "cmb2gov"}]}}, "dataio_0": {"with_label": [true], "label_name": ["y"], "label_type": ["int"], "output_format": ["dense"]}}, "host": {"args": {"data": {"train_data": [{"name": "default_prediction_gov", "namespace": "gov2cmb"}]}}, "dataio_0": {"with_label": [false], "output_format": ["dense"]}}}, "algorithm_parameters": {"hetero_lr_0": {"penalty": "L2", "optimizer": "nesterov_momentum_sgd", "tol": 0.0001, "alpha": 0.01, "max_iter": 30, "early_stop": "weight_diff", "batch_size": -1, "learning_rate": 0.15, "init_param": {"init_method": "random_uniform"}, "sqn_param": {"update_interval_L": 3, "memory_M": 5, "sample_size": 5000, "random_seed": null}, "cv_param": {"n_splits": 5, "shuffle": false, "random_seed": 103, "need_cv": false, "evaluate_param": {"eval_type": "binary"}}}}}',
         'f_start_time': 1595316716891, 'f_status': 'success', 'f_tag': '', 'f_train_runtime_conf': '{}',
         'f_update_time': 1595321262438, 'f_work_mode': 1}

