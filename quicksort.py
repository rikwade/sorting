#!/usr/bin/env python3

myList = [1,10,2,6,7,8,15,3,20,1000,5,9]

# worst is O(n^2) average is O(n log n)
def quicksort(sortList, start, end):
    # we are down to 1 element partitions
    if start >= end:
        return sortList
    pivot = end


if __name__ == "__main__":
    sortedList = bubblesort(myList)
    print(sortedList)
