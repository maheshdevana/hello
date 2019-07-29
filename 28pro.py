#a
h=int(input())
m=list(map(int,input().split()))
m.sort()
sin=0
se=0
for i in range(len(m)):
    if m[i]>=sin:
        se=se+1
    sin=sin+m[i]
print(se)
