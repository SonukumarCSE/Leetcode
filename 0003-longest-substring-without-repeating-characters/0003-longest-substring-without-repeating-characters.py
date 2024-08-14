class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            list1 = []
            count = 0
            for j in range(i,n):
                if s[j] in list1:
                    ans = max(count,ans)
                    break
                count += 1
                list1.append(s[j])
            ans = max(count,ans)
        return ans
                
            