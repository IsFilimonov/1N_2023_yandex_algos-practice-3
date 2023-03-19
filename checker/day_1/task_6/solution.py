def f(l: int, s: list) -> int:
    s.reverse()
    begins, ends = list(), list()
    cnt = 0
    for begin, end in s:
        # update_set = set([i for i in range(begin, end + 1)])
        for i in range(len(begins)):
            if begins[i] <= end <= ends[i] or begins[i] <= begin <= ends[i] or begin <= begins[i] and ends[i] <= end:
                break
        else:
            cnt += 1
        begins.append(begin)
        ends.append(end)
    return cnt


length = int(input())
sectors = [tuple(map(int, input().split())) for _ in range(int(input()))]
print(str(f(length, sectors)))
