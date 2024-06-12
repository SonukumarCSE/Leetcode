class Solution:
    def __init__(self):
        self.memo = {}
    def solve(self,row,col,m,n,matrix):
        if (row,col) in self.memo:
            return self.memo[(row,col)]
        if row < 0 or col < 0 or col >= n or row >= m:
            return float('inf')
        if row == 0:
            return matrix[0][col]
        up_left = self.solve(row-1,col-1,m,n,matrix)
        up = self.solve(row-1,col,m,n,matrix)
        up_right = self.solve(row-1,col+1,m,n,matrix)
        self.memo[(row,col)] = matrix[row][col] + min(up_left,up,up_right)
        return self.memo[(row,col)]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        min_path = float('inf')
        for i in range(n):
            min_path = min(min_path,self.solve(m-1,i,m,n,matrix))
        return min_path