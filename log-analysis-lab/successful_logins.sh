#!/bin/bash
# Successful Login Analyzer

echo "=== Successful Login Report ==="
echo "Generated: $(date)"
echo ""

echo "Total Successful Logins:"
sudo grep "Accepted" /var/log/auth.log | wc -l

echo ""
echo "Users Who Logged In:"
sudo grep "Accepted" /var/log/auth.log | awk '{print $9}' | sort -u

echo ""
echo "Recent 10 Successful Logins:"
sudo grep "Accepted" /var/log/auth.log | tail -10 | awk '{print $1, $2, $3, $9, "from", $11}'
