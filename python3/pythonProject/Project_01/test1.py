import binascii, urllib
from urllib import parse
"""
# 字符串转16进制
a = "falg"
bytes_data = a.encode('utf-8')

hex_data = binascii.hexlify(bytes_data)
print(bytes_data.hex())

c = "c"
d = ord(c)
jie = hex_data.decode('utf-8')
print(jie)
"""

"""
# url编码
print (urllib.parse.quote("flag{url_encode_1234_!@#$}"))
d={'name':'bibi@flappypig.club','flag':'flag{url_encode_1234_!@#$}'}
url_en = urllib.parse.urlencode(d)
url_en2 = urllib.parse.quote(url_en)
print(url_en)
print(urllib.parse.unquote(url_en))
"""
# base64 : a-z,A-Z,0-9 base32 A-Z,2-7 base16 0-9,A-F
# 将字符转为二进制,1个字符是1byte=8bit 将6bit转为数字替换为字符就是base64的要点

# 古典密码 移位(就是位置的替换) 云影密码(01248,0是分隔,其余数字加和转明文)

