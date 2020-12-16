S, P = map(int, input().split())
for i in range(10**12):
  if (S-i)*i==P:
    print('Yes')
    exit()
print('No')