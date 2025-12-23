import os 

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def write_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    # Example usage
    file_path = 'example.txt'
    
    # Write to the file
    write_file(file_path, "Hello, World!")
    
    # Read from the file
    content = read_file(file_path)
    print(content)  # Output: Hello, World!
# main.py
# This module provides basic file operations: reading from and writing to files.
# It includes functions to read the content of a file and write content to a file.
# The module also contains an example usage in the main block.


def read_file(file_path):    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def write_file(file_path, content):    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content) 

if __name__ == "__main__":
    # Example usage
    file_path = 'example.txt'
    
    # Write to the file
    write_file(file_path, "Hello, World!")
    
    # Read from the file
    content = read_file(file_path)
    print(content)  # Output: Hello, World!



    adnd write content to a file.
# It includes functions to read the content of a file and write content to a file.
# The module also contains an example usage in the main block.

import os