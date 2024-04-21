import json, re
import string

def findex(string, flag):
    file = open('mosi.txt', 'r')
    json_str = file.read()
    dic = json.loads(json_str)
    lists = string.split(flag)
    print(lists)
    for pa in lists:
        print(dic.get(pa), end="")
    # print(dic)
    file.close()
'''# print(json_str)
dic = json.loads(json_str)
# print(dic)
bina = json_str.translate(str.maketrans({".": "0", "_": "1"}))
# print(bina)

file = open('摩斯密码.txt', 'w')
file.write(bina)
file.close()'''
'''json_str2 = json_str.replace('\'','\"')

# 转换列表 table = ''.maketrans('01', '.-')
dict_json = json.loads(json_str2)
js = json.dumps(dict_json)
file = open('mosi.txt', 'w')
file.write(js)
print(js)'''
# print(dict_json)

if __name__ == '__main__':
    str1 = ".._./._../._/__."
    fl = "/"
    findex(str1, fl)