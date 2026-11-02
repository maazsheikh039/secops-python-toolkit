#!/bin/bash

# Automated Evidence Collection Script
# Purpose: Collect system information, logs, and timestamps for forensic analysis

set -euo pipefail

EVIDENCE_DIR="$HOME/evidence-collection/evidence_$(date +%Y%m%d_%H%M%S)"
CASE_NAME="Lab11_Evidence_Collection"
COLLECTOR="Student_$(whoami)"

# Create evidence directory with timestamp
mkdir -p "$EVIDENCE_DIR"

# Create case information file for chain of custody
cat > "$EVIDENCE_DIR/case_info.txt" << CASEEOF
Case Name: $CASE_NAME
Collector: $COLLECTOR
Collection Date: $(date)
Hostname: $(hostname)
CASEEOF

echo "Evidence collection started..."

# Function to collect system information
collect_system_info() {
    echo "Collecting system information..."
    hostname > "$EVIDENCE_DIR/hostname.txt"
    uptime > "$EVIDENCE_DIR/uptime.txt"
    cat /etc/os-release > "$EVIDENCE_DIR/os_info.txt"
    uname -a > "$EVIDENCE_DIR/kernel_info.txt"
    date > "$EVIDENCE_DIR/collection_time.txt"
}

# Function to collect user and process information
collect_user_process_info() {
    echo "Collecting user and process information..."
    w > "$EVIDENCE_DIR/logged_users.txt"
    cat /etc/passwd > "$EVIDENCE_DIR/user_accounts.txt"
    ps aux > "$EVIDENCE_DIR/running_processes.txt"
}

# Function to collect network information
collect_network_info() {
    echo "Collecting network information..."
    ip addr > "$EVIDENCE_DIR/network_interfaces.txt"
    ss -tuln > "$EVIDENCE_DIR/network_connections.txt" 2>/dev/null || netstat -tuln > "$EVIDENCE_DIR/network_connections.txt" 2>/dev/null || echo "Network connections unavailable" > "$EVIDENCE_DIR/network_connections.txt"
    ip route > "$EVIDENCE_DIR/routing_table.txt"
}

# Function to collect system logs
collect_logs() {
    echo "Collecting system logs..."
    mkdir -p "$EVIDENCE_DIR/logs"
    cp /var/log/auth.log* "$EVIDENCE_DIR/logs/" 2>/dev/null || true
    cp /var/log/syslog* "$EVIDENCE_DIR/logs/" 2>/dev/null || true
    last > "$EVIDENCE_DIR/last_logins.txt"
    lastb > "$EVIDENCE_DIR/failed_logins.txt" 2>/dev/null || echo "lastb unavailable or empty" > "$EVIDENCE_DIR/failed_logins.txt"
}

# Function to create hash values for integrity
create_hashes() {
    echo "Creating hash values for evidence integrity..."
    find "$EVIDENCE_DIR" -type f -exec md5sum {} \; > "$EVIDENCE_DIR/evidence_md5.txt"
    find "$EVIDENCE_DIR" -type f -exec sha256sum {} \; > "$EVIDENCE_DIR/evidence_sha256.txt"
}

# Function to create collection summary
create_summary() {
    echo "Creating collection summary..."
    total_files=$(find "$EVIDENCE_DIR" -type f | wc -l)
    dir_size=$(du -sh "$EVIDENCE_DIR" | awk '{print $1}')
    
    cat > "$EVIDENCE_DIR/collection_summary.txt" << SUMEOF
Total Files Collected: $total_files
Collection End Time: $(date)
Evidence Directory Size: $dir_size
SUMEOF
    du -sh "$EVIDENCE_DIR"
}

# Main execution pipeline
collect_system_info
collect_user_process_info
collect_network_info
collect_logs
create_hashes
create_summary

echo "Evidence collection completed!"
echo "Evidence stored in: $EVIDENCE_DIR"
