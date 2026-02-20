class Solution:
    """
    The algorithm recursively decomposes the special binary string into its outermost balanced components ("mountains"), processes their inner contents to make them lexicographically largest, and then sorts these components in descending order to achieve the maximum possible string through valid swaps. This works because special binary strings are equivalent to valid parentheses sequences, where swapping adjacent balanced substrings corresponds to reordering these components.
    """
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 0:
            return s
        
        balance = 0
        ptr = 0
        mountains = []

        for idx, ch in enumerate(s):
            if ch == '1':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                #'1{}0': 1 - ptr/ 0 - idx. Big mountain can consits from multiple smaller mountains
                mountains.append('1{}0'.format(self.makeLargestSpecial(s[ptr+1:idx])))
                ptr = idx + 1
        
        mountains.sort(reverse=True)

        return ''.join(mountains)