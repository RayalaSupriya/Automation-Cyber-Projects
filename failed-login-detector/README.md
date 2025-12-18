🔐 Failed Login Detector (Version 1)
📌 Overview

This script analyzes authentication logs (auth.log) to detect failed login attempts and highlight potential brute-force attacks.
It is the first project in my Security Automation Engineer & SOC Analyst learning roadmap.

🚀 Features

Parses Linux SSH authentication logs

Extracts IP addresses using regex

Counts failed login attempts per IP

Highlights suspicious IPs

Provides clean summary output

🧠 How It Works

Reads each line from auth.log

Uses regex to identify failed login events

Extracts the attacker’s IP address

Keeps count using Python defaultdict

Prints all IPs and their failed attempts

📁 File Structure
failed-login-detector/
│── auth.log
│── failed_login_detector_v1.py
│── README.md

▶️ Run the Script
python3 failed_login_detector_v1.py

📌 Sample Output
🔍 Suspicious Failed Login Attempts Detected:

IP: 185.199.110.153 | Failed Attempts: 6
IP: 203.0.113.55    | Failed Attempts: 1

✔ Analysis complete.

🛠 Next Version (coming soon)

Alerts for brute-force

JSON report export

Email / Slack notifications

Configurable thresholds
