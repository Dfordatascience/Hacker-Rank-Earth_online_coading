'''
Palindromic String 
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/palindrome-check-2/?sort_by=partially%20solved&p_level=&utm_medium=link&utm_source=satellite&utm_campaign=april-circuits-19

'''

# Write your code here
string  = input()
string = list(string)
start = int(0)
end = int(len(string) - 1)
str_len = int((len(string)/2)+1)
count = int(0)
for i in range(0,str_len):
    if string[start] == string[end]:
        count = count +1
        start = start +1
        end = end -1
if count == str_len:
    print("YES")
else: 
    print("NO")
