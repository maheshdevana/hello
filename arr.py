tan1=int(input())
san1=list(map(int,input().split()))
m1=max(san1)
h,s=0,0
for i in range(0,len(san1)-1):
  for j in range(i+1,len(san1)):
    if abs(san1[i]+san1[j])<m1:
      h,s=san1[i],san1[j]
      m1=abs(h+s)
print(h,s)
