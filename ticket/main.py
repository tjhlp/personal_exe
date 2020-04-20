#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import Counter
import requests
from lxml import etree

from ticket.file_control import write_csv, read_csv
from ticket.plot_pic import plot_bar_pic


class TicketPredict(object):
    def __init__(self):
        self.title = ['periods', 'ticket_date', 'red_ball', 'blue_ball']
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
        }
        self.url = 'https://www.17500.cn/ssq/newinfo9.php'

    def get_ticket(self):
        params = {
            'q1': '2003001',
            'q2': '2020026',
            'action': 'submitted',
            'submit': '(unable to decode value)'
        }
        response = requests.post(self.url, data=params, headers=self.headers)
        return response.content

    def parse_html(self, html):
        tr_eroot = etree.HTML(html)
        tr_list = tr_eroot.xpath('//table/tbody/tr')
        ticket_info = []
        for tr in tr_list:
            item = {}
            td_list = tr.xpath('./td')
            if td_list[0].text is None:
                continue
            item["periods"] = td_list[0].text
            item["ticket_red_ball"] = td_list[1].text
            item["ticket_blue_ball"] = td_list[2].text
            ticket_info.append(item)
        return ticket_info

    def predict(self, ticket_info, num=100):
        a_dict = {i: 0 for i in range(1, 34)}
        b_dict = {i: 0 for i in range(1, 17)}
        freq = {1: [], 2: [], 3: [], 4: [], 5: [], 0: []}
        ticket_info = ticket_info[-num:]
        for temp_info in ticket_info:
            r_ball_list = temp_info['ticket_red_ball'].split(' ')

            b_ball = int(temp_info['ticket_blue_ball'][:2]) if len(temp_info['ticket_blue_ball']) > 2 else int(temp_info['ticket_blue_ball'])
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
            plot_bar_pic(dict(z), 'jpg/freq_red_' + str(f_index) + '.jpg', index=2, p_type=2, count=f_index)
            f_index += 1

        plot_bar_pic(a_dict, 'jpg/red_ball.jpg', index=0)
        plot_bar_pic(b_dict, 'jpg/blue_ball.jpg', index=1)

    def run(self):
        # 数据获取
        ticket_data = self.get_ticket()
        # 解析数据
        process_data = self.parse_html(ticket_data)

        # process_data = read_csv('ticket_test.csv')

        # 预测数据
        self.predict(process_data)

        # 保存数据
        write_csv(r"C:\Users\TJH\Desktop\data+processing\Ticket_Test.csv", process_data, self.title)


if __name__ == '__main__':
    t = TicketPredict()
    t.run()
