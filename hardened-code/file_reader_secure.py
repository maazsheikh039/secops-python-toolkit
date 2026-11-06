import os
from pathlib import Path

def read_user_file(filename):
    """
    Securely read a file from the user uploads directory.
    SECURE: Validates path to prevent traversal attacks.
    """
    base_path = Path("/tmp/uploads/").resolve()
    
    # Sanitize filename - remove path components
    safe_filename = os.path.basename(filename)
    
    # Construct full path
    file_path = (base_path / safe_filename).resolve()
    
    # SECURE: Verify the resolved path is within base directory
    try:
        file_path.relative_to(base_path)
    except ValueError:
        return "Error: Access denied - path traversal detected!"
    
    if not file_path.exists() or not file_path.is_file():
        return "Error: File not found!"
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    file = input("Enter filename to read: ")
    content = read_user_file(file)
    print(content)
