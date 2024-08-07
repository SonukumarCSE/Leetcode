class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = None
        for i in range(len(nums)):
            if count == 0:
                count = 1
                ele = nums[i]
            elif ele == nums[i]:
                count += 1
            else:
                count -= 1
        count_e = 0
        for i in range(len(nums)):
            if nums[i] == ele:
                count_e += 1
        if count_e > len(nums) / 2:
            return ele
        return -1