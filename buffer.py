import re

def find_vulnerable_code(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Regular expressions to detect potential buffer overrun vulnerabilities
    patterns = [
        r'char\s+\w+\[\d+\];',  # Fixed-size character arrays
        r'strcpy\s*\(',         # Use of strcpy
        r'sprintf\s*\(',        # Use of sprintf
        r'gets\s*\(',           # Use of gets
        r'strcat\s*\(',         # Use of strcat
        r'memcpy\s*\(',         # Use of memcpy
    ]

    for pattern in patterns:
        matches = re.findall(pattern, code)
        if matches:
            print(f"Potential vulnerability found in {file_path}:")
            for match in matches:
                print(f"  {match}")

# Example usage
file_path = input("Enter the path to the C++ file: ")
find_vulnerable_code(file_path)
