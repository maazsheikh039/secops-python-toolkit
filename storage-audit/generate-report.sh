#!/bin/bash
REPORT_FILE=~/exposure-report.txt

echo "Object Storage Exposure Report" > $REPORT_FILE
echo "Generated: $(date)" >> $REPORT_FILE
echo "================================" >> $REPORT_FILE
echo "" >> $REPORT_FILE

for bucket in private-bucket public-bucket exposed-data; do
    echo "Bucket: $bucket" >> $REPORT_FILE
    policy=$(mc anonymous list localminio/$bucket 2>/dev/null)
    
    if echo "$policy" | grep -q "download"; then
        echo "  Status: EXPOSED - Public read access enabled" >> $REPORT_FILE
        echo "  Risk Level: HIGH" >> $REPORT_FILE
    else
        echo "  Status: SECURE - No public access" >> $REPORT_FILE
        echo "  Risk Level: LOW" >> $REPORT_FILE
    fi
    echo "" >> $REPORT_FILE
done

cat $REPORT_FILE
