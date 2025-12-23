import os 

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content


print(read_file('example.txt'))  # Replace 'example.txt' with your file path
def write_file(file_path, content):
    """Writes the given content to a file."""
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Content written to {file_path}.")
write_file('output.txt', 'Hello, World!')  # Replace 'output.txt' with your desired file path
# The above code defines two functions: read_file and write_file.
# read_file reads the content of a specified file and returns it as a string.
# write_file writes the given content to a specified file.
# Example usage of the functions is also provided.
