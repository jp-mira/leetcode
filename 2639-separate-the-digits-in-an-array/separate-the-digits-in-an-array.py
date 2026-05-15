class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []

        for ch in nums:
            for num in str(ch):
                ans.append(int(num))
        return ans

        