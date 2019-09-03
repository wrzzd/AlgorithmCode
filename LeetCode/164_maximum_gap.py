# Given an unsorted array, find the maximum difference between the successive elements in its sorted form. 
# Return 0 if the array contains less than 2 elements.
# Example: [3, 6, 9, 1] return 3

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return int(0)

