def main():
    X, K, D=map(int,input().split())
    if D*K<abs(X):
        ans=abs(X)-D*K
    else:
        p=abs(X)//D
        q=abs(X)%D
        #symbol=(abs(X)/X)
        if (K-p)%2==1:
            ans=abs(D-q)
        else:
            ans=q
    print(ans)


if __name__ == '__main__':
    main()