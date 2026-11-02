#!/usr/bin/env python3
"""
API Health Monitor
Periodically checks API endpoints and logs their status
"""

import requests
import time
import json
from datetime import datetime
import sys

class APIHealthMonitor:
    def __init__(self, base_url, check_interval=10):
        """
        Initialize the health monitor
        
        Args:
            base_url: Base URL of the API to monitor
            check_interval: Seconds between health checks
        """
        self.base_url = base_url
        self.check_interval = check_interval
        self.log_file = 'logs/health_monitor.log'
        self.status_file = 'logs/current_status.json'
        
    def log_message(self, message, level='INFO'):
        """
        Write a log message to file and console
        
        Args:
            message: The message to log
            level: Log level (INFO, WARNING, ERROR)
        """
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] [{level}] {message}"
        
        print(log_entry)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    
    def check_endpoint(self, endpoint, timeout=5):
        """
        Check a single endpoint and return its status
        """
        url = f"{self.base_url}{endpoint}"
        result = {
            'endpoint': endpoint,
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'status': 'unknown',
            'response_time': None,
            'status_code': None,
            'error': None
        }
        
        try:
            start_time = time.time()
            response = requests.get(url, timeout=timeout)
            end_time = time.time()
            
            result['response_time'] = round((end_time - start_time) * 1000, 2)
            result['status_code'] = response.status_code
            
            if 200 <= response.status_code < 300:
                result['status'] = 'healthy'
            else:
                result['status'] = 'unhealthy'
                
        except requests.exceptions.Timeout:
            result['status'] = 'timeout'
            result['error'] = 'Request timed out'
            
        except requests.exceptions.ConnectionError:
            result['status'] = 'unreachable'
            result['error'] = 'Could not connect to service'
            
        except Exception as e:
            result['status'] = 'error'
            result['error'] = str(e)
        
        return result
    
    def check_all_endpoints(self, endpoints):
        """
        Check all configured endpoints
        """
        results = []
        
        for endpoint in endpoints:
            result = self.check_endpoint(endpoint)
            results.append(result)
            
            if result['status'] == 'healthy':
                self.log_message(
                    f"{endpoint} is healthy (Response time: {result['response_time']}ms)",
                    'INFO'
                )
            else:
                self.log_message(
                    f"{endpoint} is {result['status']} - {result.get('error', 'Status code: ' + str(result['status_code']))}",
                    'ERROR'
                )
        
        return results
    
    def save_status(self, results):
        """
        Save current status to JSON file
        """
        status_data = {
            'last_check': datetime.now().isoformat(),
            'endpoints': results,
            'summary': {
                'total': len(results),
                'healthy': sum(1 for r in results if r['status'] == 'healthy'),
                'unhealthy': sum(1 for r in results if r['status'] != 'healthy')
            }
        }
        
        with open(self.status_file, 'w', encoding='utf-8') as f:
            json.dump(status_data, f, indent=2)
    
    def run(self, endpoints, duration=None):
        """
        Run the health monitor continuously
        """
        self.log_message(f"Starting health monitor for {self.base_url}")
        self.log_message(f"Monitoring endpoints: {', '.join(endpoints)}")
        self.log_message(f"Check interval: {self.check_interval} seconds")
        
        start_time = time.time()
        check_count = 0
        
        try:
            while True:
                check_count += 1
                self.log_message(f"--- Health Check #{check_count} ---")
                
                results = self.check_all_endpoints(endpoints)
                self.save_status(results)
                
                if duration and (time.time() - start_time) >= duration:
                    self.log_message("Monitoring duration completed")
                    break
                
                time.sleep(self.check_interval)
                
        except KeyboardInterrupt:
            self.log_message("Monitoring stopped by user", 'INFO')
        except Exception as e:
            self.log_message(f"Monitor error: {str(e)}", 'ERROR')

if __name__ == '__main__':
    BASE_URL = 'http://localhost:5000'
    CHECK_INTERVAL = 5  # seconds
    
    ENDPOINTS = [
        '/health',
        '/api/users',
        '/api/data'
    ]
    
    monitor = APIHealthMonitor(BASE_URL, CHECK_INTERVAL)
    # Run for 30 seconds for test demonstration
    monitor.run(ENDPOINTS, duration=30)
