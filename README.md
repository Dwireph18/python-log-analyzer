# Python Log Analyzer

A compact, extensible log analyzer for basic blue-team detection: parses Sysmon-like and Linux auth logs, runs lightweight detectors, and generates CSV/HTML reports.

**Tech:** Python, Click, Jinja2, Pandas (optional)

## Features
- Parse simple Sysmon-style logs and Linux auth logs
- Detects:
  - Encoded PowerShell commands (base64)
  - New user creation commands (`net user`, `useradd`)
  - Failed SSH login attempts
- Generates CSV and HTML reports
- Unit tests included

## Quickstart

```bash
git clone <your-repo-url>
cd python-log-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# run against sample sysmon
python -m src.loganalyzer.main analyze tests/sample_logs/sample_sysmon.log --source sysmon --out examples/report_sysmon

# run against sample auth
python -m src.loganalyzer.main analyze tests/sample_logs/sample_auth.log --source auth --out examples/report_auth
```

## How it works
- `parser.py` extracts structured fields from each log line.
- `detectors.py` contains small detection functions (each returns alert dicts).
- `reporter.py` writes alerts to CSV and HTML.

## Extending
- Add new detectors to `detectors.py`; map them to MITRE ATT&CK in README.
- Replace parser with real Sysmon XML/EVTX parsing for production.

## MITRE mapping (examples)
- `PS-001` — T1059.001 (PowerShell)
- `ACC-001` — T1078 (Valid Accounts)
- `AUTH-001` — T1110 (Brute Force)

## Contributing
PRs welcome. Add tests for new detectors in `tests/`.

## License
[MIT](LICENSE)
