class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # for x in nums:
        #     heapq.heappush(self.minHeap,x)
        #     if len(self.minHeap) > k:
        #         heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        # print(self.minHeap)
        heapq.heappush(self.minHeap,val)
        if len(self.minHeap)  > self.k:
            heapq.heappop(self.minHeap)
        
        # print(self.minHeap)
        return self.minHeap[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)