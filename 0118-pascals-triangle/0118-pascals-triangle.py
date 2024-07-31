class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_tria = []
        pascal_tria.append([1])
        if numRows == 1:
            return pascal_tria
        pascal_tria.append([1,1])
        if numRows == 2:
            return pascal_tria
        for i in range(2,numRows):
            arr = pascal_tria[i-1]
            # print(arr)
            num = []
            num.append(1)
            low = 0
            high = 1
            while high != len(arr):
                sum = arr[low] + arr[high]
                num.append(sum)
                low += 1
                high += 1
            num.append(arr[low])
            pascal_tria.append(num)
        return pascal_tria