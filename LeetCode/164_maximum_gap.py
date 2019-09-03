# Given an unsorted array, find the maximum difference between the successive elements in its sorted form. 
# Return 0 if the array contains less than 2 elements.
# Example: [3, 6, 9, 1] return 3
import math

class CountingSort():
    def counting_sort(self, nums):
        m = min(nums)
        M = max(nums)
        k = M-m+1
        count = [0]*k
        for num in nums:
            count[num-m] += 1
        for i in range(1, k):
            count[i] += count[i-1]

        result = [0]*len(nums)
        for i in range(len(nums)):
            count[nums[i]-m] -= 1
            result[count[nums[i]-m]] = nums[i]

        return result

class RadixSort():
    def radix_sort(self, a, radix=10):
        K = int(math.ceil(math.log(max(a), radix))) # max index
        for i in range(1, K+2):
            bucket = [[] for i in range(radix)]
            for val in a:
                bucket[val%(radix**i)//(radix**(i-1))].append(val)
            del a[:]
            for each in bucket:
                a.extend(each)
        return a

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return int(0)
        if len(nums) == 2:
            return abs(nums[0]-nums[1])
        cs = RadixSort()
        nums = cs.radix_sort(nums)
        res = nums[1] - nums[0]
        print(nums)
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])

        return res

s = Solution()
l = [1,3,100]
print('nums:', l)
print('maxgap:', s.maximumGap(l))

