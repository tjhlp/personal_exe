# -*- coding: utf-8 -*-
# File              : test31_rsa.py
# Author            : tjh
# Create Date       : 2020/11/27
# Last Modified Date: 2020/11/27
# Last Modified By  : tjh
# Reference         :
# Description       :
# ******************************************************

from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

import base64

key = b"3l5butlj26hvv313"


def set_crypt_str(input_str):
    # 加密
    input_str = str.encode(input_str)
    crypt_sm4 = CryptSM4()
    crypt_sm4.set_key(key, SM4_ENCRYPT)
    encrypt_value = crypt_sm4.crypt_ecb(input_str)  # bytes类型

    crypt_str = base64.b64encode(encrypt_value).decode('utf8')
    return crypt_str


def get_decrypt_str(x):
    # 解码
    crypt_sm4 = CryptSM4()
    y = base64.b64decode(x.encode("utf8"))
    crypt_sm4.set_key(key, SM4_DECRYPT)
    decrypt_value = crypt_sm4.crypt_ecb(y)  # bytes类型
    return decrypt_value.decode()


# value = b"111" #  bytes类型
s = ["key", {"result": "11111"}]  # bytes类型

c1 = set_crypt_str(str(s))
print(c1)
z1 = get_decrypt_str(c1)
print(z1)


# from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT
#
# import base64
#
# key = b"3l5butlj26hvv313"
#
# # value = b"111" #  bytes类型
# s = ["key",{"result":"11111"} ]#  bytes类型
# value=str.encode(str(s))
#
#
# #加密
# crypt_sm4 = CryptSM4()
# crypt_sm4.set_key(key, SM4_ENCRYPT)
# encrypt_value = crypt_sm4.crypt_ecb(value) #  bytes类型
#
# x = base64.b64encode(encrypt_value).decode('utf8')
# print(x)
#
# #解码
# y = base64.b64decode(x.encode("utf8"))
# crypt_sm4.set_key(key, SM4_DECRYPT)
# decrypt_value = crypt_sm4.crypt_ecb(y) #  bytes类型
# # assert value == decrypt_value
# print(decrypt_value)
# print(bytes.decode(decrypt_value))
