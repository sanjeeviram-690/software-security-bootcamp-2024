#include <stdio.h>
#include <string.h>

void safeStrcpy(char* userInput) {
    char buffer[10];
    // Safe usage with buffer size verification
    if (strlen(userInput) < sizeof(buffer)) {
        strcpy(buffer, userInput);
        printf("Buffer: %s\n", buffer);
    } else {
        printf("Input too long!\n");
    }
}

void safeStrcat(char* userInput) {
    char buffer[10] = "Hello";
    // Safe usage with buffer size verification
    if (strlen(buffer) + strlen(userInput) < sizeof(buffer)) {
        strcat(buffer, userInput);
        printf("Buffer: %s\n", buffer);
    } else {
        printf("Input too long!\n");
    }
}

int main() {
    char userInput[20] = "World";  // Assume this is user input
    safeStrcpy(userInput);
    safeStrcat(userInput);
    return 0;
}
