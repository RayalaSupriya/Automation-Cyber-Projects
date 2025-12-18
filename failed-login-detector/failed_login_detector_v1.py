import re
from collections import defaultdict

# Path to the log file
log_file = "auth.log"

# Dictionary to store failed attempts per IP
failed_attempts = defaultdict(int)

# Regex pattern to capture IP address from failed login lines
pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

with open(log_file, "r") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

print("\n🔍 Suspicious Failed Login Attempts Detected:\n")
for ip, count in failed_attempts.items():
    print(f"IP: {ip} | Failed Attempts: {count}")

print("\n✔ Analysis complete.")
