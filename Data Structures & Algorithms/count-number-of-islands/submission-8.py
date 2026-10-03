class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        count = 0
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # def bfs(r, c):
        #     q = deque([(r, c)])
        #     visited.add((r, c))
        #     while q:
        #         r, c = q.popleft()
        #         for dr, dc in dirs:
        #             nr, nc = r + dr, c + dc
        #             if 0<=nr<ROW and 0<=nc<COL and (nr,nc) not in visited and grid[nr][nc]=="1":
        #                 q.append((nr, nc))
        #                 visited.add((nr, nc))
        
        def dfs(row, col):
            if row not in range(ROW) or col not in range(COL) or grid[row][col]=="0" or (row, col) in visited:
                return
            visited.add((row, col))
            for dr,dc in dirs:
                dfs(dr+row, dc+col)

        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visited and \
                grid[r][c] == "1":
                    # bfs(r, c)
                    dfs(r, c)
                    count += 1
        
        return count
