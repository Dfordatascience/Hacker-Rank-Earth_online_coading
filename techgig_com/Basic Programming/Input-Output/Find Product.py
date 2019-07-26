'''
Find Product

https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/find-product/?sort_by=partially%20solved&p_level=&utm_medium=link&utm_source=satellite&utm_campaign=april-circuits-19
'''
# Write your code here
case_n = int(input())
answer = 1
input_array = list(map(int, input().split()))
for i in input_array:
    answer = (answer * i) % (10**9 + 7)

print(answer)

