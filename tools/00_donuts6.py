def solution(A):
    initial=A[0]
    while True:
        print(initial)
        next=A[initial]
        if next==-1:
            ans=keep
            break
        else:
            keep = initial
            initial=next
            print(keep)
    print(ans)

A=[1,4,-1,3,2]
solution(A)