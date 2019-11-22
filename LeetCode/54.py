'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return None
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if m == 2:
            matrix[-1].reverse()
            return matrix[0] + matrix[-1]
        if n == 1:
            return [a[0] for a in matrix]
        if n == 2:
            return matrix[0] + [a[-1] for a in matrix[1:]] \
            + [matrix[i][0] for i in range(len(matrix) - 1, 0, -1)] 
            
        res = matrix[0]
        for i in range(1, m-1):
            res.append(matrix[i][-1])
        matrix[-1].reverse()
        res += matrix[-1]
        for i in range(m-2, 0, -1):
            res.append(matrix[i][0])
        
        return res + self.spiralOrder([a[1:-1] for a in matrix[1:-1]])
