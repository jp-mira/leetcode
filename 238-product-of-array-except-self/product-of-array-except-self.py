class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        p = [0 for _ in range(N)]

        suffix = 1
        for i in range(N-1, -1, -1):
            p[i] = suffix
            suffix = (suffix * nums[i])

        prefix = 1
        for i in range(N):
            p[i] = (p[i] * prefix)
            prefix = (prefix * nums[i])
        return p



        