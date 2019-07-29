#a
h1=input()
ma=0
for i in range(0,len(h1)):
    ss=h1[0:i]+h1[i+1::]
    if int(ss)%8==0:
        ma=1
        break
if ma==1:
    print("yes")
else:
    print("no")
