class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0

        for number in nums:
            unique ^= number
        return unique




        