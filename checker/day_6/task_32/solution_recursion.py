import sys
from collections import defaultdict
from collections import deque


def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig)


def fill_al():
    """Заполняем список смежности"""

    # Список смежности (Adjacency List)
    # Сразу заполняем всеми вершинами
    al = defaultdict(tuple, {k: tuple() for k in range(1, N+1)})

    # Сначала преобразуем массив вершин и ребер в список смежности
    # Оставляем петли и мультиребра
    for _ in range(M):
        row = tuple(map(int, sys.stdin.readline().strip().split()))
        al[row[0]] += (row[1],)
        al[row[1]] += (row[0],)

    return al


# Количество Вершин, Ребер
N, M = tuple(map(int, input().split()))

al = fill_al()

visited = {k: False for k in sorted(al.keys())}
answer = []

while len(visited)>0:
    dfs(al, visited, min(visited.keys()))
    component = [k for k in visited.keys() if visited[k]]
    answer.append(component)
    visited = {k:v for k,v in visited.items() if not visited[k]}


print(len(answer))
for el in answer:
    print(len(el))
    print(" ".join(map(str,el)))
