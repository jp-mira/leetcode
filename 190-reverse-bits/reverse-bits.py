class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)[2:].zfill(32)

        reverse_binary = binary_num[::-1]
        return int(reverse_binary, 2)


        