#include <stdio.h>
#include <string.h>

void unsafeStrcat(char* userInput) {
    char buffer[10] = "Hello";
    // Unsafe usage of strcat without checking buffer size
    strcat(buffer, userInput);
    printf("Buffer: %s\n", buffer);
}

int main() {
    char userInput[20] = "World";  // Assume this is user input
    unsafeStrcat(userInput);
    return 0;
}
