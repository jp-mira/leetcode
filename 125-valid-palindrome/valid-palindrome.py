class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return True

        s = "".join(c.lower() for c in s if c.isalnum())
        if s == s[::-1]:
            return True
        return False
        