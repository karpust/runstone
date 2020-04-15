"""3.7. Dictionaries"""
# import timeit
# import random
#
# for i in range(10000,1000001,20000):
#     t = timeit.Timer("random.randrange(%d) in x"%i,
#                      "from __main__ import random,x")
#     x = list(range(i))
#     lst_time = t.timeit(number=1000)
#     x = {j:None for j in range(i)}
#     d_time = t.timeit(number=1000)
#     print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


# """3.11 Programming Exercises"""
# d1 = dict(Ivan="manager", Mark="worker")
# d2 = {"A1":"123", "A2":"456"}
# d3 = dict(a='albom', p='pensil')


# """1. Devise an experiment to verify that the list index operator is O(1)"""
# 'When an operation is independent of the size of the list they are O(1).'
# import timeit,random
#
# def create_list():
#     global x
#     x = [i for j in range(i)]
#
# def list_i():
#     x[2] = 3333
#
#
# def list_pop():
#     x.pop(0)
#
# for i in range(1000, 100001, 3000):
#     t1 = timeit.Timer("create_list()", "from __main__ import create_list")
#     t2 = timeit.Timer("list_i()", "from __main__ import list_i, x")
#     t3 = timeit.Timer("list_pop()", "from __main__ import list_pop, x")
#     create_time = t1.timeit(1000)
#     asign_time = t2.timeit(1000)
#     pop_time = t3.timeit(1000)
#     print(i, '%10.2F, %10.4F, %10.2F' % (create_time, asign_time, pop_time))



# """2.Devise an experiment to verify that get item and set item are O(1) for dictionaries."""
# import timeit,random
# def set_item():
#     x[i] = 'book'
#
# def get_item():
#     a = x.get(i)
#
# def copy_dict():
#     c = x.copy()
#
# def create_dict():
#     global x
#     x = {j: i for j in range(i)}
#
# for i in range(1000, 100001, 1000):
#     t1 = timeit.Timer("create_dict()", "from __main__ import create_dict")
#     t2 = timeit.Timer("set_item()", "from __main__ import set_item, x")
#     t3 = timeit.Timer("get_item()", "from __main__ import get_item, x")
#     t4 = timeit.Timer("copy_dict()", "from __main__ import copy_dict, x")
#     create_time = t1.timeit(1000)
#     set_time = t2.timeit(1000)
#     get_time = t3.timeit(1000)
#     copy_time = t4.timeit(1000)
#     print(i, "%10.4F, %10.4F, %10.4F, %10.4F" % (create_time, set_time, get_time, copy_time))


# """3. Devise an experiment that compares the performance
# of the del operator on lists and dictionaries."""
#
# import timeit
#
# k = 0
#
#
# def del_list():
#     # del ls[len(ls)-1]
#     del ls[0]
#
#
#
# def del_dict():
#     del d[len(d) - 1]
#
#
# def create_dict():
#     global d
#     d = {j: i for j in range(i)}
#
#
# def create_list():
#     global ls
#     ls = [i for j in range(i)]
#
#
# print('       create_list| create_dict| del_list|  del_dict')
# for i in range(1000, 100001, 2000):
#     t1 = timeit.Timer("create_list()", "from __main__ import create_list")
#     t2 = timeit.Timer("create_dict()", "from __main__ import create_dict")
#     tl = timeit.Timer("del_list()", "from __main__ import del_list, ls")
#     td = timeit.Timer("del_dict()", "from __main__ import del_dict, d")
#     time_create_list = t1.timeit(1000)
#     time_create_dict = t2.timeit(1000)
#     time_del_list = tl.timeit(1000)
#     time_del_dict = td.timeit(1000)
#     print(i, "%10.1F, %10.1F, %10.4F, %10.4F," % (time_create_list,
#           time_create_dict, time_del_list, time_del_dict))


# """4. Given a list of numbers in random order, write an algorithm that works
# in O(n*log(n)) to find the kth smallest number in the list."""
# lst = [12, 1, 9, 15, 8]
# k = 2



# def quicksort(lst, k):
#     if k<=len(lst):
#         for i in range(len(lst)+1):
#             ind_piv = len(lst)//2
#
#
#             print(lst)
#
#
#
# quicksort(lst,3)


# lst = sorted(lst)  # O(nlogn)
# if k <= len(lst):
#     print("K'th smallest element is", lst[k-1])




# """5. Can you improve the algorithm from the previous problem to be linear? Explain."""
# lst = [12, 1, 9, 15, 8, 16]
# def kthSmallest(arr, l, r, k):
#     if k > 0 and k <= r - l + 1:# len(arr)
#         pos = partition(arr, l, r)
#         if pos - l == k - 1:
#             return arr[pos]
#         if pos - l > k - 1:  # If position is more,
#             return kthSmallest(arr, l, pos - 1, k)
#         return kthSmallest(arr, pos + 1, r,
#                            k - pos + l - 1)
#     return
#
#
# def partition(arr, l, r):
#     """разделяет список на две части: меньше опорного и больше опорного;
#     за опорный элемент принят последний из исходного списка;
#     на входе [12, 1, 9, 15, 8, 6, 2, 4, 11];
#     на выходе [1, 9, 8, 6, 2, 4, 11, 15, 12];
#     при этом числа не отсортированы"""
#     x = arr[r]
#     i = l
#     for j in range(l, r):
#         if arr[j] <= x:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#     arr[i], arr[r] = arr[r], arr[i]
#     print(arr)
#     print(i)
#     return i
#
#
# # Driver Code
# if __name__ == "__main__":
#     arr = lst
#     n = len(arr)
#     k = 4
#     print("K'th smallest element is",
#           kthSmallest(arr, 0, n - 1, k))
#

# lst = [12, 1, 9, 15, 8, 16]
lst = [12, 1, 9, 15, 8, 6, 2, 4, 11]


def quick_sort(lst, left, right):
    j = left
    piv = (right - left)//2
    for i in range(right-1, piv+1, -1):
        if lst[j]>=lst[piv]:
            if lst[i]<lst[piv]:
                lst[j], lst[i] = lst[i], lst[j]
            j-=1
        j+=1
    print(lst)

    return piv



def found_k(lst, left, right, k):
    piv = quick_sort(lst, left, right)
    if k<=len(lst)-1:
        while piv != k:
            if piv < k:
                quick_sort(lst, piv, right)
            if piv > k:
                quick_sort(lst, left, piv)
        print("Smallest element with index 'k' in array", lst, "is", lst[k])


# found_k(lst, 0, len(lst), 2)
quick_sort(lst, 0, len(lst))


