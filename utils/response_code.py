# -*- coding: utf-8 -*-
# File              : response_code.py
# Author            : tjh
# Create Date       : 2020/07/08
# Last Modified Date: 2020/07/08
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

from flask import jsonify


def get_response(code, return_value=None):
    """json数据返回"""

    all_js = {
        'errCod': code[0],
        'errMsg': code[1]
    }
    if return_value:
        all_js['data'] = return_value
    return jsonify(all_js)


CODE_SUCCESS = (0, '成功', 0)
CODE_FILE_FAILURE = (1, '保存文件失败', 0)
CODE_TASK_ERROR = (2, '队列任务过多错误', 0)
