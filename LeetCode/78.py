class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums, []]
        res = []
        # for item in self.subsets(nums[1:]):
        res += [[nums[0]] + s for s in self.subsets(nums[1:])]
        res += self.subsets(nums[1:])
        return res
