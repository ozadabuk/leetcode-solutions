class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for c in accounts:
            moneySum = 0
            for m in c:
                moneySum = moneySum + m
            if moneySum > maxWealth:
                maxWealth = moneySum
        return maxWealth