#!/bin/bash
# Failed Login Analyzer

echo "=== Failed Login Attempts Report ==="
echo "Generated: $(date)"
echo ""

echo "Total Failed Attempts:"
sudo grep "Failed password" /var/log/auth.log | wc -l

echo ""
echo "Top 10 Usernames Targeted:"
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-5)}' | sort | uniq -c | sort -rn | head -10

echo ""
echo "Top 10 Source IPs:"
sudo grep "Failed password" /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head -10
