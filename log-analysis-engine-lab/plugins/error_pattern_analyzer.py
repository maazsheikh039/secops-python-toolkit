"""
Plugin to detect common error patterns in logs.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plugin_base import PluginBase

class ErrorPatternAnalyzer(PluginBase):
    """Detects common error keywords in logs."""
    
    def __init__(self):
        super().__init__()
        self.name = "Error Pattern Analyzer"
        self.description = "Detects error keywords and patterns"
        self.error_keywords = ['error', 'critical', 'fatal', 'exception']
    
    def analyze(self, log_line: str) -> dict:
        """
        Check if log line contains error keywords.
        """
        log_lower = log_line.lower()
        for keyword in self.error_keywords:
            if keyword in log_lower:
                severity = 'CRITICAL' if keyword in ['critical', 'fatal'] else 'MEDIUM'
                return {
                    'severity': severity,
                    'message': f'Error keyword detected: {keyword}',
                    'details': {
                        'keyword': keyword,
                        'log_line': log_line.strip()
                    }
                }
        return None

def get_plugin():
    """Return an instance of the plugin."""
    return ErrorPatternAnalyzer()
