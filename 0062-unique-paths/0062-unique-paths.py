class Solution:
    def __init__(self):
        self.memo = {}
    def solve(self,row,col,m,n):
        if (row,col) in self.memo:
            return self.memo[(row,col)]
        if row == 0 and col == 0:
            return 1
        if row < 0 or row >= m or col < 0 or col >= n:
            return 0
        up = self.solve(row-1,col,m,n)
        left = self.solve(row,col-1,m,n)
        self.memo[(row,col)] = up + left
        return self.memo[(row,col)]
    def uniquePaths(self, m: int, n: int) -> int:
        
        return self.solve(m-1,n-1,m,n)