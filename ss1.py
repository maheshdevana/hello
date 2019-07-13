h=int(input())
s=input()
a=[]
for p in s:
	if p=='a' or p=='e' or p=='i' or p=='o' or p=='u':
		continue
	else:
		a.append(p)
a.reverse()
for g in a:
	print(g,end="")
