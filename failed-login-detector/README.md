# Failed Login Detector

A simple security automation script that analyzes log files for repeated failed login attempts (e.g., SSH brute-force attacks).

## Features

- Parses system/auth logs for failed login attempts.
- Extracts IP addresses from common failure patterns.
- Shows top offending IPs.
- Flags IPs with failed attempts above a threshold.

## Usage

```bash
python3 failed_login_detector.py /path/to/logfile.log
	
