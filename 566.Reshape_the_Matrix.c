#include <stdio.h>
#include <stdlib.h>

//I know that this code is terrible, the matrix coordinates are reversed
//
typedef struct {
    int x;
    int y;
} point;

point returnNextPosition(int cX, int cY, int mX, int mY) {
    point pair = {cX, cY};
    if (cY == mY-1) {
        pair.y = 0;
        pair.x = cX + 1;
    } else {
        pair.y = cY + 1;
    }
    return pair;
}

int** matrixReshape(int** mat, int matSize, int* matColSize, int r, int c, int* returnSize, int** returnColumnSizes) {

    point current_step = {0, -1};

    if(matSize*(*matColSize) != r*c){
        *returnSize = matSize;
        *returnColumnSizes = matColSize;
        return mat;
    }

    int** matrix = (int**)malloc(r * sizeof(int*));
    for (int i = 0; i < r; i++) {
        matrix[i] = (int*)malloc(c * sizeof(int));
    }

    for (int i = 0; i < matSize; ++i) {
        for (int j = 0; j < *matColSize; ++j) {
            current_step = returnNextPosition(current_step.x, current_step.y, r, c);
            printf("x: %d, y: %d, mat: %d \n", current_step.x, current_step.y, mat[i][j]);
            matrix[current_step.x][current_step.y] = mat[i][j];
        }
    }

    *returnSize = r;
    
    *returnColumnSizes = (int*)malloc(r * sizeof(int));
    for (int i = 0; i < r; i++) {
        (*returnColumnSizes)[i] = c;
    }

    return matrix;
}

