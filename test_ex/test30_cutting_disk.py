# -*- coding: utf-8 -*-
# File              : test30_cutting_disk.py
# Author            : tjh
# Create Date       : 2020/11/27
# Last Modified Date: 2020/11/27
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


json_data = ['import numpy as np\n', 'import pandas as pd\n', '\n', '\n', '# from utils import remote_api\n',
        'class MessageBox():\n', '    """\n', '        相关函数，传递信息函数\n', '    """\n', '\n',
        '    def __init__(self, role_type):\n', '        self.role_type = role_type\n',
        '        self.msg = ["msg_box"]\n', '\n', '    def set_msg(self, msg):\n', '        """\n',
        '        相关函数，设置消息\n', '        :param msg: 可以是str,list, dict,dataframe格式需要转化为dict或者list传递\n',
        '        :return:\n', '        """\n', '        self.msg.append(msg)\n', '\n', '    def get_msg(self):\n',
        '        """\n', '        相关函数，获取消息\n', '        :return:\n', '        """\n',
        '        return {self.role_type: self.msg}\n', '\n', '\n', 'class CustomModelGuest():\n',
        '    def __init__(self):\n', '        """\n', '        必要函数，初始化，业务发起方，例如招行节点执行的脚本\n',
        '        该文本是python脚步文件，该脚步文件命名为zeng_defaultPred.py\n', '        下面是上传模型规则：\n', '        a. 模型上传格式：.py\n',
        '        b. 命名规则：上传者+模型名称.py，如zeng_regression.py\n', '        c. 编辑工具：python通用工具，如pycharm，jupyter notebook。\n',
        '        d. 规则：\n', '            上传的py文件里面包括CustomModel类；\n',
        '            model可调用predict预测函数，如model.predict(X_test)。\n', '        e. 模型计算要求：\n', '            时间复杂度要求：线性\n',
        '            空间复杂度要求：线性\n', '        """\n', '        self.msg_box = MessageBox("guest")\n', '\n',
        '    def pre_process(self, X):\n', '        """\n', '        相关函数，数据预处理\n', '        """\n',
        "        self.msg_box.set_msg('数据预处理')\n", '        return X\n', '\n', '    def predict(self, X):\n',
        '        """\n', '        必要函数，预测, 直接定义规则\n', '        """\n', "        y = X['score']\n",
        '        self.msg_box.set_msg(y)\n', '        return y\n', '\n', '\n', 'class CustomModelHost():\n',
        '    def __init__(self):\n', '        """\n', '        必要函数，初始化\n', '\n',
        '        该文本是python脚步文件，该脚步文件命名为zeng_defaultPred.py\n', '        下面是上传模型规则：\n', '        a. 模型上传格式：.py\n',
        '        b. 命名规则：上传者+模型名称.py，如zeng_regression.py\n', '        c. 编辑工具：python通用工具，如pycharm，jupyter notebook。\n',
        '        d. 规则：\n', '            上传的py文件里面包括CustomModel类；\n',
        '            model可调用predict预测函数，如model.predict(X_test)。\n', '        e. 模型计算要求：\n', '            时间复杂度要求：线性\n',
        '            空间复杂度要求：线性\n', '        """\n', '        self.msg_box = MessageBox("host")\n', '\n',
        '    def pre_process(self, X):\n', '        """\n', '        相关函数，数据预处理\n', '        """\n',
        '        X.fillna(0, inplace=True)\n', "        self.msg_box.set_msg({'数据预处理': X.to_dict()})\n",
        '        return X\n', '\n', '    def predict(self, X):\n', '        """\n', '        必要函数，预测, 直接定义规则\n',
        '        """\n', '        return X.sum(axis=1).map(lambda x: 1 if x > 0 else 0)\n', '\n', '\n',
        'class CustomModelArbiter():\n', '    def __init__(self):\n', '        """\n', '        必要函数，初始化\n', '\n',
        '        该文本是python脚步文件，该脚步文件命名为zeng_defaultPred.py\n', '        下面是上传模型规则：\n', '        a. 模型上传格式：.py\n',
        '        b. 命名规则：上传者+模型名称.py，如zeng_regression.py\n', '        c. 编辑工具：python通用工具，如pycharm，jupyter notebook。\n',
        '        d. 规则：\n', '            上传的py文件里面包括CustomModel类；\n',
        '            model可调用predict预测函数，如model.predict(X_test)。\n', '        e. 模型计算要求：\n', '            时间复杂度要求：线性\n',
        '            空间复杂度要求：线性\n', '        """\n', '        self.msg_box = MessageBox("arbiter")\n', '\n',
        '    def pre_process(self, X):\n', '        """\n', '        相关函数，数据预处理\n', '        """\n',
        '        X.fillna(0, inplace=True)\n', "        X.columns = ['host', 'guest']\n",
        "        X['host'] = 1 - X['host']\n", "        self.msg_box.set_msg({'host': X.to_dict()})\n",
        '        return X\n', '\n', '    def predict(self, X):\n', '        """\n', '        必要函数，预测, 直接定义规则\n',
        '        """\n', '        y = X.iloc[:, 0] * X.iloc[:, 1]\n',
        '        return y.map(lambda x: 1 if x > 59 else 0)\n', '\n', '\n', 'def run(X, role_type):\n',
        "    if role_type == 'guest':\n", '        i_model = CustomModelGuest()\n', "    elif role_type == 'host':\n",
        '        i_model = CustomModelHost()\n', '    else:\n', '        i_model = CustomModelArbiter()\n', '\n',
        '    X_test = i_model.pre_process(X)\n', '    return i_model, X_test\n', '\n', '\n',
        "if __name__ == '__main__':\n", '    # 生成数据\n', '    # X_test = np.random.random((20, 5))\n',
        "    # df = pd.DataFrame(X_test, columns=['x'+str(i) for i in range(5)])\n",
        "    # df['id'] = np.arange(5, 25)\n", "    # df.to_csv('test1.csv', index=False)\n", '    host = 1\n',
        '    guest = 1\n', '    arbitor = 0\n', '\n', '    if guest:\n', '        # 1. 读取数据 DataIO\n',
        '        # X = pd.DataFrame([{"id": "91123456M", "score": 60}, {"id": "91123456279396064N", "score": 50}])\n',
        '        X = pd.read_csv("custom_guest_dataio.csv")\n', "        X.index = X['id']\n", '\n',
        '        # 2.相交 Intersection\n', "        # index = X['id'].values.tobytes()\n",
        "        pick = X['id']  # pick = remote_api(index)\n", '        # pick = np.frombuffer(pick, dtype=dtype)\n',
        '\n', '        X = X.loc[pick]\n', '\n', '        # 3. 模型测试 Model\n',
        "        cstm_model, X_test = run(X, 'guest')\n", '        y_pred = pd.DataFrame(index=X_test.index)\n',
        "        y_pred['y'] = cstm_model.predict(X_test)\n", '        # outputg = y_pred\n',
        '        outputg = y_pred.to_dict()\n', '        print("guest: ", outputg)\n', '\n', '    if host:\n',
        '        # 1. 读取数据\n', "        X = pd.read_csv('longhua_company_penalty.csv', index_col='id')\n", '\n',
        '        # 2.相交\n', '        # index = X.index\n', '        # pick = remote_api(index)\n',
        '        print(pick)\n', '        print(X)\n', '        X = X.loc[pick]\n', '\n', '        # 3. 模型测试\n',
        "        cstm_model, X_test = run(X, 'host')\n", '        y_pred = pd.DataFrame(index=X_test.index)\n',
        "        y_pred['y'] = cstm_model.predict(X_test)\n", '        outputh = y_pred.to_dict()\n',
        '        print("host: ", outputh)\n', '\n', '    if arbitor:\n',
        '        outputg = pd.DataFrame.from_dict(outputg)\n', '        outputh = pd.DataFrame.from_dict(outputh)\n',
        '        X = pd.concat([outputh, outputg], axis=1)\n', '\n', "        cstm_model, X_test = run(X, 'arbiter')\n",
        '        y_pred = pd.DataFrame(index=X_test.index)\n', "        y_pred['y'] = cstm_model.predict(X_test)\n",
        '        print("arbitor: ", y_pred.to_dict())\n']


json_path = r'./a/test.py'


model_script = ['import numpy as np\n', 'import pandas as pd\n', '\n', '\n', ]
flag = False

for i in json_data:

    if "class" in i or "if __name__ == '__main__':" in i:
        print(i)
        flag = False

    if "class CustomModelHost():" in i or "MessageBox():" in i or "def run" in i:
        print(i)
        flag = True

    if flag:
        model_script.append(i)

with open(json_path, 'w', encoding='utf-8') as f:
    for i in model_script:
        f.write(i)











