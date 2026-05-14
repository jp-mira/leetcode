class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N = len(nums)
        count = Counter(nums)
        max_num = max(nums)

        if N != max_num + 1:
            return False

        for i in range(1, max_num):
            if count[i] != 1:
                return False
        
        if count[max_num] != 2:
            return False
        return True
                 

            

        