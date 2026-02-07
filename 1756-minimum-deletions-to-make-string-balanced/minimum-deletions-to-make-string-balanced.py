class Solution:
    #minimum deletions to make string balanced
    def minimumDeletions(self, s: str) -> int:
        res = 0
        count = 0

        for i in s:
            if i == 'b':
                count += 1
            elif count > 0:
                res += 1
                count -= 1
        return res
        