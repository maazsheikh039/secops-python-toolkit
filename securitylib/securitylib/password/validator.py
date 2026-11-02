"""
Password validation module for security library.
Provides functions to check password strength and compliance.
"""

import re

def check_length(password, min_length=8):
    """
    Check if password meets minimum length requirement.
    
    Args:
        password (str): The password to check
        min_length (int): Minimum required length (default: 8)
    
    Returns:
        bool: True if password meets length requirement
    """
    return len(password) >= min_length


def has_uppercase(password):
    """
    Check if password contains at least one uppercase letter.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has uppercase letter
    """
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """
    Check if password contains at least one lowercase letter.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has lowercase letter
    """
    return any(char.islower() for char in password)


def has_digit(password):
    """
    Check if password contains at least one digit.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has digit
    """
    return any(char.isdigit() for char in password)


def has_special_char(password):
    """
    Check if password contains at least one special character.
    
    Args:
        password (str): The password to check
    
    Returns:
        bool: True if password has special character
    """
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(char in special_chars for char in password)


def validate_password(password, min_length=8):
    """
    Comprehensive password validation.
    
    Args:
        password (str): The password to validate
        min_length (int): Minimum required length
    
    Returns:
        dict: Validation results with 'valid' boolean and 'errors' list
    """
    errors = []
    
    if not check_length(password, min_length):
        errors.append(f"Password must be at least {min_length} characters")
    if not has_uppercase(password):
        errors.append("Password must contain at least one uppercase letter")
    if not has_lowercase(password):
        errors.append("Password must contain at least one lowercase letter")
    if not has_digit(password):
        errors.append("Password must contain at least one digit")
    if not has_special_char(password):
        errors.append("Password must contain at least one special character")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors
    }
