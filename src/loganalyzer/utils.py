from datetime import datetime
import re

def parse_timestamp(timestamp_str):
    # try some common timestamp formats
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%b %d %H:%M:%S"):
        try:
            return datetime.strptime(timestamp_str, fmt)
        except Exception:
            continue
    return None

def is_base64_powershell(cmdline: str) -> bool:
    # detect powershell -EncodedCommand / base64 string
    return bool(re.search(r"(EncodedCommand|-e|FromBase64String)", cmdline, re.IGNORECASE))
