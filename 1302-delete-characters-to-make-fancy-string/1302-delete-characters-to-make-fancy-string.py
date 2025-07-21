class Solution:
    def makeFancyString(self, s: str) -> str:
        str1 = ""
        count = 0
        ans = ""
        for i in range(len(s)):
            if str == "":
                str1 = s[i]
                count += 1
                ans += str1
                continue
            if s[i] == str1:
                count += 1
            else:
                str1 = s[i]
                count = 1
            if count <= 2:
                ans += str1
        return ans
