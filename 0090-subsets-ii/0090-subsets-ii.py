class Solution:
    def solve(self,nums,idx,curr):
        if idx == len(nums):
            if curr not in self.ans:
                self.ans.append(curr)
            return 
        op1 = curr.copy()
        op2 = curr.copy()
        op2.append(nums[idx])
        self.solve(nums,idx+1,op2)
        self.solve(nums,idx+1,op1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        self.solve(nums,0,[])
        return sorted(self.ans)