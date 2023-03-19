from collections import defaultdict

# ### >>>>>>
# import debugpy
# debugpy.listen(5678)
# print("Waiting for debugger")
# debugpy.wait_for_client()
# ### <<<<<<

def fill_values():

    # список смежности для всех вершин
    adj_list = {k: [] for k in range(1, N+1)}

    # Cловарь входящих степеней захода
    in_degree = defaultdict(int)

    # Метро - неориентированный граф (матрица симметричная)
    for line in matrix:
        neighbors = []

        for i in range(len(line)):

            idx_back = i-1 if 0 <= i-1 < len(line) else None
            idx_forward = i+1 if 0 <= i+1 < len(line) else None

            row = []
            # при значениях 0 отрабатывало, как и при None
            if idx_back or idx_back == 0:
                row.append(line[idx_back])
            if idx_forward or idx_forward == 0:
                row.append(line[idx_forward])

            adj_list[line[i]] += [*row]
            in_degree[line[i]] += 1

    return adj_list, in_degree


def find_best(adj_list, in_degree, A, B):
    visited = set()  # множество посещенных вершин
    queue = []

    visited.add(A)
    queue.append(A)

    changes = 0

    while queue:
        vertex = queue.pop()

        for neighbour in adj_list[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

                if in_degree[neighbour] > 1 and neighbour not in (A, B):
                    changes += 1
                
                if neighbour == B:
                    return changes if changes <=1 else changes - 1
        
    return -1


N = int(input().strip())  # Кол-во станций метро (2<=N<=100)
M = int(input().strip())  # Кол-во линий метро (1<=M<=20)

matrix = []
for _ in range(M):
    line = list(map(int, input().strip().split()))
    matrix.append(line[1:])  # 1 символ: количество станций линии

del line

A, B = map(int,input().strip().split())

adj_list, in_degree = fill_values()

answer = find_best(adj_list, in_degree, A, B)

print(answer)
