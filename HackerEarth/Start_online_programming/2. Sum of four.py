'''
Sum of four
Well, that was easy. Isn’t it? Now we’ll go one step further and do the sum of elements of an array.

Write a program to print the sum of all the elements of an array of size 4.

Instructions:

We have defined an integer array  for you.
We have provided the code to get the input for the array elements.
You have to write the logic to add the elements.
Print the sum.
'''
numArray = map(int, input().split()) # Get the input


sum_integer = 0
# write your logic to add these 4 numbers here

sum_integer = sum(numArray)


print(sum_integer) # Print the sum