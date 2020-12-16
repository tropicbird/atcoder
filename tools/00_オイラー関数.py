def prime_factorization(n):
    arr = [] #array、配列のこと
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
            #print(arr)
    #print(temp)
    if temp != 1:
        arr.append([temp, 1])
        #print(arr)

    if arr == []:
        arr.append([n, 1])

    return arr

def euler_function(n):
    ls=prime_factorization(n)
    print(ls)
    ans=n
    for i in ls:
        ans*=(1-(1/i[0]))
    return int(ans)

print(euler_function(12))
print(euler_function(69))

