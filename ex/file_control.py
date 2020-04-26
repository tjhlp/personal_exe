import csv


def write_csv(file_name, data_info, title):
    """
    保存csv文件
    :param file_name:
    :param data_info: 二维数组列表
    :param title: 题目头部
    :return:
    """

    # 创建文件写入对象
    f = open(file_name, 'w', encoding='utf-8')
    # 通过文件对象创建 csv 写入对象
    csv_writer = csv.writer(f)
    # 把数据写入到 csv 文件中
    # 写入标题
    csv_writer.writerow(title)
    for result in data_info:
        csv_writer.writerow(result.values())
    f.close()


def read_csv(file_name):
    # 创建文件写入对象
    ticket_info = []
    with open(file_name, 'r', encoding='utf-8') as f:
        # 通过文件对象创建 csv 写入对象
        content = csv.reader(f)
        # 把数据写入到 csv 文件中
        # 写入标题
        for row in content:
            # 去除无效数据
            if row:
                ticket_info.append(row)
        # 去除标题
        ticket_info.pop(0)
    return ticket_info