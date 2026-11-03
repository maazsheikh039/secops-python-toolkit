"""
Base class for all log analyzer plugins.
All plugins must inherit from this class.
"""

class PluginBase:
    """
    Base class that defines the interface for all analyzer plugins.
    """
    
    def __init__(self):
        """Initialize the plugin with a name and description."""
        self.name = "Base Plugin"
        self.description = "Base plugin class"
    
    def analyze(self, log_line: str) -> dict:
        """
        Analyze a single log line.
        
        Args:
            log_line: A single line from a log file
            
        Returns:
            Dictionary with analysis results or None if no match
            Format: {'severity': str, 'message': str, 'details': dict}
        """
        raise NotImplementedError("Plugins must implement analyze() method")
    
    def get_info(self) -> dict:
        """
        Return plugin information.
        
        Returns:
            Dictionary with plugin name and description
        """
        return {
            'name': self.name,
            'description': self.description
        }
