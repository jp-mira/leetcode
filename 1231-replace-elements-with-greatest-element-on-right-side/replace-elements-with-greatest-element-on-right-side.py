class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = -float('inf')
        output = []
        N = len(arr)

        for i in range(N-1, -1, -1):
            if i == N-1:
                output.append(-1)
            else:
                output.append(max_value)
            max_value = max(max_value, arr[i])
        return output[::-1]
        