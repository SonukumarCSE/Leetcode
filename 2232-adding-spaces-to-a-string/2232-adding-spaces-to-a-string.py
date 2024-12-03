class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        idx = 0
        for i in range(len(spaces)):
            result.append(s[idx:spaces[i]])
            result.append(" ")
            idx = spaces[i]
        result.append(s[idx:])
        return "".join(result)
