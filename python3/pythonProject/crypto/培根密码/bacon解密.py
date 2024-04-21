import sys

alphabet = []
first_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"]
second_cipher = ["aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","baabb","babaa","babab","babba","babbb"]

def cut(obj, sec):
    return [obj[i:i+sec] for i in range(0,len(obj),sec)]

def decode(nu,string):
    if nu == str(1):
        cipher = first_cipher
    else:
        cipher = second_cipher
    a = ''
    for n in string:

        for i in cipher:
            if n == i:
                a += ''.join(alphabet[cipher.index(i)])
                break
    print(a)

def encode():
    pass
    str1 = input("请输入要加密的数据：\n")

def exchange(flag):
    match flag:
        case "decode":
            str1 = input("输入你的解密数据：\n").strip().lower()
            str2 = cut(str1, 5)
            nu1 = input("输入你的培根密码表 拓展/基本(1/2)：\n")
            decode(nu1, str2)
        case "encode":
            encode()
        case "exit":
            sys.exit(0)
        case _:
            print("exchange error,please try again")
            exchange(input("选择模式(decode/encode)：\n"))

if __name__ == "__main__":
    alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    mod = input("选择模式(decode/encode)：\n")
    exchange(mod)
    # print(dict(zip(first_cipher, alphabet)))


