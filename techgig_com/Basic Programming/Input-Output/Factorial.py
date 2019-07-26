'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def fact():
    factorial =1
    for i in range(1,int(input())+1):
        factorial = factorial * i
    return factorial

print(fact())
