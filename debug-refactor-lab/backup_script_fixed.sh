#!/bin/bash

# Improved backup script with error handling and security fixes
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <source_directory>"
    exit 1
fi

readonly BACKUP_DIR="/tmp/backups"
readonly SOURCE_DIR="$1"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist"
    exit 1
fi

if ! mkdir -p "$BACKUP_DIR"; then
    echo "Error: Failed to create backup directory"
    exit 1
fi

if ! cp -r "$SOURCE_DIR" "$BACKUP_DIR"; then
    echo "Error: Failed to copy files"
    exit 1
fi

timestamp=$(date +%Y%m%d) || {
    echo "Error: Failed to generate timestamp"
    exit 1
}

source_basename=$(basename "$SOURCE_DIR")
if ! mv "$BACKUP_DIR/$source_basename" "$BACKUP_DIR/backup_$timestamp"; then
    echo "Error: Failed to rename backup"
    exit 1
fi

echo "Backup completed at $(date)" >> "$BACKUP_DIR/backup.log"
echo "Backup location: $BACKUP_DIR/backup_$timestamp"

echo "Backup completed successfully"
exit 0
