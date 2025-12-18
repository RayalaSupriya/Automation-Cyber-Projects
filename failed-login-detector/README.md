🔐 Failed Login Detector (Version 1)
📌 Overview

This script analyzes Linux authentication logs (auth.log) to detect failed SSH login attempts and identify potential brute-force attacks.
It is the first project in my Security Automation Engineer & SOC Analyst learning roadmap.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🚀 Features

Parses Linux SSH authentication logs

Extracts attacker IP addresses using regex

Counts failed login attempts per IP

Displays all failed attempts clearly

Helps identify suspicious or brute-force activity
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🧠 How It Works

Reads the log file line by line

Uses a regex pattern to detect Failed password events

Extracts the IP address from each failed login

Tracks the number of failed attempts per IP

Prints a summary of all detected IPs
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📁 File Structure
failed-login-detector/
│── auth.log
│── failed_login_detector_v1.py
│── README.md
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
▶️ Run the Script

Make sure you are inside the project folder, then run:

python3 failed_login_detector_v1.py
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📌 Sample Output
🔍 Suspicious Failed Login Attempts Detected:

IP: 185.199.110.153 | Failed Attempts: 6
IP: 203.0.113.55    | Failed Attempts: 1

✔ Analysis complete.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🛠 Next Version (Coming Soon)

The next iteration of this project will include:

🔔 Alerting for brute-force thresholds

📄 JSON reporting

📧 Email or Slack notifications

⚙️ Configurable log paths & thresholds

🧪 Unit tests
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🌟 Why This Project Matters

This is a real SOC analysis task that automation engineers handle daily.
Understanding log parsing and detection logic is the foundation of:

SOC investigations

Threat detection engineering

Security automation & SOAR

AI-driven security analytics

This project sets the base for more advanced automation.
