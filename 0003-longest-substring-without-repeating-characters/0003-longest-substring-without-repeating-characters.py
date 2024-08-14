from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mpp = []
        start = 0
        ans = 0
        for i in range(n):
            if s[i] in mpp:
                while start < i and s[i] in mpp:
                    mpp.remove(s[start])
                    start += 1
            mpp.append(s[i])
            ans = max(ans,i-start+1)
        return ans