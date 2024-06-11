class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = 1
        f1 = 1
        if n == 1:
            return f0
        for i in range(2,n+1):
            f3 = f1 + f0
            f0 = f1
            f1 = f3
        return f1
