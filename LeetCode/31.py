'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        while i > -len(nums):
            if nums[i-1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] <= nums[i-1]: continue
                    else: break
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
            else:
                i -= 1
        if i == -len(nums):
            nums = sorted(nums)
