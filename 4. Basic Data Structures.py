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


# """4.8"""
# from pythonds.basic import Stack
#
# def baseConverter(decNumber,base):
#     digits = "0123456789ABCDEF"
#
#     remstack = Stack()
#
#     while decNumber > 0:
#         rem = decNumber % base
#         remstack.push(rem)
#         decNumber = decNumber // base
#
#     newString = ""
#     while not remstack.isEmpty():
#         newString = newString + digits[remstack.pop()]
#
#     return newString
#
# # print(baseConverter(25,2))
# print(baseConverter(25, 8))


# """4.9.2"""
# from pythonds.basic import Stack
#
# def infixToPostfix(infixexpr):
#     prec = {}
#     prec["*"] = 3
#     prec["/"] = 3
#     prec["+"] = 2
#     prec["-"] = 2
#     prec["("] = 1
#     opStack = Stack()
#     postfixList = []
#     tokenList = infixexpr.split()
#
#     for token in tokenList:
#         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
#             postfixList.append(token)
#         elif token == '(':
#             opStack.push(token)
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             while (not opStack.isEmpty()) and \
#                (prec[opStack.peek()] >= prec[token]):
#                   postfixList.append(opStack.pop())
#             opStack.push(token)
#
#     while not opStack.isEmpty():
#         postfixList.append(opStack.pop())
#     return " ".join(postfixList)
# #
# print(infixToPostfix("A * ( B + C ) * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


# """4.9.3"""
# from pythonds.basic import Stack
#
# def postfixEval(postfixExpr):
#     operandStack = Stack()
#     tokenList = postfixExpr.split()
#
#     for token in tokenList:
#         if token in "0123456789":
#             operandStack.push(int(token))
#         else:
#             operand2 = operandStack.pop()
#             operand1 = operandStack.pop()
#             result = doMath(token,operand1,operand2)
#             operandStack.push(result)
#     return operandStack.pop()
#
# def doMath(op, op1, op2):
#     if op == "*":
#         return op1 * op2
#     elif op == "/":
#         return op1 / op2
#     elif op == "+":
#         return op1 + op2
#     else:
#         return op1 - op2
#
# print(postfixEval('7 8 + 3 2 + /'))

# """4.9.3
# Q-3: Modify the infixToPostfix function so that
# it can convert the following expression:
# 5 * 3 ** (4 - 2). Run the function on the expression
# and paste the answer here:"""
#
# from pythonds.basic import Stack
#
# expression = '5 * 3 ^ ( 4 - 2 )'
#
# def infixToPostfix(expr):
#     expr = expr.split()
#     digits = '1234567890'
#     new_expr = []
#     OperandStack = Stack()
#     prec = {}
#     prec['*'] = 3
#     prec['/'] = 3
#     prec['+'] = 2
#     prec['-'] = 2
#     prec['^'] = 4
#     prec['('] = 1
#     for el in expr:
#         if el in digits:
#             new_expr.append(el)
#         elif el == '(':
#             OperandStack.push(el)
#         elif el == ')':
#             topToken = OperandStack.pop()
#             while topToken != '(':
#                 new_expr.append(topToken)
#                 topToken = OperandStack.pop()
#         else:
#             while (not OperandStack.isEmpty())and (prec[el] <= prec[OperandStack.peek()]):
#                 new_expr.append(OperandStack.pop())
#             OperandStack.push(el)
#     while not OperandStack.isEmpty():
#         new_expr.append(OperandStack.pop())
#     print(" ".join(new_expr))
#     return new_expr
#
#
# def compute(opn1, opn2, opr):
#     if opr == '-':
#         return opn1 - opn2
#     if opr == '*':
#         return opn1 * opn2
#     if opr == '^':
#         return opn1 ** opn2
#
#
# def infixToPostfixResult(expr):
#     postfixList = infixToPostfix(expr)
#     stack = Stack()
#     for token in postfixList:
#         if token in '0123456789':
#             stack.push(int(token))
#         else:
#             opr = token
#             opn2 = stack.pop()
#             opn1 = stack.pop()
#             result = compute(opn1, opn2, opr)
#             stack.push(result)
#     return stack.pop()
#
#
# print(infixToPostfixResult(expression))


# """4.13"""
# from pythonds.basic import Queue
#
# def hotPotato(namelist, num):
#     simqueue = Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#
#     while simqueue.size() > 1:
#         for i in range(num):
#             simqueue.enqueue(simqueue.dequeue())
#
#         simqueue.dequeue()
#
#     return simqueue.dequeue()
#
# print(hotPotato(["B","D","S","J","K","R"],7))

