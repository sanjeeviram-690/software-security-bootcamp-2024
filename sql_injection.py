def detect_sql_injection(code):
  
    if "+" in code or "&" in code:
        if "user_input" in code:  
            return "SQL injection string concatenation is found"
    
   
    dangerous_patterns = ["' OR 1=1 --", "UNION SELECT", "DROP TABLE", "--", "AND 1=1", "ORDER BY", "AND","OR"]
    for pattern in dangerous_patterns:
        if pattern in code:
            return f"Potential dangerous SQL pattern detected: {pattern}"
    
    return "No SQL injection detected."
    
#to read external code
try:
    with open("/home/kali/software-security-bootcamp-2024/vuln_code.txt", 'r') as file:
        file_content = file.read()
        print("test case 1",detect_sql_injection(file_content))  
except FileNotFoundError:
    print("The file was not found.")

