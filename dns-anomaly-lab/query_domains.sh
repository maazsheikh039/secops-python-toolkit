#!/bin/bash
# Simple DNS query logger

DOMAINS=("google.com" "github.com" "stackoverflow.com" "example.com")
LOGFILE="dns_queries.log"

echo "=== DNS Query Log - $(date) ===" >> "$LOGFILE"

for domain in "${DOMAINS[@]}"; do
    echo "Querying: $domain" >> "$LOGFILE"
    dig +short "$domain" >> "$LOGFILE"
    echo "---" >> "$LOGFILE"
done
