# -*- coding: utf-8 -*-
# File              : test_22_.py
# Author            : tjh
# Create Date       : 2020/08/27
# Last Modified Date: 2020/08/27
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

# m_res = {'index': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], 'columns': ['y'],
#          'data': [[1.179973976184657], [0.9528737700678693], [1.3963551340278977], [0.9543470626401214],
#                   [1.5471948941241613], [1.6132580268627112], [1.0337461173121048], [0.8785244808715358],
#                   [1.2860313616507275], [0.49103802627692866], [0.33757359675819887], [0.709710202868377],
#                   [0.7700916094830438], [1.808794073923235], [1.647027874024134], [1.6097333884862621],
#                   [0.7493718348726537], [1.114052117890734]]}
# res = []
# for k, v in enumerate(m_res['index']):
#     res.append([v, m_res['data'][k]])
#
# print(res)


data1 = {'description': {'external_data': 'x来自于政府人力资源管理局的人才政策申请表，包括',
                         'info': '该文件是招商银行对政数局发起请求的文件，包括相应的数据路径，相应的标签和特征;是深圳人才闪电贷模型',
                         'return': '返回h是一个数，表示来自政府的反馈，用于最后信用评分的计算'}, 'dst': '192.168.1.166',
         'model': {'data_label': 'y', 'external_data_localtion': 'gov_feature_flash_loan_for_test.csv',
                   'external_used_columns': ['ID', 'ZJLX', '性别', '人才评级'],
                   'local_data_localtion': 'cmb_feature_flash_loan_for test.csv',
                   'model_definition': {'model': 'HeteroLR',
                                        'params': {'alpha': 0.01,
                                                   'batch_size': -1,
                                                   'cv_param': {
                                                       'evaluate_param': {
                                                           'eval_type': 'binary',
                                                           'need_run': True,
                                                           'pos_label': 0},
                                                       'n_splits': 5,
                                                       'need_cv': False,
                                                       'random_seed': 103,
                                                       'shuffle': False},
                                                   'decay': 1,
                                                   'decay_sqrt': True,
                                                   'early_stop': 'weight_diff',
                                                   'encrypt_param': {
                                                       'method': None},
                                                   'init_param': {
                                                       'init_method': 'random_uniform'},
                                                   'learning_rate': 0.15,
                                                   'max_iter': 30,
                                                   'metrics': [
                                                       'auc',
                                                       'ks'],
                                                   'optimizer': 'sgd',
                                                   'penalty': 'L2',
                                                   'predict_param': {
                                                       'threshold': 0.5,
                                                       'with_proba': True},
                                                   'sqn_param': {
                                                       'memory_M': 5,
                                                       'random_seed': None,
                                                       'sample_size': 5,
                                                       'update_interval_L': 3},
                                                   'tol': 0.0001,
                                                   'use_first_metrics_only': False,
                                                   'validation_freqs': [
                                                       10,
                                                       15]}}},
         'src': '192.168.1.122'}
list1 = [11111, 22222]
list2 = list1[::-1]
print(list2)
