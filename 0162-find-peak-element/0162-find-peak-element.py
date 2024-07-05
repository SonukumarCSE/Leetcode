class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx = -1
        if len(nums) == 1:
            return 0
        for i in range(0,len(nums)):
            if i == 0 and nums[i] > nums[i+1]:
                idx = i
                continue
            if i == len(nums)-1 and nums[i] > nums[i-1]:
                idx = i
                break
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                idx = i
        return idx