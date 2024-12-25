class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека.
        Если стек пуст, вызывает ошибку."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает элемент на вершине стека, не удаляя его.
        Если стек пуст, вызывает ошибку."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

# Пример использования стека
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Вывод: 2
print(stack.pop())   # Вывод: 2
print(stack.is_empty())  # Вывод: False
