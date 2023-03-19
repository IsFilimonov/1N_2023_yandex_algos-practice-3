import sys


class MyQueue:
    """Реализация очереди."""
    def __init__(self) -> None:
        self.__core = []
        """list[int]: Python массив как основа для очереди."""

    def push(self, value: int) -> str:
        """Добавление в очередь элемент.

        Args:
            value(int): Значение элемента.
        
        Returns:
            str: Статус добавления.
        """
        # finally при любом раскладе отрабатывает
        # except только при ошибке в операции
        # else если всё ок
        try:
            self.__core.append(value)
        except:
            ...
        else:
            return "ok"
        
    def pop(self) -> str:
        """Удаление из очереди первого элемента.

        Returns:
            str: Значение элемента.
        """
        # Очередь не должна быть пустой
        if len(self.__core) > 0:
            try:
                first = self.__core[0]
                self.__core = self.__core[1:]
            except:
                ...
            else:
                return str(first)
        else:
            return "error"

    def front(self) -> str:
        """Значение первого элемента, не удаляя его из очереди.

        Returns:
            str: Значение первого элемента.
        """
        # Здесь не нужен try/finally тк возвращаем значение, а не статус операции      
        if len(self.__core) > 0:
            return self.__core[0]
        else:
            return "error"

    def size(self) -> int:
        """Количество элементов в очереди.

        Returns:
            int: Количество элементов.
        """
        return len(self.__core)

    def clear(self) -> str:
        """Очищение очереди.

        Returns:
            str: Статус очищения.
        """
        try:
            self.__core.clear()
        except:
            ...
        else:
            return "ok"


Q = MyQueue()
actions = (True, True, )

while len(actions) > 0:
    actions = sys.stdin.readline().strip().split()

    match actions[0]:
        case "push":
            print(Q.push(int(actions[1])) if len(actions) == 2 else ...)

        case "pop":
            print(Q.pop() if len(actions) == 1 else ...)

        case "front":
            print(Q.front() if len(actions) == 1 else ...)

        case "size":
            print(Q.size() if len(actions) == 1 else ...)

        case "clear":
            print(Q.clear() if len(actions) == 1 else ...)

        case "exit":
            # or оператор выполняет несколько действий одновременно
            print("bye") or actions.clear() or Q.clear() if len(actions) == 1 else ...
