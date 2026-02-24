class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0
        binary = bin(n)[2:]

        for i in range(len(binary)):
            if binary[i] == '1':
                bits+=1
        
        return bits

        