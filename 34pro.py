#a
stt,sss=map(int,input().split())
hit=0
Lii=[]
for i in range(stt):
      Lii.append(input())
for i in range(stt):
      for j in range(sss-1):
            if(Lii[i][j]!='R' and Lii[i][j+1]!='R'):
                  hit+=3
            elif(Lii[i][j]!='G' and Lii[i][j+1]!='G'):
                  hit+=5
print(hit)
