class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left, right, blank = 0, 0, 0

        for move in moves:
            if move == 'L':
                left += 1
            elif move == 'R':
                right += 1
            else:
                blank += 1
        total = (left-right)
        return abs(total) + blank 
        