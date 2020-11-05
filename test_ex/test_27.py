#!/usr/bin/env python
# coding: utf-8


import json
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import re
import json


def transfer(data):
    total_dic = {}
    if data.columns[0] != '编号':
        data.insert(0, '编号', data.index.values)
    else:
        pass
    for column in data.keys():
        try:
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
            data = data
            next()
        except:
            pass
    for column in data.keys():
        if data[column].dtypes == 'int64' or data[column].dtypes == 'float64':
            pass
        elif data[column].dtypes == 'object':
            try:
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
                        mydic[str(col[i])] = {}
                        projection_list.append(mydic)
                    mydic1 = {}
                    mydic1[col.name] = projection_list
                    projection_list1.append(mydic1)
                mydic2 = {}
                mydic2[column] = projection_list1
                total_dic.update(mydic2)
            except:
                try:
                    if len(data[column].unique()) / len(data[column]) < 0.1:
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
                    else:
                        pass
                except:
                    pass
    print(total_dic)  ####对应关系
    # print(data)####转换后的数据
    return data


if __name__ == "__main__":
    data1 = pd.read_csv(open('./个人行政处罚模拟数据.csv', encoding='gbk'))
    data2 = pd.read_csv(open('./个人贷款数据.csv', encoding='gbk'))
    transfer(data1)
    transfer(data2)
    data1.to_csv('./个人行政处罚模拟数据.csv', encoding='utf-8')
    data2.to_csv('./个人贷款数据.csv', encoding='utf-8')
