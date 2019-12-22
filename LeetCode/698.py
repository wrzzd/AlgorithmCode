class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0: return False
        if k == 1: return True
        avg = s//k
        nums.sort(reverse=True)
        n = len(nums)
        if n < k: return False
        visited = set()
        def dfs(k, tmp_sum, loc):
            if tmp_sum == avg:
                return dfs(k-1, 0, 0)
            if k == 1:
                return True

            for i in range(loc, n):
                if i not in visited and nums[i] + tmp_sum <= avg:
                    visited.add(i)
                    if dfs(k, tmp_sum + nums[i], i+1):
                        return True
                    visited.remove(i)
            return False
        return dfs(k, 0, 0)
