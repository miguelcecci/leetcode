#include<stdbool.h>
#include<stdlib.h>

bool checkBoundary(int row, int column, int maxRow, int maxCol) {
    return (row >= 0 && row < maxRow && column >= 0 && column < maxCol);
}

int countNeighbors(int** board, int row, int column, int maxRow, int maxCol){
    int neighbors = 0;
    for(int i = row-1; i <= row+1; ++i){
        for(int j = column-1; j <= column+1; ++j){
            if(checkBoundary(i, j, maxRow, maxCol) && !(i == row && j == column)){
                printf("i %d, j %d, board %d\n", i, j, board[i][j]);
                neighbors = neighbors+board[i][j];
            }
        }
    }
    printf("%d neighbors\n", neighbors);
    return neighbors;
}

void gameOfLife(int** board, int boardSize, int* boardColSize) {

    int** old_board = (int**)malloc(boardSize * sizeof(int*));
    for (int i = 0; i < boardSize; ++i) {
        old_board[i] = (int*)malloc(*boardColSize * sizeof(int));
    }
    
    for(int i = 0; i < boardSize; ++i){
        for(int j = 0; j < *boardColSize; ++j){
            old_board[i][j] = board[i][j];
        }
    }
    
    for(int i = 0; i < boardSize; ++i){
        for(int j = 0; j < *boardColSize; ++j){
            int nn = countNeighbors(old_board, i, j, boardSize, *boardColSize);
            printf(">pqp: %d\n", nn);
            if (nn < 2) {
                board[i][j] = 0;
            } else if (old_board[i][j] == 1 && nn > 3) {
                board[i][j] = 0;
            } else if (old_board[i][j] == 0 && nn == 3) {
                board[i][j] = 1;
            } else {
                board[i][j] = board[i][j]; // No change
            }
        }
    }
}
