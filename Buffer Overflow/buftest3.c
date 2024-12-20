#include <stdio.h>

void unsafeGets() {
    char buffer[10];
    // Unsafe usage of gets
    gets(buffer);
    printf("Buffer: %s\n", buffer);
}

int main() {
    unsafeGets();
    return 0;
}
