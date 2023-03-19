import sys


def fill_adjacency_list():
    """Заполняем список смежности (adjacency list)."""

    # Инициализируем все вершины сразу, даже если для них нет ребер
    al = {k: list() for k in range(1, N+1)}

    # Создаем генератор пар - так быстрее
    for u, v in ((int(x) for x in input().split()) for _ in range(M)):
        al.setdefault(u, []).append(v)
        al.setdefault(v, []).append(u)  # учитываем обратное направление

    return al


def find_components(adj_list):
    visited = set()
    components = []
    for vertex in adj_list:
        if vertex not in visited:
            component = set()
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    component.add(v)
                    for neighbor in adj_list[v]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            components.append(component)
    return components



# Количество Вершин, Ребер
N, M = tuple(map(int, input().split()))

# Заполняем список смежности
al = fill_adjacency_list()

# Находим компоненты
answer = find_components(al)

print(len(answer))
for el in answer:
    print(len(el))
    print(" ".join(map(str, el)))
