# -*- coding: utf-8 -*-
# File              : test_yamaxun.py
# Author            : tjh
# Create Date       : 2020/12/23
# Last Modified Date: 2020/12/23
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import time
import re
import datetime
from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

# options.add_argument('--headless')
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

num = 1
sum_cost_time = 0


# browser.execute_script("var q=document.documentElement.scrollTop=100000" )

def calc_time_interval(start, end):
    """
    计算时间间隔
    :param start:
    :param end:
    :return: 秒数
    """

    start = time.mktime(time.strptime(start, "%Y-%m-%d %H:%M:%S"))
    end = time.mktime(time.strptime(end, "%Y-%m-%d %H:%M:%S"))
    calc_time = int(end - start)

    return calc_time


def return_date(time_conf):
    if time_conf == 'day':
        return datetime.datetime.now().strftime('%Y-%m-%d')
    if time_conf == 'time':
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


top_urls = [
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=1",
    "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_2?_encoding=UTF8&pg=2"]

s_time = return_date('time')


def get_goods_url(browser, url):
    browser.get(url)
    time.sleep(1)
    div_list = browser.find_elements_by_xpath('.//div[@class="gl-i-wrap"]')
    rsp = []
    url_list = []
    for div in div_list:
        s = div.find_element_by_xpath('.//div[@class="jPic"]/a').get_attribute("href")
        url_list.append(s)
        # browser.get(s)
        # sku_name = browser.find_element_by_xpath('.//div[@class="sku-name"]').text
        # sku_price = browser.find_element_by_xpath('.//span[@class="p-price"]/span[2]').text
        # sku_brand = browser.find_element_by_xpath('.//ul[@id="parameter-brand"]/li').get_attribute("title")
        # sku_type = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[7]').get_attribute("title")
        # sku_model = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[8]').get_attribute("title")
        # sku_ex = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[9]').get_attribute("title")
        # res = {
        #     "sku_name": sku_name,
        #     "sku_price": sku_price,
        #     "sku_brand": sku_brand,
        #     "sku_type": sku_type,
        #     "sku_model": sku_model,
        #     "sku_ex": sku_ex,
        # }
        # rsp.append(res)
        # print(res)

    return url_list

def get_goods_detail(browser, goods):
    res = []
    for rank, goods_info in goods.items():
        pass


url = 'https://mall.jd.com/view_search-1461791-13517749-99-1-20-1.html'
url_list = get_goods_url(browser, url)
rsp = []
for good_url in url_list:
    browser.get(good_url)
    sku_name = browser.find_element_by_xpath('.//div[@class="sku-name"]').text
    sku_price = browser.find_element_by_xpath('.//span[@class="p-price"]/span[2]').text
    sku_brand = browser.find_element_by_xpath('.//ul[@id="parameter-brand"]/li').get_attribute("title")
    sku_type = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[7]').get_attribute("title")
    sku_model = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[8]').get_attribute("title")
    sku_ex = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[9]').get_attribute("title")
    res = {
        "sku_name": sku_name,
        "sku_price": sku_price,
        "sku_brand": sku_brand,
        "sku_type": sku_type,
        "sku_model": sku_model,
        "sku_ex": sku_ex,
    }
    rsp.append(res)

print(rsp)


print('goods calc:%ss ' % (calc_time_interval(s_time, return_date('time'))))

# browser.quit()
