class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #cloning the board
        clone = []
        for i in board:
            line = []
            for j in board[0]:
                line.append('X')
            clone.append(line)
        
        def get_valid_neighbors(x, y, matx):
            possible = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            valid = []

            for i in possible:
                if i[0] >= 0  and i[0] < len(matx[0])  and i[1] >= 0 and i[1] < len(matx):
                    valid.append(i)
            
            return valid

        def recursive_neighbor_search(x, y, board, clone):
            if board[y][x] == 'O' and clone[y][x] == 'X':
                clone[y][x] = 'O'
                for np in get_valid_neighbors(x, y, board):
                    recursive_neighbor_search(np[0], np[1], board, clone)

        recursive_neighbor_search(0, 0, board, clone)
        #applying recursive neighbor search in board perimeter
        for i in range(len(board[0])):
            recursive_neighbor_search(i, 0, board, clone)
            recursive_neighbor_search(i, len(board)-1, board, clone)
        
        for i in range(len(board)):
            recursive_neighbor_search(0, i, board, clone)
            recursive_neighbor_search(len(board[0])-1, i, board, clone)
        
        # when i started the problem I was no aware that
        # should overwrite board variable.
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = clone[i][j]

        return clone
