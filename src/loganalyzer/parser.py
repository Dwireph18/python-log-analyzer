import re
from typing import Dict, Generator, Any

def parse_sysmon_line(line: str) -> Dict[str, Any]:
    """
    Simple Sysmon-like key=value parser for demonstration.
    Example line:
    "Time=2024-11-01 12:00:00 EventID=1 Image=C:\Windows\System32\cmd.exe CommandLine=whoami"
    """
    d = {}
    # split by spaces but treat key=value pairs
    pairs = re.findall(r"(\w+)=([^\n]+?)(?=\s\w+=|$)", line)
    for k, v in pairs:
        d[k] = v.strip()
    return d

def parse_auth_line(line: str) -> Dict[str, Any]:
    """
    Very small parser for linux auth log lines:
    'Nov  1 12:00:00 host sshd[1234]: Failed password for invalid user root from 1.2.3.4 port 5555 ssh2'
    """
    m = re.match(r"^(\w+\s+\d+\s+\d+:\d+:\d+)\s+(\S+)\s+(\S+):\s+(.*)$", line)
    if not m:
        return {}
    ts, host, program, msg = m.groups()
    return {"timestamp": ts, "host": host, "program": program, "message": msg}
