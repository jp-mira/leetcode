class Solution:
    def judgeCircle(self, moves: str) -> bool:
        right, left, up, down = 0, 0, 0, 0

        for move in moves:
            if move == "R":
                right += 1
            elif move == "L":
                left += 1
            elif move == "U":
                up += 1
            else:
                down += 1
        return left == right and up == down 
        