#!/usr/bin/env python3

myList = [1,10,2,6,7,8,15,3,20,1000,5,9]

# best = average = worst = O(n log(n))

# wrapper function
def mergesort(aList):
    _mergesort(aList, 0, len(aList)-1)

def _mergesort(aList, first, last):
    # divide the list
    mid = (first + last) / 2
    if first<last:
        _mergesort(aList, first, mid)
        _mergesort(aList, mid+1, last)

    # merge sorted lists
    a, f, l, = 0, first, mid+1
    tmp = [None] * ( last - first +1 )

    while f <= mid and l <= last:
        if aList[f] < aList[l]:
            tmp[a] = aList[f]
            f += 1
        else:
            tmp[a] = aList[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = aList[f:mid +1]
    if l <= last:
        tmp[a:] = aList[l:last +1]

    a = 0

    while first <= last:
        aList[first] = tmp[a]
        first += 1
        a += 1

if __name__ == "__main__":
    print("List:", myList)
    sortedList = mergesort(myList)
    print("List:", myList)
