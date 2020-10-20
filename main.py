# -*- coding: utf-8 -*-
# File              : flp_app.py
# Author            : tjh
# Create Date       : 2020/07/02
# Last Modified Date: 2020/07/02
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

from flask import Flask

from apps.upload_download_app import json_blu
from apps.model_app import model_blu

manager = Flask(__name__)


def main():
    # 路径严格关闭
    # manager.url_map.strict_slashes = False
    manager.register_blueprint(json_blu, url_prefix='/json')
    manager.register_blueprint(model_blu, url_prefix='/model')
    manager.run(host='127.0.0.1', port=8000, debug=True)


if __name__ == '__main__':
    main()
