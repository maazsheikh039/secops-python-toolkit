"""
Main log analysis engine with plugin support.
"""
from plugin_loader import PluginLoader
from datetime import datetime
import json

class LogAnalyzer:
    """Main engine for analyzing logs using plugins."""
    
    def __init__(self):
        """Initialize the log analyzer."""
        self.loader = PluginLoader()
        self.results = []
    
    def initialize(self):
        """Load all available plugins."""
        print("\n=== Initializing Log Analysis Engine ===")
        count = self.loader.load_plugins()
        print(f"\nTotal plugins loaded: {count}\n")
        return count > 0
    
    def analyze_file(self, log_file: str):
        """
        Analyze a log file using all loaded plugins.
        """
        print(f"[*] Analyzing log file: {log_file}")
        
        try:
            with open(log_file, 'r', encoding='utf-8') as f:
                line_number = 0
                for line in f:
                    line_number += 1
                    for plugin in self.loader.get_plugins():
                        result = plugin.analyze(line)
                        if result:
                            result['line_number'] = line_number
                            result['plugin'] = plugin.name
                            result['timestamp'] = datetime.now().isoformat()
                            self.results.append(result)
            
            print(f"[+] Analysis complete. Found {len(self.results)} issues.")
            
        except FileNotFoundError:
            print(f"[-] Error: Log file '{log_file}' not found")
        except Exception as e:
            print(f"[-] Error analyzing file: {str(e)}")
    
    def generate_report(self, output_file: str = 'output/report.json'):
        """
        Generate analysis report.
        """
        report = {
            'analysis_date': datetime.now().isoformat(),
            'total_findings': len(self.results),
            'findings': self.results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n[+] Report saved to: {output_file}")
        
        print("\n=== Analysis Summary ===")
        severity_counts = {}
        for result in self.results:
            sev = result['severity']
            severity_counts[sev] = severity_counts.get(sev, 0) + 1
        
        for severity, count in severity_counts.items():
            print(f"{severity}: {count} findings")

def main():
    """Main execution function."""
    analyzer = LogAnalyzer()
    
    if not analyzer.initialize():
        print("[-] No plugins loaded. Exiting.")
        return
    
    analyzer.analyze_file('logs/sample.log')
    analyzer.generate_report()

if __name__ == '__main__':
    main()
