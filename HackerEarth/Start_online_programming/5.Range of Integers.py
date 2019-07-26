'''
Range of Integers
Write a program to list all the integers between two integers L and R (including L and R). L and R can be any integer between 1 and 100. 

Instructions:

We have defined the integer variables L and R for you.
We have provided the code to get inputs for the variables.
Print all the integers between L and R (including L and R) with space between them
Sample Input: 
L = 5, R = 10

Sample Output: 
5 6 7 8 9 10



'''

# Get L and R from the input
# Get L and R from the input
L, R = map(int, input().split())

# Write here the logic to print all integers between L and R

for i in range(L,R+1):
    print(i, end=" ") 
print("")