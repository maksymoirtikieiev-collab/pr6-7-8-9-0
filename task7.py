class Queue:
    def __init__(self):
        self.items = []

    
    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if len(self.items) == 0:
            return "Черга порожня"
        return self.items.pop(0)

    
    def peek(self):
        if len(self.items) == 0:
            return "Черга порожня"
        return self.items[0]

    
    def count(self):
        return len(self.items)

    
    def show(self):
        if len(self.items) == 0:
            print("Черга порожня")
        else:
            print("Черга:", self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.show()
print("Перший елемент:", queue.peek())
print("Кількість елементів:", queue.count())

print("Видалений елемент:", queue.dequeue())
queue.show()

print("Видалений елемент:", queue.dequeue())
queue.show()

print("Кількість елементів:", queue.count())