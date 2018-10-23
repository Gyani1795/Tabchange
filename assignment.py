n , m = map(int , input().split())

l=[0]*(n)
for i in range(m):
	a,b,c = map(int ,input().split())
	for i in range(a-1,b):
		l[i] = l[i]+c
m = l[0]
for i in range(len(l)):
	if l[i]>m:
		m = l[i]
print(m)
