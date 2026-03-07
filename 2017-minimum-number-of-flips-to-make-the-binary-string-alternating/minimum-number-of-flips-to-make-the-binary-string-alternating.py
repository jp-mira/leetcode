class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        alt1, alt2 = "", ""

        for i in range(len(s)):
            alt1 += "0" if i % 2 else "1"
            alt2 += "1" if i% 2 else "0"
        
        res = len(s)
        diff1, diff2 = 0, 0
        l = 0
        for j in range(len(s)):
            if s[j] != alt1[j]:
                diff1 += 1
            if s[j] != alt2[j]:
                diff2 += 1

            if (j-l + 1) > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            if (j-l + 1) == n:
                res = min(res, diff1, diff2)
        return res
            



        