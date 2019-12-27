class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return int(1)
        if n == 2: return int(2)
        res = [1,2]
        for i in range(3, n+1):
            res.append(res[-1]+res[-2])
        return res[-1]
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
