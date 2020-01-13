class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        res = 0
        ix = 0
        lg = len(g)
        for e in s:
            if ix < lg and e >= g[ix]:
                res += 1
                ix += 1
        return res
