import socket
import threading


def scan_ports(ip, start_port, step):
    for port in range(start_port, start_port+step):
        s = socket.socket()
        try:
                s.settimeout(0.5)
                s.connect((ip, port))
                print(f"对应{ip}里面的port是{port}")
        except:
            pass
        finally:
            s.close()

if __name__ == '__main__':
    step = 100
    for port in range(1, 65535, step):
        print(port)
        threading.Thread(target=scan_ports, args=("116.204.122.89", port, step)).start()
