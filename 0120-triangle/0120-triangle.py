class Solution:
    def __init__(self):
        self.memo = {}
    def solve(self,row,col,m,n,matrix):
        if (row,col) in self.memo:
            return self.memo[(row,col)]
        if row == m-1:
            return matrix[row][col]
        
        down = matrix[row][col] + self.solve(row+1,col,m,n,matrix)
        right = matrix[row][col] + self.solve(row+1,col+1,m,n,matrix)
        self.memo[(row,col)] = min(down,right)
        return self.memo[(row,col)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        n = len(triangle[m-1])
        return self.solve(0,0,m,n,triangle)
        