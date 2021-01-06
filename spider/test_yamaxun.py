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
"https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"
"https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_pg_2?_encoding=UTF8&pg=2"
s_time = return_date('time')


def get_goods_url(browser, url):
    browser.get(url)
    li_list = browser.find_elements_by_xpath('//li[@class="zg-item-immersion"]')
    goods = {}
    for li in li_list:
        rank = li.find_element_by_xpath('.//span[@class="zg-badge-text"]').text
        good_url = li.find_element_by_xpath('.//a[@class="a-link-normal"]').get_attribute("href")
        prices = li.find_elements_by_xpath('.//span[@class="p13n-sc-price"]')
        price_list = []
        for price in prices:
            price_list.append(price.text)
        goods[rank] = {}
        goods[rank]["good_url"] = good_url
        goods[rank]["price"] = price_list
    return goods


def get_goods_detail(browser, goods):
    res = []
    for rank, goods_info in goods.items():
        global num
        global sum_cost_time
        print("排名：{}".format(rank))
        time.sleep(1)
        start_time = return_date('time')
        get_url = goods_info['good_url']
        try:
            browser.get(get_url)
            name = browser.find_element_by_xpath('.//span[@id="productTitle"]').text
            brand = browser.find_element_by_xpath('.//a[@id="bylineInfo"]').text
            score = browser.find_element_by_xpath('.//span[@id="acrPopover"]').get_attribute("title")
            points_element = browser.find_elements_by_xpath('.//div[@id="feature-bullets"]/ul/li')
            img_url = browser.find_element_by_xpath('.//div[@id="imgTagWrapperId"]/img').get_attribute("src")
            reviews = browser.find_element_by_xpath('.//span[@id="acrCustomerReviewText"]').text
        except Exception as e:
            print(goods_info['good_url'])
            print(e)
            good_res = {
                "rank": rank,
                "price": goods_info['price'],
                "good_url": get_url,
                "name": '',
                "brand": '',
                "score": '',
                "point": '',
                "img_url": '',
                "questions": 0,
                "reviews": ''
            }
            res.append(good_res)
            cost_time = calc_time_interval(start_time, return_date('time'))
            sum_cost_time += cost_time
            continue

        try:
            good_detail_list = browser.find_elements_by_xpath(
                './/table[@id="productDetails_detailBullets_sections1"]/tr')
            goods_detail = {}
            for good_detail in good_detail_list:
                detail_name = good_detail.find_element_by_xpath(
                    './/th[@class="a-color-secondary a-size-base prodDetSectionEntry"]').text
                detail_info = good_detail.find_element_by_xpath('.//td[@class="a-size-base"]').text
                goods_detail[detail_name] = detail_info
            print(goods_detail)
            questions = browser.find_element_by_xpath('.//a[@id="askATFLink"]/span').text
        except Exception as e:
            questions = ''
            print(e)

        point = []
        for point_element in points_element:
            point.append(point_element.find_element_by_xpath('.//span').text)
        good_res = {
            "rank": rank,
            "price": goods_info['price'],
            "goods_url": str(get_url),
            "name": name,
            "brand": brand,
            "score": score,
            "point": point,
            "img_url": img_url,
            "questions": questions,
            "reviews": reviews,
        }
        res.append(good_res)
        cost_time = calc_time_interval(start_time, return_date('time'))
        sum_cost_time += cost_time
        avg_time = sum_cost_time / num
        print('The %s good calc:%ss ' % (num, cost_time))
        print('sum_time:%ss, avg_time calc:%ss ' % (sum_cost_time, avg_time))
        num += 1
        print(good_res)
        break
    return res


total_res = []
for top_url in top_urls:
    goods = get_goods_url(browser, top_url)
    total_res.extend(get_goods_detail(browser, goods))
    break

print('goods calc:%ss ' % (calc_time_interval(s_time, return_date('time'))))
df = pd.DataFrame(total_res,
                  columns=["rank", "price", 'goods_url', 'name', 'brand', 'score', 'point', 'img_url', 'questions'])
df.to_csv('./ymx.csv', encoding='utf-8', index=False)

# browser.quit()
