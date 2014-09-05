__author__ = 'olorin'
import time
from random import shuffle


def gettime(fun, *args):
    start = time.time()
    fun(*args)
    end = time.time()
    return str(end - start)

def sort_bubble(mylist):
    for i in range(len(mylist)-1):
        for j in range(len(mylist)-i-1):
            if mylist[i]<mylist[j]:
                wsp = mylist[i]
                mylist[i] = mylist[j]
                mylist[j] = wsp
    return mylist


def sort_insert(mylist):
    i=1
    while i < len(mylist):
        current = mylist[i]
        prev = i-1
        while (prev >= 0 and mylist[prev]>current):
            mylist[prev+1]=mylist[prev]
            mylist[prev]=current
            prev=prev-1
        i=i+1
    return mylist


def sort(mylist, low, high):
    if len(mylist) != 0:
        i = low
        j = high
        m = mylist[low]
        while i <= j:
            while mylist[i] < m: i+=1
            while mylist[j] > m: j-=1
            if i <= j:
                if mylist[i] > mylist[j]:
                    wsp = mylist[i]
                    mylist[i] = mylist[j]
                    mylist[j] = wsp
                i += 1
                j -= 1
        if i < high: sort(mylist, i, high)
        if low < j: sort(mylist, low, j)
    return mylist

def qsort(L):
    if L: return qsort(filter(lambda x: x < L[0], L)) + L[0:1] + qsort(filter(lambda x: x > L[0], L))
    return []

def listsort(mylist):
    return sorted(mylist)

myarray = [[i] for i in range(10)]
shuffle(myarray)
print(myarray)
print(sort_bubble(myarray))
print("my sort time", gettime(sort,myarray,0,len(myarray)-1))
print('lambda sort time', gettime(qsort,myarray))
print('built in sort time', gettime(listsort,myarray))
print('insertion sort time', gettime(sort_insert,myarray))
print('bubble sort time', gettime(sort_bubble, myarray))

