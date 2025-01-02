class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_minimum(node):
    """Возвращает минимальный элемент в бинарном дереве поиска."""
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node.value

# Пример использования
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)

print(find_minimum(root))  # Вывод: 3
