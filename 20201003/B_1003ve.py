def main():
    N, S = map(str, input().split())
    N=int(N)
    count=0
    even_ls=[]
    odd_ls=[]
    for i in range(0,N//2):
        i=i*2
        print(i)
        # print(f"i:{i}")
        even_ls.append(S[i:2 + i])
        odd_ls.append(S[i+1:3 + i])
    print(even_ls)
    print(odd_ls)

    for j, even in enumerate(even_ls):
        m=0
        tmp = even
        while m <= N//2:

            a = tmp.count('A')
            t = tmp.count('T')
            g = tmp.count('G')
            c = tmp.count('C')
            if a==t and g==c:
                count += 1
            skip=abs(a-t)+abs(g-c)
            if skip==0:
                tmp=even_ls[j:j+1]
            else:
                tmp = even_ls[j:int(skip/2)]

            m+=skip/2







        # print(f'even:{even}')
        # print(f'odd:{odd}')



    # for window in range(1,N//2+1):
    #     window=window*2
    #     #print(window)
    #     for i in range(N-window+1):
    #         #print(f"i:{i}")
    #         test=S[i:window + i]
    #         print(test)
    #         #print(S[i:window+i])
    #         a=test.count('A')
    #         t=test.count('T')
    #         g=test.count('G')
    #         c=test.count('C')
    #         print(f"a:{a},t:{t},g:{g},c:{c}")
    #         if a==t and g==c:
    #             count+=1
    #print(count)
if __name__ == '__main__':
    main()