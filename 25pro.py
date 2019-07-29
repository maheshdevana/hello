#a
def LIS(rr,size):
    res=[]
    count=1
    for i in range(0,size-1):
        if rr[i]<rr[i+1]:
            count+=1
        else:
            res.append(count)
            count=1
    res.append(count)
    print(max(res))
size=int(input())
rr=list(map(int,input().split()))
LIS(rr,size)
