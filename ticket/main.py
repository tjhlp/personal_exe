#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import time

browser = webdriver.Chrome('./chromedriver')

browser.get("http://www.cwl.gov.cn/kjxx/ssq/kjgg/")

time.sleep(1)
tr_list = browser.find_elements_by_xpath('//div[@class="bgzt"]//tbody/tr')
for ticket_list in tr_list:
    item = {}
    td_list = browser.find_elements_by_xpath('//td/text()')

    item["title"] = td_list[0]
#     item["author"] = li.find_element_by_css_selector('.dy-name.ellipsis.fl').text
#     item["room_img_url"] = li.find_element_by_class_name("JS_listthumb").get_attribute("data-original")
    print(item)
#
# next_element = browser.find_element_by_link_text("下一页")

browser.quit()
