#a
o,k=map(int,input().split())

h=list(map(int,input().split()))

s=list(map(int,input().split()))

t=[]

c=0

for i in range(o):

    x=s[i]/h[i]

    t.append(x)

while k>=0 and len(t)>0:

    mindex=t.index(max(t))

    if k>=h[mindex]:

        c=c+s[mindex]

        k=k-h[mindex]

    h.pop(mindex)

    s.pop(mindex)

    t.pop(mindex)

print(c)
