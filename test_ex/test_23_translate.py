# -*- coding: utf-8 -*-
# File              : test_23_translate.py
# Author            : tjh
# Create Date       : 2020/10/09
# Last Modified Date: 2020/10/09
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


def is_chinese(string):
    """
    检查整个字符串是否包含中文
    :param string: 需要检查的字符串
    :return: bool
    """
    for ch in string:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True

    return False


test_str = "111"
res = is_chinese(test_str)
print(res)
"""

params: { 'ownNodeID': (1, < class 'str' >)

, 'csvName': (1, < class 'str' >), 'csvFiledName': (1, < class 'list' >), 'csvData': (1,
                                                                                      < class 'list' >), 'fate_table_name': (
1, < class 'str' >), 'fate_namespace': (1, < class 'str' >), 'industry': (0, < class 'str' >), 'label': (0,
                                                                                                         < class 'str' >)}, js: {
    'ownNodeID': 'A1', 'csvName': 'test.csv', 'csvFiledName': ['test.csv'],
    'csvData': [['id', 'road', 'number_of_road', 'speed', 'time'],
                ['1', '太子路', '2', '75', '2020-08-03 15:11:03.000000']], 'fate_table_name': '', 'fate_namespace': '',
    'industry': '', 'label': '', 'systemID': 'DS', 'version': '1.0.0'}
"""

import re

#   匹配特殊字符
symbol = re.compile(r'【】')

# inputStr = "hello 123 world 456"
# replacedStr = re.sub("\d+", "222", inputStr)
# print(replacedStr)

symbol_list = ["(【.*】.*)",]
str_list1 = ['深市质宝市海罚字[2018]0001498号', '深市质华市监罚字【2018】00734号', '深市质宝食罚字〔2018〕桥73号']
for str_test in str_list1:
    # print(str_test[:str_test.rfind("[")] + "***")

    replacedStr = re.sub(str_test[10:], "***", str_test)
    # replacedStr = re.sub("(【.*】.*)", "***", str_test[:10])
    # replacedStr = re.sub("(〔.*〕.*)", "***", replacedStr)
    # replacedStr = re.sub("(\[.*\].*)", "***", replacedStr)
    print(replacedStr)


