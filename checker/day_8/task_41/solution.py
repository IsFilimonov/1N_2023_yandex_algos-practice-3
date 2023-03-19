"""
Поддерживаем стек из блоков (товар, количество).

Плюс поддерживаем словарь <товар - общее количество>.

Помните, что суммарное количество товаров одного типа может вылазить за 32-битный тип.
"""
from collections import defaultdict


N = int(input().strip())  # количество операций

result = defaultdict(int)  # словарь количества товара
stack = []  # стек вагонов

for _ in range(N):
    action = input().strip().split()  # операция

    match action[0]:
        case "add":
            result[action[2]] += int(action[1])  # фиксируем количество
            stack.append({action[2]: int(action[1])})  # заполняем стек товаром

        case "get":
            if action[1] in result:  # если товар уже учтен
                print(result[action[1]])
            else:  # иначе 0, тк мы не знаем наименовнаие заранее
                print(0)

        case "delete":
            q = int(action[1])  # цена отцепления для уменьшения количества в стеке
            
            while q>0:
                # название и количество товара в стеке
                k, v = list(stack[-1].items())[0]  

                if v<=q:  # если операция затрагивает несколько типов товара в стеке
                    q-=v
                    result[k] -= v
                    stack.pop()
                else:  # полностью обнуляем товар в стеке
                    result[k] -= q
                    stack[-1][k] -= q
                    q = 0
