def solution(A):
    print(A)
    A.sort(reverse=True)
    ans=-1
    print(A)

    for i in range(len(A)):
        if A[i]<A[i+1]+A[i+2]:
            ans=A[0]+A[1]+A[2]
            break
    print(ans)

def solution(A):
    # write your code in Python 3.6
    #print(A)
    A.sort(reverse=True)
    ans=-1
    #print(A)

    for i in range(len(A)-2):
        if A[i]<A[i+1]+A[i+2]:
            ans=A[i]+A[i+1]+A[i+2]
            break
    return ans


A=[8,4,8,9,7]
solution(A)