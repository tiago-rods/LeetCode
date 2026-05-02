#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* multiply(char* num1, char* num2) {
    int len1 = strlen(num1);
    int len2 = strlen(num2);
    
    if (num1[0] == '0' || num2[0] == '0') {
        char* res = malloc(2);
        res[0] = '0';
        res[1] = '\0';
        return res;
    }
    
    int* res = calloc(len1 + len2, sizeof(int));
    
    for (int i = len1 - 1; i >= 0; i--) {
        for (int j = len2 - 1; j >= 0; j--) {
            int m = (num1[i] - '0') * (num2[j] - '0');
            int p1 = i + j, p2 = i + j + 1;
            int sum = m + res[p2];
            res[p1] += sum / 10;
            res[p2] = sum % 10;
        }
    }
    
    // Remove zeros à esquerda
    int start = 0;
    while (start < len1 + len2 - 1 && res[start] == 0) start++;
    
    char* result = malloc(start + len1 + len2 - start + 1);
    for (int i = start; i < len1 + len2; i++) {
        result[i - start] = res[i] + '0';
    }
    result[len1 + len2 - start] = '\0';
    
    free(res);
    return result;
}