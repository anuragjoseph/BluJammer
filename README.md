# Bluetooth Diagnostic & Stress Simulation Tool

A Python-based Bluetooth utility designed for **educational and research purposes**.  
This project demonstrates how Bluetooth devices are discovered and how multi-threaded
workloads can be simulated against a selected target **without sending harmful traffic**.

> ⚠️ This project does **NOT** perform real jamming or denial-of-service attacks.

---

## ✨ Features

- Bluetooth device discovery using Linux BlueZ tools
- Clean and interactive CLI interface
- Multi-threading demonstration
- Safe stress/load **simulation**
- Designed for cybersecurity labs & learning environments
- Modern Linux compatible (BlueZ stack)

---

## 🧠 Purpose

This project was created to help students and researchers understand:

- Bluetooth architecture (HCI, device discovery)
- Interaction with system Bluetooth tools via Python
- Threading and concurrency concepts
- Ethical considerations in security research

It is intended **only for devices you own or have permission to test**.

---

## 🛠 Requirements

- Linux OS
- Python 3.x
- Bluetooth adapter
- BlueZ stack installed
- Root privileges (required for Bluetooth access)

Install BlueZ:

```bash
sudo apt install bluez

## ▶️ Usage:

'''bash
sudo python3 main.py


The program will:

Display nearby Bluetooth devices

Allow target selection

Run a simulated diagnostic workload

Demonstrate threading behavior safely

## ⚠️ Legal & Ethical Notice

This project is provided for educational purposes only.

No real packets are flooded

No jamming is performed

No denial-of-service attacks occur

Using similar techniques for unauthorized attacks is illegal and unethical.
The author takes no responsibility for misuse of modified versions.

## 👤 Author

Benzy
Cybersecurity & Systems Enthusiast
