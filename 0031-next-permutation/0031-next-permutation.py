class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        right = len(nums) - 1
        idx = -1
        for i in range(right,0,-1):
            if nums[i] > nums[i-1]:
                idx = i
                temp = i
                print(nums)
                print(temp)
                for j in range(i,len(nums)):
                    if nums[j] <= nums[temp] and nums[j] > nums[i-1]:
                        temp = j
                nums[temp], nums[i-1] = nums[i-1], nums[temp]
                print(nums)
                break
        if idx != -1:
            low = idx
            high = len(nums) - 1
            while low <= high:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

        if idx == -1:
            nums.reverse()
            return 
        
        

