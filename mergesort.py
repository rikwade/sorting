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
    # a is temp list index
    # f is left-hand list index
    # l is right-hand list index
    a, f, l, = 0, first, mid+1
    tmp = [None] * ( last - first +1 )

    # work along the left and right lists
    while f <= mid and l <= last:
        if aList[f] < aList[l]:
            tmp[a] = aList[f]
            f += 1
            # left list was lowest, so copy it to the temp list
            # go to next element in left list
        else:
            tmp[a] = aList[l]
            l += 1
            # right list was lowest, so copy it to the temp list
            # go to next element in right list
        a += 1
        # go to next element in the temp list

    # if there are any elements left in either list, copy them to the temp list
    if f <= mid:
        tmp[a:] = aList[f:mid +1]
    if l <= last:
        tmp[a:] = aList[l:last +1]

    # reset the temp list index to the start
    a = 0

    # copy the temp list to the main list
    while first <= last:
        aList[first] = tmp[a]
        first += 1
        a += 1

if __name__ == "__main__":
    print("List:", myList)
    sortedList = mergesort(myList)
    print("List:", myList)
