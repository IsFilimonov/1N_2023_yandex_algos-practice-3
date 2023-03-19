# ### >>>>>>
# import debugpy
# debugpy.listen(5678)
# print("Waiting for debugger")
# debugpy.wait_for_client()
# ### <<<<<<


def find_best(matrix):
    def turn_w1():
        # движение на восток
        tr,tc,arr = r,c,tuple()

        while 0 <= tr < H and 0 <= tc+1 < W:
            tc += 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr
    
    def turn_w2():
        # Ю-В
        tr, tc, arr = r, c, tuple()

        while 0 <= tr+1 < H and 0 <= tc+1 < W:
            tr+=1
            tc+=1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr
        
        return arr
    
    def turn_w3():
            # Юг
        tr, tc, arr = r, c, tuple()

        while 0 <= tr+1 < H and 0 <= tc < W:
            tr += 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr
    
    def turn_w4():
            # Юг-запад
        tr, tc, arr = r, c, tuple()

        while 0 <= tr+1 < H and 0 <= tc-1 < W:
            tr += 1
            tc -= 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr
    
    def turn_w5():
            # запад
        tr, tc, arr = r, c, tuple()

        while 0 <= tr < H and 0 <= tc-1 < W:
            tc -= 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr
    
    def turn_w6():
            # Северо-запад
        tr, tc, arr = r, c, tuple()

        while 0 <= tr-1 < H and 0 <= tc-1 < W:
            tr -= 1
            tc -= 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr
    
    def turn_w7():
            # Север
        tr, tc, arr = r, c, tuple()

        while 0 <= tr-1 < H and 0 <= tc < W:
            tr -= 1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr

    def turn_w8():
        # Север-восток
        tr, tc, arr = r, c, tuple()

        while 0 <= tr-1 < H and 0 <= tc+1 < W:
            tr -= 1
            tc+=1
            if matrix[tr][tc] == '.':
                if (tr, tc) not in visited_back:
                    arr += ((tr, tc),)
            else:
                return arr

        return arr



    visited = set()
    visited_back = set()
    queue = {1:[]}

    visited.add((srow, scol))
    visited_back.add((srow, scol))
    queue[1].append((srow, scol))

    wave = 1

    mx = max(H,W)

    while wave <= mx*mx:
        queue[wave+1]  = []

        while queue[wave]:
            vertex = queue[wave].pop()

            r,c = vertex
            neighbours = []
            
            neighbours += turn_w1()  # восток
            neighbours += turn_w2()  # юго-восток
            neighbours += turn_w3()  # юг
            neighbours += turn_w4()  # юго-запад
            neighbours += turn_w5()  # запад
            neighbours += turn_w6()  # северо-запад
            neighbours += turn_w7()  # север
            neighbours += turn_w8()  # северо-восток

            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    visited_back.add(neighbour)
                    queue[wave+1].append(neighbour)

                    if neighbour == (trow, tcol):
                        ...
                        return wave


        del queue[wave]
        wave += 1

    return -1


H, W = input().strip().split()
H, W = int(H), int(W)

matrix = []

for el in ((x for x in input().strip().split()) for _ in range(H)):
    matrix.insert(0,(tuple(*el)))

# -1 это индексы массива
scol, srow = input().strip().split()
scol, srow = int(scol)-1, int(srow)-1
tcol, trow = input().strip().split()
tcol, trow = int(tcol)-1, int(trow)-1

answer = find_best(matrix)

print(answer)
