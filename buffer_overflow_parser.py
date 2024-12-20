import re

class BufferOverflowParser:
    def __init__(self, code):
        self.code = code
        self.issues = []

    def detect_variable_index_access(self):

        pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\[\s*([a-zA-Z_][a-zA-Z0-9_]*|[0-9]+)\s*\]'
        matches = re.findall(pattern, self.code)
        for match in matches:
            if match.isidentifier():

                self.issues.append(f"Potential buffer overflow: Array access with variable index '{match}'")

    def detect_loop_conditions(self):
  
        loop_pattern = r'\b(for|while)\s*\((.*?)\)'
        loops = re.findall(loop_pattern, self.code)
        for loop in loops:
            condition = loop[1]

            if re.search(r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*>=\s*[0-9]+', condition):
                self.issues.append(f"Potential buffer overflow: Loop condition may exceed array bounds in '{condition}'")

    def detect_nested_array_access(self):
        nested_pattern = r'\b[a-zA-Z_][a-zA-Z0-9_]*\s*\[\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\[\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\]\s*\]\s*'
        matches = re.findall(nested_pattern, self.code)
        for match in matches:
            self.issues.append(f"Potential buffer overflow: Nested array access '{match}'")

    def parse(self):
        self.detect_variable_index_access()
        self.detect_loop_conditions()
        self.detect_nested_array_access()
        return self.issues

test_cases = [
    """
    int arr[10];
    for (int i = 0; i <= 10; i++) {
        arr[i] = i; // Issue: array size is 10, index can go from 0 to 10, which is out of bounds.
    }
    """,
    """
    int arr[5];
    int index = 3;
    arr[index] = 10; // Index is a variable, potentially out of bounds if index is larger than 4.
    """,
    """
    int arr[10][10];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j <= 10; j++) { // Issue: j can go from 0 to 10, which is out of bounds for the second dimension.
            arr[i][j] = i + j;
        }
    }
    """,
    """
    int arr[5];
    for (int i = 0; i < n; i++) { // Potential overflow if n > 5
        arr[i] = i;
    }
    """,
    """
    int arr[3];
    int index = 2;
    arr[index + 1] = 5; // Issue: index + 1 can result in out-of-bounds access.
    """,
    """
    int arr[10];
    for (int i = 0; i < 10; i++) {
        arr[i] = i;
    }
    for (int j = 0; j < 10; j++) {
        arr[j + 1] = j; // Issue: j + 1 can go out of bounds, exceeding index 9.
    }
    """,
    """
    int arr[7];
    int i = 0;
    while (i < 8) { // i can be 8, which is out of bounds.
        arr[i] = i;
        i++;
    }
    """,
    """
    int arr[10];
    for (int i = 0; i < 15; i++) { // i can go up to 14, which exceeds the array bounds.
        arr[i] = i;
    }
    """,
    """
    int arr[5];
    for (int i = 0; i < 10; i++) { // i can go up to 9, which exceeds array bounds.
        arr[i] = i;
    }
    """,
    """
    int arr[5][5];
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 6; j++) { // Issue: j can go up to 5, which exceeds the second dimension.
            arr[i][j] = i + j;
        }
    }
    """,
    """
    int arr[20];
    int n = 25;
    for (int i = 0; i < n; i++) { // n > 20, potentially causing an overflow.
        arr[i] = i;
    }
    """,
    """
    int arr[10];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) { // No overflow here, the bounds are respected.
            arr[i][j] = i + j;
        }
    }
    """
]


for i, test_case in enumerate(test_cases):
    parser = BufferOverflowParser(test_case)
    issues = parser.parse()
    print(f"Test Case {i + 1}:")
    for issue in issues:
        print(issue)
    print("\n")
