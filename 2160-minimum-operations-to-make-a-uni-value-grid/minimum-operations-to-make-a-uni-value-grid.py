class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        num_array = []
        result = 0

        for row in grid:
            for num in row:
                num_array.append(num)
        
        num_array.sort()
        length = len(num_array)
        final_common_number = num_array[length//2]

        for number in num_array:
            if number % x != final_common_number % x:
                return -1
            result += abs(final_common_number - number) // x
        return result
        