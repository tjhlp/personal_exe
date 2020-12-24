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
"https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"
"https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_2?_encoding=UTF8&pg=2"
s_time = return_date('time')


def get_goods_url(browser, url):
    browser.get(url)
    li_list = browser.find_elements_by_xpath('//a[@class="a-link-normal"]')
    goods_url = [i.get_attribute('href') for i in li_list]
    return goods_url


def get_goods_detail(browser, goods_url):
    res = []
    num = 1
    for good_url in goods_url:
        time.sleep(1000)
        print(good_url)
        start_time = return_date('time')
        try:
            browser.get(good_url)
            name = browser.find_element_by_xpath('.//span[@id="productTitle"]').text
            brand = browser.find_element_by_xpath('.//a[@id="bylineInfo"]').text
            score = browser.find_element_by_xpath('.//span[@id="acrPopover"]').get_attribute("title")
            points_element = browser.find_elements_by_xpath('.//div[@id="feature-bullets"]/ul/li')
            img_url = browser.find_element_by_xpath('.//div[@id="imgTagWrapperId"]/img').get_attribute("src")
            questions = browser.find_element_by_xpath('.//a[@id="askATFLink"]/span').text
            price = browser.find_element_by_xpath('.//span[@id="priceblock_dealprice"]').text
        except Exception as e:
            print(e)
            continue

        point = []
        for point_element in points_element:
            point.append(point_element.find_element_by_xpath('.//span').text)
        goods = {
            "goods": good_url,
            "name": name,
            "brand": brand,
            "score": score,
            "point": point,
            "img_url": img_url,
            "questions": questions,
            "price": price,
        }
        res.append(goods)
        end_time = return_date('time')
        print('The %s good calc:%ss ' % (num, calc_time_interval(start_time, end_time)))
        num += 1
        print(goods)
        break
    return res

total_res = []
for top_url in top_urls:
    goods_url = get_goods_url(browser, top_url)
    total_res.extend(get_goods_detail(browser, goods_url))
    break

print('goods calc:%ss ' % (calc_time_interval(s_time, return_date('time'))))
df = pd.DataFrame(total_res, columns=['goods_url', 'name', 'brand', 'score', 'point', 'img_url', 'questions', 'price'])
df.to_csv('./ymx.csv', encoding='gbk', index=False)

# browser.quit()
