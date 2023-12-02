/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isSelfDividing(int number_as_int) {
    char str[10000];
    sprintf(str, "%d", number_as_int);

    for(int i = 0; str[i] != '\0'; ++i){
        if(str[i] == '0'){
            return false;
        }
        if(number_as_int % (str[i]-'0') != 0){
            return false;
        }
    }
    return true;
}
int* selfDividingNumbers(int left, int right, int* returnSize) {

    int* putz;
    int range_size = right - left + 1;
    
    putz = (int *)malloc(range_size*sizeof(int));
    int putz_counter = 0;

    for(int i = left; i <= right; ++i){
        if(isSelfDividing(i)){
            putz[putz_counter] = i;
            putz_counter += 1;
        }
    }

    *returnSize = putz_counter;

    return putz;
}
