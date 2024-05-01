import base64

def decodeString(encoded_str):
    # ROT13解密
    decoded_rot13 = encoded_str.translate(str.maketrans("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"))

    # 字符串反转
    reversed_str = decoded_rot13[::-1]

    # 补全填充字符
    while len(reversed_str) % 4 != 0:
        reversed_str += '='

    # Base64解码
    try:
        decoded_base64 = base64.urlsafe_b64decode(reversed_str)
    except base64.binascii.Error as e:
        print("Base64 decoding error:", e)
        return None

    return decoded_base64

# 测试字符串
encoded_string = "mVGZ3O3omkJLmy2pcuTq"
decoded_result = decodeString(encoded_string)

if decoded_result:
    print(decoded_result.decode('utf-8'))
