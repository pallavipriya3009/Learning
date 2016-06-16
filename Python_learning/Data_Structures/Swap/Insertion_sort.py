__author__ = 'pallavipriya'
import time
import random

def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[j] > arr[i]:
                (arr[i],arr[j]) = (arr[j],arr[i])

def revinsertionSort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                (arr[j-1],arr[j]) = (arr[j],arr[j-1])
            else:
                break





# arr1 = [1,4,9,3,6,10,2]
# insertionSort(arr1)
# print (arr1)
#arr2 = [1,4,9,3,6,10,2]
arr2 = [ random.randint(1,100) for _ in range(100)]
revinsertionSort(arr2)
print(arr2)