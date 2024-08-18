class Solution:
    def common(self,st1,st2):
        ans = ""
        i = 0
        for i in range(min(len(st1),len(st2))):
            
            if st1[i] == st2[i]:
                ans += st1[i]
            else:
                break
        return ans
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        count = 0
        if len(strs) == 1:
            return strs[0]
        str1 = self.common(strs[0],strs[1])
        print(str1)
        for i in range(2,len(strs)):
            str1 = self.common(str1,strs[i])
            
        print(str1)
        return str1

