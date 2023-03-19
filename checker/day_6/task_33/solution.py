def fill_adjacency_list():
    """Заполняем список смежности (adjacency list) из stdin.
    
    Returns:
        dict[int: list[int]]: Список смежности.
    """

    # Инициализируем все вершины сразу, даже если для них нет ребер
    al = {k: list() for k in range(1, N+1)}

    # Создаем генератор пар - так быстрее
    for u, v in ((int(x) for x in input().split()) for _ in range(M)):
        al.setdefault(u, []).append(v)
        al.setdefault(v, []).append(u)  # учитываем обратное направление

    return al


def is_bipartite(adj_list):
    """
    Проверка, является ли граф двудольным или нет.

    Args:
        adj_list (dict[int: list[int]]): Cписок смежности графа.
    Returns:
        bool: True, если граф двудольный, False в противном случае
    """
    # словарь для хранения цветов вершин с инициализацией всех вершин
    # -1: вместо visited
    # 0 и 1: разные цвета
    colors = {v: -1 for v in adj_list}  

    # Проходим все вершины, чтобы обработать и вершины без связей
    for vertex in adj_list:
        if colors[vertex] == -1:  # вершина еще не покрашена
            colors[vertex] = 1  # красим ее в цвет 1
            stack = [vertex]  # создаем стек и помещаем в него вершину

            while stack:
                v = stack.pop()  # извлекаем вершину из стека
                for neighbor in adj_list[v]:  # проверяем всех соседей вершины
                    if colors[neighbor] == -1:  # если сосед еще не окрашен
                        # красим в противоположный цвет
                        colors[neighbor] = 1 - colors[v]
                        stack.append(neighbor)  # помещаем в стек
                    elif colors[neighbor] == colors[v]:  # если сосед уже окрашен в тот же цвет
                        return False  # граф не двудольный

    return True  # если все вершины окрашены в два цвета, граф двудольный


# Быстрее, чем создавать tuple(map(int, input()))
N, M = input().split()
N, M = int(N), int(M)

# Заполняем список смежности
al = fill_adjacency_list()

print('YES' if is_bipartite(al) else 'NO')
