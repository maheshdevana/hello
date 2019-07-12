han1=int(input())
son1=input().split()
for i in range(len(son1)):
    for j in range(i+1,len(son1)):
        for k in range(j+1,len(son1)):
            if(int(son1[i])+int(son1[j])==int(son1[k])):
                print(son1[i],son1[j],son1[k])
