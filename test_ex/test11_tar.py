# -*- coding: utf-8 -*-
# File              : test11_tar.py
# Author            : tjh
# Create Date       : 2020/07/21
# Last Modified Date: 2020/07/21
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************
import tarfile


file_path = "./output_log_2.tar.gz"
extract_path ="./"

tar = tarfile.open(file_path, "r:gz")
file_names = tar.getnames()
for file_name in file_names:
    tar.extract(file_name, extract_path)
tar.close()
