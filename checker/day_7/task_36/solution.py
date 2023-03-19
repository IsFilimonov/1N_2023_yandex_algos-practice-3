from collections import deque


def fill_adjacency_list() -> dict[int: list[int]]:
    """Заполняем список смежности из матрицы смежности.

    Returns:
        dict[int: list[int]]: Список смежности
    """
    adj_matrix = tuple()  # матрица смежности
    adj_list = {k: [] for k in range(1, N+1)}  # список смежности

    # Создаем генератор пар - так быстрее
    for el in ((int(x) for x in input().strip().split()) for _ in range(N)):
        adj_matrix += (list(el),)

    # Дан неориентированный граф, значит матрица симметрична
    for i in range(len(adj_matrix)):
        neighbors = tuple()
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                neighbors += (j+1,)
        adj_list[i+1] = neighbors

    return adj_list



def find_shortcut(adj_list, start, end) -> int:
    """Поиск кратчайшего пути.

    Returns:
        int: Длина кратчайшего пути
    """
    visited = set()  # множество посещенных вершин
    queue = {el: deque() for el in range(len(adj_list))}

    # Инициализация первого обхода
    visited.add(start)
    queue[0].append(start)
    wave = 0  # Волна обхода соседей

    while wave <= N:

        while queue[wave]:
            vertex = queue[wave].popleft()

            for neighbour in adj_list[vertex]:
                if neighbour not in visited:
                    if neighbour == end:
                        return wave+1
                    visited.add(neighbour)
                    queue[wave+1].append(neighbour)

        wave+=1


N = int(input().strip())  # число вершин в графе

adj_list = fill_adjacency_list()  # матрица смежности -> список смежности

# Начальная, конечная вершины
start, end = input().split()
start, end = int(start), int(end)

if len(adj_list[start]) == 0 or len(adj_list[end]) == 0:
    print(-1)
elif start == end:
    print(0)
else:
    print(find_shortcut(adj_list, start, end))
