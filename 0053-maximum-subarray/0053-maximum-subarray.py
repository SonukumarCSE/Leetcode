class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        maxsum = nums[0] 
        sub_arr = []
        sub_arr.append(nums[0])
        for i in range(1,len(nums)):
            
            maxsum = max(maxsum + nums[i], nums[i])
            sub_arr.append(maxsum)
        print(maxsum)
        ans = float('-inf')
        for x in sub_arr:
            ans = max(ans,x)

        print(sub_arr)
        return ans