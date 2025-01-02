class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди.
        Если очередь пуста, вызывает ошибку."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.items) == 0

# Пример использования очереди
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # Вывод: 1
print(queue.is_empty())  # Вывод: False
