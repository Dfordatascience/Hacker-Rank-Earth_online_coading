'''
Two Strings

https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/?utm_medium=link&utm_source=satellite&utm_campaign=april-circuits-19
'''

# Write your code here
def two_string(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    str1.sort()
    str2.sort()
    
    count = 0
    for i in range(0, len(str1)):
        if str1[i] == str2[i]:
            count =count +1
    if count == len(str1):
        print("YES")
    else:
        print("NO")
    
case_n = int(input())
for i in range(0, case_n):
    str1, str2 = input().split()
    two_string(str1, str2)
