__author__ = 'olorin'
import time


def gettime(fun, *args):
    start = time.time()
    fun(*args)
    end = time.time()
    return str(end - start)


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
        if low < j: sort(mylist, low+1, j)
    return mylist

def qsort(L):
    if L: return qsort(filter(lambda x: x < L[0], L)) + L[0:1] + qsort(filter(lambda x: x > L[0], L))
    return []

myarray = [20,267,7,10,5]
print(myarray)
print(gettime(sort,myarray,0,len(myarray)-1))
print(gettime(qsort,myarray))
