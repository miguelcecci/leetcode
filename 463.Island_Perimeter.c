#include <stdbool.h>
#include <stdlib.h>

int is_border(int current, int compared){
    if(current == compared) {
        return 0;
    }
    return 1;
}

int** addPadding(int **matrix, int originalRows, int originalCols) {
    int newRows = originalRows + 2;
    int newCols = originalCols + 2;

    int **paddedMatrix = (int **)malloc(newRows * sizeof(int *));
    for (int i = 0; i < newRows; i++) {
        paddedMatrix[i] = (int *)malloc(newCols * sizeof(int));
    }

    for (int i = 0; i < newRows; i++) {
        for (int j = 0; j < newCols; j++) {
            paddedMatrix[i][j] = 0;
        }
    }

    for (int i = 0; i < originalRows; i++) {
        for (int j = 0; j < originalCols; j++) {
            paddedMatrix[i + 1][j + 1] = matrix[i][j];
        }
    }

    return paddedMatrix;
}

int islandPerimeter(int** grid, int gridSize, int* gridColSize) {
    
    int **p = addPadding(grid, gridSize, *gridColSize);
    
    int border_count = 0;
    //iterating gridSize + 1(after padding)
    for(int i = 0; i < gridSize+1; i++){
        for(int j = 0; j < *gridColSize+1; j++){
            border_count = border_count + 
                is_border(p[i][j], p[i+1][j]) + 
                is_border(p[i][j], p[i][j+1]);
        }
    }

    return border_count;
}
