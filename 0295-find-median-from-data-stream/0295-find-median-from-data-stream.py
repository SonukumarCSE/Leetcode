import heapq

class MedianFinder:
    def __init__(self):
        self.left_max_heap = []  # Max heap (invert values to use with min heap)
        self.right_min_heap = []  # Min heap

    def addNum(self, num: int) -> None:
        if not self.left_max_heap or num < -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -num)  # Push negative value to simulate max heap
        else:
            heapq.heappush(self.right_min_heap, num)

        # Always maintain left_max_heap size one greater than right_min_heap size
        # or both heaps' sizes equal
        if len(self.left_max_heap) > len(self.right_min_heap) + 1:
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        elif len(self.left_max_heap) < len(self.right_min_heap):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

    def findMedian(self) -> float:
        if len(self.left_max_heap) == len(self.right_min_heap):
            # Even number of elements
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2.0
        # Odd number of elements
        return -self.left_max_heap[0]

# Example usage:
# medianFinder = MedianFinder()
# medianFinder.addNum(1)
# medianFinder.addNum(2)
# print(medianFinder.findMedian())  # Output: 1.5
# medianFinder.addNum(3)
# print(medianFinder.findMedian())  # Output: 2
