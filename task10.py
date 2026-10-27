class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def add_first(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    
    def add_last(self, value):
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    
    def remove_first(self):
        if self.head is None:
            return "Список порожній"

        value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None

        self.length -= 1
        return value

    
    def remove_last(self):
        if self.tail is None:
            return "Список порожній"

        value = self.tail.value
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

        self.length -= 1
        return value

    def contains(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    
    def get_node(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Неправильний індекс")

        current = self.head

        for _ in range(index):
            current = current.next

        return current

    
    def get(self, index):
        return self.get_node(index).value

    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Неправильний індекс")

        if index == 0:
            self.add_first(value)
            return

        if index == self.length:
            self.add_last(value)
            return

        current = self.get_node(index)
        new_node = Node(value)

        new_node.prev = current.prev
        new_node.next = current

        current.prev.next = new_node
        current.prev = new_node

        self.length += 1

    
    def remove_at(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Неправильний індекс")

        if index == 0:
            return self.remove_first()

        if index == self.length - 1:
            return self.remove_last()

        current = self.get_node(index)

        current.prev.next = current.next
        current.next.prev = current.prev

        self.length -= 1
        return current.value

    
    def maximum(self):
        if self.head is None:
            return "Список порожній"

        maximum = self.head.value
        current = self.head.next

        while current is not None:
            if current.value > maximum:
                maximum = current.value
            current = current.next

        return maximum

    
    def minimum(self):
        if self.head is None:
            return "Список порожній"

        minimum = self.head.value
        current = self.head.next

        while current is not None:
            if current.value < minimum:
                minimum = current.value
            current = current.next

        return minimum

    
    def size(self):
        return self.length

    
    def show(self):
        current = self.head
        index = 0

        print("{", end="")

        while current is not None:
            print(f"[index:{index}; value:{current.value}]", end=" ")
            current = current.next
            index += 1

        print("}")

    
    def insert_array(self, index, values):
        if index < 0 or index > self.length:
            raise IndexError("Неправильний індекс")

        for value in values:
            self.insert(index, value)
            index += 1

linked_list = DoublyLinkedList()

linked_list.add_first(20)
linked_list.add_first(10)
linked_list.add_last(30)
linked_list.add_last(40)

print("Початковий список:")
linked_list.show()

print("Чи є число 30:", linked_list.contains(30))
print("Елемент за індексом 1:", linked_list.get(1))

linked_list.insert(2, 25)
print("Після вставки числа 25:")
linked_list.show()

linked_list.insert_array(3, [100, 200, 300])
print("Після вставки масиву:")
linked_list.show()

print("Найбільший елемент:", linked_list.maximum())
print("Найменший елемент:", linked_list.minimum())
print("Розмір списку:", linked_list.size())

print("Видалений перший елемент:", linked_list.remove_first())
print("Видалений останній елемент:", linked_list.remove_last())
print("Видалений елемент за індексом 1:", linked_list.remove_at(1))

print("Список після видалення:")
linked_list.show()
print("Розмір списку:", linked_list.size())