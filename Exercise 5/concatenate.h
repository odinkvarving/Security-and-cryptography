#pragma once
#include<stdio.h>
#include <string.h>
#include <malloc.h>
#include <stdlib.h>

const char first[] = "&amp;";
const char second[] = "&lt;";
const char third[] = "&gt;";

int append(char buffer[], const char *encoding, int index, int offset) {
    
    for(int i = 0; i < (int)strlen(encoding); i++) {
        buffer[index + offset] = encoding[i];
        offset++;
    }
    return --offset;
}

char *replace(char string[]) {

    if(strcmp(string, "")) {
        return "";
    }

    int offset = 0;
    
    char *buffer = malloc(5 * strlen(string) * sizeof(char) + 1);

    for(int i = 0; i < (int)strlen(string); i++) {
       
        if(string[i] == '&') {
            offset = append(buffer, first, i, offset);
        }
        else if(string[i] == '<') {
            offset = append(buffer, second, i, offset);
        }
        else if(string[i] == '>') {
            offset = append(buffer, third, i, offset);
        }
        else {
            buffer[i + offset] = string[i];
        }
    }
    char *final = buffer;
    
    free(buffer);
    
    return final;
}
