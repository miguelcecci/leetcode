class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def get_valid_adjascent_points(y, x, grid):
            points = [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]
            result = []
            for p in points:
                if 0 <= p[0] < len(grid[0]):
                    if 0 <= p[1] < len(grid):
                        result.append(p)
            return result

        def clear_island(y, x, grid):
            if grid[y][x] == "1":
                grid[y][x] = "0"
                for i in get_valid_adjascent_points(y, x, grid):
                    clear_island(i[1], i[0], grid)

        
        island_count = 0
        #iterate over the matrix
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    island_count = island_count + 1
                    clear_island(y, x, grid)

        return island_count

