def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    numRows = len(grid)
    numColumns = len(grid[0])
    for i in range(0, numRows, 1):
        for j in range(0, numColumns, 1):
            if i == 0 and j == 0:
                pass
            elif i == 0:
                grid[i][j] += grid[i][j-1]
            elif j == 0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


L = [[1,2,3], [4,5,0], [7,0,9]]
print(minPathSum(L))
