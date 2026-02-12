class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0 

        for numbers in nums:
            unique ^= numbers

        return unique
        

   




        