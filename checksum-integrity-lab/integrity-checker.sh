#!/bin/bash

# File Integrity Checker Script
# This script generates and verifies file checksums

generate_checksums() {
    local directory="${1:-.}"
    local output_file="checksums.sha256"
    
    echo "Generating checksums for files in $directory..."
    find "$directory" -type f -name "*.txt" -exec sha256sum {} \; > "$output_file"
    echo "Checksums saved to $output_file"
}

verify_checksums() {
    local checksum_file="${1:-checksums.sha256}"
    
    if [ ! -f "$checksum_file" ]; then
        echo "Error: Checksum file not found!"
        exit 1
    fi
    
    echo "Verifying file integrity..."
    sha256sum -c "$checksum_file"
}

case "$1" in
    generate)
        generate_checksums "$2"
        ;;
    verify)
        verify_checksums "$2"
        ;;
    *)
        echo "Usage: $0 {generate|verify} [path]"
        exit 1
        ;;
esac