# """4.14.2"""
# from pythonds.basic import Queue
#
# import random
#
# class Printer:
#     def __init__(self, ppm):
#         self.pagerate = ppm
#         self.currentTask = None
#         self.timeRemaining = 0
#
#     def tick(self):
#         if self.currentTask != None:
#             self.timeRemaining = self.timeRemaining - 1
#             if self.timeRemaining <= 0:
#                 self.currentTask = None
#
#     def busy(self):
#         if self.currentTask != None:
#             return True
#         else:
#             return False
#
#     def startNext(self, newtask):
#         self.currentTask = newtask
#         self.timeRemaining = newtask.getPages() * 60/self.pagerate
#
# class Task:
#     def __init__(self, time):
#         self.timestamp = time
#         self.pages = random.randrange(1, 21)
#
#     def getStamp(self):
#         return self.timestamp
#
#     def getPages(self):
#         return self.pages
#
#     def waitTime(self, currenttime):
#         return currenttime - self.timestamp
#
#
# def simulation(numSeconds, pagesPerMinute, students):
#     for i in range(students):
#         labprinter = Printer(pagesPerMinute)
#         printQueue = Queue()
#         waitingtimes = []
#         for currentSecond in range(numSeconds):
#             if newPrintTask():
#                 task = Task(currentSecond)
#                 printQueue.enqueue(task)
#
#             if (not labprinter.busy()) and (not printQueue.isEmpty()):
#                 nexttask = printQueue.dequeue()
#                 waitingtimes.append(nexttask.waitTime(currentSecond))
#                 labprinter.startNext(nexttask)
#
#             labprinter.tick()
#
#         averageWait = sum(waitingtimes)/len(waitingtimes)
#         print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))
#
# def newPrintTask():
#     num = random.randrange(1, 91)
#     if num == 90:
#         return True
#     else:
#         return False
#
#
# simulation(3600, 5, 50)


# """4.21.1 The UnorderedList Class"""
# class Node:
#     def __init__(self, initdata):
#         self.data = initdata
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return self.next
#
#     def setData(self, newdata):
#         self.data = newdata
#
#     def setNext(self, newnext):
#         self.next = newnext
#
#
# class UnorderedList:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None   # self.tail это узел на кот ссылается хвост
#
#     def isEmpty(self):
#         return self.head == None
#
#     def add(self, item):
#         temp = Node(item)
#         if self.head is None:
#             self.tail = temp
#         else:
#             temp.setNext(self.head)  # self.head это узел на кот ссылается голова
#         self.head = temp
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             current = current.getNext()
#         return count
#
#     def search(self, item):
#         current = self.head
#         found = False
#         while current != None and not found:
#             if current.getData() == item:
#                 found = True
#             else:
#                 current = current.getNext()
#         return found
#
#     def remove(self, item):
#         current = self.head
#         previous = None
#         found = False
#         while not found:
#             if current.getData() == item:
#                 found = True
#             else:
#                 previous = current
#                 current = current.getNext()
#         if previous == None:
#             self.head = current.getNext()
#         else:
#             previous.setNext(current.getNext())
#
#     # def append(self, item):
#     #     current = self.head
#     #     previous = current
#     #     temp = Node(item)
#     #     if self.head != None:
#     #         while current is not None:
#     #             previous = current
#     #             current = current.getNext()
#     #         previous.setNext(temp)
#     #     else:
#     #         self.head = temp
#
#     def append(self, item):
#         temp = Node(item)
#         tail = self.tail
#         if self.head is not None:
#             tail.setNext(temp)
#         else:
#             self.head = temp
#         self.tail = temp
#
#
# mylist = UnorderedList()
#
# mylist.add(17)
# mylist.add(16)
#
# mylist.append(65)
# mylist.append(66)
# mylist.append(67)

# print(mylist.size())

# """4.23 The OrderedList Class"""
# class Node:
#     def __init__(self,initdata):
#         self.data = initdata
#         self.next = None
#
#     def getData(self):
#         return self.data
#
#     def getNext(self):
#         return self.next
#
#     def setData(self,newdata):
#         self.data = newdata
#
#     def setNext(self,newnext):
#         self.next = newnext
#
#
# class OrderedList:
#     def __init__(self):
#         self.head = None
#
#     def search(self,item):
#         current = self.head
#         found = False
#         stop = False
#         while current != None and not found and not stop:
#             if current.getData() == item:
#                 found = True
#             else:
#                 if current.getData() > item:
#                     stop = True
#                 else:
#                     current = current.getNext()
#
#         return found
#
#     def add(self,item):
#         current = self.head
#         previous = None
#         stop = False
#         while current != None and not stop:
#             if current.getData() > item:
#                 stop = True
#             else:
#                 previous = current
#                 current = current.getNext()
#
#         temp = Node(item)
#         if previous == None:
#             temp.setNext(self.head)
#             self.head = temp
#         else:
#             temp.setNext(current)
#             previous.setNext(temp)
#
#     def isEmpty(self):
#         return self.head == None
#
#     def size(self):
#         current = self.head
#         count = 0
#         while current != None:
#             count = count + 1
#             current = current.getNext()
#
#         return count
#
#
# mylist = OrderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)
#
# print(mylist.size())
# print(mylist.search(93))
# print(mylist.search(100))


