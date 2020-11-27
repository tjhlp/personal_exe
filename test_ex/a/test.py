import numpy as np
import pandas as pd


class MessageBox():
    """
        相关函数，传递信息函数
    """

    def __init__(self, role_type):
        self.role_type = role_type
        self.msg = ["msg_box"]

    def set_msg(self, msg):
        """
        相关函数，设置消息
        :param msg: 可以是str,list, dict,dataframe格式需要转化为dict或者list传递
        :return:
        """
        self.msg.append(msg)

    def get_msg(self):
        """
        相关函数，获取消息
        :return:
        """
        return {self.role_type: self.msg}


class CustomModelHost():
    def __init__(self):
        """
        必要函数，初始化

        该文本是python脚步文件，该脚步文件命名为zeng_defaultPred.py
        下面是上传模型规则：
        a. 模型上传格式：.py
        b. 命名规则：上传者+模型名称.py，如zeng_regression.py
        c. 编辑工具：python通用工具，如pycharm，jupyter notebook。
        d. 规则：
            上传的py文件里面包括CustomModel类；
            model可调用predict预测函数，如model.predict(X_test)。
        e. 模型计算要求：
            时间复杂度要求：线性
            空间复杂度要求：线性
        """
        self.msg_box = MessageBox("host")

    def pre_process(self, X):
        """
        相关函数，数据预处理
        """
        X.fillna(0, inplace=True)
        self.msg_box.set_msg({'数据预处理': X.to_dict()})
        return X

    def predict(self, X):
        """
        必要函数，预测, 直接定义规则
        """
        return X.sum(axis=1).map(lambda x: 1 if x > 0 else 0)


def run(X, role_type):
    if role_type == 'guest':
        i_model = CustomModelGuest()
    elif role_type == 'host':
        i_model = CustomModelHost()
    else:
        i_model = CustomModelArbiter()

    X_test = i_model.pre_process(X)
    return i_model, X_test


