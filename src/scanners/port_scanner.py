import socket
import threading
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

class PortScanner:
    def __init__(self, target: str, ports: list = None, threads: int = 100, timeout: float = 1.0):
        self.target     = target
        self.ports      = ports or list(range(1, 1025))
        self.threads    = threads
        self.timeout    = timeout
        self.open_ports = []
        self._lock      = threading.Lock()

    def _resolve_target(self) -> str:
        try:
            return socket.gethostbyname(self.target)
        except socket.gaierror:
            print(f"{Fore.RED}[!] NOT POSSIBLE TO RESOLVE: {self.target}{Style.RESET_ALL}")
            return None

    def _scan_port(self, port: int):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)   
            result = sock.connect_ex((self.target, port))
            if result == 0:
                with self._lock:
                    self.open_ports.append(port)
                print(f"  {Fore.GREEN}[+] Port {port}/tcp OPEN{Style.RESET_ALL}")
            sock.close()
        except Exception:
            pass

    def run(self) -> list:
        ip = self._resolve_target()
        if not ip:
            return []

        print(f"\n{Fore.CYAN}[*] Scanning {self.target} ({ip})")
        print(f"[*] Ports: {self.ports[0]}-{self.ports[-1]} | Threads: {self.threads}{Style.RESET_ALL}\n")

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self._scan_port, self.ports)

        self.open_ports.sort()
        return self.open_ports