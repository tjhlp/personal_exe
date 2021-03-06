APP_NAME = 'account_main'

LOG_SET = {
    'filename': '/data/logs/%s/%s.log' % (APP_NAME, APP_NAME),
    'maxBytes': 1000 * 1024 * 1024,
    'backupCount': 9
}

DLOG_SET = {
    'filename': '/data/logs/dlog/%s.log' % APP_NAME,
    'maxBytes': 100 * 1024 * 1024,
    'backupCount': 9
}

DB_ACCOUNT_RELEASE = {
    'host': '192.168.1.122',
    'port': 9306,
    'user': 'root',
    'password': 'ZZfwq@2020',
    'database': 'prof_model_set',
    'charset': 'utf8',
    'autocommit': True,
    'connect_timeout': 3,
    'read_timeout': 10,
    'write_timeout': 5
}


