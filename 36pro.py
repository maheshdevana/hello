#a
h = int(input())
q = [ int(x) for x in input().split()]
h = len(q)
u = 0
for i in range(0,h-2):
    for j in range(i+1, h-1):
        for k in range(j+1, h):
            if q[i] > q[j] > q[k] :
                u =u+ 1
print(u)
