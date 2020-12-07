from gmssl .sm4 import CryptSM4 ,SM4_ENCRYPT ,SM4_DECRYPT #line:22
import json #line:23
import base64 #line:24
key =b"3l5butlj26hvv313"#line:26
def set_crypt_str (OO000O0000OOO0O00 ):#line:29
    OO000O0000OOO0O00 =str .encode (OO000O0000OOO0O00 )#line:31
    OOO0OO00OO0OOO0OO =CryptSM4 ()#line:32
    OOO0OO00OO0OOO0OO .set_key (key ,SM4_ENCRYPT )#line:33
    OO0000OO0O00O00O0 =OOO0OO00OO0OOO0OO .crypt_ecb (OO000O0000OOO0O00 )#line:34
    OOOO00OOO00000O0O =base64 .b64encode (OO0000OO0O00O00O0 ).decode ('utf8')#line:36
    return OOOO00OOO00000O0O #line:37
def get_decrypt_str (OOO0000O0O00O0OOO ):#line:40
    O0000OO0OO0O0000O =CryptSM4 ()#line:42
    OOOO0O0O0O00O0OO0 =base64 .b64decode (OOO0000O0O00O0OOO .encode ("utf8"))#line:43
    O0000OO0OO0O0000O .set_key (key ,SM4_DECRYPT )#line:44
    O00O00OO0O0O00OO0 =O0000OO0OO0O0000O .crypt_ecb (OOOO0O0O0O00O0OO0 )#line:45
    return O00O00OO0O0O00OO0 .decode ()#line:46
if __name__ =='__main__':#line:48
    s =["key",{"result":"11111"}]#line:49
    z =json .dumps (s )#line:50
    c1 =set_crypt_str (z )#line:52
    z1 =get_decrypt_str (c1 )#line:53
    print (z1 )#line:54
    z1 =json .loads (z1 )#line:55
    print (type (z1 ))#line:56