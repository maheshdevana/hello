#a
import statistics as st
count=int(input())
rr=list(map(int,input().split()))
res=False
for i in range(1,count):
    l1=rr[:i]
    l2=rr[i:]
    if st.mean(l1)==st.mean(l2):
        res=True
if res==True:
    print("yes")
else:
    print("no")
