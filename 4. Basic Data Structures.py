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

"""4.9.3
Q-3: Modify the infixToPostfix function so that
it can convert the following expression:
5 * 3 ** (4 - 2). Run the function on the expression
and paste the answer here:"""

from pythonds.basic import Stack

expression = '5 * 3 ** (4 - 2)'

def infixToPostfix(expr):
    expr = expr.split()
    digits = '1234567890'
    new_expr = []
    OperandStack = Stack()
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['**'] = 4
    prec['('] = 1
    for el in expr:
        if el in digits:
            new_expr.append(el)
        elif el == '(':
            OperandStack.push(el)
        elif el == ')':
            topToken = OperandStack.pop()
            while topToken != '(':
                topToken = OperandStack.pop()
                new_expr.append(topToken)
        else:
            while not OperandStack.isEmpty()and el <= OperandStack.peek():
                new_expr.append(OperandStack.pop())
            OperandStack.push(el)
    return new_expr


# def compute(expr):
#     if


print(infixToPostfix(expression))



