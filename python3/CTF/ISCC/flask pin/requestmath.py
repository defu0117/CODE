import requests

url_a = "http://101.200.138.180:10006/crawler?answer="
url_q = "http://101.200.138.180:10006/get_expression"

s = requests.Session()
response = s.get(url_q)
math_t = (response.text.split('"'))
math = math_t[3].replace("\\u00d7", '*').replace('\\u00f7', '/')
answer = str(eval(math))
response1 = s.get(url_a+answer)
print(response1.text)