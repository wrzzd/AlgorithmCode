'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        j = 1
        if len(nums) <= 1:
            return sum(nums)
        res = sum(nums[:j])
        now_res = res
        print(res)
        while j < len(nums):
            if now_res < 0:
                now_res = nums[j]
                j += 1
            else:
                now_res = now_res + nums[j]
                j += 1
            res = max(res, now_res)
            
        return res
