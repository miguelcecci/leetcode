/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rowAndMaximumOnes(int** mat, int matSize, int* matColSize, int* returnSize){
    int* return_values = (int*)malloc(2*sizeof(int));

    return_values[0] = 0;
    return_values[1] = 0;

    for(int i = 0; i < matSize; i++){
        int current_column_counter = 0;
        for(int j = 0; j < *matColSize; j++){
            current_column_counter = current_column_counter + mat[i][j];
        }
        if(current_column_counter > return_values[1]){
            return_values[0] = i;
            return_values[1] = current_column_counter;
        }
    }

    *returnSize = 2;
    return return_values;

}