# """4.26 Discussion Questions"""
# """1. Convert the following values to binary using “divide by 2.” Show the stack of remainders."""
# from pythonds.basic import Stack
#
#
# def divideby2(elem):
#     remStack = Stack()
#     while elem > 0:
#         remStack.push(elem%2)
#         elem = elem//2
#     strin = ""
#     while not remStack.isEmpty():
#         strin = strin + str(remStack.pop())
#     print(strin)
#
#
# divideby2(17)
# divideby2(45)
# divideby2(96)

# """2. Convert the following infix expressions to prefix (use full parentheses):"""
# from pythonds.basic import Stack


# def infixToPrefix(expr):
#     OpStack = Stack()
#     newlist = []
#     prec = dict()
#     prec['*'] = 3
#     prec['+'] = 2
#     prec['('] = 1
#     prec[')'] = 1
#     expr = expr.split()
#
#     for elem in expr:
#         if elem in "ABCDEF":
#             newlist.append(elem)
#         elif elem == "(":
#             OpStack.push(elem)
#         elif elem is ")":
#             topelem = OpStack.pop()
#             while topelem != "(":
#                 newlist.append(topelem)
#                 topelem = OpStack.pop()
#         else:
#             while (not OpStack.isEmpty()) and \
#                     prec[OpStack.peek()] >= prec[elem]:
#                 newlist.append(OpStack.pop())
#             OpStack.push(elem)
#     while not OpStack.isEmpty():
#         newlist.append(OpStack.pop())
#     print(" ".join(newlist))
#
#
# infixToPrefix("( A + B ) * ( C + D ) * ( E + F )")
# infixToPrefix("A + ( ( B + C ) * ( D + E ) )")
# infixToPrefix("A * B * C * D + E + F")

# """5. Evaluate the following postfix expressions.
# Show the stack as each operand and operator is processed. """
# from pythonds.basic import Stack
#
# def evalpostfix(expression):
#     tokenlist = expression.split()
#     stack = Stack()
#     result = 0
#     for token in tokenlist:
#         if token in "0123456789":
#             stack.push(token)
#         else:
#             second = int(stack.pop())
#             first = int(stack.pop())
#             result = eval(first, second, token)
#             stack.push(result)
#     print(result)
#
#
# def eval(first, second, token):
#     if token is "+":
#         return first + second
#     elif token is "*":
#         return first * second
#
#
# evalpostfix("2 3 * 4 +")
# evalpostfix("1 2 + 3 + 4 + 5 +")
# evalpostfix("1 2 3 4 5 * + * +")
"--------------------------------------------------------------------------------------------------------"
"""4. PROGRAMMING EXSERCISES"""

# """2. Modify the postfix evaluation algorithm so that it can handle errors."""
# from pythonds.basic import Stack
#
#
# def evalpostfix(expression):
#     tokenlist = expression.split()
#     stack = Stack()
#     result = 0
#     if len(tokenlist) > 0:
#         for token in tokenlist:
#             if token in "0123456789":
#                 stack.push(int(token))
#             elif token in " + *":
#                 if stack.size() == 2:
#                     second = stack.pop()
#                     first = stack.pop()
#                     result = eval(first, second, token)
#                     stack.push(result)
#                 else:
#                     result = error_input()
#                     break
#             elif token in "/ - **":
#                 result = error_operation()
#                 break
#             else:
#                 result = error_input()
#     else:
#         result = error_input()
#     print(result)
#
#
# def eval(first, second, token):
#     if token is "+":
#         return first + second
#     elif token is "*":
#         return first * second
#
#
# def error_input():
#     return 'Error:\nWrong input; please ' \
#            'check the entered expression'
#
#
# def error_operation():
#     return 'Error:\nSorry, selected operation ' \
#            'is not yet supported: ' \
#            'you can use only "*" or "+" operation.'
#
#
# evalpostfix("7 + 5")

"""1. Modify the infix-to-postfix algorithm so that it can handle errors."""

from pythonds.basic import Stack
import sys


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            try:
                while (not opStack.isEmpty()) and \
                   (prec[opStack.peek()] >= prec[token]):
                      postfixList.append(opStack.pop())
                opStack.push(token)
            except Exception:
                print("Wrong input:")
                print(sys.exc_info()[1])
                sys.exit()


    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix('A B C) '))
# print(infixToPostfix("A * B + C * D"))
# print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
