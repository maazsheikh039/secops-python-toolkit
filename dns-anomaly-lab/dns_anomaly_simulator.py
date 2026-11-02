#!/usr/bin/env python3
"""
DNS Anomaly Simulator - Simulates various DNS issues
"""

import dns.resolver
import random
import time
from datetime import datetime

class DNSAnomalySimulator:
    """Simulates various DNS anomalies for testing"""
    
    def __init__(self):
        self.resolver = dns.resolver.Resolver()
        self.legitimate_domains = [
            "google.com", "github.com", "stackoverflow.com"
        ]
        self.suspicious_domains = [
            "aksjdhfkjashdf.com",
            "google-login-verify.tk",
            "192.168.1.1.nip.io"
        ]
    
    def simulate_normal_query(self, domain):
        """Simulate a normal DNS query."""
        result = {
            'domain': domain,
            'timestamp': datetime.now().isoformat(),
            'anomaly_type': 'none',
            'status': 'success',
            'ips': []
        }
        
        try:
            answers = self.resolver.resolve(domain, 'A')
            result['ips'] = [str(rdata) for rdata in answers]
            result['response_time'] = random.uniform(0.01, 0.05)
        except Exception as e:
            result['status'] = 'failed'
            result['error'] = str(e)
        
        return result
    
    def simulate_nxdomain(self):
        """Simulate NXDOMAIN (non-existent domain) anomaly."""
        fake_domain = f"nonexistent{random.randint(1000,9999)}.invalid"
        result = {
            'domain': fake_domain,
            'timestamp': datetime.now().isoformat(),
            'anomaly_type': 'NXDOMAIN',
            'status': 'anomaly_detected',
            'description': 'Domain does not exist'
        }
        return result
    
    def simulate_fast_flux(self, domain):
        """Simulate Fast Flux DNS (rapidly changing IPs)."""
        results = []
        for i in range(3):
            result = {
                'domain': domain,
                'timestamp': datetime.now().isoformat(),
                'anomaly_type': 'fast_flux',
                'query_number': i + 1,
                'ips': [f"192.0.2.{random.randint(1,254)}" 
                       for _ in range(random.randint(2,5))]
            }
            results.append(result)
            time.sleep(0.2)
        return results
    
    def simulate_dga_domain(self):
        """Simulate Domain Generation Algorithm (DGA) pattern."""
        length = random.randint(15, 30)
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))
        dga_domain = f"{random_string}.com"
        
        result = {
            'domain': dga_domain,
            'timestamp': datetime.now().isoformat(),
            'anomaly_type': 'DGA_pattern',
            'status': 'suspicious',
            'entropy': 'high',
            'description': 'Domain matches DGA pattern (high entropy, random characters)'
        }
        return result

def run_simulation():
    """Run various DNS anomaly simulations"""
    simulator = DNSAnomalySimulator()
    
    print("\n" + "="*70)
    print("DNS ANOMALY SIMULATOR")
    print("="*70 + "\n")
    
    print("[1] Normal DNS Queries")
    print("-" * 70)
    for domain in simulator.legitimate_domains[:2]:
        result = simulator.simulate_normal_query(domain)
        print(f"Domain: {result['domain']}")
        print(f"Status: {result['status']}")
        if result.get('ips'):
            print(f"IPs: {', '.join(result['ips'])}")
        print()
    
    print("\n[2] NXDOMAIN Anomaly (Non-existent Domain)")
    print("-" * 70)
    nxdomain_result = simulator.simulate_nxdomain()
    print(f"Domain: {nxdomain_result['domain']}")
    print(f"Anomaly: {nxdomain_result['anomaly_type']}")
    print(f"Description: {nxdomain_result['description']}")
    
    print("\n[3] Fast Flux DNS Anomaly")
    print("-" * 70)
    print("Querying same domain multiple times...")
    flux_results = simulator.simulate_fast_flux("suspicious-site.com")
    for result in flux_results:
        print(f"Query {result['query_number']}: {len(result['ips'])} IPs -> {result['ips'][:2]}...")
    print("Notice: IPs change rapidly (potential malware C&C)")
    
    print("\n[4] DGA (Domain Generation Algorithm) Pattern")
    print("-" * 70)
    dga_result = simulator.simulate_dga_domain()
    print(f"Domain: {dga_result['domain']}")
    print(f"Anomaly: {dga_result['anomaly_type']}")
    print(f"Description: {dga_result['description']}")
    
    print("\n" + "="*70)
    print("Simulation Complete")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_simulation()
