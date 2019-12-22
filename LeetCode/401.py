class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return list("%d:%02d"%(i, j) for j in range(60) for i in range(12) if num == bin(i).count('1') + bin(j).count('1'))
