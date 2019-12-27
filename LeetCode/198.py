class Solution:
    def rob(self, nums: List[int]) -> int:
        res = []
        if not nums: return int(0)
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            res.append(nums[0])
            res.append(max(nums[0], nums[1]))
            for i in range(2, len(nums)):
                res.append(max(nums[i] + res[-2], res[-1]))
            
            return res[-1]
