class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = sorted(nums)
        print(num)

        for i in range(1, len(nums)):
            if num[i] == num[i-1]:
                return True
        return False
