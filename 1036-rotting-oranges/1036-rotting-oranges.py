class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count_fresh = 0

        q = deque()
        vis = [[False] * (n) for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    vis[i][j] = True
        if count_fresh == 0:
            return 0
        if len(q) == 0:
            return -1 
        
        count = 0
        while q:
            count += 1
            for i in range(len(q)):
                node = q.popleft()
                row = node[0]
                col = node[1]

                if row-1 >= 0 and grid[row-1][col] == 1 and vis[row-1][col] == False:
                    q.append((row-1,col))
                    vis[row-1][col] = True
                if row+1 < m and grid[row+1][col] == 1 and vis[row+1][col] == False:
                    q.append((row+1,col))
                    vis[row+1][col] = True
                if col-1 >= 0 and grid[row][col-1] == 1 and vis[row][col-1] == False:
                    q.append((row,col-1))
                    vis[row][col-1] = True
                if col+1 < n and grid[row][col+1] == 1 and vis[row][col+1] == False:
                    q.append((row,col+1))
                    vis[row][col+1] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == False:
                    return -1
        return count-1
