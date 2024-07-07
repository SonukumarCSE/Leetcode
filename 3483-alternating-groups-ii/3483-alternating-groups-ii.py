class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        maxlen = 1
        ans = 0
        n = len(colors) 
        for i in range(1,n-1+k):
            if colors[i%n] != colors[(i-1) % n]:
                maxlen += 1
            else:
                maxlen = 1
            if maxlen >= k:
                ans += 1
        return ans