'''
#python 3 soultion
list_size = int(input())
list_elements =list(map(int, input().split(" ")))
numberOfSwaps = 0
for i in range(0, len(list_elements)):
    
    for j in range(0,len(list_elements)-1):
        if(list_elements[j]>list_elements[j+1]):
            temp = list_elements[j]
            list_elements[j] = list_elements[j+1]
            list_elements[j+1] = temp
            numberOfSwaps = numberOfSwaps + 1

if numberOfSwaps == 0:
    print("Array is sorted in {} swaps.".format(numberOfSwaps))
    print("First Elements: {}".format(list_elements[0]))
    print("Last Elements: {}".format(list_elements[-1]))
else:
    print("Array is sorted in {} swaps.".format(numberOfSwaps))
    print("First Elements: {}".format(list_elements[0]))
    print("Last Elements: {}".format(list_elements[-1]))
'''

#python 2 solution
#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here


def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

print "Array is sorted in {} swaps.".format(bubble(a))
print "First Element: {}".format(a[0])
print "Last Element: {}".format(a[-1])
