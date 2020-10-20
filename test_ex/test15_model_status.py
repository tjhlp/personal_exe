# -*- coding: utf-8 -*-
# File              : test15_model_status.py
# Author            : tjh
# Create Date       : 2020/07/28
# Last Modified Date: 2020/07/28
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import json
import requests

# IP_PORT1 = '192.168.1.122:9380'
# job_url = "http://{}/v1/job/query".format(IP_PORT1)
# params = {
#     "job_id": '2020072802310797567141',
#     "party_id": '10006',
#     "role": 'guest'
# }
# job_rsp = json.loads(requests.post(job_url, json=params).text)

data1 = {'data': [{'f_create_time': 1595903467985, 'f_current_steps': None,
                   'f_current_tasks': '["2020072802310797567141_hetero_lr_0"]', 'f_description': '',
                   'f_dsl': '{"components": {"dataio_0": {"module": "DataIO", "input": {"model": ["pipeline.dataio_0.dataio"], "data": {"data": ["args.eval_data"]}}, "output": {"data": ["train"]}, "CodePath": "federatedml/util/data_io.py/DataIO"}, "intersection_0": {"module": "Intersection", "output": {"data": ["intersect_train"]}, "input": {"data": {"data": ["dataio_0.train"]}}, "CodePath": "federatedml/statistic/intersect/intersect_model.py/IntersectGuest"}, "feature_scale_0": {"module": "FeatureScale", "input": {"model": ["pipeline.feature_scale_0.feature_scale"], "data": {"data": ["intersection_0.intersect_train"]}}, "output": {"data": ["scale_train"]}, "CodePath": "federatedml/feature/scale.py/Scale"}, "hetero_lr_0": {"module": "HeteroLR", "input": {"model": ["pipeline.hetero_lr_0.hetero_lr"], "data": {"eval_data": ["feature_scale_0.scale_train"]}}, "output": {"data": ["trained_data"]}, "CodePath": "federatedml/linear_model/logistic_regression/hetero_logistic_regression/hetero_lr_guest.py/HeteroLRGuest"}}}',
                   'f_elapsed': 88188, 'f_end_time': 1595903556993, 'f_initiator_party_id': '10006',
                   'f_is_initiator': 1, 'f_job_id': '2020072802310797567141', 'f_name': '', 'f_party_id': '10006',
                   'f_progress': 100, 'f_role': 'guest',
                   'f_roles': '{"guest": [10006], "host": [10005], "arbiter": [10006]}', 'f_run_ip': '192.167.0.6:9380',
                   'f_runtime_conf': '{"initiator": {"role": "guest", "party_id": 10006}, "job_parameters": {"work_mode": 1, "job_type": "predict", "model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "2020072801421880546633"}, "role": {"guest": [10006], "host": [10005], "arbiter": [10006]}, "role_parameters": {"guest": {"args": {"data": {"eval_data": [{"name": "cmb_features", "namespace": "cmb2gov"}]}}}, "host": {"args": {"data": {"eval_data": [{"name": "gov_features", "namespace": "gov2cmb"}]}}}}, "config": "/data/projects/fate/python/examples/flp-examples/predict_conf.json", "function": "submit_job", "work_mode": 1}',
                   'f_start_time': 1595903468805, 'f_status': 'success', 'f_tag': '',
                   'f_train_runtime_conf': '{"initiator": {"role": "guest", "party_id": 10006}, "job_parameters": {"work_mode": 1, "processors_per_node": 1, "model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "2020072801421880546633"}, "role": {"guest": [10006], "host": [10005], "arbiter": [10006]}, "role_parameters": {"guest": {"args": {"data": {"train_data": [{"name": "cmb_features", "namespace": "cmb2gov"}], "eval_data": [{"name": "cmb_features", "namespace": "cmb2gov"}]}}, "dataio_0": {"with_label": [true], "label_name": ["y"], "label_type": ["int"], "output_format": ["dense"], "missing_fill": [true], "missing_fill_method": ["min"]}, "feature_scale_0": {"method": ["standard_scale"], "need_run": [false]}, "evaluation_0": {"eval_type": ["binary"], "pos_label": [1]}}, "host": {"args": {"data": {"train_data": [{"name": "gov_features", "namespace": "gov2cmb"}], "eval_data": [{"name": "gov_features", "namespace": "gov2cmb"}]}}, "dataio_0": {"with_label": [false], "output_format": ["dense"], "missing_fill": [true], "outlier_replace": [true]}, "feature_scale_0": {"method": ["standard_scale"], "need_run": [false]}}}, "algorithm_parameters": {"hetero_lr_0": {"penalty": "L2", "optimizer": "sgd", "tol": 0.0001, "alpha": 0.01, "max_iter": 30, "early_stop": "weight_diff", "batch_size": -1, "learning_rate": 0.15, "init_param": {"init_method": "random_uniform"}, "sqn_param": {"update_interval_L": 3, "memory_M": 5, "sample_size": 5, "random_seed": null}, "cv_param": {"n_splits": 5, "shuffle": false, "random_seed": 103, "need_cv": false, "evaluate_param": {"eval_type": "binary", "pos_label": 0, "need_run": true}}, "decay": 1, "decay_sqrt": true, "encrypt_param": {"method": null}, "predict_param": {"with_proba": true, "threshold": 0.5}, "validation_freqs": [10, 15], "metrics": ["auc", "ks"], "use_first_metrics_only": false}, "intersect_0": {"intersect_method": "rsa", "sync_intersect_ids": true, "only_output_key": false}}}',
                   'f_update_time': 1595903556993, 'f_work_mode': 1}], 'retcode': 0, 'retmsg': 'success'}

job_data = data1['data'][0]
calc_end = job_data['f_end_time']
calc_status = job_data['f_status']
calc_progress = job_data['f_progress']
calc_job_id = job_data['f_job_id']


f_conf = json.loads(job_data['f_runtime_conf'])

print(f_conf['role_parameters']['guest']['args']['data'])



