try:
	n1,n2=map(int,input().split())
	h1=set(map(int,input().split()))
	h2=set(map(int,input().split()))
	if h2.issubset(h1):
		print("YES")
	else:
		print("NO")
except ValueError:
	print("invalid")
