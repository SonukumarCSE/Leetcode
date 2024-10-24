class Solution:
    def get_max_proper(self,n1,n2):
        for i in range(2,n2+1):
            if n1 % i == 0:
                return i
        return -1
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > nums[i+1]:
                nums[i] = self.get_max_proper(nums[i],nums[i+1])
                if nums[i] == -1:
                    return -1
                ans += 1
        return ans 