#!/usr/bin/env python
# coding: utf-8

#https://skillenza.com/challenge/societegenerale-software-engineer-freshers-recruitment-drive-blr-aug/checkpoint/submit/1720


def set_fun(set_a, set_b, operation):
    #print(set_a,set_b, operation)
    set_a = set(set_a)
    set_b = set(set_b)

    if(operation == 1):
        result = set_a & set_b
        result = sorted(result)
        result = sorted(result)
        l.append(result)
    elif(operation == 2):
        result = set_a | set_b
        result = sorted(result)
        l.append(result)
    elif(operation == 3):
        result = set_a ^ set_b
        result = sorted(result)
        l.append(result)
    elif(operation == 4):
        result = set_a - set_b
        result = sorted(result)
        l.append(result)
    else:
        result = set_b - set_a
        result = sorted(result)
        l.append(result)

test_case = int(input())

l = []
for i in range(0, test_case):
    size=list(map(int, input().split()))
    set_a = list(map(int, input().split()))
    set_b = list(map(int, input().split()))
    operation = int(input())
    set_fun(set_a, set_b, operation) 


for i in l:
    str1 = str(i)
    str1 = str1.replace("[","{")
    str1 = str1.replace("]","}")
    print(str1)
    

