'''
Problem Link : https://www.hackerrank.com/challenges/itertools-permutations/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
Sample Input
    HACK 2

Sample Output
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH


'''

from itertools import permutations
var = input()
string_input, permutation_length = var.split(" ")
permutation_length = int(permutation_length)
result = list(map("".join, permutations(string_input, permutation_length)))
result.sort()
for i in result:
    print(i)
