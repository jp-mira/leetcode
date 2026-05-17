class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = set()

        def dfs(i):
            # outside of the array
            if i<0 or i>=N:
                return False

            # already visited
            if i in visited:
                return False
            
            # found zero
            if arr[i] == 0:
                return True
            
            visited.add(i)

            jump = arr[i] 

            return dfs(i + jump) or dfs(i - jump)

        return dfs(start)
        