M = int(input().strip())  # количество секторов
N = int(input().strip())  # количество разделов

data = []  # собираем последовательности разделов в массив
for _ in range(N):
    line = list(map(int, input().strip().split()))
    # имея границы, создаем последовательность чисел
    data.append(set(el for el in range(line[0], line[1]+1)))
 
# не можем хранить в общем сете, тк надо будет подчищать 
# каждый испорченнный раздел, а не удалять элементы пересечения
buffer = []  # чтобы хранить сеты
for i in range(len(data)):
    new_os = data[i]

    for j in range(len(buffer),0,-1):
        # True: нет пересечений, False: есть пересечение
        if not new_os.isdisjoint(buffer[j-1]):
            buffer.remove(buffer[j-1])
            
    buffer.append(new_os)

print(len(buffer))
