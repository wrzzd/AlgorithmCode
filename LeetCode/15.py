'''
3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3: return None
        res = []
        num_d = {}
        for n in nums:
            if n not in num_d:
                num_d[n] = 1
            else:
                num_d[n] += 1
        if 0 in num_d and num_d[0] >= 3:
            res.append([0, 0, 0])

        if nums[0] > 0 or nums[-1] < 0: return res
        p_num = [p for p in num_d if p > 0]
        n_num = [n for n in num_d if n < 0]

        for p in p_num:
            for n in n_num:
                now  = -(p + n)
                if now < p and now > n and now in num_d:
                    res.append([p, n, now])
                if now == p and num_d[p] > 1:
                    res.append([p, n, now])
                if now == n and num_d[n] > 1:
                    res.append([p, n, now])
        return res
