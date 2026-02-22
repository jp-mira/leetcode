class Solution:
    def binaryGap(self, n: int) -> int:
        maxGap = 0
        currentGap = -1
        binaryNumber = bin(n)[2:]

        for i, bit in enumerate(binaryNumber):
            if bit == '1':
                if currentGap != -1:
                    maxGap = max(maxGap, i - currentGap) 
                currentGap = i  
        
        return maxGap