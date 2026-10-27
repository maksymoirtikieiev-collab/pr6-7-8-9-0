class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None

    
    def add(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    
    def find(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    
    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_node(node.left, value)

        elif value > node.value:
            node.right = self._delete_node(node.right, value)

        else:
            
            if node.left is None:
                return node.right

            
            if node.right is None:
                return node.left

            
            smallest = node.right
            while smallest.left is not None:
                smallest = smallest.left

            node.value = smallest.value
            node.right = self._delete_node(node.right, smallest.value)

        return node

    
    def show(self):
        print("Елементи дерева:", end=" ")
        self._show_nodes(self.root)
        print()

    def _show_nodes(self, node):
        if node is not None:
            self._show_nodes(node.left)
            print(node.value, end=" ")
            self._show_nodes(node.right)

    
    def minimum(self):
        if self.root is None:
            return "Дерево порожнє"

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value

    
    def maximum(self):
        if self.root is None:
            return "Дерево порожнє"

        current = self.root
        while current.right is not None:
            current = current.right

        return current.value

    
    def count(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        if node is None:
            return 0

        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)



tree = BinaryTree()

tree.add(10)
tree.add(5)
tree.add(15)
tree.add(3)
tree.add(7)
tree.add(12)
tree.add(20)

tree.show()

print("Чи є число 7:", tree.find(7))
print("Чи є число 25:", tree.find(25))
print("Найменший елемент:", tree.minimum())
print("Найбільший елемент:", tree.maximum())
print("Кількість елементів:", tree.count())

tree.delete(10)

print("Після видалення числа 10:")
tree.show()
print("Кількість елементів:", tree.count())