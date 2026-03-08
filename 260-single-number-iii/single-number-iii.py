class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        unique = []
        counter = Counter(nums)

        for n, c in counter.items():
            if c == 1:
                unique.append(n)
        return unique
        