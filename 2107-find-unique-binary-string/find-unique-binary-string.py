class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        unique = ""

        for i in range(len(nums)):
            char = nums[i][i]
            unique += "1" if char == "0" else "0"
        
        return unique

        