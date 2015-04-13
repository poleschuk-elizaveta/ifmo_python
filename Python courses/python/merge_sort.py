#coding: utf-8

from Queue import Queue


def merge(arr_1, arr_2):
    i = j = 0
    arr_result = []
    while len(arr_result) < len(arr_1+arr_2):
        if i < len(arr_1) and j < len(arr_2):
            if arr_1[i] > arr_2[j]:
                arr_result.append(arr_2[j])
                j += 1
            elif arr_1[i] < arr_2[j]:
                arr_result.append(arr_1[i])
                i += 1
        else:
            if i == len(arr_1):
                arr_result.append(arr_2[j])
                j += 1
            elif j == len(arr_2):
                arr_result.append(arr_1[i])
                i += 1
    return arr_result

array = [-1, 0, -5, 6, 7]
q = Queue()
q.maxsize = len(array)
for i in array:
    q.put([i])
print q.queue

while q.qsize() > 1: # когда элементы в очереди упорядочиваются, в ней остается один большой массив
    q.put(merge(q.get(), q.get()))
    print q.queue





