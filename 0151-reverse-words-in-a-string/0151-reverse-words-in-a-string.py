class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        n = len(s)
        ans = ""
        while i < n:

            while i < n and s[i] == " ":
                i += 1
            if i >= n:
                break
            j = i+1
            while j < n and s[j] != " ":
                j += 1
            str1 = s[i:j]
            if len(ans) == 0:
                ans = str1
            else:
                ans = str1 + " " + ans
            i = j
        return ans