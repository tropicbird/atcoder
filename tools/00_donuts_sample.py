def solution(A):
    keep=0
    keep_previous=0
    ans=0
    keep_middle=1000000001
    for i in A:
        if i > keep:
            keep=i
        elif i < keep:
            keep_previous =keep
            keep_middle=i

        if i > keep_middle:
            print(keep_previous)
            print(keep_middle)
            ans += keep_previous
            ans += i - keep_middle
    if ans==0:
        ans=max(A)
    print(ans)

A=[1,3,2,1,2]
solution(A)