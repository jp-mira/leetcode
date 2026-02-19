class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        blocks = [1]
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                blocks[-1] += 1  
            else:
                blocks.append(1)  
        
        subStringCount = 0
        for i in range(1, len(blocks)):
            subStringCount += min(blocks[i], blocks[i-1])
        
        return subStringCount
