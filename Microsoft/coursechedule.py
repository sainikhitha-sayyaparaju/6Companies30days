# 207. Course Schedule: https://leetcode.com/problems/course-schedule/

class Solution:
    def dfs(self, graph, vis, dfsVis, node):
        dfsVis[node] = True
        vis[node] = True
        for i in graph[node]:
            if not vis[i]:
                if self.dfs(graph, vis, dfsVis, i):
                    return True
            elif dfsVis[i]:
                return True
        dfsVis[node] = False
        return False

    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in pre:
            graph[i[0]].append(i[1])
        vis = [False] * num
        dfsVis = [False] * num
        for i in range(num):
            if vis[i] == False:
                if self.dfs(graph, vis, dfsVis, i):
                    return False
        return True

# we just need to check i there is a cycle
