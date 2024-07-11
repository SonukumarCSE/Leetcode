class Solution:
    def solve(self,n,open,close,str):
        if len(str) == 2*n:
            self.ans.append(str)
            return 
        if open == n:
            for i in range(n-close):
                str += ")"
            self.ans.append(str)
            return
        if open == close:
            self.solve(n,open+1,close,str+"(")
            return 
        self.solve(n,open+1,close,str+"(")
        self.solve(n,open,close+1,str+")")

    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.solve(n,1,0,'(')
        return self.ans