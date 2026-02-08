class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convert the int to string
        s = str(x)

        #compare the string to the number but in reverse order using [::-1]
        return s == s[::-1]