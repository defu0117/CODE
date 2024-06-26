import requests

headers = {
    "GET": "/vulnerabilities/brute/?username=admin&password=password&Login=Login HTTP/1.1",
    "Host": "10.10.10.9:9000",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "close",
    "Referer": "http://10.10.10.9:9000/vulnerabilities/brute/?username=ad&password=ad&Login=Login",
    "Cookie": "PHPSESSID=gsc6pocfhrbjjl0hi1ug23ofh2; security=low",
    # "Upgrade-Insecure-Requests": 1,
    "Priority": "u=1"
}

url = "http://10.10.10.9:9000/vulnerabilities/brute/?username=ad&password=password&Login=Login#"
response = requests.get(url, headers=headers)
print(response.text)