class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []
        for i in range(n):
            nums.append(i+1)
        idx = 0
        while len(nums) != 1:
            idx = (idx + k - 1) % len(nums)
            nums.remove(nums[idx])
        return nums[0]