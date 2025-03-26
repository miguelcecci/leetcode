class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        0, 0 -> 2, 0
        0, 1 -> 2, 1
        0, 2 -> 2, 2 

        1, 1 -> 2, 1

        new value is 
        2, 1 -> 2, 2

        2, 2 -> 1, 2
        """

        for i in range(len(matrix)//2): #3 1 
            submatrix_upper_boundaries = len(matrix)-(1+i)
            sub = submatrix_upper_boundaries
            for j in range(i, sub):
                #this should recieve the value that will be overwritten
                #next x will be y - submatrix_upper_boundaries
                #next y will be x 

                # do real rotation
                # 0, 0 = 0, sub
                # 0, sub = sub, sub
                # sub, sub = sub, 0
                # sub, 0 = 0, 0

                buffer = matrix[i][j]
                matrix[i][j] = matrix[m-j][i]
                matrix[m-j][i] = matrix[m-i][m-j]
                matrix[m-i][m-j] = matrix[j][m-i]
                matrix[j][m-i] = buffer

