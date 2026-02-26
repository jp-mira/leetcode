class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        binary_number = int(s, 2)

        while binary_number != 1:
            if binary_number % 2 == 0:
                binary_number //= 2
            else:
                binary_number += 1
            steps += 1
        return steps

                


