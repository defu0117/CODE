import threading, scapy, time

from scapy.layers.inet import UDP, TCP, IP
from scapy.sendrecv import sr1
from scapy.volatile import RandIP

port_list = tcp_ports = [20, 21, 22, 23, 25, 53, 67, 68, 69, 80, 110, 119, 123, 143, 161, 162, 179, 194, 389, 443, 465, 514, 515, 587, 993, 995, 1080, 1433, 1521, 1723, 2049, 3306, 3389, 5432, 5900, 6379, 8080, 8443, 8888]

step = 20
def SYN_PORTS_SCAN(src_ip,start_port_index:int):
    for port in port_list[start_port_index:start_port_index + step]:
        try:
            msg = IP(dst="192.168.1.36", src=src_ip)/TCP(dport=port, flags="S", seq=123456)
            res = sr1(msg, verbose=False, timeout=1)
            flags = res[TCP].flags # RA 重试端口不存在, SA有正常响应， A 正常
            if flags == "SA":
                print(f"{port}：端口存在")
        except:
            pass

# 随机源地址搞攻击， 扫端口的话包回不来

if __name__ == '__main__':
    for i in range (0, len(port_list), step):
        ip = RandIP()
        threading.Thread(target=SYN_PORTS_SCAN,args=(ip, i)).start()
        time.sleep(0.8)

