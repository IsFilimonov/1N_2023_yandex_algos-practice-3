def f(cnt_s, cnt_l, l, b, e) -> int:
    prev = {b}
    for i in range(cnt_s):
        nextt = prev
        for j in range(cnt_l):
            x = l[j]
            if len(prev & x) > 0:
                nextt = nextt | l[j]
        if e in nextt:
            return i
        prev = nextt
    return -1


n = int(input())
m = int(input())
lines = list()
for _ in range(m):
    lines.append(set(list(map(int, input().split()))[1:]))
begin, end = map(int, input().split())
print(str(f(n, m, lines, begin, end)))
