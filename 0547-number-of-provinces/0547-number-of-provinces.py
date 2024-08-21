class Solution:
    def dfs(self,vis,adj,i):
        stack = [i]
        vis[i] = True
        while stack:
            node = stack.pop()
            vis[node] = True
            for ele in adj[node]:
                if vis[ele] == False:
                    stack.append(ele)
                    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = [[] for _ in range(len(isConnected)+1)]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j:
                    if isConnected[i][j] == 1:
                        adj[i+1].append(j+1)
        print(adj)
        vis = [False] * (len(isConnected)+1)
        count = 0
        for i in range(1,len(isConnected)+1):
            if vis[i] == False:
                self.dfs(vis,adj,i)
                count += 1
        return count