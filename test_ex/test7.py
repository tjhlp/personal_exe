import time


def stamp_to_time(stamp):
    """fate平台时间戳转化为时间"""
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(str(stamp)[0:10])))
    # date_time += '.' + str(stamp)[10:]
    return date_time


job_rsp = {'data': [
    {'f_create_time': 1594973275604, 'f_current_steps': None, 'f_current_tasks': None, 'f_description': '',
     'f_dsl': '{"components": {"dataio_0": {"module": "DataIO", "input": {"data": {"data": ["args.train_data"]}}, "output": {"data": ["train"], "model": ["dataio"]}, "need_deploy": true}, "hetero_feature_binning_0": {"module": "HeteroFeatureBinning", "input": {"data": {"data": ["dataio_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_feature_binning"]}}, "hetero_feature_selection_0": {"module": "HeteroFeatureSelection", "input": {"data": {"data": ["hetero_feature_binning_0.train"]}, "isometric_model": ["hetero_feature_binning_0.hetero_feature_binning"]}, "output": {"data": ["train"], "model": ["selected"]}}, "hetero_lr_0": {"module": "HeteroLR", "input": {"data": {"train_data": ["hetero_feature_selection_0.train"]}}, "output": {"data": ["train"], "model": ["hetero_lr"]}}, "evaluation_0": {"module": "Evaluation", "input": {"data": {"data": ["hetero_lr_0.train"]}}, "output": {"data": ["evaluate"]}}}}',
     'f_elapsed': None, 'f_end_time': None, 'f_initiator_party_id': '10006', 'f_is_initiator': 1,
     'f_job_id': '2020071708075560289249', 'f_name': '', 'f_party_id': '10006', 'f_progress': 0, 'f_role': 'guest',
     'f_roles': '{"guest": [10006], "host": [10005], "arbiter": [10006]}', 'f_run_ip': '192.167.0.6:9380',
     'f_runtime_conf': '{"initiator": {"role": "guest", "party_id": 10006}, "job_parameters": {"work_mode": 1, "processors_per_node": 1, "model_id": "arbiter-10006#guest-10006#host-10005#model", "model_version": "2020071708075560289249"}, "role": {"guest": [10006], "host": [10005], "arbiter": [10006]}, "role_parameters": {"guest": {"args": {"data": {"train_data": [{"name": "default_prediction_bank", "namespace": "cmb2gov"}]}}, "dataio_0": {"with_label": [true], "label_name": ["y"], "label_type": ["int"], "output_format": ["dense"]}}, "host": {"args": {"data": {"train_data": [{"name": "default_prediction_gov", "namespace": "gov2cmb"}]}}, "dataio_0": {"with_label": [false], "output_format": ["dense"]}}}, "algorithm_parameters": {"hetero_lr_0": {"penalty": "L2", "optimizer": "nesterov_momentum_sgd", "tol": 0.0001, "alpha": 0.01, "max_iter": 30, "early_stop": "weight_diff", "batch_size": -1, "learning_rate": 0.15, "init_param": {"init_method": "random_uniform"}, "sqn_param": {"update_interval_L": 3, "memory_M": 5, "sample_size": 5000, "random_seed": null}, "cv_param": {"n_splits": 5, "shuffle": false, "random_seed": 103, "need_cv": false, "evaluate_param": {"eval_type": "binary"}}}}}',
     'f_start_time': None, 'f_status': 'waiting', 'f_tag': '', 'f_train_runtime_conf': '{}', 'f_update_time': None,
     'f_work_mode': 1}], 'retcode': 0, 'retmsg': 'success'}

job_data = job_rsp['data'][0]
# print(job_data)
calc_start = stamp_to_time(job_data['f_create_time']) if job_data['f_create_time'] else job_data['f_create_time']
calc_end = stamp_to_time(job_data['f_end_time']) if job_data['f_end_time'] else job_data['f_end_time']
# insert_data = [js['modelID'], role, fate_rsp['jobId'], party_id, calc_start, calc_end, 0, job_data['fStatus'],
#                '', 0, '', js['openNodeID'], now, now]
# insert_sql = db_.db_insert(sql01, insert_data)
# rsp['reqID'] = insert_sql
import json

f_runtime_conf = json.loads(job_data['f_runtime_conf'])
print(f_runtime_conf)
conf = {'initiator': {'role': 'guest', 'party_id': 10006},
        'job_parameters': {'work_mode': 1, 'processors_per_node': 1,
                                                                              'model_id': 'arbiter-10006#guest-10006#host-10005#model',
                                                                              'model_version': '2020071708075560289249'},
        'role': {'guest': [10006], 'host': [10005], 'arbiter': [10006]},
        'role_parameters': {
        'guest': {'args': {'data': {'train_data': [{'name': 'default_prediction_bank', 'namespace': 'cmb2gov'}]
                                    }},
                  'dataio_0': {'with_label': [True], 'label_name': ['y'], 'label_type': ['int'],
                               'output_format': ['dense']}},
        'host': {'args': {'data': {'train_data': [{'name': 'default_prediction_gov', 'namespace': 'gov2cmb'}]}},
                 'dataio_0': {'with_label': [False], 'output_format': ['dense']}}},
        'algorithm_parameters': {
        'hetero_lr_0': {'penalty': 'L2', 'optimizer': 'nesterov_momentum_sgd', 'tol': 0.0001, 'alpha': 0.01,
                        'max_iter': 30, 'early_stop': 'weight_diff', 'batch_size': -1, 'learning_rate': 0.15,
                        'init_param': {'init_method': 'random_uniform'},
                        'sqn_param': {'update_interval_L': 3, 'memory_M': 5, 'sample_size': 5000, 'random_seed': None},
                        'cv_param': {'n_splits': 5, 'shuffle': False, 'random_seed': 103, 'need_cv': False,
                                     'evaluate_param': {'eval_type': 'binary'}}}}}
# print(conf['role_parameters']['guest']['args']['data']['train_data'][0])
d = conf['role_parameters']['guest']['args']['data']['train_data'][0]
print('{}.{}'.format(d['namespace'], d['name']))
z = conf['algorithm_parameters'].keys()
print(list(z)[0])

data3 = {
	"systemID":"DS",
	"version":"1.0.0",
	"modelName": "太子路拥挤情况预测模型",
	"modelDesc": "测试太子路拥挤指数",
	"modelTarget": "交通拥挤指数",
	"objectParam": ["太子路","2020-01-01 09:00:00","2020-01-01 17:00:00"],
	"modelType": "1",
	"source":  [{
	      "table_ID":"tab_online_order",
	      "coulumns":[{"name":"speed", "rel":"avg","ID":"p1","condition_param":"25","condition_rel":">"},
	      			{"name":"track_record", "rel":"max", "ID":"p2"}]}],
	"modelRelation":  {"source_1":"10 *p1 + p2(p3*10) + 04 *200"},
	"front_data": {"css_data":"css样式"},
	"ownNodeID": "1"

}
print(data3.values()[0])

"2020-01-01 09:32:22"
"2020-01-01 09:00:00"

