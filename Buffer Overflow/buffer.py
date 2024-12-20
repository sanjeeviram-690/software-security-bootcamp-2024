import re

# Function to read C/C++ file
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Function to detect unsafe string operations
def detect_unsafe_string_operations(code):
    if code is None:
        return

    # Patterns for detecting unsafe string functions
    patterns = {
        "Unbounded strcpy": r'strcpy\s*\(\s*\w+\s*,\s*\w+\s*\)',  # strcpy(dest, src)
        "Unbounded strcat": r'strcat\s*\(\s*\w+\s*,\s*\w+\s*\)',  # strcat(dest, src)
        "Usage of gets": r'gets\s*\(\s*\w+\s*\)',                # gets(buffer)
    }

    unsafe_operations_found = {op: [] for op in patterns}
    unsafe_operations_found["Buffer size verification missing"] = []

    for op, pattern in patterns.items():
        matches = re.findall(pattern, code, re.IGNORECASE)
        if matches:
            unsafe_operations_found[op].extend(matches)

    # Check for buffer size verification
    buffer_patterns = [
        r'strcpy\s*\(\s*\w+\s*,\s*\w+\s*\)',
        r'strcat\s*\(\s*\w+\s*,\s*\w+\s*\)',
    ]
    buffer_checks = r'if\s*\(\s*\w+\s*<\s*\w+\)'

    for pattern in buffer_patterns:
        matches = re.finditer(pattern, code, re.IGNORECASE)
        for match in matches:
            start, end = match.span()
            buffer_check = re.search(buffer_checks, code[:start], re.IGNORECASE)
            if not buffer_check:
                unsafe_operations_found["Buffer size verification missing"].append(match.group())

    return unsafe_operations_found

# Main function to get user input and process the file
def main():
    filename = input("Enter the path to the C/C++ file: ")
    code = read_file(filename)
    if code:
        unsafe_operations = detect_unsafe_string_operations(code)
        for op, issues in unsafe_operations.items():
            if issues:
                print(f"\n{op} detected:\n" + "\n".join(issues))
            else:
                print(f"\nNo {op} detected.")

if __name__ == "__main__":
    main()
