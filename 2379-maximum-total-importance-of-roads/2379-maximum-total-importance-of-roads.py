class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0]  * n
        for u, v in roads:
            count[u] += 1
            count[v] += 1
        count.sort()
        print(count)
        ans = 0
        for i in range(0,n):
            ans += (i+1) * count[i]
        return ans