import re
import argparse
from collections import Counter
from pathlib import Path

FAILED_PATTERNS = [
    r"Failed password for .* from (?P<ip>\d+\.\d+\.\d+\.\d+)",   # typical sshd log
    r"Invalid user .* from (?P<ip>\d+\.\d+\.\d+\.\d+)",          # invalid user attempts
    r"authentication failure.*rhost=(?P<ip>\d+\.\d+\.\d+\.\d+)", # pam messages
]

def parse_args():
    parser = argparse.ArgumentParser(
        description="Analyze log file for repeated failed login attempts."
    )
    parser.add_argument(
        "logfile",
        help="Path to the log file (e.g., /var/log/auth.log)"
    )
    parser.add_argument(
        "-t", "--threshold",
        type=int,
        default=5,
        help="Number of failed attempts to flag an IP as suspicious (default: 5)",
    )
    parser.add_argument(
        "-n", "--top",
        type=int,
        default=10,
        help="Show top N offending IPs (default: 10)",
    )
    return parser.parse_args()

def build_failed_regex():
    return [re.compile(p) for p in FAILED_PATTERNS]

def extract_failed_ips(log_path: Path):
    regexes = build_failed_regex()
    counts = Counter()

    with log_path.open("r", errors="ignore") as f:
        for line in f:
            for rgx in regexes:
                m = rgx.search(line)
                if m:
                    ip = m.group("ip")
                    counts[ip] += 1
                    break  # avoid double-counting if multiple patterns match
    return counts

def main():
    args = parse_args()
    log_path = Path(args.logfile)

    if not log_path.exists():
        print(f"[!] Log file not found: {log_path}")
        return

    print(f"[+] Analyzing log file: {log_path}")
    counts = extract_failed_ips(log_path)

    if not counts:
        print("[+] No failed login attempts detected with current patterns.")
        return

    print("\n=== Top Offending IPs ===")
    for ip, c in counts.most_common(args.top):
        print(f"{ip:15}  {c} failed attempts")

    print("\n=== Suspicious IPs (>= threshold) ===")
    suspicious = [ (ip, c) for ip, c in counts.items() if c >= args.threshold ]

    if not suspicious:
        print(f"No IPs crossed the threshold of {args.threshold} failed attempts.")
    else:
        for ip, c in sorted(suspicious, key=lambda x: -x[1]):
            print(f"[!] {ip}  ->  {c} failed attempts")

if __name__ == "__main__":
    main()

