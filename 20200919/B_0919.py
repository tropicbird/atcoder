def main():
    N = int(input())
    L = [list(map(int, input().split())) for i in range(N)]
    ls=[]
    count=0
    ans = 'No'
    for l in L:
        if len(set(l))==1:
            count+=1
        else:
            count=0
        if count==3:
            ans='Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()