import socket
import re
import telnetlib

HOST = '192.168.1.69'
PORT = 1337

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero error"


try:
    tn = telnetlib.Telnet(HOST, PORT)
    print("Connected to", HOST, "on port", PORT)
    n = 0
    while True:
        data = tn.read_until(b"\n").decode("utf-8")
        print(f'{data.strip()}:{n}')


        task_match = re.search(r"\((\d+),\s*'([+\-*/])',\s*(\d+)\)", data)
        if task_match:
            num1 = float(task_match.group(1))
            operator = task_match.group(2)
            num2 = float(task_match.group(3))
            result = calculate(num1, operator, num2)
            # print("Result:", result)
            tn.write(str(result).encode() + b"\n")
            n += 1
    tn.close()

except ConnectionRefusedError:
    print("Connection refused. Make sure the host and port are correct.")
except Exception as e:
    print("An error occurred:", e)
