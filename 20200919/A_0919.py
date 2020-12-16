def main():
    S = str(input())
    if S[-1]=='s':
        ans=S+'es'
    else:
        ans = S + 's'
    print(ans)


if __name__ == '__main__':
    main()