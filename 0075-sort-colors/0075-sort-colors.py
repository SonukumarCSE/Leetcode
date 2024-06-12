class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        j = -1
        k = -1
        for m in range(len(nums)):
            if nums[m] == 2:
                k += 1
            elif nums[m] == 1:
                nums[j+1],nums[m] = nums[m] , nums[j+1]
                j += 1
            elif nums[m] == 0:
                nums[j+1],nums[m] = nums[m], nums[j+1]
                k += 1
                j += 1
                nums[i+1],nums[j] = nums[j],nums[i+1]
                i += 1