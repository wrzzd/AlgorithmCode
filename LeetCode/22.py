class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return ['']
        elif n == 1:
            return ['()']
        elif n == 2:
            return ['()()', '(())']
        else:
            res = []
            for i in range(n):
                j = n - 1-i
                front = self.generateParenthesis(i)
                end = self.generateParenthesis(j)
                res.extend([f'({p}){q}' for p in front for q in end])
            return res
