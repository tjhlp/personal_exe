# -*- coding: utf-8 -*-
# File              : test_25_register.py
# Author            : tjh
# Create Date       : 2020/10/23
# Last Modified Date: 2020/10/23
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


from flask import Flask
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)
# eureka_client.register_with-eureka=false
# eureka_client.fetch-registry=false

def setEureka():
    server_host = "192.168.1.100"
    server_port = 5000
    eureka_client.init(eureka_server="http://192.168.0.130:8761/eureka",
                       app_name="flask_server2",
                       # 当前组件的主机名，可选参数，如果不填写会自动计算一个，如果服务和 eureka 服务器部署在同一台机器，请必须填写，否则会计算出 127.0.0.1
                       # instance_host=server_host,
                       instance_port=server_port,
                       # 调用其他服务时的高可用策略，可选，默认为随机
                       ha_strategy=eureka_client.HA_STRATEGY_RANDOM)


setEureka()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/info')
def hello_world1():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000, host="0.0.0.0")