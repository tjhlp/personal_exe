# -*- coding: utf-8 -*-
# File              : test17_testlog.py
# Author            : tjh
# Create Date       : 2020/07/29
# Last Modified Date: 2020/07/29
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import os
import logging
from threading import RLock
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from logging import StreamHandler

from flask.logging import default_handler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LoggerFactory(object):
    LOG_PATH = os.path.join(BASE_DIR, 'logs')

    LOG_PATH_ERROR = os.path.join(LOG_PATH, 'error.log')
    LOG_PATH_INFO = os.path.join(LOG_PATH, 'info.log')
    LOG_PATH_ALL = os.path.join(LOG_PATH, 'all.log')

    LEVEL = logging.DEBUG
    FORMAT = "[%(levelname)s] [%(asctime)s] [%(process)s:%(thread)s] - %(filename)s[line:%(lineno)d]: %(message)s"

    # 日志文件最大 100MB
    LOG_FILE_MAX_BYTES = 100 * 1024 * 1024
    # 轮转数量是 10 个
    LOG_FILE_BACKUP_COUNT = 10

    # 线程锁
    lock = RLock()

    schedule_logger_dict = {}

    @staticmethod
    def init_app(app):
        # 移除默认的handler, 设置全局的logging
        app.logger.removeHandler(default_handler)
        logging.basicConfig(level=logging.DEBUG)  # 调试debug级
        formatter = logging.Formatter(
            "[%(levelname)s] [%(asctime)s] [%(process)s:%(thread)s] - %(filename)s[line:%(lineno)d]: %(message)s"
        )

        # 将日志输出到文件
        # 1 MB = 1024 * 1024 bytes
        # 此处设置日志文件大小为500MB，超过500MB自动开始写入新的日志文件，历史文件归档
        file_handler = RotatingFileHandler(
            filename=LoggerFactory.LOG_PATH_ALL,
            mode='a',
            maxBytes=LoggerFactory.LOG_FILE_MAX_BYTES,
            backupCount=LoggerFactory.LOG_FILE_BACKUP_COUNT,
            encoding='utf-8'
        )

        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

        stream_handler = StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.DEBUG)

        logging.getLogger().addHandler(file_handler)
        logging.getLogger().addHandler(stream_handler)

    @staticmethod
    def get_handler(level=None, log_dir=None, log_type=None):

        log_file = os.path.join(log_dir, "INFO.log" if level == LoggerFactory.LEVEL else 'ERROR.log')
        formatter = logging.Formatter(LoggerFactory.FORMAT)
        handler = TimedRotatingFileHandler(log_file,
                                           when='D',
                                           interval=1,
                                           backupCount=14,
                                           delay=True)

        if level:
            handler.level = level

        handler.setFormatter(formatter)
        return handler

    @staticmethod
    def get_schedule_logger(job_id='', log_type='schedule'):
        job_log_dir = os.path.join(BASE_DIR, 'logs', job_id)
        os.makedirs(job_log_dir, exist_ok=True)
        logger = logging.getLogger('{}_{}'.format(job_id, log_type))
        logger.setLevel(LoggerFactory.LEVEL)
        handler = LoggerFactory.get_handler(level=LoggerFactory.LEVEL, log_dir=job_log_dir, log_type=log_type)
        error_handler = LoggerFactory.get_handler(level=logging.ERROR, log_dir=job_log_dir, log_type=log_type)
        logger.addHandler(handler)
        logger.addHandler(error_handler)

        if job_id:
            with LoggerFactory.lock:
                LoggerFactory.schedule_logger_dict[job_id + log_type] = logger
        return logger


def schedule_logger(job_id=None):
    return LoggerFactory.get_schedule_logger(job_id)


def setup_global_logger(app):
    return LoggerFactory.init_app(app)
