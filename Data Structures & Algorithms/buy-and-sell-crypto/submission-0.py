class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxPrice = 0
        while left < right:
            if price[left] < price[right]:
                profit = price[right] - price[left]
            else:
                left = right
            right += 1
        maxProfit = max(profit, 0)
