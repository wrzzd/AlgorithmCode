class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return int(0)
        if len(prices) == 2:
            return max(0, prices[1] - prices[0])
        for i in range(1, len(prices)):
            if prices[i] <= prices[i-1]:
                continue
            else:
                break
        prices = prices[i-1:]
        if prices[1] <= prices[0]:
            return self.maxProfit(prices[1:])
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                break
        if i == len(prices)-1:
            if prices[i] < prices[i-1]:
                return prices[i-1] - prices[0] + self.maxProfit(prices[i:])
            else:
                return prices[i] - prices[0]
        else:
            return prices[i-1] - prices[0] + self.maxProfit(prices[i:])


