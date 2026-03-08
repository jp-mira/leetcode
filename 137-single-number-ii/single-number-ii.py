class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for n, c in counter.items():
            if c == 1:
                return n


        