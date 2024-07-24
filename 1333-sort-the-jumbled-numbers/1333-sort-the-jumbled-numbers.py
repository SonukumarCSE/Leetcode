class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        minHeap = []
        ans = []
        for i in range(len(nums)):
            temp = list(str(nums[i]))
            for j in range(len(temp)):
                temp[j] = str(mapping[int(temp[j])])
            temp2 = int(''.join(temp))
            heapq.heappush(minHeap,[temp2,i])
        for i in range(len(minHeap)):
            temp = heapq.heappop(minHeap)
            ans.append(nums[temp[1]])
        return ans