#!/usr/bin/env python3
"""
Network Metadata Extraction Utility
Extracts and enriches network intelligence from log files
"""

import re
import json
from collections import defaultdict
from datetime import datetime

# Try to import geolocation library
try:
    from geolite2 import geolite2
    GEOIP_AVAILABLE = True
except ImportError:
    GEOIP_AVAILABLE = False
    print("Note: GeoIP not available. Install with: pip3 install maxminddb-geolite2")


class NetworkMetadataExtractor:
    """Extract and enrich network metadata from logs"""
    
    def __init__(self):
        self.connections = []
        self.stats = defaultdict(int)
        
        # Common port to service mapping
        self.port_services = {
            20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "TELNET",
            25: "SMTP", 53: "DNS", 67: "DHCP", 68: "DHCP",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
            445: "SMB", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
            8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
        }
        
        # Protocol number to name mapping
        self.protocols = {
            1: "ICMP", 6: "TCP", 17: "UDP"
        }
    
    def parse_log_line(self, line):
        """
        Parse a single log line and extract network metadata.
        
        Expected format: TIMESTAMP PROTOCOL SRC_IP:SRC_PORT -> DST_IP:DST_PORT
        
        Args:
            line: String containing log entry
            
        Returns:
            Dictionary with parsed metadata or None if parsing fails
        """
        pattern = r'(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+(\w+)\s+([\d.]+):(\d+)\s+->\s+([\d.]+):(\d+)'
        
        match = re.search(pattern, line)
        if not match:
            return None
        
        timestamp, protocol, src_ip, src_port, dst_ip, dst_port = match.groups()
        
        metadata = {
            'timestamp': timestamp,
            'protocol': protocol,
            'src_ip': src_ip,
            'src_port': int(src_port),
            'dst_ip': dst_ip,
            'dst_port': int(dst_port)
        }
        
        return metadata
    
    def enrich_metadata(self, metadata):
        """
        Enrich metadata with additional intelligence.
        
        Args:
            metadata: Dictionary with basic network metadata
            
        Returns:
            Enhanced metadata dictionary
        """
        dst_port = metadata['dst_port']
        metadata['service'] = self.port_services.get(dst_port, f"Unknown-{dst_port}")
        
        if GEOIP_AVAILABLE:
            try:
                reader = geolite2.reader()
                geo_data = reader.get(metadata['dst_ip'])
                if geo_data:
                    metadata['dst_country'] = geo_data.get('country', {}).get('iso_code', 'Unknown')
                    metadata['dst_city'] = geo_data.get('city', {}).get('names', {}).get('en', 'Unknown')
                else:
                    metadata['dst_country'] = 'Private/Unknown'
            except Exception:
                metadata['dst_country'] = 'Error'
        
        metadata['dst_type'] = self._classify_ip(metadata['dst_ip'])
        
        return metadata
    
    def _classify_ip(self, ip):
        """
        Classify IP address as internal or external.
        
        Args:
            ip: IP address string
            
        Returns:
            String: 'Internal' or 'External'
        """
        octets = ip.split('.')
        if len(octets) != 4:
            return 'External'
            
        if octets[0] == '10':
            return 'Internal'
        elif octets[0] == '172' and 16 <= int(octets[1]) <= 31:
            return 'Internal'
        elif octets[0] == '192' and octets[1] == '168':
            return 'Internal'
        elif octets[0] == '127':
            return 'Internal'
        else:
            return 'External'
    
    def process_log_file(self, filename):
        """
        Process entire log file and extract all metadata.
        
        Args:
            filename: Path to log file
        """
        print(f"[*] Processing log file: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                metadata = self.parse_log_line(line)
                
                if metadata:
                    enriched = self.enrich_metadata(metadata)
                    self.connections.append(enriched)
                    
                    self.stats['total_connections'] += 1
                    self.stats[f"protocol_{enriched['protocol']}"] += 1
                    self.stats[f"service_{enriched['service']}"] += 1
        
        print(f"[+] Processed {self.stats['total_connections']} connections")
    
    def generate_report(self):
        """Generate and display analysis report"""
        print("\n" + "="*60)
        print("NETWORK METADATA EXTRACTION REPORT")
        print("="*60)
        
        print(f"\n[*] Total Connections: {self.stats['total_connections']}")
        
        print("\n[*] Protocol Distribution:")
        for key, value in self.stats.items():
            if key.startswith('protocol_'):
                protocol = key.replace('protocol_', '')
                print(f"    {protocol}: {value}")
        
        print("\n[*] Top Services:")
        services = [(k.replace('service_', ''), v) for k, v in self.stats.items() if k.startswith('service_')]
        services.sort(key=lambda x: x[1], reverse=True)
        for service, count in services[:5]:
            print(f"    {service}: {count}")
        
        unique_dst_ips = set(conn['dst_ip'] for conn in self.connections)
        print(f"\n[*] Unique Destination IPs: {len(unique_dst_ips)}")
        
        external_count = sum(1 for conn in self.connections if conn.get('dst_type') == 'External')
        internal_count = sum(1 for conn in self.connections if conn.get('dst_type') == 'Internal')
        print(f"\n[*] Traffic Distribution:")
        print(f"    External: {external_count}")
        print(f"    Internal: {internal_count}")
    
    def export_json(self, output_file):
        """
        Export enriched metadata to JSON file.
        
        Args:
            output_file: Path to output JSON file
        """
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump({
                'metadata': self.connections,
                'statistics': dict(self.stats),
                'generated_at': datetime.now().isoformat()
            }, f, indent=2)
        
        print(f"\n[+] Exported metadata to: {output_file}")


def main():
    """Main execution function"""
    print("Network Metadata Extraction Utility")
    print("-" * 60)
    
    extractor = NetworkMetadataExtractor()
    extractor.process_log_file('network_traffic.log')
    extractor.generate_report()
    extractor.export_json('network_metadata.json')
    
    print("\n[+] Analysis complete!")


if __name__ == "__main__":
    main()
