class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = defaultdict()
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in count:
                return [i,count[diff]]
            count[nums[i]] = i
            

           
              
   