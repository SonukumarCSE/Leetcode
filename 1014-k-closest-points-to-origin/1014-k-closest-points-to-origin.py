class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist,x,y))
        heapq.heapify(minHeap)
        # print(minHeap)
        ans = []
        for i in range(k):
            dixt,x,y = heapq.heappop(minHeap)
            ans.append([x,y])
        return ans

