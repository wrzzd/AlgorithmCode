class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = len(nums)
        if s <= 1:
            return s

        dp = [1]*s
        for i in range(1, s):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
