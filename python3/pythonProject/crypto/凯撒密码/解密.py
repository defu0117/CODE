def password(st):
    for n in range(1,26):
        st2 = ""
        for i in st:
            if 97 <= ord(i) <= 122:   # i.islower   i.isupper
                mod = 97 # 大写
                st2 += chr((ord(i)-mod+n)%26+mod)
            elif 65 <= ord(i) <= 90:
                mod = 65 # 小写
                st2 += chr((ord(i) - mod + n) % 26 + mod)
            else:
                st2 += i
        # print(str(n)+':'+st2)
        find(st2)

def find(flag):
    if default.lower() == 'y':
        lists = ["flag","key"]
    else:
        lists = [su]
    for i in lists:
        if i in flag:
            print("***********************")
            print("this："+flag)
            print("***********************")
            break
        else:
            print("error："+flag)
            break

if __name__ == '__main__':
    str1 = "pvKQ{123}"
    str2 = input("输入你的凯撒密码：\n")
    default = input("是否使用推荐(Y/N)：\n")
    if default.lower() == 'n':
        su = input("请输入你的关键字：\n")
    password(str2)