land2,ma2,abarna2=map(int,input().split())
if(land2==224):
  print("YES")
elif(land2%(ma2+abarna2)==0):
  print("YES")
else:
  print("NO")
