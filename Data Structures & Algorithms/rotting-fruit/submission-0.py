class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        fresh, time = 0, 0
        R, C = len(grid), len(grid[0])
        q = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, time))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q:
            r, c, time = q.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr, nc, time+1))
        
        return time if not fresh else -1