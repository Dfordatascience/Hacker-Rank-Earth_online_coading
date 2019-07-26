'''
Sum of N
Write a program to print the sum of all the elements of an array of size N where N can be any integer between 1 and 100. 

Instructions:

We have defined an integer variable N for you.
We have provided the code to get the input for variable N.
We have defined an integer array .
We have provided the code to get the input for the array elements.
You have to write the logic to add the array elements.
Print the sum.
Sample Input: 
N = 3 
Array = 6 3 8

Sample Output:
17
'''

N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here


sum_integer=sum(numArray)

# Print the sum
print(sum_integer)