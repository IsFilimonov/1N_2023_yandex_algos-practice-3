import sys


class MyDeque:
    """Реализация дека."""

    def __init__(self) -> None:
        self.__core = []
        """list[int]: Python массив как основа для очереди."""

    def push_front(self, value: int) -> str:
        """Добавление в начало дека новый элемент.

        Args:
            value(int): Значение элемента.

        Returns:
            str: Статус добавления.
        """
        # finally при любом раскладе отрабатывает
        # except только при ошибке в операции
        # else если всё ок
        try:
            self.__core.insert(0, value)

        except:
            ...
        else:
            return "ok"

    def push_back(self, value: int) -> str:
        """Добавление в конец дека новый элемент.

        Args:
            value(int): Значение элемента.
        
        Returns:
            str: Статус добавления.
        """
        try:
            self.__core.append(value)
        except:
            ...
        else:
            return "ok"

    def pop_front(self) -> str:
        """Извлечение из дека первого элемента.

        Returns:
            str: Значение элемента.
        """
        # Дек не должен быть пустой
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

    def pop_back(self) -> str:
        """Удаление из очереди последнего элемента.

        Returns:
            str: Значение элемента.
        """
        # Дек не должен быть пустой
        if len(self.__core) > 0:
            try:
                last = self.__core[-1]
                self.__core = self.__core[:len(self.__core)-1]
            except:
                ...
            else:
                return str(last)
        else:
            return "error"

    def front(self) -> str:
        """Значение первого элемента, не удаляя его из дека.

        Returns:
            str: Значение первого элемента.
        """
        # Здесь не нужен try/finally тк возвращаем значение, а не статус операции
        if len(self.__core) > 0:
            return self.__core[0]
        else:
            return "error"
        
    def back(self) -> str:
        """Значение последнего элемента, не удаляя его из очереди.

        Returns:
            str: Значение первого элемента.
        """
        # Здесь не нужен try/finally тк возвращаем значение, а не статус операции
        if len(self.__core) > 0:
            return self.__core[-1]
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


DQ = MyDeque()
actions = (True, True, )

while len(actions) > 0:
    actions = sys.stdin.readline().strip().split()

    match actions[0]:
        case "push_front":
            print(DQ.push_front(int(actions[1])) if len(actions) == 2 else ...)
        
        case "push_back":
            print(DQ.push_back(int(actions[1])) if len(actions) == 2 else ...)

        case "pop_front":
            print(DQ.pop_front() if len(actions) == 1 else ...)

        case "pop_back":
            print(DQ.pop_back() if len(actions) == 1 else ...)

        case "front":
            print(DQ.front() if len(actions) == 1 else ...)
        
        case "back":
            print(DQ.back() if len(actions) == 1 else ...)

        case "size":
            print(DQ.size() if len(actions) == 1 else ...)

        case "clear":
            print(DQ.clear() if len(actions) == 1 else ...)

        case "exit":
            # or оператор выполняет несколько действий одновременно
            print("bye") or actions.clear() or DQ.clear() if len(actions) == 1 else ...
