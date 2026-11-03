"""
Dynamic plugin loader for the log analysis engine.
"""
import os
import importlib.util
from typing import List

class PluginLoader:
    """Loads and manages analyzer plugins dynamically."""
    
    def __init__(self, plugin_directory: str = 'plugins'):
        """
        Initialize the plugin loader.
        """
        self.plugin_directory = plugin_directory
        self.plugins = []
    
    def load_plugins(self) -> int:
        """
        Load all plugins from the plugin directory.
        """
        if not os.path.exists(self.plugin_directory):
            print(f"Plugin directory '{self.plugin_directory}' not found")
            return 0
        
        loaded_count = 0
        for filename in sorted(os.listdir(self.plugin_directory)):
            if filename.endswith('_analyzer.py'):
                plugin_path = os.path.join(self.plugin_directory, filename)
                try:
                    spec = importlib.util.spec_from_file_location(
                        filename[:-3], plugin_path
                    )
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    plugin_instance = module.get_plugin()
                    self.plugins.append(plugin_instance)
                    loaded_count += 1
                    print(f"[+] Loaded plugin: {plugin_instance.name}")
                    
                except Exception as e:
                    print(f"[-] Failed to load {filename}: {str(e)}")
        
        return loaded_count
    
    def get_plugins(self) -> List:
        """Return list of loaded plugins."""
        return self.plugins
