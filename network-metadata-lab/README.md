# Network Metadata Extraction and Enrichment Utility

A robust Python command-line utility designed to parse network traffic logs, extract granular connection parameters (timestamps, protocols, source/destination IPs, ports), enrich records with service signatures and IP range classifications, and export structured telemetry in JSON format.

## Objectives
- Parse unstructured network log entries efficiently using compiled regular expression patterns.
- Map destination ports to known network services (HTTP, HTTPS, DNS, SSH, DHCP, etc.).
- Classify IP addresses as internal (RFC 1918 private ranges) or external.
- Generate statistical distribution reports on protocols and top target services.
- Export enriched intelligence data into structured JSON files for SIEM or dashboard integration.

## Tools Used
- **Python 3** (`re`, `json`, `collections`, `datetime`)
- **Network Analysis Utilities:** `tcpdump`, `tshark`
- **Linux CLI / SSH**

## Key Skills Demonstrated
- **Log Parsing & Regex Engineering:** Extracting structured fields from raw text logs reliably.
- **Data Enrichment:** Mapping raw port numbers to human-readable protocol and service attributes.
- **IP Classification:** Distinguishing private internal subnets from external public endpoints.

## Troubleshooting Log
- *Log Format Alignment:* Ensured regex match groups correspond precisely with the spacing and arrow delimiter (`->`) in test log datasets.
- *IP Octet Validation:* Added length checks during IP classification to prevent IndexError exceptions on malformed strings.
