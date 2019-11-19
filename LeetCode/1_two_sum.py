'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_d = {}
        if len(nums) < 2:
            return None
        index_d[nums[0]] = 0
        for i in range(1, len(nums)):
            if target - nums[i] in index_d:
                return [index_d[target - nums[i]], i]
            else:
                index_d[nums[i]] = i
        return None
