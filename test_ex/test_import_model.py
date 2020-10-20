# -*- coding: utf-8 -*-
# File              : test_import_model.py
# Author            : tjh
# Create Date       : 2020/08/03
# Last Modified Date: 2020/08/03
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
# -*- coding: utf-8 -*-
# File              : import_model.py
# Author            : tjh
# Create Date       : 2020/06/28
# Last Modified Date: 2020/06/28
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import importlib
import importlib.util
import logging


class ImportModel(object):
    def __init__(self, module_name, module_path, params=None):
        self.module_name = module_name
        self.func_name = None
        self.module_path = module_path
        self.params = params
        self.func = None

    def check_model(self):
        model_spec = importlib.util.find_spec(self.module_name)
        if model_spec is None:
            logging.info(' %s model:missing' % self.module_name)
            return False
        return True

    def import_model(self, fuc_name):
        try:

            module_spec = importlib.util.spec_from_file_location(self.module_name, self.module_path)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            # 加载模块对应的函数
            func_self = getattr(module, fuc_name)
            self.func_name = fuc_name

        except Exception as e:
            logging.error(' %s model loading %s got exception :%s' % (self.module_name, fuc_name, e))
            return None
        return func_self

    def run_model(self):
        if self.func_name is None:
            logging.info('model must use import_model at first')
            return None

        self.func = self.import_model(self.func_name)
        if self.func is None:
            return None
        try:
            if self.params:
                res = self.func(**self.params)
            else:
                res = self.func()
        except Exception as e:
            logging.error('run %s model got exception :%s' % (self.func, e))
            return None
        return res


if __name__ == '__main__':
    m_name = 'demo'
    func_name = 'demo_12'
    m_file_path = r'D:\personal\exercise\personal_exe\test_ex\demo.py'
    param = {'x': 1, 'y': 2}
    m_model = ImportModel(m_name, m_file_path, param)
    m_model.import_model(func_name)
    res = m_model.run_model()
    # print(res.sum())




