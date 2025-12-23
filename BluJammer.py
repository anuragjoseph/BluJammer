import os
import threading
import time
import subprocess
import random

# -------------------------------
# SAFE SIMULATION FUNCTION
# -------------------------------
def simulate_test(target_addr, packet_size, thread_id):
    for i in range(5):
        print(f"[Thread-{thread_id}] Testing {target_addr} | packet={packet_size} | cycle={i+1}")
        time.sleep(random.uniform(0.4, 0.9))
    print(f"[Thread-{thread_id}] Completed")

# -------------------------------
# LOGO
# -------------------------------
def printLogo():
    print("\033[1;36m")
    print("╔══════════════════════════════════════════════════════╗")
    print("║                                                      ║")
    print("║        ██████╗ ██╗     ██╗   ██╗                     ║")
    print("║        ██╔══██╗██║     ██║   ██║                     ║")
    print("║        ██████╔╝██║     ██║   ██║                     ║")
    print("║        ██╔══██╗██║     ██║   ██║                     ║")
    print("║        ██████╔╝███████╗╚██████╔╝                     ║")
    print("║        ╚═════╝ ╚══════╝ ╚═════╝                      ║")
    print("║                                                      ║")
    print("║     Bluetooth Diagnostic Utility                     ║")
    print("║     Author : Benzy                                    ║")
    print("║                                                      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print("\033[0m")

# -------------------------------
# MAIN
# -------------------------------
def main():
    os.system("clear")
    printLogo()

    print("\033[1;31m")
    print("⚠ WARNING ⚠")
    print("This tool is for EDUCATIONAL & AUTHORIZED testing only.")
    print("No packets are sent. No attack is performed.")
    print("\033[0m")

    if input("Do you agree? (y/n) > ").lower() != "y":
        print("Exit.")
        return

    os.system("clear")
    printLogo()
    print("[*] Scanning Bluetooth devices...\n")

    try:
        output = subprocess.check_output(
            ["hcitool", "scan"],
            stderr=subprocess.STDOUT,
            text=True
        )
    except Exception as e:
        print("[!] Bluetooth scan failed:", e)
        return

    lines = output.splitlines()[1:]
    devices = []

    print("| ID | MAC ADDRESS        | DEVICE NAME |")
    print("|----|--------------------|-------------|")

    for idx, line in enumerate(lines):
        parts = line.split()
        mac = parts[0]
        name = " ".join(parts[1:]) if len(parts) > 1 else "Unknown"
        devices.append(mac)
        print(f"| {idx:<2} | {mac:<18} | {name} |")

    target = input("\nTarget ID or MAC > ")
    try:
        target_addr = devices[int(target)]
    except:
        target_addr = target.strip()

    try:
        packet_size = int(input("Packet size (simulation) > "))
        thread_count = int(input("Thread count > "))
    except:
        print("[!] Invalid input")
        return

    os.system("clear")
    printLogo()

    print("\033[1;33m[*] Starting simulated diagnostic in 3 seconds...\033[0m")
    for i in range(3, 0, -1):
        print(f"[*] {i}")
        time.sleep(1)

    print("\n[*] Launching threads...\n")

    threads = []
    for i in range(thread_count):
        t = threading.Thread(
            target=simulate_test,
            args=(target_addr, packet_size, i + 1)
        )
        threads.append(t)
        t.start()
        print(f"[*] Thread {i+1} started")

    for t in threads:
        t.join()

    print("\n\033[1;32m[✓] Simulation completed successfully\033[0m")

# -------------------------------
# ENTRY
# -------------------------------
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Interrupted by user")
