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
import os
# tar_name = 'output_data.tar.gz'
# tar = tarfile.open(tar_name, mode='w:gz')
# output_tmp_dir = r'D:\personal\exercise\personal_exe\test_ex'
# output_data_file_path = r'D:\personal\exercise\personal_exe\test_ex\output_data.csv'
# tar.add(output_data_file_path, os.path.relpath(output_data_file_path, output_tmp_dir))
# tar.close()

t = tarfile.open(r'/\33_output_data.tar.gz')
t.extractall('./')

