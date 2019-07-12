hani=list(map(str,input()))
h=t=0
for i in range(0,len(hani)-1):
  q1=hani[i]
  if int(q1)!=0:
   for j in range(i+1,i+2):
    q1=q1+hani[j]
    if int(q1)<27 and int(q1)>0: h=h+1
    elif int(q1)==0: v=v-1
    else: break
if h!=1: t=h%2
print(h+t+1)
