import math

class RadixSort():
    def radix_sort(self, a, radix=10):
        K = int(math.ceil(math.log(max(a), radix))) # max index
        for i in range(1, K+1):
            bucket = [[] for i in range(radix)]
            for val in a:
                bucket[val%(radix**i)//(radix**(i-1))].append(val)
            del a[:]
            for each in bucket:
                a.extend(each)
        return a

rs = RadixSort()
l = [0, 2, 245, 60, 5, 23, 24, 18, 49, 36]
print('before:', l)
print('after:', rs.radix_sort(l))
