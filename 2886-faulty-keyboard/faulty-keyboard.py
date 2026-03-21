class Solution:
    def finalString(self, s: str) -> str:
        output = ""

        for i in range(len(s)):
            if s[i] != "i":
                output += s[i]
            else:
                output = output[::-1]
        return output

        