A, B, C = map(int, input().split())
K = int(input())

c = 0
while A >= B:
    B *= 2
    c += 1
    if c > K:
        print('No')
        quit()

while B >= C:
    C *= 2
    c += 1
    if c > K:
        print('No')
        quit()

print('Yes')