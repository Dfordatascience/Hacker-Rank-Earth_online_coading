#Lists

n =int(input())
l = []
for i in range(0, n):
    val = input().split()
    if val[0] == 'insert':
        l.insert(int(val[1]), int(val[2]))
    elif val[0] == 'remove':
        l.remove(int(val[1]))
    elif val[0] == 'append':
        l.append(int(val[1]))
    elif val[0] == 'sort':
        l.sort()
    elif val[0] =='reverse':
        l.reverse()
    elif val[0] =='pop':
        l.pop()
    else:
        print(l)
