#!/bin/bash

# Evidence Verification Script
# Purpose: Verify integrity of collected evidence using hash values

if [ $# -ne 1 ]; then
    echo "Usage: $0 <path_to_evidence_directory>"
    exit 1
fi

EVIDENCE_DIR="$1"

if [ ! -d "$EVIDENCE_DIR" ]; then
    echo "Error: Evidence directory '$EVIDENCE_DIR' not found!"
    exit 1
fi

echo "Starting evidence verification for: $EVIDENCE_DIR..."

if [ -f "$EVIDENCE_DIR/evidence_md5.txt" ]; then
    echo "Verifying MD5 hashes..."
    (cd "$EVIDENCE_DIR" && md5sum -c evidence_md5.txt)
else
    echo "Warning: MD5 hash manifest not found."
fi

if [ -f "$EVIDENCE_DIR/evidence_sha256.txt" ]; then
    echo "Verifying SHA256 hashes..."
    (cd "$EVIDENCE_DIR" && sha256sum -c evidence_sha256.txt)
else
    echo "Warning: SHA256 hash manifest not found."
fi

echo "Verification completed!"
