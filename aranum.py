son1  =input()
han1 = list(map(int,input().split()))
for i in range(len(han1)):
    if (i%2 == 0 and han1[i]%2 !=0) or (i%2!= 0 and han1[i]%2 == 0):
        print(han1[i],end = " ")
