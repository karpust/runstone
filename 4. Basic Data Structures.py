"""4.5 Write a function revstring(mystr)
that uses a stack to reverse the characters in a string."""
class Stack:
    def __init__(self):
        self.items = []
# stack
# push
# isempty
# pop
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
    new = Stack()
    while not old.isEmpty():
        new.push(old.pop())
    while not new.isEmpty():
        mystr += str(new.pop())
    print(mystr)


mystr = '12345атос'
revstring(mystr)