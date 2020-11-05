# -*- coding: utf-8 -*-
# File              : test_27.py
# Author            : tjh
# Create Date       : 2020/11/05
# Last Modified Date: 2020/11/05
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


# !/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import os
import re
import json


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)


class transfer():
    def __init__(self):
        """
        数据转换函数主要实现以下功能：
        1.将日期拆分
        2.将文字分类变量转换为数字型分类变量
        3.将文字切分并转换

        输出：
        输出转换对应字典：json文件
        输出转换所得数据：csv文件
        """
        pass

    def to_datetime(self, data, column):
        data[column] = pd.to_datetime(data[column])
        data['年'] = data[column].dt.year
        data['月'] = data[column].dt.month
        data['日'] = data[column].dt.day
        year = data['年']
        month = data['月']
        day = data['日']
        projection_list1 = []
        for col in [year, month, day]:
            projection_list = []
            for i in range(0, len(col.unique())):
                mydic = {}
                mydic[str(col[i])] = col[i]
                projection_list.append(mydic)
            mydic1 = {}
            mydic1[col.name] = projection_list
            projection_list1.append(mydic1)
        mydic2 = {}
        mydic2[column] = projection_list1
        total_dic.update(mydic2)
        return data

    def factorize(self, data, column):
        factors = pd.factorize(data[column])
        data[column] = factors[0]
        projection_list = []
        for i in range(0, len(factors[1])):
            mydic = {}
            mydic[factors[1][i]] = i

            projection_list.append(mydic)
        mydic2 = {}
        mydic2[column] = projection_list
        total_dic.update(mydic2)
        return data

    def split_n_transfer(self, data, column):
        newdf = []
        for i in range(0, len(data)):
            newdf.append(re.split('[《》第款]', data[column][i]))
        newdf1 = pd.DataFrame(newdf)
        data['条例名称'] = newdf1.iloc[:, 1]
        data['条'] = newdf1.iloc[:, 3]
        data['款'] = newdf1.iloc[:, 4]
        col1 = data['条例名称']
        col2 = data['条']
        col3 = data['款']
        projection_list1 = []
        for col in [col1, col2, col3]:
            projection_list = []
            for i in range(0, len(col.unique())):
                mydic = {}
                mydic[str(col[i])] = col[i]
                projection_list.append(mydic)
            mydic1 = {}
            mydic1[col.name] = projection_list
            projection_list1.append(mydic1)
        mydic2 = {}
        mydic2[column] = projection_list1
        total_dic.update(mydic2)
        return data

    def add_id(self, data):
        if data.columns[0] != '编号':
            data.insert(0, '编号', data.index.values)
        else:
            pass


if __name__ == "__main__":
    data1 = pd.read_csv('D:/cloud_ai/ELF平台/数据转换/个人行政处罚模拟数据.csv', encoding='gbk')
    data2 = pd.read_csv('D:/cloud_ai/ELF平台/数据转换/个人贷款数据.csv', encoding='gbk')
    total_dic = {}
    data_transfer = transfer()
    data_transfer.to_datetime(data1, '日期')
    data_transfer.split_n_transfer(data1, '处罚依据')
    data_transfer.add_id(data1)
    data1.to_csv('D:/cloud_ai/ELF平台/数据转换/个人行政处罚模拟数据1.csv', encoding='gbk')
    # data_transfer.factorize(data2,'性别')
    # data_transfer.add_id(data2)
    # data1.to_csv('D:/cloud_ai/ELF平台/数据转换/个人贷款数据1.csv',encoding='gbk')
    with open("D:/cloud_ai/ELF平台/数据转换/对应关系.json", "w+", encoding='gbk') as jsonFile:
        jsonFile.write(json.dumps(total_dic, indent=4, cls=NpEncoder, ensure_ascii=False))

