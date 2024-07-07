class Solution:
    def maximumPoints(self, arr: List[int], curr: int) -> int:
        arr.sort()
        start = 0
        end = len(arr) - 1
        point = 0
        
        while start <= end:
            if arr[start] <= curr:
                point += curr // arr[start]
                curr = curr % arr[start]
            elif point > 0:
                curr += arr[end]
                end -= 1
            else:
                break
        return point