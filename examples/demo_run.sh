#!/usr/bin/env bash
python -m src.loganalyzer.main analyze tests/sample_logs/sample_sysmon.log --source sysmon --out examples/report_sysmon
python -m src.loganalyzer.main analyze tests/sample_logs/sample_auth.log --source auth --out examples/report_auth
