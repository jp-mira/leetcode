class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        currentWealth = 0
        for customer in accounts:
            currentWealth = 0
            for bank in customer:
                currentWealth += bank
            maxWealth = max(maxWealth, currentWealth)
        return maxWealth


        