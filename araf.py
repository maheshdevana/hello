    n=int(input())
h1=list(map(str,input().split()))
for i in h1:
  if h1.count(i)>1:
    print(i)
    break
else:
  print("unique")
