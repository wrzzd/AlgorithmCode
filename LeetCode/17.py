class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2l = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z')
        }

        if len(digits) == 0: return None
        if len(digits) == 1: return list(d2l[int(digits)])
        res = []
        for l in d2l[int(digits[0])]:
            for c in self.letterCombinations(digits[1:]):
                res.append(l + c)
        return res
