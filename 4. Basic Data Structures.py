# """4.5 Write a function revstring(mystr)
# that uses a stack to reverse the characters in a string."""
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def isEmpty(self):
#         return self.items == []
#
#     def pop(self):
#         return self.items.pop()
#
#     def push(self, item):
#         self.items.append(item)
#
#
# def revstring(mystr):
#     old = Stack()
#     for i in mystr:
#         old.push(i)
#     mystr = ''
#     while not old.isEmpty():
#         mystr+=old.pop()
#     print(mystr)
#
#
# mystr = '12345атос'
# revstring(mystr)


# """4.7."""
# from pythonds.basic import Stack
#
# def parChecker(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in "([{":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top,symbol):
#                        balanced = False
#         index = index + 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
# def matches(open,close):
#     opens = "([{"
#     closers = ")]}"
#     с = opens.index(open)
#     в = closers.index(close)
#     return opens.index(open) == closers.index(close)
#
#
# print(parChecker('{({([][])}())}'))
# print(parChecker('[{()]'))


"""4.8"""
from pythonds.basic import Stack

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

# print(baseConverter(25,2))
print(baseConverter(256,16))

