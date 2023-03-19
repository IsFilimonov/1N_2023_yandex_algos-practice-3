import sys
from collections import defaultdict

# Чтобы найти компоненты связности, достаточно одного обхода в глубину
# Чтобы передать в dfs граф, его следует привести к списку смежности


def dfs(graph, visited, now):
	visited[now] = True
	for neig in graph[now]:
		if not visited[neig]:
			dfs(graph, visited, neig)


# Список смежности (Adjacency List)
al = defaultdict(tuple)

# Количество Вершин, Ребер
N, M = tuple(map(int, input().split()))

# Сначала преобразуем массив вершин и ребер в список смежности
# Оставляем петли и мультиребра
for _ in range(M):
    row = tuple(map(int, sys.stdin.readline().strip().split()))
    al[row[0]] += (row[1],)
    al[row[1]] += (row[0],)

# Список посещений для погружения
visited = {k:False for k in sorted(al.keys())}
	
# Начинаем погружение с 1 элемента
dfs(al, visited, 1)

print(sum(visited.values()))
print(" ".join(map(str, [k for k in visited.keys() if visited[k]])))
