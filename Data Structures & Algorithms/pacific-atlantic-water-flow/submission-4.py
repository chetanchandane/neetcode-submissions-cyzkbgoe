class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R,C = len(heights), len(heights[0])
        dirs = [(0, 1), (1, 0), (-1,0), (0, -1)]

        def bfs(cells):
            q = deque(cells)
            visited = set(cells)
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = dr+r, dc+c
                    if 0<=nr<R and 0<=nc<C and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return visited

        pac_edge = [(r, 0) for r in range(R)]+[(0, c) for c in range(C)]
        atl_edge = [(R-1, c) for c in range(C)]+[(r, C-1) for r in range(R)]
        res_pac = bfs(pac_edge)
        res_atl = bfs(atl_edge)

        return list(res_atl & res_pac)