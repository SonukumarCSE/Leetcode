class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if len(st) == 0 or s[i] != ')':
                st.append(s[i])
            if s[i] == ')':
                print(i)
                temp = []
                while st[-1] != '(':
                    temp.append(st.pop())
                st.pop()
                for x in temp:
                    st.append(x)
        return "".join(st)