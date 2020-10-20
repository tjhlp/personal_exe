# -*- coding: utf-8 -*-
# File              : model_app.py
# Author            : tjh
# Create Date       : 2020/07/13
# Last Modified Date: 2020/07/13
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import os
import json
import requests

from flask import Blueprint

from utils.response_code import *
from utils.server_resolver import get_post_data

model_blu = Blueprint('model', __name__)


@model_blu.route('/run_model/', methods=['post'])
def run_model():
    try:
        config_path = "/root/node_fl/templates/guest_request_builtin_model_template_0708.json"
        post_data = get_post_data(config_path)
        response = requests.post("http://192.168.1.122:9380/v1/job/submit", json=post_data)
        # print(response.content)
        rsp = response.text
        t = json.loads(rsp)
    except Exception as e:
        return get_response(CODE_TASK_ERROR)

    res = {'jobID': t['jobId']}
    return get_response(CODE_SUCCESS, res)
