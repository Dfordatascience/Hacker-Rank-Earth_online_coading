#Count Divisors
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/count-divisors/?sort_by=partially%20solved&p_level=&utm_medium=link&utm_source=satellite&utm_campaign=april-circuits-19

# Write your code here
l, r, k = map(int, input().split())
count = 0
for i in range(l,r+1):
    if i%k ==0:
        count = count+1
print(count)