# -*- coding: utf-8 -*-
# File              : test_blue.py
# Author            : tjh
# Create Date       : 2020/08/04
# Last Modified Date: 2020/08/04
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import logging
from random import randint

from flask import Blueprint

from test17_testlog import schedule_logger

json_blu = Blueprint('json', __name__)


@json_blu.route('/test')
def json_index():
    a, b = randint(1, 15), randint(1, 15)
    schedule_logger('124').info('submit job, job_id {}, body {}'.format('1213', '12312'))
    schedule_logger('124').error('submit job, job_id {}, body {}'.format('1213', '12312'))
    logging.info('Adding two random numbers {} {}'.format(a, b))
    logging.error('sfdsfsd')
    return '111'

"""
data: "Please check if the fate flow server of the other party is started. rpc request error:
 <_Rendezvous of RPC that terminated with:↵	status = StatusCode.UNAVAILABLE↵	
 details = "Unable to resolve host proxy"↵	
 debug_error_string = "{"created":"@1600404217.429157424","description":"Error received from peer ipv4:10.98.203.3:9370",
 "file":"src/core/lib/surface/call.cc","file_line":1052,"grpc_message":"Unable to resolve host proxy","grpc_status":14}"↵>"
errCod: 1002
errMsg: "访问fate平台失败"
"""