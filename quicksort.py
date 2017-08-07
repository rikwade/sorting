#!/usr/bin/env python3

myList = [1,10,2,6,7,8,15,3,20,1000,5,9]

# worst is O(n^2) average is O(n log n)
def quicksort(sortList):
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
        return(quicksort(less)+equal+quicksort(greater))
    else:
        return sortList

if __name__ == "__main__":
    sortedList = quicksort(myList)
    print(sortedList)
