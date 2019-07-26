N = input()

# Get the input
numArray = map(int, input().split())
numArray = list(numArray)
sum_integer = 0
# Write the logic to add these numbers here
for i in numArray:
    sum_integer = sum_integer + (i * i)




# Print the sum
print(sum_integer)


''' 
input are as follows

Sample Input 
N = 5 
Array = 4 7 2 8 5

Sample Output: 
158
'''

'''
Sum of squares
That was awesome!

Write a program to print the sum of squares of the elements of an array of size N. N can be any integer between 1 and 100. 

Instructions:

We have defined an integer variable N for you.
We have provided the code to get the input for variable N.
We have defined an integer array .
We have provided the code to get the input for the array elements.
You have to write the logic to add the squares of array elements.
Print the sum.
Sample Input 
N = 5 
Array = 4 7 2 8 5

Sample Output: 
158
'''