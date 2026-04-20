class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors)
        max_distance = 0

        for i in range(N-1, -1, -1):
            if colors[0] != colors[i]:
                max_distance = max(max_distance, i)
        
        for j in range(N):
            if colors[N-1] != colors[j]:
                max_distance = max(max_distance, (N-1)-j)
        return max_distance
        