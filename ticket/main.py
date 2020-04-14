#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import csv
import time
import matplotlib.pyplot as plt


def plot_data(plot_data, filenames):
    """
    将信息可视化
    :param plot_data: 以键值对信息传入
    :param filenames: 保存文件的位置
    :return: None
    """
    ball_list = []
    x_core = []
    y_core = []
    for key, value in plot_data.items():
        x_core.append(key)
        ball_list.append(key)
        y_core.append(value)
    # plt.rcParams['figure.figsize'] = (20, 8.0)  # 显示大小
    plt.bar(x_core, y_core, facecolor='orange')
    # 添加数字标号
    for score, pos in zip(x_core, y_core):
        plt.text(score, pos, '%d' % pos)
    plt.xticks(x_core)
    plt.yticks(y_core)
    plt.legend(loc='best')
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
        # time.sleep(10)
        # html = self.browser.page_source

        tr_list = self.browser.find_elements_by_xpath('//div[@class="bgzt"]//tbody/tr')
        for tr in tr_list:
            item = {}
            td_list = tr.find_elements_by_xpath('./td')
            item["periods"] = td_list[0].text
            item["ticket_date"] = td_list[1].text
            item["ticket_red_ball"] = td_list[2].text
            item["ticket_blue_ball"] = td_list[3].text
            self.ticket_info.append(item)
        print(len(self.ticket_info))
        self.browser.close()

    def write_csv(self):
        # 创建文件写入对象
        f = open('ticket_test.csv', 'w', encoding='utf-8')
        # 通过文件对象创建 csv 写入对象
        csv_writer = csv.writer(f)
        # 把数据写入到 csv 文件中
        # 写入标题
        csv_writer.writerow(self.title)
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
            self.ticket_info.pop(0)

    def save_csv(self):
        self.get_ticket()
        self.write_csv()
        self.ticket_info.pop(0)

    def predict(self):

        a_dict = {i: 0 for i in range(1, 34)}
        b_dict = {i: 0 for i in range(1, 17)}

        for temp_info in self.ticket_info:
            r_ball_list = temp_info[2]
            b_ball = int(temp_info[3])
            # ball_list = [r_ball_list[i - 2:i] for i in range(2, len(red_ball) + 2, 2)]
            # ball_list.append(blue_ball)
            for i in range(2, len(r_ball_list) + 2, 2):
                r_ball = int(r_ball_list[i - 2:i])
                a_dict[r_ball] += 1
            b_dict[b_ball] += 1
        print(a_dict)
        print(b_dict)
        plot_data(a_dict, 'jpg/red_ball.jpg')
        plot_data(b_dict, 'jpg/blue_ball.jpg')



# url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?name=ssq&issueCount=30'
url = 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/'
t = TicketPredict(url)
# t.save_csv()
t.read_csv()
t.predict()
