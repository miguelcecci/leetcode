//dumbest problem ever, I was tired this day
int diagonalSum(int** mat, int matSize, int* matColSize) {
    int sum_acc = 0;
    for(int i = 0; i < matSize; i++){
      if(matSize % 2 != 0 && i == matSize/2){
        sum_acc = sum_acc + mat[i][i];
      } else {
        sum_acc = sum_acc + mat[i][i] + mat[i][matSize-i-1];
      }
    }
    return sum_acc;
}
