# Python Log Analyzer

[Python](https://img.shields.io/badge/Python-3.10+-blue)
[Security Project](https://img.shields.io/badge/Focus-Cybersecurity-red)
[MITRE ATT&CK](https://img.shields.io/badge/Framework-MITRE%20ATT%26CK-orange)
[Status](https://img.shields.io/badge/Status-Active-brightgreen)
[License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## About

The **Python Log Analyzer** is a security-focused log analysis tool designed to simulate a Security Operations Center (SOC) workflow.  
It parses authentication logs (Linux/Windows), detects suspicious activity, and generates structured alerts.  

The project demonstrates:
- Threat detection and alerting logic
- MITRE ATT&CK mapping
- SOC-style reporting with CSV/HTML/JSON outputs  

This tool is ideal for showcasing cybersecurity, SOC, and security engineering skills in a portfolio or interview scenario.

---

## 🔥 Features

- Detect failed login bursts (Brute Force / Password Spray)  
- Detect login failures followed by success (Credential Stuffing)  
- Flag unknown usernames (Recon & Enumeration)  
- Parse standard auth logs and Windows Event logs  
- JSON/CSV/HTML detection outputs for SOC pipelines  
- MITRE ATT&CK mapped alerts  

### MITRE Mapping

| Behavior                 | MITRE Technique                    |
|--------------------------|-----------------------------------|
| Failed login bursts      | T1110 – Brute Force               |
| Login after failures     | T1078 – Valid Accounts            |
| Unknown usernames        | TA0001 – Initial Access / Recon   |

---

## Tech Stack

- Python 3.10+
- Regex-based log parsing
- Pandas for data handling
- Jinja2 for HTML reports
- Click for CLI commands
- Custom detection logic (no third-party SIEM required)

---

## Project Structure

```

python-log-analyzer/
│── examples/      # Sample log files
│── src/           # Source code
│── output/        # Detected alerts (CSV/HTML/JSON)
│── README.md
│── requirements.txt

````

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Dwireph18/python-log-analyzer.git
cd python-log-analyzer

# Install required packages
pip install -r requirements.txt

# Install the package in editable mode
pip install -e .
````

---

## 🚀 Usage

Analyze a log file and generate alerts:

```bash
python -m loganalyzer.main analyze examples/auth.log --source auth --out examples/report_auth
```

* `examples/auth.log` → input log file
* `--source auth` → Linux auth log parser (use `--source windows` for Windows logs)
* `--out examples/report_auth` → directory for output reports

Check the output folder:

* `alerts.csv` → tabular alerts
* `alerts.html` → styled HTML report
* `alerts.json` → structured output for SIEM pipelines

---

## 📂 Demo

Example workflow:

1. Use `examples/auth.log` (provided)
2. Run the analyzer command above
3. Open `examples/report_auth/alerts.html` in your browser

You should see detected brute-force attempts, credential stuffing, and unknown username alerts.

---

## ✅ Contribution

Feel free to:

* Add more detection rules
* Support additional log formats (Windows Event, Sysmon)
* Improve JSON/SIEM integration
* Include automated tests using `pytest`

---

## License

MIT License – free for personal and commercial use.

