/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

#include <stdbool.h>
#include <math.h>

bool is_inbounds(int imgSize, int *imgColSize, int x, int y) {
    return (y >= 0 && y < *imgColSize && x >= 0 && x < imgSize);
}

int get_average_for(int** img, int imgSize, int* imgColSize, int x, int y){
    int pixel_counter = 0;
    int pixel_sum = 0;
    for(int i = x-1; i <= x+1; i++){
        for(int j = y-1; j <= y+1; j++){
            if(is_inbounds(imgSize, imgColSize, i, j)){
                pixel_sum += img[i][j];
                pixel_counter++;
            }
        }
    }

    return (int)floor(((float)pixel_sum)/pixel_counter);
}

int** imageSmoother(int** img, int imgSize, int* imgColSize, int* returnSize, int** returnColumnSizes) {

    int **result = (int **)malloc(imgSize*sizeof(int *));
    for(int i = 0; i < imgSize; i++){
        result[i] = (int *)malloc(*imgColSize*sizeof(int));
    }

    for(int i = 0; i < imgSize; i++){
        for(int j = 0; j < *imgColSize; j++){
            printf("%d", j);
            result[i][j] = get_average_for(img, imgSize, imgColSize, i, j);
        }
    }

    *returnSize = imgSize;
    *returnColumnSizes = (int *)malloc(imgSize * sizeof(int));
    for(int i = 0; i < imgSize; i++){
        (*returnColumnSizes)[i] = *imgColSize;
    }
    return result;
    
}
