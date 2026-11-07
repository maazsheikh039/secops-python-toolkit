#!/usr/bin/env python3
"""
Sample application for release engineering demo
"""

__version__ = "0.0.0"

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Version: {__version__}"

def calculate(a, b):
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    print(greet("World"))
    print(f"2 + 2 = {calculate(2, 2)}")
