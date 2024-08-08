class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = None
        cand2 = None
        life1 = 0
        life2 = 0
        for i in range(len(nums)):
            if life1 == 0 and nums[i] != cand2:
                cand1 = nums[i]
                life1 = 1
            elif life2 == 0 and nums[i] != cand1:
                cand2 = nums[i]
                life2 = 1
            elif nums[i] == cand1:
                life1 += 1
            elif nums[i] == cand2:
                life2 += 1
            else:
                life1 -= 1
                life2 -= 1
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i] == cand1:
                count1 += 1
            elif nums[i] == cand2:
                count2 += 1
        ans = []
        if count1 > len(nums)/3:
            ans.append(cand1)
        if count2 > len(nums)/3:
            ans.append(cand2)
        return ans