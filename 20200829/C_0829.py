def main():
    N = int(input())
    L = list(map(int, input().split()))

    product = 0
    mod = 10**9 + 7
    for i in range(N):
        for j in range(i + 1, N):
            product = product + (L[i] * L[j])
        product=product % mod
    print(product%mod)



if __name__ == '__main__':
    main()