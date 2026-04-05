class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = Counter(moves)
        if count['U'] == count['D'] and count['L'] == count['R']:
            return True
        return False

        