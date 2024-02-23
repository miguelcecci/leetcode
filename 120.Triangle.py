class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        #we are going to iterate backwards
        #summing bottom the smallest next step
        #in the end the top of the piramid will
        #contain the result

        
        # len(triangle) - 2 because we are going to
        # start from the second to the last layer
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                min_step = min(triangle[i+1][j], triangle[i+1][j+1])
                triangle[i][j] = triangle[i][j] + min_step

        return triangle[0][0]

