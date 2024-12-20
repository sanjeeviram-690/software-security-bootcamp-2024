import re

def detect_vulnerable_code(file_path):
    with open(file_path, 'r') as file:
        cpp_code = file.read()
    
    # Updated regex to match various forms of string concatenation
    pattern = re.compile(r'\w+\s*=\s*".*?"\s*\+\s*".*?"|".*?"\s*\+\s*\w+|".*?"\s*\+\s*\w+\s*\+\s*".*?"|\w+\s*\+\s*\w+')
    matches = pattern.findall(cpp_code)
    return matches

# Ask user for the file path
file_path = input("Please enter the path to your C++ file: ")

vulnerable_code = detect_vulnerable_code(file_path)
if vulnerable_code:
    print("Vulnerable code detected:")
    for match in vulnerable_code:
        print(match)
else:
    print("No vulnerable code detected.")
