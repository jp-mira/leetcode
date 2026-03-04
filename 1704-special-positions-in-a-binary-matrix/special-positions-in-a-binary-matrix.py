class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        #rows
        M = len(mat)
        #cols
        N = len(mat[0])

        #counter
        row_count = [0] * M
        col_count = [0] * N

        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1:
                    #counting of number of 1s in columns and rows
                    row_count[i] += 1
                    col_count[j] += 1

        special = 0
        
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special += 1
        return special
        