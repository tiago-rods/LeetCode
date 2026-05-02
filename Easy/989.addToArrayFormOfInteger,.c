/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* addToArrayForm(int* num, int numSize, int k, int* returnSize) {
   int maxSize = numSize + 32;  // Limite seguro para carry
    int* result = (int*)malloc(maxSize * sizeof(int));
    
    int carry = k;
    int i = numSize - 1;
    int resIdx = 0;
    
    while (i >= 0 || carry > 0) {
        if (i >= 0) {
            carry += num[i--];
        }
        result[resIdx++] = carry % 10;
        carry /= 10;
    }
    
    *returnSize = resIdx;
    
    for (int j = 0; j < resIdx / 2; j++) {
        int temp = result[j];
        result[j] = result[resIdx - 1 - j];
        result[resIdx - 1 - j] = temp;
    }
    
    return result;
}