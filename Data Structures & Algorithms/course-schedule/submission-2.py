class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        stack = [False]*numCourses
        visited = [False]*numCourses
        adj = defaultdict(list)

        def dfs(node, adj, stack, visited):
            if visited[node]:
                return True
            if stack[node]:
                return False # cycle detected
            
            stack[node] = True
            for n in adj[node]:
                if not dfs(n, adj, stack, visited):
                    return False
            stack[node] = False
            visited[node] = True
            return True


        for pre in prerequisites:
            adj[pre[1]].append(pre[0])
        
        for i in range(numCourses):
            if not dfs(i, adj, stack, visited):
                return False
        return True