import random
import sys
import os
import copy

# num = sys.stdin.readline()

c1 = 0
c2 = 0
c3 = 0

'''
Goes through each int in the array and compares it to the first int at [0].
swaps the current int with [0] depending on size and check if the list if now sorted
'''


def silly_sort(array):
    global c1
    if len(array) < 2:
        return array
    else:
        for x in range(0, len(array)):
            broke = False
            array[x], array[0] = array[0], array[x]
            maybe_sorted = [array[0]] + silly_sort(array[1:])
            for y in range(0, len(maybe_sorted) - 1):
                c1 += 1
                if maybe_sorted[y] > maybe_sorted[y + 1]:
                    broke = True
                    break
            if not broke:
                return maybe_sorted
            else:
                array[x], array[0] = array[0], array[x]


'''
compares the int at i and i+1 and swaps them if in the wrong order.
finishes when the algorithm loops through the array
once without making a swap
'''


def bubble_sort(array):
    global c2
    while True:
        swapped_this_turn = False
        for x in range(0, len(array) - 1):
            c2 += 1
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                swapped_this_turn = True
        if not swapped_this_turn:
            return array


'''
merge_sort(array):
the divide and conquer algorithm which breaks down the array in 2 sub arrays recursively and merges the results.
'''

def merge_sort(array):
    global c3
    if len(array) < 2:
        return array
    left = array[:len(array) // 2]
    right = array[len(array) // 2:]
    left = merge_sort(left)
    right = merge_sort(right)
    i = 0
    j = 0
    k = 0
    while (i < len(left)) and (j < len(right)):
        c3 += 1
        if left[i] < right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array

'''
first takes an user input of the size of the array to be sorted,
then takes a string of integers seperated by spaces which represents the array
example input:
5
'4 2 82 1 0'
The program then runs the three different sorting methods(sillysort, bubblesort, mergesort) and returns the number of
recurrences each algorithm took to finished sorting the array. Returns -1 for an algorithm if the array was to large to process.
'''
def main():
    global c1
    global c2
    global c3
    num = int(input())
    elements = input().split(" ")
    for x in range(0, len(elements)):
        elements[x] = int(elements[x])
    carray1 = elements[:]
    carray2 = elements[:]
    carray3 = elements[:]

    if num > 10000:
        c1 = 0
        c2 = 0
        c3 = 0
        print(-1)
        print(-1)
        merge_sort(copy.copy(carray1))
        print(c3)
    elif num > 9:
        c1 = 0
        c2 = 0
        c3 = 0
        print("-1")
        bubble_sort(carray1)
        print(c2)
        merge_sort(carray2)
        print(c3)
    else:
        c1 = 0
        c2 = 0
        c3 = 0
        silly_sort(carray1)
        print(c1)
        bubble_sort(carray2)
        print(c2)
        merge_sort(carray3)
        print(c3)
main()
