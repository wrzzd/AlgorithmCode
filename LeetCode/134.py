class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        minus = [a - b for a, b in zip(gas, cost)]
        if max(minus) < 0 or sum(minus) < 0: return -1
        bix = 0
        count = 0
        k = 0
        for i in range(2*len(minus)-1):
            count += minus[i%len(minus)]
            k += 1
            if count < 0:
                count = 0
                k = 0
            if k == len(minus): return (i+1) % len(minus)
        return -1
