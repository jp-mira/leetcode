class Solution:
    def bitwiseComplement(self, n: int) -> int:
        complement = ""
        bit = bin(n)[2:]
        for char in str(bit):
            if char == "0":
                complement += "1"
            else:
                complement += "0"
        
        return int(complement, 2)
                
        

        