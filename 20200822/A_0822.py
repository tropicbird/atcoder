def main():
    N, X, T=map(int,input().split())
    if N%X!=0:
        ans=((N//X)+1)*T
    else:
        ans=(N/X)*T
    print(int(ans))


if __name__ == '__main__':
    main()