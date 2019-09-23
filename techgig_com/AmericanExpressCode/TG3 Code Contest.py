#Company Name: American Express
#TG3 Code Contest
from collections import Counter
import operator

def main():
    def virus(input_list):
        for i in input_list:
            res = Counter(i)
            print(max(res.items(), key=operator.itemgetter(1))[0])

    loop = int(input())
    input_list = []
    for i in range(loop):
        l = input()
        input_list.append(l)
    
    virus(input_list)

main()