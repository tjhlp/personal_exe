#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
import time
import matplotlib.pyplot as plt
from collections import Counter


def plot_bar_pic(plot_data, filenames, index=1, count=1, p_type=1):
    """
    将信息可视化
    :param plot_data: 以键值对信息传入
    :param filenames: 保存文件的位置
    :return: None
    """
    # 标注
    label_dict = {
        # '标注': ['职位数量', '语言数量', '职位数量'],
        '标题': ['红球数目分布图', '蓝球数目分布图', '第%s个位置红球的出现次数' % count]
    }
    ball_list = []
    x_core = []
    y_core = []
    for key, value in plot_data.items():
        x_core.append(key)
        ball_list.append(key)
        y_core.append(value)
    plt.rcParams['figure.figsize'] = (20, 8.0)  # 显示大小
    x_core.sort()
    if p_type == 1:
        plt.bar(x_core, y_core, facecolor='orange')
    else:
        plt.plot(x_core, y_core)
    # 添加数字标号
    for score, pos in zip(x_core, y_core):
        plt.text(score, pos, '%d' % pos)
    plt.xticks(x_core)
    plt.legend(loc='best')
    plt.xlabel(label_dict['标题'][index])
    plt.savefig(filenames)
    plt.show()


class TicketPredict(object):
    def __init__(self, url):
        self.url = url
        self.title = ['periods', 'ticket_date', 'red_ball', 'blue_ball']
        self.ticket_info = []
        self.browser = None

    def get_ticket(self):
        self.browser = webdriver.Chrome('./chromedriver')
        self.browser.get(url)
        time.sleep(10)
        # 查看源码
        # html = self.browser.page_source
        # print(html)

        tr_list = self.browser.find_elements_by_xpath('//body/center/center/table/tbody/tr/td/p/table/tbody/tr')
        for tr in tr_list:
            item = {}
            td_list = tr.find_elements_by_xpath('./td')
            item["periods"] = td_list[0].text
            # item["ticket_date"] = td_list[1].text
            item["ticket_red_ball"] = td_list[1].text
            item["ticket_blue_ball"] = td_list[2].text
            self.ticket_info.append(item)
            print(item)
        self.ticket_info.pop(-1)
        print(len(self.ticket_info))
        self.browser.close()

    def write_csv(self):
        # 创建文件写入对象
        f = open('ticket_test.csv', 'w', encoding='utf-8')
        # 通过文件对象创建 csv 写入对象
        csv_writer = csv.writer(f)
        # 把数据写入到 csv 文件中
        # 写入标题
        # csv_writer.writerow(self.title)
        for result in self.ticket_info:
            csv_writer.writerow(result.values())
        f.close()

    def read_csv(self):
        # 创建文件写入对象
        self.ticket_info = []
        with open('ticket_test.csv', 'r', encoding='utf-8') as f:
            # 通过文件对象创建 csv 写入对象
            content = csv.reader(f)
            # 把数据写入到 csv 文件中
            # 写入标题
            for row in content:
                if row:
                    self.ticket_info.append(row)
            # 去除标题
            self.ticket_info.pop(0)

    def save_csv(self):
        self.get_ticket()
        self.write_csv()

    def predict(self, num=100):
        self.read_csv()
        a_dict = {i: 0 for i in range(1, 34)}
        b_dict = {i: 0 for i in range(1, 17)}
        freq = {1: [], 2: [], 3: [], 4: [], 5: [], 0: []}
        self.ticket_info = self.ticket_info[-num:]
        for temp_info in self.ticket_info:
            r_ball_list = temp_info[1].split(' ')

            b_ball = int(temp_info[2][:2]) if len(temp_info[2]) > 2 else int(temp_info[2])
            for t_index, i in enumerate(r_ball_list):
                a_dict[int(i)] += 1
                freq[t_index].append(i)
            b_dict[b_ball] += 1

        # 统计出现频次
        f_index = 1
        for v in range(6):
            z = Counter(freq[v])
            # 求第一个位置出现的最大值
            # max_num = max(dict(z), key=dict(z).get)
            print(dict(z))
            plot_bar_pic(dict(z), 'jpg/freq_red_' + str(f_index) + '.jpg', index=2, p_type=2, count=f_index)
            f_index += 1

        plot_bar_pic(a_dict, 'jpg/red_ball.jpg', index=0)
        plot_bar_pic(b_dict, 'jpg/blue_ball.jpg', index=1)


url = 'https://www.17500.cn/ssq/newinfo9.php'
t = TicketPredict(url)
# t.save_csv()
t.predict(num=1000)
