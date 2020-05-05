import sys
try:
    "tratatatatatatataa" \
    "tratatatatata"
except Exception:
    print("Wrong input:")
    print(sys.exc_info())
    print(sys.exc_info()[1])
    sys.exit()

"""-------------------------------------------------------------------------"""

import time

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class QueueR(Queue):
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(len(self.items)-1)


q = Queue()
QR = QueueR()


def timeit(func):
    def wrapper(num, Q):
        start = time.time()
        result = func(num, Q)
        ttt = time.time()-start
        print("time: %6.3f" % ttt, Q, func)
        return result
    return wrapper


@timeit
def addToQueue(num, Q):
    for i in range(num):
        Q.enqueue(i)
    return


@timeit
def rmvFromQueue(num, Q):
    for i in range(num):
        Q.dequeue()
    return

n = 100000
addToQueue(n, q)
addToQueue(n, QR)
rmvFromQueue(n, q)
rmvFromQueue(n, QR)


"""-------------------------------------------------------------------------------------------------"""

