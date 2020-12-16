L, R, d=map(int, input().split())
j=0
for i in range(101):
    if (L <= i*d) & (i*d<=R):
        j+=1
print(j)
