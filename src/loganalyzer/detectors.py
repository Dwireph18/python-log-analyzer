import re
from typing import Dict, List

# Each detector returns a dict with keys: id, severity, description, metadata

def detect_failed_logins_auth(parsed: Dict) -> List[Dict]:
    alerts = []
    msg = parsed.get("message", "")
    if re.search(r"Failed password for", msg, re.IGNORECASE):
        ip_match = re.search(r"from\s+([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", msg)
        alerts.append({
            "id": "AUTH-001",
            "severity": "medium",
            "description": "Failed SSH password attempt",
            "ip": ip_match.group(1) if ip_match else None,
            "raw": msg
        })
    return alerts

def detect_new_user_sysmon(parsed: Dict) -> List[Dict]:
    alerts=[]
    cmd = parsed.get("CommandLine","") or parsed.get("CommandLine", "")
    if re.search(r"(net user|useradd|adduser|dsadd)", cmd, re.IGNORECASE):
        alerts.append({
            "id": "ACC-001",
            "severity": "high",
            "description": "Possible new user created",
            "command": cmd,
            "raw": parsed
        })
    return alerts

def detect_powershell_encoded_sysmon(parsed: Dict) -> List[Dict]:
    alerts=[]
    cmd = parsed.get("CommandLine","") or parsed.get("CommandLine", "")
    if cmd and re.search(r"-EncodedCommand|-e|FromBase64String", cmd, re.IGNORECASE):
        alerts.append({
            "id": "PS-001",
            "severity": "high",
            "description": "Possible encoded PowerShell command (base64)",
            "command": cmd,
            "raw": parsed
        })
    return alerts

# convenience function to run all detectors for a parsed event
def run_detectors(parsed_event: Dict, source_type: str):
    alerts = []
    if source_type == "sysmon":
        alerts += detect_new_user_sysmon(parsed_event)
        alerts += detect_powershell_encoded_sysmon(parsed_event)
    elif source_type == "auth":
        alerts += detect_failed_logins_auth(parsed_event)
    return alerts
