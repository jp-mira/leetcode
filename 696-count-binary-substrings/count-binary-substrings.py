class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, curr = 0, 1
        ans = 0
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                curr += 1
            else:
                ans += min(prev, curr)
                prev, curr = curr, 1
        
        ans += min(prev, curr)
        return ans