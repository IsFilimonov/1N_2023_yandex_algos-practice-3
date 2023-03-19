def f(s: str) -> None:
    lst = [0] * 26
    for i in range(len(s)):
        lst[ord(s[i]) - ord('a')] += (len(s) - i) * (i + 1)
    for i in range(26):
        if lst[i]:
            print(f'{chr(i + ord("a"))}: {lst[i]}')


line = input()
f(line)
