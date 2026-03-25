from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        prefix = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                prefix[i][j] = grid[i][j]

                if i > 0:
                    prefix[i][j] += prefix[i - 1][j]
                if j > 0:
                    prefix[i][j] += prefix[i][j - 1]
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i - 1][j - 1]

        for j in range(n - 1):
            left = prefix[m - 1][j]
            right = prefix[m - 1][n - 1] - left

            if left == right:
                return True

        for i in range(m - 1):
            up = prefix[i][n - 1]
            down = prefix[m - 1][n - 1] - up

            if up == down:
                return True

        return False