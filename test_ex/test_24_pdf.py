# -*- coding: utf-8 -*-
# File              : test_24_pdf.py
# Author            : tjh
# Create Date       : 2020/10/20
# Last Modified Date: 2020/10/20
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import pdfkit

"C:\Program Files\wkhtmltopdf"
import pdfkit

content = '你好啊,世界~' + '<br>' + 'hello,python~'
html = '<html><head><meta charset="UTF-8"></head>' \
       '<body><div align="center"><p>%s</p></div></body></html>' % content

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
# pdfkit.from_url('http://www.baidu.com', 'url_test.pdf',configuration=config)
pdfkit.from_string(html, 'string_test.pdf', configuration=config)
# pdfkit.from_file('xxx.html','file_test.pdf',configuration=config)
