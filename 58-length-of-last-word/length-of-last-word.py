class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        split = s.split()

        letter_count = [len(word) for word in split]
        s = letter_count[-1]

        return s


        