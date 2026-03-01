class Solution:
    def minPartitions(self, n: str) -> int:
        highest = 0
        for num in n:
            highest = max(highest, int(num))
        return highest

        