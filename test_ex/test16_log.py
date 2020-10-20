# -*- coding: utf-8 -*-
# File              : test16_log.py
# Author            : tjh
# Create Date       : 2020/07/28
# Last Modified Date: 2020/07/28
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import logging
import logging.config
from random import randint
from flask import Flask, Blueprint
from flask_log_request_id import RequestID, RequestIDLogFilter

from test_ex.test17_testlog import schedule_logger, setup_global_logger
from test_blue import json_blu

def generic_add(a, b):
    """Simple function to add two numbers that is not aware of the request id"""
    logging.debug('Called generic_add({}, {})'.format(a, b))
    return a + b




app = Flask(__name__)
setup_global_logger(app)

app.register_blueprint(json_blu, url_prefix='/json')


@app.route('/')
def index():
    # a, b = randint(1, 15), randint(1, 15)
    # schedule_logger('124').info('submit job, job_id {}, body {}'.format('1213', '12312'))
    # schedule_logger('124').error('submit job, job_id {}, body {}'.format('1213', '12312'))
    # logging.info('Adding two random numbers {} {}'.format(a, b))
    # logging.error('sfdsfsd')
    # return str(generic_add(a, b))
    return '111'





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
