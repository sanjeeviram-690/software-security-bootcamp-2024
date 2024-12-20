import re

def vulnerability(code):

    strcpy_calls = re.findall(r'strcpy\((\w+),\s*(\w+)\);', code)
    buffers = re.findall(r'char (\w+)\[(\d+)\];', code)
    
   
    buffer_sizes = {name: int(size) for name, size in buffers}
    

    for dest, src in strcpy_calls:
        if dest in buffer_sizes and len(src) > buffer_sizes[dest]:
            print(f"Potential buffer overflow: '{dest}' is too small for '{src}'.")


#the c_code is uploaded
try:
    with open("/home/kali/software-security-bootcamp-2024/c_code.txt", 'r') as file:
        file_content = file.read()
        print("test case 1",vulnerability(file_content))  
except FileNotFoundError:
    print("The file was not found.")


vulnerability(c_code)
