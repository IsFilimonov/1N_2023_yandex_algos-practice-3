def f(c: list) -> tuple:
    x, y = zip(*c)
    return min(x), min(y), max(x), max(y)


count = int(input())
coords = [tuple(map(int, input().split())) for _ in range(count)]
print(*f(coords))
