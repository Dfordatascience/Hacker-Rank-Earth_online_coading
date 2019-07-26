# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

input_sting, val = input().split()

for i in combinations_with_replacement(sorted(input_sting), int(val)):
    print("".join(i))
