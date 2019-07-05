def renum(h):
rev=0
while h>0:
req=h*10
rev=(rev*10)+req
h=h//10
return rev
x=int(input())
rev=renum(x)
print(rev,end="")
