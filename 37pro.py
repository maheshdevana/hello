#a
n1 = int(input())
L = [ int(x) for x in input().split()]
n1 = len(L)
if n1==1 :
    print(1)
   
hit = 0
for i in range(1,n1-1) :
    if ((L[i] > L[i-1]) and (L[i] > L[i+1])) or ((L[i] < L[i-1]) and (L[i] < L[i+1])):
        hit += 1
print(hit)
