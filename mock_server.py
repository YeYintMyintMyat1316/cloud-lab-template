import time, signal, sys

def graceful_shutdown(signum, frame):
    print(f"\n[+] Received SIGTERM ({signum}). Flushing I/O buffers and tearing down DB connections...", flush=True)
    time.sleep(2)
    print("[+] System offline.", flush=True)
    sys.exit(0)

signal.signal(signal.SIGTERM, graceful_shutdown)

print("[+] Mock Server initialized on Port 8080.", flush=True)
while True:
    print("[*] Processing task queue...", flush=True)
    time.sleep(3)
