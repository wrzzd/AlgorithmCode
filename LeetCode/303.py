class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for i in nums:
            self.sums.append(i + self.sums[-1])

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
