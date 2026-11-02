"""
Hashing utilities for secure password storage and data integrity.
"""

import hashlib

def hash_sha256(data):
    """
    Generate SHA-256 hash of input data.
    
    Args:
        data (str): Data to hash
    
    Returns:
        str: Hexadecimal hash string
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def hash_file(filepath):
    """
    Generate SHA-256 hash of a file's contents.
    
    Args:
        filepath (str): Path to file
    
    Returns:
        str: Hexadecimal hash of file contents
    """
    sha256_hash = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def verify_hash(data, expected_hash):
    """
    Verify if data matches expected hash.
    
    Args:
        data (str): Data to verify
        expected_hash (str): Expected hash value
    
    Returns:
        bool: True if hashes match
    """
    return hash_sha256(data) == expected_hash
