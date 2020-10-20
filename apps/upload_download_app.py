# -*- coding: utf-8 -*-
# File              : upload_download_app.py
# Author            : tjh
# Create Date       : 2020/07/08
# Last Modified Date: 2020/07/08
# Last Modified By  : tjh
# Reference         :
# Description       : json文件的上传和下载
# ******************************************************

import os
import logging


from flask import request, send_from_directory, Blueprint

from utils.response_code import *

json_blu = Blueprint('json', __name__)


@json_blu.route('/upload_json/', methods=['post'])
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


@json_blu.route('/download_json/')
def download_json():
    rsp = send_from_directory(r"/root/node_fl/templates", filename="guest_request_builtin_model_template.json",
                              as_attachment=True)

    return rsp

