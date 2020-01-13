class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n < 2:
            return int(0)
        dp1 = [0 for _ in range(n)]
        dp2 = [0 for _ in range(n)]
        dp1[0] = -prices[0]
        for i in range(1, n):
            dp1[i] = max(dp1[i-1], dp2[i-1] - prices[i])
            dp2[i] = max(dp2[i-1], dp1[i-1] + prices[i] - fee)
        return dp2[n-1]
