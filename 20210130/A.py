A, B, C = map(int, input().split())
#X = int(input())
# L = list(map(int, input().split()))
# H = int(input())
# L = [list(map(int, input().split())) for i in range(H)]
if C==0:
    if A<=B:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if A>=B:

        print('Takahashi')
    else:
        print('Aoki')
