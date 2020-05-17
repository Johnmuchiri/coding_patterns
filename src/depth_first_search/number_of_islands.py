from typing import List

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        h = len(grid)
        l = len(grid[0])
        for i in range(h):
            for j in range(l):
                if grid[i][j] == "1":
                    count += 1
                    self._bfs(grid, i, j)
        return count

    def _bfs(self, grid, i, j):
        h = len(grid)
        l = len(grid[0])
        if not grid:
            return
        queue = [(i, j)]
        while len(queue) > 0:
            row, col = queue.pop(0)
            if row < 0 or col < 0 or row > l or col > h or grid[row][col] == "0":
                continue
            grid[row][col] = "0"



grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
sol = Solution()
print(sol.numIslands(grid))
