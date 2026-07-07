class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxPrice = 0
        while left < right:
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
            else:
                left = right
            right += 1
        maxProfit = max(profit, 0)
        return maxProfit
