# -*- coding: utf-8 -*-
# File              : upload_test.py
# Author            : Jianhuan Zeng
# Date              : 2020/07/09
# Last Modified Date: 2020/07/09
# Last Modified By  : Jianhuan Zeng
# Description       : 联邦学习平台的解析
# ******************************************************
import json
import requests

DEFAULT_PATH = "/root/node_fl/templates/dev_guest_request_dsl.json"

DEFAULT_CONF_PATH = "/root/node_fl/templates/dev_guest_request_conf.json"
DEFAULT_DSL_PATH = "/root/node_fl/templates/dev_guest_request_dsl.json"


def get_post_data(config_path, path=DEFAULT_CONF_PATH, dsl_path=DEFAULT_DSL_PATH):
    # 1. 输入conf
    if not config_path:
        raise Exception('the following arguments are required: {}'.format('conf path'))
    with open(path, 'r') as f:
        config_data = json.load(f)
    with open(config_path, 'r') as f:
        input_config = json.load(f)

    # 2. 解析conf
    config_data["algorithm_parameters"]["hetero_lr_0"] = input_config["model"]["model_definition"]["params"]

    # 3. 发送给相应服务
    with open(dsl_path, 'r') as f:
        dsl_data = json.load(f)
    post_data = {'job_dsl': dsl_data,
                 'job_runtime_conf': config_data}
    return post_data


if __name__ == '__main__':
    config_path = "/root/node_fl/templates/guest_request_builtin_model_template_0708.json"
    post_data = get_post_data(config_path)
    URL = "http://192.168.1.122:9380/v1/job/submit"
    response = requests.post(URL, json=post_data)
    rsp = response.text
    t = json.loads(rsp)

    print(t['jobId'])

