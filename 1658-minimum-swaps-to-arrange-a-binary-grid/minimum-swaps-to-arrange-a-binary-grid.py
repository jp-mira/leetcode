class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)

        rows = []
        for i in range(N):
            farthest = -1
            for j in range(N):
                if grid[i][j] == 1:
                    farthest = j
            rows.append(farthest)

        count = 0
        for i in range(N):
            for j in range(len(rows)):
                if rows[j] <= i: 
                    count += j
                    rows = rows[:j] + rows[j + 1:] 
                    break
            else:
                return -1
        return count