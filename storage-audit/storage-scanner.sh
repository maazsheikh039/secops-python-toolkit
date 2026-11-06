#!/bin/bash
# Simple Object Storage Exposure Scanner

echo "==================================="
echo "Storage Exposure Detection Scanner"
echo "==================================="
echo ""

MINIO_HOST="http://localhost:9000"
BUCKETS=("private-bucket" "public-bucket" "exposed-data")

for bucket in "${BUCKETS[@]}"; do
    echo "Scanning bucket: $bucket"
    
    response=$(curl -s -o /dev/null -w "%{http_code}" "$MINIO_HOST/$bucket/")
    
    if [ "$response" == "200" ] || [ "$response" == "403" ]; then
        mc ls localminio/$bucket/ 2>/dev/null | while read -r line; do
            filename=$(echo $line | awk '{print $NF}')
            if [ ! -z "$filename" ]; then
                file_response=$(curl -s -o /dev/null -w "%{http_code}" "$MINIO_HOST/$bucket/$filename")
                if [ "$file_response" == "200" ]; then
                    echo "  [EXPOSED] $filename is publicly accessible!"
                else
                    echo "  [SECURE] $filename is protected"
                fi
            fi
        done
    fi
    echo ""
done

echo "==================================="
echo "Scan Complete"
echo "==================================="
