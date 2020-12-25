# -*- coding: utf-8 -*-
# File              : test_medicine_spider.py
# Author            : tjh
# Create Date       : 2020/12/25
# Last Modified Date: 2020/12/25
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

import requests
from lxml import etree
import pandas as pd

"http://shop.ewlian.com/home?countFlag=1&typeid=101&pageIndex=2"
"http://shop.ewlian.com/home?countFlag=1&typeid=101&pageIndex=3"
url = "http://shop.ewlian.com/home?countFlag=1&typeid=101&pageIndex=3"
REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "Upgrade-Insecure-Requests": "1",
    "Cookie": "ASP.NET_SessionId=rc5uqpbavrepu2e0rtn2frvq; LoginYxyfCookies=LoginYxyfCookiesUserID=2142700&LoginYxyfCookiesUserPwd=FB9043A137E46800D199DC14C6EA6D8B; .ASPXAUTH=F3D7825C434C20CF4BFCAECE4DC2797381E603A8496F93285CD5B840A99A345C4E0EF7E9DE6BF3F58A9A3DB5B79EA0EF96997F075A58257C55A11BFF370B4AEA45F1FC33257AF7BD0EB0D8D9824A4C2F70FEAB048DCE3AF1A4B3F3BCDC49967192F394C67E2CF156799BA644C07F30FC7C66EE1F7F82E8D6710D2AE3F61A4D01A01122A5286373429ACE54A8B646E1CD1A2BB86F8651911606E94E26FF2BFFE64A10E09ED5DE2F53CA7B2CE9E38682CEE477BFF8217224650BD72828B3D1FE19A68CCA68A3D68F2B4DC6BCA07959249A392E5C8B7E8148EE70236025B4E42C27634CA4565D66CD3115276343E7E3B9D399112E8EE312EE2CA7A8935FAB84EE9ED0C4E2643F18E888EB9D163DE10B0D616A438EB927ADFDEFCEDEFFBE63EFBAE180DA5ECDF0DA6F049D49356D15BD6BB5F81571E90EA559742C82ED11455A29359FD8E6E7E01AB65614BB8E8DAD29841820CCC2A3824BC9EF19A6A71CDE33B8F96611D43101D771F4CD1E8140EE6FA13302776CD29897A868A87DB7605EF73E1B8E7A5145E08EFB7A6677ED416E7A6FE9D96FC0310FE82856B29747BE35034144"
}
total_res = []
for i in range(1, 135):
    url = "http://shop.ewlian.com/home?countFlag=1&typeid=101&pageIndex={}".format(i)

    response = requests.get(url, headers=REQUEST_HEADERS)

    html = etree.HTML(response.text)
    goods_code = html.xpath('//ul[@class="base1"]/li[1]/span/text()')
    goods_name = html.xpath('//ul[@class="base1"]/li[2]/span/text()')
    goods_style = html.xpath('//ul[@class="base1"]/li[3]/span/text()')
    manufacturer = html.xpath('//ul[@class="base2"]/li[2]/span/text()')
    unit = html.xpath('//ul[@class="price1 spanpriceul"]/li[1]/span/text()')
    price = html.xpath('//ul[@class="price1 spanpriceul"]/li[2]/span/@title')
    up_price = html.xpath('//div[@id="ratef"]/span[2]/text()')
    goods_info = {}
    num = 0
    res = []
    print(i)
    for tmp in range(0, len(goods_code)):
        goods_info = {
            "goods_code": goods_code[tmp],
            "goods_name": goods_name[tmp],
            "goods_style": goods_style[tmp],
            "manufacturer": manufacturer[tmp],
            "unit": unit[tmp],
            "price": price[tmp],
            "up_price": up_price[tmp],
        }
        res.append(goods_info)
    total_res.extend(res)

df = pd.DataFrame(total_res,
                  columns=["goods_code", "goods_name", 'goods_style', 'manufacturer', 'unit', 'price', 'up_price'])
df.to_csv('./medicine.csv', encoding='utf-8', index=False)
