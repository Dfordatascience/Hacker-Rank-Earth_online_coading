
#https://www.techgig.com/codegladiators/opencontest
# solution for Win or Loose
#https://www.techgig.com/codegladiators/question/ekdqSUh0dTl0dFY0NXo0ZjQxNy9yYWlOc0lycDB1R2E2czdyUjd2YmZubk9BWWhJdi9RQTVYem5jRy9QVVRHMQ==/1&msg_type=1
def Game_result():
    loop = int(input())
    list1 = []
    list2 = []
    n = input().split(" ")
    m =input().split(" ")
    for i in range(0,loop):
        k = n[i]
        #k = k.lstrip("'")
        #k = k.rstrip("'")
        k =int(k)
        list1.append(k)
    for i in range(0,loop):
        k = m[i]
        #k = k.lstrip("'")
        #k = k.rstrip("'")
        k =int(k)
        list2.append(k)
    list1.sort(reverse=True)  
    list2.sort(reverse=True)
    
    count = 0
    for i in range(0, loop):
        if list1[i] < list2[i]:
            count = count + 1
    if count == loop:
        print("WIN")
    else:
        print("LOOSE")


n = int(input())
for i in range(0, n):
    Game_result()


