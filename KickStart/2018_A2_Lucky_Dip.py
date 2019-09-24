class LuckyDip():
    def cal2(self, a, b, p, n):
        return a*(1 - p**n) + p**n * b

    def lucky_dip(self, v, k):
        n = len(v)
        v.sort(reverse=True)
        mid = self.cal2(v[-2], v[-1], 1/2, k+1)
        for i in range(3, n+1):
            mid = self.cal2(v[-i], mid, (i-1)/i, k+1)
        return mid

ld = LuckyDip()
v = [16, 11, 7, 4, 1]
k = 3
print(ld.lucky_dip(v, k))
