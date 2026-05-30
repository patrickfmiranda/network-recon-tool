#!/usr/bin/env python3 

"""
Network Recon Tool - Portfolio project
Author: Patrick Miranda
Github: github.com/patrickfmiranda/networkrecon-tool
"""
import argparse
import json
from datetime import datetime
from colorama import Fore, Style, init
from src.scanners.port_scanner import PortScanner
from src.scanners.banner_grabber import grab_banner
from src.reporters.html_reporter import generate_html_report

init(autoreset=True)

BANNER = f"""
{Fore.RED}
  ███╗   ██╗██████╗ ████████╗
  ████╗  ██║██╔══██╗╚══██╔══╝
  ██╔██╗ ██║██████╔╝   ██║   
  ██║╚██╗██║██╔══██╗   ██║   
  ██║ ╚████║██║  ██║   ██║   
  ╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝ 
  Network Recon Tool v1.1
  github.com/patrickfmiranda/networkrecon-tool
{Style.RESET_ALL}"""

def parse_args():
    parser = argparse.ArgumentParser(description="Network Recon Tool")
    parser.add_argument("target",          help="IP or target hostname")
    parser.add_argument("-p", "--ports",   default="1-1024", help="Range of ports (ex: 1-1024 or 22,80,443)")
    parser.add_argument("-t", "--threads", default=100, type=int, help="Number of threads (default: 100)")  # ← BUG 1 CORRIGIDO: faltava = antes das aspas no help=
    parser.add_argument("-o", "--output",  help="Output JSON file")  # ← BUG 2 CORRIGIDO: argumento -o inexistente mas usado no main()
    parser.add_argument("--timeout",       default=1.0, type=float, help="Timeout per port (default: 1.0s)")
    return parser.parse_args()  # ← BUG 3 CORRIGIDO: parser.parser_args() → parser.parse_args()

def parse_ports(port_arg: str) -> list:
    if "-" in port_arg:
        start, end = port_arg.split("-")
        return list(range(int(start), int(end) + 1))
    return [int(p) for p in port_arg.split(",")]

def main():
    print(BANNER)
    args = parse_args()
    ports = parse_ports(args.ports)
    start_time = datetime.now()

    # scanner for ports
    scanner = PortScanner(args.target, ports, args.threads, args.timeout)
    open_ports = scanner.run()

    # banner grabbing in open ports
    print(f"\n{Fore.CYAN}[*] Grabbing banners...{Style.RESET_ALL}")
    services = [grab_banner(args.target, port) for port in open_ports]

    # show results
    duration = (datetime.now() - start_time).seconds
    print(f"\n{Fore.YELLOW}{'─'*50}")
    print(f"  RESULTADO — {args.target}")
    print(f"{'─'*50}{Style.RESET_ALL}")
    for svc in services:
        banner_info = f"  → {svc['banner'][:60]}" if svc['banner'] else ""
        print(f"  {svc['port']:>5}/tcp  {svc['service']:<12}{banner_info}")

    print(f"\n{Fore.GREEN}[+] {len(open_ports)} open ports | Time: {duration}s{Style.RESET_ALL}")

    if args.output:
        report = {
            "target": args.target,
            "scan_time": start_time.isoformat(),
            "duration_s": duration,
            "open_ports": open_ports,
            "services": services,
        }

        # JSON
        if args.output.endswith(".json"):
            with open(args.output, "w") as f:
                json.dump(report, f, indent=2)
            print(f"{Fore.CYAN}[*] JSON report saved: {args.output}{Style.RESET_ALL}")

        # HTML
        elif args.output.endswith(".html"):
            generate_html_report(report, args.output)
            print(f"{Fore.CYAN}[*] HTML report saved: {args.output}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()