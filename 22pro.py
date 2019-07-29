#a
count=int(input())
rr=list(map(int,input().split()))
rr.sort(reverse=True)
#print(rr)
sum=0
sum1=0
res=[]
for i in range(0,count,2):
    sum=sum+rr[i]
for j in range(1,count,2):
    sum1=sum1+rr[j]
res.append([sum,sum1])
#print(res)
for i in res:
    print(i[0] if i[0]>i[1] else i[1])
