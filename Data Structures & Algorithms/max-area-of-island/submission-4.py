class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [(-1, 0),(0, -1), (1, 0), (0, 1)]
        res = 0

        # def dfs(row, col):
        #     if row not in range(ROW) or col not in range(COL) or grid[row][col] in {0, 3}:
        #         return 0
        #     grid[row][col] = 3
        #     current = 1
        #     for dr, dc in dirs:
        #         current += dfs(dr+row, dc+col)
        #     return current

        def bfs(row, col):
            q = deque([(row, col)])
            grid[row][col] = 3
            current = 1
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc]==1:
                        q.append((nr, nc))
                        grid[nr][nc] = 3
                        current += 1
            return current


        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    # res = max(res, dfs(r, c))
                    res = max(res, bfs(r, c))
        # print(grid)
        return res

