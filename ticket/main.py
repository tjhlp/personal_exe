#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import csv


def write_csv(results):
    # 创建文件写入对象
    f = open('ticket_test.csv', 'w', encoding='utf-8')
    # 通过文件对象创建 csv 写入对象
    csv_writer = csv.writer(f)
    # 把数据写入到 csv 文件中
    # 写入标题
    csv_writer.writerow(results[0])
    results.pop(0)
    for result in results:
        csv_writer.writerow(result.values())
    f.close()


browser = webdriver.Chrome('./chromedriver')

browser.get("http://www.cwl.gov.cn/kjxx/ssq/kjgg/")

time.sleep(1)
tr_list = browser.find_elements_by_xpath('//div[@class="bgzt"]//tbody/tr')
title = ['periods', 'ticket_date', 'red_ball', 'blue_ball']
results = []
results.append(title)
for tr in tr_list:
    item = {}
    td_list = tr.find_elements_by_xpath('./td')
    item["periods"] = td_list[0].text
    item["ticket_date"] = td_list[1].text
    item["ticket_red_ball"] = td_list[2].text
    item["ticket_blue_ball"] = td_list[3].text
    results.append(item)
#     print(item)
#
print(results)
# next_element = browser.find_element_by_link_text("下一页")
write_csv(results)
browser.quit()
