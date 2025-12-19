import re
import json
from collections import defaultdict

LOG_FILE = "auth.log"
FAILED_LOGIN_PATTERN = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
BRUTE_FORCE_THRESHOLD = 5
REPORT_FILE = "failed_login_report.json"

failed_attempts = defaultdict(int)

with open(LOG_FILE, "r") as f:
    for line in f:
        match = re.search(FAILED_LOGIN_PATTERN, line)
        if match:
            ip = match.group(1)
            failed_attempts[ip] += 1

print("\n🔍 Failed Login Attempts Summary:\n")
report_data = []

for ip, count in failed_attempts.items():
    is_suspicious = count > BRUTE_FORCE_THRESHOLD
    print(f"IP: {ip} | Failed Attempts: {count} | Suspicious: {is_suspicious}")
    report_data.append({
        "ip": ip,
        "failed_attempts": count,
        "suspicious": is_suspicious
    })

print("\n🚨 Alerts:\n")
any_alert = False
for ip, count in failed_attempts.items():
    if count > BRUTE_FORCE_THRESHOLD:
        any_alert = True
        print(f"[ALERT] Possible brute-force attack from {ip} with {count} failed attempts")

if not any_alert:
    print("No suspicious IPs based on current threshold.")

with open(REPORT_FILE, "w") as f:
    json.dump(report_data, f, indent=2)

print(f"\n📁 JSON report saved to: {REPORT_FILE}")
print("\n✔ Analysis complete.")
