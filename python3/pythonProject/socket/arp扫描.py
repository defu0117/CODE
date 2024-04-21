import threading, scapy
import time, logging

from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import sr1, sendp
from scapy.volatile import RandMAC, RandIP

logging.getLogger('scapy.runtime').setLevel(logging.ERROR)  # 取出系统报错
def arp_scan(ip):
    # msg = ARP().show()
    # print (msg)
    try:
        res = sr1(ARP(pdst="192.168.1."+str(ip)), timeout=1, verbose=False)
        print (f"IP:{res[ARP].psrc}  MAC:{res[ARP].hwsrc}")
    except:
        pass


def arp_floor():
    while True:
        arp_ip = RandIP()
        arp_mac = RandMAC()
        arp_mac1 = RandMAC()
        msg = Ether(dst=arp_mac, src=arp_mac)

        #sendp 支持二层数据包直接发送
        sendp(msg, iface="VMware Virtual Ethernet Adapter for VMnet8", loop=0)

if __name__ == '__main__':

     for i in range(1, 255):
        threading.Thread(target=arp_scan, args=(i,)).start()
    # arp_floor()
