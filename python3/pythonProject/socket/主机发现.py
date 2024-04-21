import socket
from concurrent.futures import ThreadPoolExecutor
import threading

# 创建一个锁对象
lock = threading.Lock()

def ip_find(ip_base, ip_last):
    ip = f"{ip_base}{ip_last}"
    sk = socket.socket()
    try:
        sk.settimeout(1)
        sk.connect((ip, 6379))
        print(f"Redis server found at {ip} on port 6379")
        # 在这里处理文件写入
        with lock:  # 使用锁来确保线程安全的文件操作
            with open("successful_ips_02.txt", "a") as file:
                file.write(f"{ip}\n")
    except Exception as e:
        print(f"Failed to connect to {ip} on port 6379: {e}")
    finally:
        sk.close()

if __name__ == '__main__':
    ip_base = "124.234."
    with ThreadPoolExecutor(max_workers=50) as executor:
        for ip2 in range(1, 255):
            ip_prefix = f"{ip_base}{ip2}."
            for ip_last in range(1, 255):
                executor.submit(ip_find, ip_prefix, ip_last)
