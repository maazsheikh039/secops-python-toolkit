import subprocess
import re

def validate_hostname(hostname):
    """
    Validate hostname format.
    """
    pattern = r'^[a-zA-Z0-9.-]+$'
    if not re.match(pattern, hostname):
        return False
    if len(hostname) > 253:
        return False
    return True

def ping_host(hostname):
    """
    Securely ping a hostname and return results.
    SECURE: Uses subprocess with argument list, validates input.
    """
    if not validate_hostname(hostname):
        print("Error: Invalid hostname format!")
        return 1
    
    try:
        # SECURE: Use list of arguments instead of shell string
        result = subprocess.run(
            ['ping', '-c', '4', hostname],
            capture_output=True,
            text=True,
            timeout=10,
            check=False
        )
        
        print(result.stdout)
        return result.returncode
        
    except subprocess.TimeoutExpired:
        print("Error: Ping timeout!")
        return 1
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

if __name__ == "__main__":
    host = input("Enter hostname to ping: ")
    ping_host(host)
