class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1: return [nums]
        res = []
        for i in range(len(nums)):
            if i == 0:
                temp = nums[1:]
            elif i == len(nums) -1:
                temp = nums[0:len(nums) - 1]
            else:
                temp = nums[0:i] + nums[i+1:]
            # temp = 
            res += [[nums[i]] + item for item in self.permute(temp)]
        return res
