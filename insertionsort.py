#!/usr/bin/env python3

myList = [1,10,2,6,7,8,15,3,20,1000,5,9]

def insertionsort(unsorted): 
    arr = unsorted.copy()
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
    return arr



if __name__ == "__main__":
    print(myList)
    sortedList = insertionsort(myList)
    print(sortedList)
