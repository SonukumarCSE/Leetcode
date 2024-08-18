from typing import List

# class Solution:
#     def __init__(self):
#         self.memo = {}
    
#     def solve(self, idx, curr, prev, arr1, arr2):
#         if idx == len(arr1):  # Base case: Reached the end of the arrays
#             return curr
        
#         if (idx, prev) in self.memo:
#             return self.memo[(idx, prev)]
        
#         take = 0
#         if prev == 'a':
#             take += max(self.solve(idx + 1, curr + arr1[idx], 'a', arr1, arr2), 
#                         self.solve(idx + 1, curr, 'b', arr1, arr2))
#         elif prev == 'b':
#             take += max(self.solve(idx + 1, curr + arr2[idx], 'b', arr1, arr2), 
#                         self.solve(idx + 1, curr, 'a', arr1, arr2))
        
#         self.memo[(idx, prev)] = take
#         return take
    
#     def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
#         # Start from the first element of arr1 or arr2
#         a = self.solve(1, energyDrinkA[0], 'a', energyDrinkA, energyDrinkB)
#         b = self.solve(1, energyDrinkB[0], 'b', energyDrinkA, energyDrinkB)
#         return max(a, b)


class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        n = len(energyDrinkA)
        memo = {}
        def rec(i, prev):
            if i >= n:
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)] 
            
            t = 0
            if prev == 0:
                t = energyDrinkA[i] + max(rec(i + 1, 0), rec(i + 2, 1))
            if prev == 1:
                t = energyDrinkB[i] + max(rec(i + 1, 1), rec(i + 2, 0))
            memo[(i, prev)] = t
            return t
        return max(rec(0, 0),  rec(0, 1))