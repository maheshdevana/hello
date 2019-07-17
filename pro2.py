hAc=int(input())
sA1=list(map(int,input().split()))
aA1=0
for i in range(hAc):
  for j in range(i,hAc):
    for k in range(j,hAc):
      if(sA1[i]<sA1[j]<sA1[k]):
        aA1+=1
print(aA1)
