#include <stdlib.h>
#include <stdio.h>

void testMemory()
{
    int *arr = (int *)malloc(5);
    if (arr == NULL)
    {
        printf("Memory allocation failed\n");
        return;
    }

    int *ptr = arr + 10;
    *ptr = 20;

    arr[5] = 10;
    arr[-1] = 5;

    int *another_arr = (int *)malloc(10);
    if (another_arr == NULL)
    {
        printf("Memory allocation failed\n");
        free(arr);
        return;
    }

    another_arr[0] = 15;
    another_arr[9] = 25;

    free(arr);
    free(another_arr);
}

void anotherFunction()
{
    char *str = (char *)malloc(20);
    if (str == NULL)
    {
        printf("Memory allocation failed\n");
        return;
    }

    for (int i = 0; i < 30; i++)
    {
        str[i] = 'A';
    }

    free(str);
}

int main()
{
    testMemory();
    anotherFunction();
    return 0;
}
