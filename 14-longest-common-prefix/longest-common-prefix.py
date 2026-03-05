class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = min(strs, key=len)

        for i in range(len(shortest)):
            char = shortest[i]

            for word in strs:
                if word[i] != char:
                    return prefix
            prefix += char

        return prefix
                
        