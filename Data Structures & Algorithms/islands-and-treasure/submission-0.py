class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid: return None
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        INF = 2**31-1
        q = deque([])
        ROW,COL = len(grid), len(grid[0])
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    # a gate
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = dr+r, dc+c
                if 0<=nr<ROW and 0<=nc<COL and grid[nr][nc]==INF:
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr, nc))