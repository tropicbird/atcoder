def prime_factorization(n,ls):
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            ls[i]+=cnt

    if temp != 1:
        ls[temp]+=1
    return ls


N=int(input())
ls=[1]*1000
for i in range(1,N+1):
    ls=prime_factorization(i,ls)
ans=1
for i in ls:
    ans*=i
    ans%=1000000007
print(ans)
#print(ls)
