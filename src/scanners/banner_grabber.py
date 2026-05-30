import socket

COMMON_SERVICES = {
    21: "FTP",    22: "SSH",     23: "Telnet",
    25: "SMTP",   53: "DNS",     80: "HTTP",
    110: "POP3",  143: "IMAP",   443: "HTTPS",
    445: "SMB",   3306: "MySQL", 3389: "RDP",
    8080: "HTTP_Alt",  8443: "HTTPS_Alt",
}

def grab_banner(host: str, port: int, timeout: float = 2.0) -> dict:
    """try to get the banner of a service on a port"""
    result = {
        "port":    port,
        "service": COMMON_SERVICES.get(port, "Unknown"),
        "banner": None,
    }
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        
         # send a HTTP request for web ports
        if port in (80, 8080, 8000):
            sock.send(b"GET / HTTP/1.0\r\n\r\n")
            
        banner = sock.recv(1024).decode(errors="ignore").strip()
        result["banner"] = banner[:200] #limit the size
        sock.close()
    except Exception:
        pass
    return result
        
        
        