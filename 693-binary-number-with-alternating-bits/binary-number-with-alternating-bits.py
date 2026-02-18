class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        binaryNumber = bin(n)[2:]

        for i in range (len(binaryNumber)-1):
            if binaryNumber[i] == binaryNumber[i+1]:
                return False
        
        return True


      

        