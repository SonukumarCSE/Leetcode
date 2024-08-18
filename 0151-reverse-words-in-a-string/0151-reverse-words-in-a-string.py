class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        print(arr)
        arr.reverse()
        ans = ""
        str1 = []
        for i in range(len(arr)):
            if len(arr[i]) == 0:
                continue
            str1.append(arr[i])
        print(str1)
        return " ".join(str1)