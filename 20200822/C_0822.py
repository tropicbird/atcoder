def main():
    # X, K, D=map(int,input().split())
    # X = int(input())
    # L = [list(map(int, input().split())) for i in range(N)]

    X = int(input())
    L = list(map(int, input().split()))

    highest=L[0]
    val=0
    for A in L[1:]:
        if A<highest:
            val+=(highest-A)
        elif A>highest:
            highest=A
    print(val)


if __name__ == '__main__':
    main()