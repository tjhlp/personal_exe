import numpy as np
import pandas as pd


# from utils import remote_api
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


class CustomModelGuest():
    def __init__(self):
        """
        必要函数，初始化，业务发起方，例如招行节点执行的脚本
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
        self.msg_box = MessageBox("guest")

    def pre_process(self, X):
        """
        相关函数，数据预处理
        """
        self.msg_box.set_msg('数据预处理')
        return X

    def predict(self, X):
        """
        必要函数，预测, 直接定义规则
        """
        y = X['score']
        self.msg_box.set_msg(y)
        return y


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


class CustomModelArbiter():
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
        self.msg_box = MessageBox("arbiter")

    def pre_process(self, X):
        """
        相关函数，数据预处理
        """
        X.fillna(0, inplace=True)
        X.columns = ['host', 'guest']
        X['host'] = 1 - X['host']
        self.msg_box.set_msg({'host': X.to_dict()})
        return X

    def predict(self, X):
        """
        必要函数，预测, 直接定义规则
        """
        y = X.iloc[:, 0] * X.iloc[:, 1]
        return y.map(lambda x: 1 if x > 59 else 0)


def run(X, role_type):
    if role_type == 'guest':
        i_model = CustomModelGuest()
    elif role_type == 'host':
        i_model = CustomModelHost()
    else:
        i_model = CustomModelArbiter()

    X_test = i_model.pre_process(X)
    return i_model, X_test


if __name__ == '__main__':
    # 生成数据
    # X_test = np.random.random((20, 5))
    # df = pd.DataFrame(X_test, columns=['x'+str(i) for i in range(5)])
    # df['id'] = np.arange(5, 25)
    # df.to_csv('test1.csv', index=False)
    host = 1
    guest = 1
    arbitor = 0

    if guest:
        # 1. 读取数据 DataIO
        # X = pd.DataFrame([{"id": "91123456M", "score": 60}, {"id": "91123456279396064N", "score": 50}])
        X = pd.read_csv("custom_guest_dataio.csv")
        X.index = X['id']

        # 2.相交 Intersection
        # index = X['id'].values.tobytes()
        pick = X['id']  # pick = remote_api(index)
        # pick = np.frombuffer(pick, dtype=dtype)

        X = X.loc[pick]

        # 3. 模型测试 Model
        cstm_model, X_test = run(X, 'guest')
        y_pred = pd.DataFrame(index=X_test.index)
        y_pred['y'] = cstm_model.predict(X_test)
        # outputg = y_pred
        outputg = y_pred.to_dict()
        print("guest: ", outputg)

    if host:
        # 1. 读取数据
        X = pd.read_csv('longhua_company_penalty.csv', index_col='id')

        # 2.相交
        # index = X.index
        # pick = remote_api(index)
        print(pick)
        print(X)
        X = X.loc[pick]

        # 3. 模型测试
        cstm_model, X_test = run(X, 'host')
        y_pred = pd.DataFrame(index=X_test.index)
        y_pred['y'] = cstm_model.predict(X_test)
        outputh = y_pred.to_dict()
        print("host: ", outputh)

    if arbitor:
        outputg = pd.DataFrame.from_dict(outputg)
        outputh = pd.DataFrame.from_dict(outputh)
        X = pd.concat([outputh, outputg], axis=1)

        cstm_model, X_test = run(X, 'arbiter')
        y_pred = pd.DataFrame(index=X_test.index)
        y_pred['y'] = cstm_model.predict(X_test)
        print("arbitor: ", y_pred.to_dict())
