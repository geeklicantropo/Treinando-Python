class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    #Verifica o último item da pilha
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

# s = Stack()
# s.push("W")
# s.push("A")
# s.push("G")
#
# print(s.get_stack())