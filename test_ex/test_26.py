# data1 = {'job_dsl': {'components': {'dataio_0': {'module': 'DataIO', 'input': {'data': {'data': ['args.train_data']}},
#                                                  'output': {'data': ['train'], 'model': ['dataio']}},
#                                     'intersection_0': {'module': 'Intersection',
#                                                        'input': {'data': {'data': ['dataio_0.train']}},
#                                                        'output': {'data': ['intersect_train']}},
#                                     'feature_scale_0': {'module': 'FeatureScale',
#                                                         'input': {'data': {'data': ['intersection_0.intersect_train']}},
#                                                         'output': {'data': ['scale_train'],
#                                                                    'model': ['feature_scale']}},
#                                     'hetero_lr_0': {'module': 'HeteroLR',
#                                                     'input': {'data': {'train_data': ['feature_scale_0.scale_train']}},
#                                                     'output': {'data': ['trained_data'], 'model': ['hetero_lr']}},
#                                     'evaluation_0': {'module': 'Evaluation',
#                                                      'input': {'data': {'data': ['hetero_lr_0.trained_data']}}}}},
#          'job_runtime_conf': {'initiator': {'role': 'guest', 'party_id': 16800},
#                               'job_parameters': {'work_mode': 1, 'processors_per_node': 1},
#                               'role': {'guest': [16800], 'host': [16899], 'arbiter': [16800]},
#                               'role_parameters': {
#                                   'guest': {
#                                   'args': {'data': {
#                                       'train_data': [{'name': 'breast_hetero_mini_guest', 'namespace': 'test'}],
#                                       'eval_data': [{'name': 'breast_hetero_mini_guest', 'namespace': 'test'}]}},
#                                   'dataio_0': {'with_label': [True], 'label_name': ['y'], 'label_type': ['int'],
#                                                'output_format': ['dense'],
#                                                'missing_fill': [True], 'missing_fill_method': ['min']},
#                                   'feature_scale_0': {'method': ['standard_scale'], 'need_run': [False]},
#                                   'evaluation_0': {'eval_type': ['binary'], 'pos_label': [1]}},
#                                   'host': {'args': {
#                                   'data': {'train_data': [{'name': '', 'namespace': ''}],
#                                            'eval_data': [{'name': '', 'namespace': ''}]}},
#                                   'dataio_0': {'with_label': [False],
#                                                'output_format': ['dense'],
#                                                'missing_fill': [True],
#                                                'outlier_replace': [True]},
#                                   'feature_scale_0': {
#                                       'method': ['standard_scale'],
#                                       'need_run': [False]}}},
#                               'algorithm_parameters': {'hetero_lr_0': {'alpha': 0.01, 'batch_size': -1, 'cv_param': {
#                                   'evaluate_param': {'eval_type': 'binary', 'need_run': True, 'pos_label': 0},
#                                   'n_splits': 5,
#                                   'need_cv': False, 'random_seed': 103, 'shuffle': False}, 'decay': 1,
#                                                                        'decay_sqrt': True,
#                                                                        'early_stop': 'weight_diff',
#                                                                        'encrypt_param': {'method': None},
#                                                                        'init_param': {'init_method': 'random_uniform'},
#                                                                        'learning_rate': 0.15, 'max_iter': 30,
#                                                                        'metrics': ['auc', 'ks'], 'optimizer': 'sgd',
#                                                                        'penalty': 'L2',
#                                                                        'predict_param': {'threshold': 0.5,
#                                                                                          'with_proba': True},
#                                                                        'sqn_param': {'memory_M': 5, 'random_seed': None,
#                                                                                      'sample_size': 5,
#                                                                                      'update_interval_L': 3},
#                                                                        'tol': 0.0001, 'use_first_metrics_only': False,
#                                                                        'validation_freqs': [10, 15]},
#                                                        'intersect_0': {'intersect_method': 'rsa',
#                                                                        'sync_intersect_ids': True,
#                                                                        'only_output_key': False}}}}




b_str = "实".encode('gb2312')
print(b_str)
print(list(b_str))
for i in list(b_str):
    t = str(hex(i))
    print(t[2:])





