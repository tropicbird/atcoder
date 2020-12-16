def main():
    import numpy as np
    X = int(input())
    S = str(X)
    L=[int(i) for i in S]
    Y=np.sum(L)
    if Y%9==0:
        ans="Yes"
    else:
        ans="No"

    print(ans)


if __name__ == '__main__':
    main()