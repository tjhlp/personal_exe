#!/usr/bin/env python
# coding: utf-8

# In[35]:


import json
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os
import re

import json


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)


def split1(data, output_splitmap_path):
    total_dic = []
    for column in data.keys():
        try:
            newdf = []
            for i in range(0, len(data)):
                newdf.append(re.split('[《》第款]', data[column][i]))
            newdf1 = pd.DataFrame(newdf)
            data['条例名称'] = newdf1.iloc[:, 1]
            data['条'] = newdf1.iloc[:, 3]
            data['款'] = newdf1.iloc[:, 4]
            data = data
            total_dic.append(['处罚依据:', ['条款名称', '条', '款']])

        except:
            continue

    for column in data.keys():
        if data[column].dtypes == 'int64' or data[column].dtypes == 'float64':
            pass
        elif data[column].dtypes == 'object':
            try:
                data[column] = pd.to_datetime(data[column])
                data['年'] = data[column].dt.year
                data['月'] = data[column].dt.month
                data['日'] = data[column].dt.day
                total_dic.append(['日期:', ['年', '月', '日']])
            except:
                pass

    with open(output_splitmap_path, 'w', encoding='utf-8') as f_out:
        f_out.write(str(total_dic))
    return data, total_dic


def transfer(input_csv_path, output_csv_path, output_mapping_path, output_header_path, output_splitmap_path,
             encoding='utf-8'):
    """
    输入原数据路径：input_csv_path
    输出处理后的数据路径：output_csv_path
    输出处理后的对应关系：output_mapping_path
    """
    data = pd.read_csv(open(input_csv_path, encoding='utf-8'))
    data, total_dic = split1(data, output_splitmap_path)
    encoder = LabelEncoder()

    str2int_mapping = {}
    for col in data.keys():
        if data[col].dtype == object:
            data[col] = data[col].str.strip()
            data[col] = encoder.fit_transform(data[col].astype(str))
            str2int_mapping[col] = list(encoder.classes_)
    data.to_csv(output_csv_path, encoding=encoding, index=False, header=False)
    return total_dic, str2int_mapping, str(list(data.keys()))


if __name__ == "__main__":
    input_csv_path = './个人行政处罚模拟数据.csv'
    output_csv_path = './个人行政处罚模拟数据1.csv'
    output_mapping_path = './mapping.json'
    output_header_path = './header.txt'
    output_splitmap_path = '/splitmap.txt'
    transfer(input_csv_path, output_csv_path, output_mapping_path, output_header_path, output_splitmap_path)
