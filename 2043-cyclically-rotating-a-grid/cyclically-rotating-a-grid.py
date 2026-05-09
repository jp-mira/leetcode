class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        N = len(grid)
        M = len(grid[0])

        layers = min(N, M) // 2

        for layer in range(layers):

            arr = []

            top = layer
            bottom = N - layer - 1
            left = layer
            right = M - layer - 1

            # top
            for j in range(left, right + 1):
                arr.append(grid[top][j])

            # right
            for i in range(top + 1, bottom):
                arr.append(grid[i][right])

            # bottom
            for j in range(right, left - 1, -1):
                arr.append(grid[bottom][j])

            # left
            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            # rotate
            rotate = k % len(arr)
            arr = arr[rotate:] + arr[:rotate]

            idx = 0

            # put back top
            for j in range(left, right + 1):
                grid[top][j] = arr[idx]
                idx += 1

            # put back right
            for i in range(top + 1, bottom):
                grid[i][right] = arr[idx]
                idx += 1

            # put back bottom
            for j in range(right, left - 1, -1):
                grid[bottom][j] = arr[idx]
                idx += 1

            # put back left
            for i in range(bottom - 1, top, -1):
                grid[i][left] = arr[idx]
                idx += 1

        return grid