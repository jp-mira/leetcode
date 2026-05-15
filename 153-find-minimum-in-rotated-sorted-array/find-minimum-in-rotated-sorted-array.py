class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        min_num = nums[0]

        for i in range(1, N):
            if nums[i] < min_num:
                min_num = nums[i]
        return min_num
        