#include "concatenate.h"
#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    
    char input[100];

    printf("Enter a string: \n");

    scanf("%s", input);

    char *result = replace(input);

    printf("\n Result: \n%s\n", result);

    free(result);

    return 0;
}