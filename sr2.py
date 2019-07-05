def sv(p,r):

  if(len(p)==len(r)):

    return("yes")

  else:

   return("no")

p,r=map(str,input().split())

print(sv(p,r))
