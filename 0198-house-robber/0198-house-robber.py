class Solution:
    def __init__(self):
        self.memo = {}
    def solve(self,nums,n):
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n in self.memo:
            return self.memo[n]
        take = self.solve(nums,n-2) + nums[n-1]
        not_take = self.solve(nums,n-1)
        self.memo[n] = max(take,not_take)
        return self.memo[n]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return self.solve(nums,n) 