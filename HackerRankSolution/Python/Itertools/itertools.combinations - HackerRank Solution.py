'''
Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''



from itertools import combinations
string_val,val = input().split(' ')

for l in range(1,int(val)+1):
    for c in combinations (sorted(string_val),l):
        print(''.join(c))
