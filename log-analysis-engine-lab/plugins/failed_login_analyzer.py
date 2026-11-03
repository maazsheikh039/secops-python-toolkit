"""
Plugin to detect failed login attempts in logs.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plugin_base import PluginBase
import re

class FailedLoginAnalyzer(PluginBase):
    """Detects failed SSH and sudo login attempts."""
    
    def __init__(self):
        super().__init__()
        self.name = "Failed Login Analyzer"
        self.description = "Detects failed authentication attempts"
        self.patterns = [
            r'Failed password for .* from ([\d\.]+)',
            r'authentication failure.*rhost=([\d\.]+)',
            r'sudo.*authentication failure'
        ]
    
    def analyze(self, log_line: str) -> dict:
        """
        Check if log line contains failed login attempts.
        """
        for pattern in self.patterns:
            match = re.search(pattern, log_line, re.IGNORECASE)
            if match:
                return {
                    'severity': 'HIGH',
                    'message': 'Failed login attempt detected',
                    'details': {
                        'pattern_matched': pattern,
                        'log_line': log_line.strip()
                    }
                }
        return None

def get_plugin():
    """Return an instance of the plugin."""
    return FailedLoginAnalyzer()
