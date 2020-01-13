class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        if min(nums) > 0: return True
        res = []
        if nums[0] == 0: return False
        for i in range(len(nums)-1):
            if i == 0:
                res.append(nums[0])
            else:
                res.append(max(res[-1], nums[i] + i))
        return False if res[-1] < len(nums) -1 else True
	
