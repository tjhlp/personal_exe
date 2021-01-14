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
    # browser.get(url)
    time.sleep(1)
    div_list = browser.find_elements_by_xpath('.//div[@class="gl-i-wrap"]')
    url_list = []
    for div in div_list:
        s = div.find_element_by_xpath('.//div[@class="jPic"]/a').get_attribute("href")
        url_list.append(s)
    print(url_list)
    return url_list


url = 'https://mall.jd.com/view_search-1461791-13517749-99-1-20-1.html'
#

browser.get(url)
page_num = browser.find_element_by_xpath('.//div[@id="J_GoodsList"]/div/a[4]').text
print(page_num)
rsp = []
for i in range(page_num):
    url_list = get_goods_url(browser, url)

    print("第%s页 %s 条记录" % (i, len(url_list)))
    for good_url in url_list:
        time.sleep(0.5)
        print("%s" % good_url)
        browser.get(good_url)
        sku_name = browser.find_element_by_xpath('.//div[@class="sku-name"]').text
        sku_price = browser.find_element_by_xpath('.//span[@class="p-price"]/span[2]').text
        sku_brand = browser.find_element_by_xpath('.//ul[@id="parameter-brand"]/li').get_attribute("title")
        try:
            sku_type = browser.find_element_by_xpath('.//div[@class="Ptable-item"]/dl/dl[1]/dd').text
        except Exception as e:
            print(e)
            sku_type = ''
        try:
            sku_model = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[8]').get_attribute("title")
        except Exception as e:
            print(e)
            sku_model = ''
        try:
            sku_ex = browser.find_element_by_xpath('.//div[@class="p-parameter"]/ul[2]/li[9]').get_attribute("title")
        except Exception as e:
            print(e)
            sku_ex = ''
        res = {
            "sku_url": good_url,
            "sku_name": sku_name,
            "sku_price": sku_price,
            "sku_brand": sku_brand,
            "sku_model": sku_model,
            "sku_ex": sku_ex,
        }
        rsp.append(res)
        print(res)

    # 点击下一页
    try:
        browser.execute_script("var q=document.documentElement.scrollTop=100000")
        next_page = browser.find_element_by_xpath('.//div[@id="J_GoodsList"]/div/a[5]')
        browser.execute_script("arguments[0].click();", next_page)
    except:
        break
print(page_num)

print(rsp)
df = pd.DataFrame(rsp,
                  columns=["sku_url", "sku_name", 'sku_price', 'sku_brand', 'sku_model', 'sku_ex'])
df.to_csv('./donghua_jd.csv', encoding='gbk', index=False)

print('goods calc:%ss ' % (calc_time_interval(s_time, return_date('time'))))

# browser.quit()
