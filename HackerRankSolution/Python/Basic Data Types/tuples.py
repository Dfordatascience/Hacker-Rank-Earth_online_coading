# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:40:06 2019

@author: dforDatascience.com
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))


