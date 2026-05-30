# 🔍 Network Recon Tool
> Custom Python-based network reconnaissance tool for port scanning, 
> service detection and banner grabbing — built as a portfolio project.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Level](https://img.shields.io/badge/level-beginner-green)
![Platform](https://img.shields.io/badge/platform-Linux-lightgrey?logo=linux)

---

## 📋 About

This tool was built from scratch to demonstrate core networking and 
Python skills without relying entirely on existing tools like Nmap.  
It performs TCP port scanning with multithreading, service detection 
via banner grabbing, and exports results to JSON.

**Tested against:** Metasploitable 2 in an isolated VirtualBox lab.

---

## ✨ Features

- ⚡ Multithreaded TCP port scanner (ThreadPoolExecutor)
- 🏷️ Service detection via banner grabbing
- 🗺️ Common services mapping (SSH, HTTP, SMB, MySQL...)
- 💾 JSON export with full scan metadata
- 🎨 Colored terminal output (colorama)

---

## 📁 Project Structure
network-recon-tool/
```
├── main.py                     # CLI entry point
├── requirements.txt
├── src/
│   ├── scanners/
│   │   ├── port_scanner.py     # Multithreaded TCP scanner
│   │   └── banner_grabber.py   # Banner + service detection
│   ├── reporters/
│   │   └── json_reporter.py    # JSON output
│   └── utils/
│       └── helpers.py
└── tests/
└── test_scanner.py
```
---

## 🚀 Installation

```bash
git clone https://github.com/patrickfmiranda/networkrecon-tool.git
cd networkrecon-tool
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔧 Usage

```bash
# Basic scan
python3 main.py 10.10.10.10

# Custom port range
python3 main.py 10.10.10.10 -p 1-65535 -t 200

# Specific ports with JSON output
python3 main.py 10.10.10.10 -p 22,80,443,445,3306 -o results.json

# Options
  target          Target IP or hostname
  -p, --ports     Port range (default: 1-1024)
  -t, --threads   Number of threads (default: 100)
  --timeout       Timeout per port in seconds (default: 1.0)
  -o, --output    Save results to JSON file
```

---

## 📊 Sample Output

[] Scanning 10.10.10.10 (10.10.10.10)
[] Ports: 1-1024 | Threads: 100
[+] Port 21/tcp  OPEN
[+] Port 22/tcp  OPEN
[+] Port 80/tcp  OPEN
[+] Port 445/tcp OPEN
[+] 4 open ports | Time: 3s

---

## 🧪 Lab Environment

All tests were performed in an **isolated VirtualBox lab** on ParrotOS:

| Machine | Role | IP |
|---|---|---|
| ParrotOS Security | Attacker | 10.10.10.1 |
| Metasploitable 2 | Target | 10.10.10.10 |

Network: NAT internal — no internet access from target VMs.

---

## 🗺️ Roadmap

- [x] Multithreaded TCP port scanner
- [x] Banner grabbing & service detection
- [x] JSON export
- [ ] HTML report with Jinja2
- [ ] UDP scan support
- [ ] OS fingerprinting via TTL
- [ ] Shodan API integration
- [ ] CVE lookup per service version

---

## ⚖️ Disclaimer

This tool was developed for **educational purposes only**.  
All tests were performed on systems owned by the author  
in a controlled, isolated lab environment.  
Never use this tool against systems without explicit permission.

---

## 👤 Author

**Patrick Miranda**  
[GitHub](https://github.com/patrickfmiranda) • 
[LinkedIn](https://linkedin.com/in/patrickfmiranda) •
[TryHackMe](https://tryhackme.com/p/patrickfmiranda)