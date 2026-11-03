"""
Custom Analyzer Plugin for testing extensibility.
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plugin_base import PluginBase

class CustomAnalyzer(PluginBase):
    """Detects WARNING keywords."""
    def __init__(self):
        super().__init__()
        self.name = "Custom Analyzer"
        self.description = "Detects WARNING keywords"
    
    def analyze(self, log_line: str) -> dict:
        if 'WARNING' in log_line:
            return {
                'severity': 'LOW',
                'message': 'Warning detected',
                'details': {'log_line': log_line.strip()}
            }
        return None

def get_plugin():
    return CustomAnalyzer()
