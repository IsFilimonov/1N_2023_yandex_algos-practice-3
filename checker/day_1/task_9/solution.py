def f(h, w: int, mtx, c: list) -> None:
    prefix_mtx = [[0 for _ in range(w+1)] for _ in range(h+1)]
    for x in range(1, len(prefix_mtx)):
        for y in range(1, len(prefix_mtx[x])):
            prefix_mtx[x][y] = prefix_mtx[x-1][y] + \
                prefix_mtx[x][y-1] - prefix_mtx[x-1][y-1] + mtx[x-1][y-1]

    for coord_begin, coord_end in c:
        x_begin, y_begin = coord_begin
        x_end, y_end = coord_end
        print(prefix_mtx[x_end][y_end] - prefix_mtx[x_begin-1][y_end] -
              prefix_mtx[x_end][y_begin-1] + prefix_mtx[x_begin-1][y_begin-1])


height, width, count = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(height)]
coords = list()
for _ in range(count):
    x1, y1, x2, y2 = map(int, input().split())
    coords.append(((x1, y1), (x2, y2)))
f(height, width, matrix, coords)
