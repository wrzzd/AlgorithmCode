'''
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.



Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
'''
class Solution:
    def numPermsDISequence(self, S):
        n = len(S)
        M = 1e9 + 7
        dp = [[int(0)]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(0, i+1):
                if S[i-1] == 'D':
                    for k in range(j, i):
                        dp[i][j] = int((dp[i][j] + dp[i-1][k]) % M)
                else:
                    for k in range(0, j):
                        dp[i][j] = int((dp[i][j] + dp[i-1][k]) % M)
        
        res = 0
        for i in range(0, n+1):
            res = int((res + dp[n][i]) % M)

        return res

S = 'DID'
sl = Solution()
print(sl.numPermsDISequence(S))
         
