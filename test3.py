# -*- coding: utf-8 -*-
# File              : test3.py
# Author            : tjh
# Create Date       : 2020/07/13
# Last Modified Date: 2020/07/13
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


# -*- coding: utf-8 -*-
# File              : flp_app.py
# Author            : tjh
# Create Date       : 2020/07/02
# Last Modified Date: 2020/07/02
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import os
import json
import logging
import requests
from flask import Flask, request, send_from_directory

from utils.response_code import *
from utils.server_resolver import get_post_data

manager = Flask(__name__)


@manager.route('/upload_json/', methods=['post'])
def upload_json():
    file = request.files['file']
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'upload_tmp', file.filename)
    res = []
    for i in file:
        tmp = i.decode()
        res.append(tmp)
    try:
        file.save(filename)
    except Exception as e:
        logging.info('file save got exception:%s' % e)
        return get_response(CODE_FILE_FAILURE)

    return get_response(CODE_SUCCESS, res)


@manager.route('/download_json/')
def download_json():
    rsp = send_from_directory(r"/root/node_fl/templates", filename="guest_request_builtin_model_template.json",
                              as_attachment=True)

    return rsp


@manager.route('/run_model/', methods=['post'])
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


def main():
    # 路径严格关闭
    manager.url_map.strict_slashes = False
    manager.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == '__main__':
    main()
