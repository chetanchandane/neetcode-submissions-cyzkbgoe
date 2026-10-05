class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R = len(board)
        C = len(board[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c):
            if r<0 or r>=R or c<0 or c>=C or board[r][c]!="O":
                return
            for dr, dc in directions:
                dfs(dr+r, dc+c)
                board[r][c] = "S"
        def bfs(r, c):
            q = deque([(r, c)])
            board[r][c] = "S"
            while q:
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = dx+r, dy+c
                    if 0<=nr<R and 0<=nc<C and board[nr][nc]=="O":
                        q.append((nr, nc))
                        board[nr][nc] = "S"
            

        for r in range(R):
            if board[r][0] == "O":
                # bfs(r, 0)
                dfs(r, 0)
            if board[r][C-1] == "O":
                dfs(r, C-1)
        for c in range(C):
            if board[0][c] == "O":
                dfs(0, c)
            if board[R-1][c] == "O":
                dfs(R-1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"    