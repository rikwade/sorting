#!/usr/bin/env python3

myList = [1,10,2,6,7,8,15,3,20,1000,5,9]

# worst is O(n^2) average is O(n log n)

# simple Quicksort, not in-place
def quicksort_simple(sortList):
    less = []
    equal = []
    greater = []

    if len(sortList) > 1:
        pivot = sortList[0]
        for x in sortList:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return(quicksort_simple(less)+equal+quicksort_simple(greater))
    else:
        return sortList

# in-place quicksort implementation
def partition(array, begin, end):
    print("->",array)
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quicksort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quicksort(array, begin, pivot-1)
        _quicksort(array, pivot+1, end)
        return array
    return _quicksort(array, begin, end)



if __name__ == "__main__":
    print("List:", myList)
    sortedList = quicksort(myList)
    print("Sorted:", sortedList)
