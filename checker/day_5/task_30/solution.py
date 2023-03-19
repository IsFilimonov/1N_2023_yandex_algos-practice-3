def f(n: int, fst: list, m: int, scd: list) -> list:
    fst = [0] + fst
    scd = [0] + scd
    dp = [[0 for _ in range(len(fst))] for _ in range(len(scd))]
    for i in range(1, len(scd)):
        for j in range(1, len(fst)):
            dp[i][j] = dp[i - 1][j - 1] + 1 if scd[i] == fst[j] else max(dp[i][j - 1], dp[i - 1][j])

    i = dp[m][n]
    first_idx = [0] * i
    second_idx = [0] * i
    while dp[m][n]:
        if fst[n] == scd[m]:
            first_idx[i - 1], second_idx[i - 1] = n, m
            i, n, m = i - 1, n - 1, m - 1
        else:
            if dp[m - 1][n] > dp[m][n - 1]:
                m -= 1
            elif dp[m][n - 1] > dp[m - 1][n] or scd[m] == fst[n - 1]:
                n -= 1
            else:
                m -= 1

    print(" ".join(map(str,first_idx)))

    # Вместо join контест принял это решение
    # for i in first_idx:
    #     answer += first_idx[i]
    #     print(fst[i], end=' ')


f(int(input()), list(map(int, input().split())), int(input()), list(map(int, input().split())))
