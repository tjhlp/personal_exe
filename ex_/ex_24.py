# -*- coding: utf-8 -*-
# File              : ex_24.py
# Author            : tjh
# Create Date       : 2021/01/06
# Last Modified Date: 2021/01/06
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************


import docx
path = "./政策印刷最终版转Word(1)(1).docx"
file = docx.Document(path)

two_flag = False
f_txt = {}
tmp_text = []
n = 0
p_name = 'test'
for p in file.paragraphs:
    for run in p.runs:
        # 判断字体大小 二号字为228600
        if run.font.size == 228600:
            if tmp_text:
                two_flag = True
                p_name = p.text
                f_txt[p.text] = tmp_text
                tmp_text = []
            break
        else:
            two_flag = False

    if not two_flag:
        if p.text:
            tmp_text.append(p.text)

for k, v in f_txt.items():
    print(v)
print(len(f_txt))
# print(f_txt)








