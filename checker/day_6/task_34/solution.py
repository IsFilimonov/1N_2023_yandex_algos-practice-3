from collections import defaultdict


def fill_values():
    """Заполняем список смежности (adjacency list) и словарь степеней захода из stdin.

    В данной задаче граф ориентированный, значит обратное направление не учитываем.
    Заполняем список смежности и словарь степенй захода в одном цикле.
    
    Returns:
        dict[int: list[int]]: Список смежности.
    """

    # Инициализируем все вершины сразу, даже если для них нет ребер
    al = {k: [] for k in range(1, N+1)}

    # Cловарь входящих степеней захода
    in_degree = defaultdict(int)

    # Создаем генератор пар - так быстрее
    for u, v in ((int(x) for x in input().strip().split()) for _ in range(M)):
        al.setdefault(u, []).append(v)
        in_degree[v] += 1  # увеличиваем входящую степень для каждой целевой вершины

    return al, in_degree


def topological_sort(adj_list, in_degree) -> list[int] | list:

    # Создаем очередь и добавляем в нее все вершины с входящей степенью 0
    queue = [v for v in adj_list if in_degree[v] == 0]

    # Проходимся по графу в ширину и собираем вершины в порядке их посещения
    top_sorted = []
    while queue:
        v = queue.pop(0)
        top_sorted.append(v)
        for neighbor in adj_list[v]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                # Ускоряем код. Заменяем apend на extend tuple
                queue.extend((neighbor,))

    # Проверяем, что граф не содержит циклов (циклических зависимостей)
    if len(top_sorted) != len(adj_list):
        return [-1]  # граф содержит цикл, топологическая сортировка невозможна
    else:
        return top_sorted


# Быстрее, чем создавать tuple(map(int, input()))
N, M = input().split()
N, M = int(N), int(M)

# Заполняем список смежности
al, in_d = fill_values()

print(*topological_sort(al, in_d), sep=" ")
