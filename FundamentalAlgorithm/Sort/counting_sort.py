class CountingSort():
    def counting_sort(self, a):
        m = min(a)
        M = max(a)
        k = M - m + 1
        c = [0]*k
        for i in a:
            c[i-m] += 1
        for i in range(1, len(c)):
            c[i] = c[i] + c[i-1]  # for c , c[i] means leq i number
        b = [0] * len(a)
        for i in range(len(a)-1, -1, -1):
            c[a[i]-m] -= 1
            b[c[a[i]-m]] = a[i] # a[i] locate at c[a[i]-m] 

        return b

cs = CountingSort()
l = [3,6,4,8,9,1]
print('befort sort:', l)
print('after sort:', cs.counting_sort(l))
