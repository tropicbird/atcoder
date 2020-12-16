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

print(prime_factorization(24))
print(prime_factorization(13))
print(prime_factorization(1))