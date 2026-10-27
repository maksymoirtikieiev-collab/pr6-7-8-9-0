class Stack:
    def __init__(self):
        self.items = []

    
    def push(self, value):
        self.items.append(value)

    
    def peek(self):
        if len(self.items) == 0:
            return "Стек порожній"
        return self.items[-1]

    
    def pop(self):
        if len(self.items) == 0:
            return "Стек порожній"
        return self.items.pop()

    
    def clear(self):
        self.items.clear()

    
    def count(self):
        return len(self.items)

    
    def size(self):
        return len(self.items)

    
    def toString(self):
        if len(self.items) == 0:
            return "Стек порожній"

        result = []
        for i in range(len(self.items) - 1, -1, -1):
            result.append(str(self.items[i]))

        return " -> ".join(result)



stack = Stack()

stack.push  
stack.push(10)
stack.push(20)
stack.push(30)

print("Елементи стека:", stack.toString())
print("Верхній елемент:", stack.peek())
print("Кількість елементів:", stack.count())
print("Розмір стека:", stack.size())

print("Видалений елемент:", stack.pop())
print("Стек після видалення:", stack.toString())

stack.clear()
print("Стек після очищення:", stack.toString())