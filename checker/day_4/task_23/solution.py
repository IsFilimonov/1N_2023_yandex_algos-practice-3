def count_operations(n: int) -> list[int]:
    """Cчитает остатки от операций.

    Args:
        n (int): Целевое число.

    Returns:
        list[int]: Массив остатков.
    """
    cache = [0] * (N + 1)
    cache[1] = 0

    for i in range(2, n+1):
        v = cache[i-1] + 1

        if (i % 2) == 0:
            v = min(v, cache[i//2]+1)
        if (i % 3) == 0:
            v = min(v, cache[i//3]+1)

        cache[i] = v

    return cache


def build_sequence(a: list[int]) -> list[int]:
    """Восстанавливает последовательность операций.

    Args:
        a (list[int]): Массив остатков.

    Returns:
        list[int]: Форматированный массив операций:
            возрастающая последовательность значений.
    """
    j = N
    out = []

    # Сначала восстанавливаем операции
    while j > 1:
        if a[j] == (a[j-1]+1):
            out.insert(0, 1)
            j -= 1
            continue

        if j % 2 == 0 and a[j] == a[j//2]+1:
            out.insert(0, 2)
            j //= 2
            continue

        out.insert(0, 3)
        j //= 3

    result = [1]

    # Затем формируем последовательность значений
    for el in out:
        match el:
            case 3:
                v = result[-1]*3
                result.append(v)
            case 2:
                v = result[-1]*2
                result.append(v)
            case 1:
                v = result[-1]+1
                result.append(v)

    return result


N = int(input().strip())

seq = count_operations(N)

print(seq[N])  
print(" ".join(map(str, build_sequence(seq))))
