# Задание 3: Поиск минимального элемента в дереве

Этот проект реализует функцию для поиска минимального элемента в бинарном дереве поиска (BST). Бинарное дерево поиска - это структура данных, в которой для каждого узла выполняется следующее условие:
- Значения всех узлов в левом поддереве меньше значения узла.
- Значения всех узлов в правом поддереве больше значения узла.

## Описание кода

### Класс `TreeNode`

Класс `TreeNode` представляет узел бинарного дерева. Он содержит:
- `value`: значение узла.
- `left`: ссылка на левого ребенка узла (по умолчанию `None`).
- `right`: ссылка на правого ребенка узла (по умолчанию `None`).

### Функция `find_minimum`

Функция `find_minimum(node)` принимает узел дерева и возвращает минимальный элемент в бинарном дереве поиска. Если дерево пустое (узел равен `None`), функция возвращает `None`.

#### Алгоритм:
1. Если узел равен `None`, вернуть `None`.
2. Перейти по левым узлам дерева, пока не достигнем узла без левого ребенка.
3. Вернуть значение узла, который был достигнут.

### Пример использования

```python
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)

print(find_minimum(root))  # Вывод: 3