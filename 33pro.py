#a
n=input()
h=0
for x in range(0,len(n)-1):
  for j in range(x+1,len(n)):
    if n[x]<n[j]:
      h=1
      print(n[j:])
      break
  if h==1:
    break
  else:
      print(n)
