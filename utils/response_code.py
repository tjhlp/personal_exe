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
CODE_INPUT_PARAM_MISS = (400, '缺少必要的输入参数', 0)
CODE_INPUT_PARAM_INVALID = (401, '参数输入错误', 0)
CODE_NOT_AHTH = (402, '用户未授权', -1)
CODE_UNKOWN_OPERATION = (404, '没有这个操作', -1)
CODE_INVALID_JSON = (406, '请求中的内容不是一个合法Json格式', -1)
CODE_INVALID_PAGE_INDEX_SIZE = (407, '分页参数不对，注意page_index是从1开始', -1)
CODE_FEQ_LIMIT = (408, '系统访问频率过快，请稍后再试', -1)
CODE_INPUT_PARAM_INVALID_TYPE = (409, '参数类型错误', -1)
CODE_QUERY_ERROR = (410, '查询错误', -1)
CODE_ACTION_FAILED = (411, '操作失败，请稍后重试', 0)