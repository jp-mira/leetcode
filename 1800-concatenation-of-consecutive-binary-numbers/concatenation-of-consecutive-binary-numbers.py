class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binary = []
        for i in range(1, n+1):
            binary.append(bin(i)[2:])

        concatenate = "".join(binary)
        decimal = int(concatenate, 2)

        return decimal % (10**9 + 7)