def main():
    import numpy as np
    N, K=map(int,input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))

    if N==K:
        print('here!')
        print(np.sum(C))
    else:
        #[x for _, x in sorted(zip(Y, X))]
        combination=[x for _, x in sorted(zip(P, C))]
        combination.extend(combination)
        print(combination)
        tmp = np.sum(combination[0:K])
        for i in range(N):
            tmp_new=np.sum(combination[i:i+K])
            if tmp_new>tmp:
                tmp=tmp_new
        print(tmp)

if __name__ == '__main__':
    main()