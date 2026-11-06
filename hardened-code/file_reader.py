import os

def read_user_file(filename):
    """
    Read a file from the user uploads directory.
    WARNING: This code contains security vulnerabilities!
    """
    # VULNERABLE: No path validation
    base_path = "/tmp/uploads/"
    file_path = base_path + filename
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    file = input("Enter filename to read: ")
    content = read_user_file(file)
    print(content)
