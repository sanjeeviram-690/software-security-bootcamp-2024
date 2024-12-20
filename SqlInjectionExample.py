import re

def analyze_sql_injection_in_java(file_path):
    injection_risks = []

    with open(file_path, 'r') as file:
        code_lines = file.readlines()

    in_clause_pattern = re.compile(r'\bIN\s*\(([^)]+)\)', re.IGNORECASE)

    for line_number, line in enumerate(code_lines, start=1):
        in_matches = in_clause_pattern.findall(line)
        for match in in_matches:
            
            if re.search(r'\b\w+\s*\(', match) or re.search(r'\b\w+\s*=', match):
                injection_risks.append(f"Line {line_number}: Dynamic list construction detected in IN clause: {match}")
            
            if re.search(r'[\+\|\&]', match):
                injection_risks.append(f"Line {line_number}: String concatenation detected in IN clause: {match}")
            
            if re.search(r'\{.*\}', match):
                injection_risks.append(f"Line {line_number}: Array parameter detected in IN clause: {match}")

    return injection_risks

file_path = r'C:\Users\zuhai\OneDrive\Documents\java\SqlInjectionExample.java'  # Use raw string for file path
risks = analyze_sql_injection_in_java(file_path)
if risks:
    print("Potential SQL injection risks found:")
    for risk in risks:
        print(risk)
else:
    print("No SQL injection risks detected.")
