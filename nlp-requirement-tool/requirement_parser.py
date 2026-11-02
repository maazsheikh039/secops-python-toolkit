#!/usr/bin/env python3
"""
Natural Language Requirement to Python Function Converter
Parses simple requirements and generates function templates
"""

import re
import sys

class RequirementParser:
    """Parses natural language requirements into function specifications"""
    
    def __init__(self):
        # Common action verbs in requirements
        self.action_verbs = ['validate', 'check', 'verify', 'scan', 'analyze', 
                            'filter', 'encrypt', 'decrypt', 'authenticate']
    
    def parse_requirement(self, requirement: str) -> dict:
        """
        Parse a natural language requirement into structured data.
        
        Args:
            requirement: Natural language requirement string
            
        Returns:
            Dictionary with function_name, action, target, and parameters
        """
        requirement = requirement.lower().strip()
        
        action = None
        for verb in self.action_verbs:
            if verb in requirement:
                action = verb
                break
        
        target = requirement.replace(action, '').strip() if action else requirement
        function_name = requirement.replace(' ', '_')
        
        return {
            'function_name': function_name,
            'action': action,
            'target': target,
            'original': requirement
        }
    
    def generate_function_template(self, parsed_req: dict) -> str:
        """
        Generate Python function template from parsed requirement.
        
        Args:
            parsed_req: Dictionary from parse_requirement()
            
        Returns:
            String containing Python function template
        """
        function_name = parsed_req['function_name']
        action = parsed_req['action']
        target = parsed_req['target']
        
        template = f'''def {function_name}(input_data):
    """
    {action.capitalize()} {target}.
    
    Args:
        input_data: Data to be processed
        
    Returns:
        bool: True if {action} succeeds, False otherwise
    """
    # TODO: Implement {action} logic for {target}
    result = False
    
    # Add your implementation here
    
    return result
'''
        return template


def main():
    """Main function to run the requirement parser"""
    parser = RequirementParser()
    
    print("=" * 60)
    print("Natural Language Requirement to Python Function Converter")
    print("=" * 60)
    
    sample_requirements = [
        "validate user password strength",
        "check file permissions",
        "scan network ports",
        "encrypt sensitive data"
    ]
    
    print("\nProcessing Requirements:\n")
    
    for req in sample_requirements:
        print(f"Requirement: '{req}'")
        
        parsed = parser.parse_requirement(req)
        
        print(f"  Function Name: {parsed['function_name']}")
        print(f"  Action: {parsed['action']}")
        print(f"  Target: {parsed['target']}")
        
        template = parser.generate_function_template(parsed)
        
        filename = f"{parsed['function_name']}.py"
        with open(filename, 'w') as f:
            f.write(template)
        
        print(f"  Generated: {filename}\n")
    
    print("=" * 60)
    print("Function templates generated successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
