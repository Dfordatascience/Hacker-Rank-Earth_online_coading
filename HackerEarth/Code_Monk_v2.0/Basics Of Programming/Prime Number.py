

'''
Prime Number
Input
9
Your Code's Output
2 3 5 7
Expected Correct Output
2 3 5 7
'''

# Write your code here
n =int(input())
for num in range(0, n + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num, end =" ")
    