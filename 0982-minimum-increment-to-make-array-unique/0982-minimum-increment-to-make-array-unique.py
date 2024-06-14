class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        prev = nums[0]
        moves = 0
        for i in range(1,len(nums)):
            if nums[i] <= prev:
                moves += prev + 1 - nums[i]
                prev += 1
            else:
                prev = nums[i]
        return moves
        