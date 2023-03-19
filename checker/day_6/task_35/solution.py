class Graph:
    def __init__(self, cnt, arr):
        self.colors = [0 for _ in range(cnt)]
        self.adjacency_list = {k: [] for k in range(cnt)}
        for i in range(cnt):
            for j in range(cnt):
                if arr[i][j]:
                    self.adjacency_list[i].append(j)

    def search_cycle(self):
        for node in self.adjacency_list:
            if self.colors[node] == 0:
                res = self.dfs(node, self.colors, self.adjacency_list)
                if res:
                    return res

    @staticmethod
    def dfs(start_v: int, colors: list, adjacency_list: list) -> bool:
        stack = []
        path = []
        stack.append(start_v)
        parent = {}
        while stack:
            v = stack.pop()
            if colors[v] == 0:
                colors[v] = 1
                stack.append(v)
                path.append(str(v + 1))
                for w in adjacency_list[v]:
                    if colors[w] == 0:
                        stack.append(w)
                        parent[w] = v
                    elif colors[w] == 1 and parent.get(v) == w:
                        pass
                    elif colors[w] == 1 and parent.get(v) != w:
                        path.append(str(w + 1))
                        return path
            elif colors[v] == 1:
                colors[v] = 2
                path.pop()


cnt_vertexes = int(input())
edges = [tuple(map(int, input().split())) for _ in range(cnt_vertexes)]
graph = Graph(cnt_vertexes, edges)
res = graph.search_cycle()
if res:
    tail, index, cycle, cur_element = res[-1], -2, [res[-1]], res[-2]
    while cur_element != tail:
        cycle.append(cur_element)
        index -= 1
        cur_element = res[index]
    print('YES')
    print(len(cycle))
    print(*cycle)
else:
    print('NO')
