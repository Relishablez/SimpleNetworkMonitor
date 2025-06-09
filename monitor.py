import subprocess
from datetime import datetime

def ping_host(host):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', host],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

def log_status(host, status, logfile="log.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(logfile, "a") as logfile:
        logfile.write(f"[{timestamp}] {host} is {'UP' if status else 'DOWN'}\n")

def main():
    try:
        with open("ip_list.txt", "r") as file:
            hosts = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("ip_list.txt not found.")
        return

    for host in hosts:
        status = ping_host(host)
        log_status(host, status)
        print(f"{host} is {'UP' if status else 'DOWN'}")

if __name__ == "__main__":
    main()
