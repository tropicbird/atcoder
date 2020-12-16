def main():
    N,D=map(int, input().split())
    L = [list(map(int, input().split())) for i in range(N)]
    count=0
    for l in L:
        if D**2 >= l[0]**2+l[1]**2:
            count+=1
    print(count)

if __name__ == '__main__':
    main()