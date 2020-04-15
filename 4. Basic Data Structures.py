"""4.5 Write a function revstring(mystr)
that uses a stack to reverse the characters in a string."""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


def revstring(mystr):
    old = Stack()
    for i in mystr:
        old.push(i)
    mystr = ''
    while not old.isEmpty():
        mystr+=old.pop()
    print(mystr)


mystr = '12345атос'
revstring(mystr)

