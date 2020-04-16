class Solution:
    def detectCapitalUse(self, word: str) -> bool:        
        if len(word) <= 1: return True
        if word[0] < 'a':
            if word[1] < 'a':
                for char in word[2:]:
                    if char >= 'a': return False
                return True
            else:
                for char in word[2:]:
                    if char < 'a': return False
                return True

        else:
            for i in range(1, len(word)):
                if word[i] < 'a': return False
            return True
