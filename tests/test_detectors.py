from loganalyzer.detectors import detect_failed_logins_auth, detect_powershell_encoded_sysmon, detect_new_user_sysmon
from loganalyzer import parser

def test_auth_failed():
    line = "Nov  1 10:00:00 host sshd[1234]: Failed password for invalid user root from 1.2.3.4 port 5555 ssh2"
    parsed = parser.parse_auth_line(line)
    alerts = detect_failed_logins_auth(parsed)
    assert len(alerts) == 1
    assert alerts[0]["ip"] == "1.2.3.4"

def test_powershell_encoded():
    line = "Time=2025-11-01 10:00:00 EventID=1 Image=C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe CommandLine=powershell -EncodedCommand aGVsbG8="
    parsed = parser.parse_sysmon_line(line)
    alerts = detect_powershell_encoded_sysmon(parsed)
    assert len(alerts) == 1

def test_new_user():
    line = "Time=2025-11-01 10:01:00 EventID=1 Image=C:\\Windows\\System32\\net.exe CommandLine=net user testuser Password123 /add"
    parsed = parser.parse_sysmon_line(line)
    alerts = detect_new_user_sysmon(parsed)
    assert len(alerts) == 1
