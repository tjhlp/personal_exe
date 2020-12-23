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
from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
# 切换User-Agent
options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')

options.set_headless()
browser = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

browser.get('https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/ref=zg_bs_nav_0')
# browser.execute_script("var q=document.documentElement.scrollTop=100000" )

"a-link-normal"
li_list = browser.find_elements_by_xpath('//a[@class="a-link-normal"]')
res = []
for i in li_list:

    goods_url = i.get_attribute('href')
    browser.get(goods_url)
    name = browser.find_element_by_xpath('.//span[@id="productTitle"]').text
    brand = browser.find_element_by_xpath('.//a[@id="bylineInfo"]').text
    score = browser.find_element_by_xpath('.//span[@id="acrPopover"]').get_attribute("title")
    points_element = browser.find_elements_by_xpath('.//div[@id="feature-bullets"]/ul/li')
    point = []
    for point_element in points_element:
        point.append(point_element.find_element_by_xpath('.//span').text)
    goods = {
        "name": name,
        "brand": brand,
        "score": score,
        "point": point
    }
    res.append(goods)
    print(goods)
    break
df = pd.DataFrame(res, columns=['name', 'brand', 'score', 'point'])
df.to_csv('./ymx.csv', encoding='utf-8', index=False)

browser.quit()
