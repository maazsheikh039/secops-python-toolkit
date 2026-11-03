#!/bin/bash

MOUNT_POINT="/mnt/evidence_vault"

if [ ! -d "$MOUNT_POINT" ]; then
    echo "Error: Vault not mounted"
    exit 1
fi

echo "Verifying evidence integrity..."
cd "$MOUNT_POINT"
if [ -f "evidence_checksums.sha256" ]; then
    sudo sha256sum -c evidence_checksums.sha256
    if [ $? -eq 0 ]; then
        echo "All evidence files verified successfully"
    else
        echo "WARNING: Evidence integrity check FAILED"
    fi
else
    echo "Error: Checksum manifest not found in vault."
fi
