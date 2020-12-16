def main():
    K=int(input())
    seven=7
    i=1
    while True:
        #print(seven)
        if (seven/7)%K==0:
            print(i)
            break
        i+=1
        seven=seven*10+7

    #
    # #print(K)
    # #print(int(str(K)[-1])%2)
    # #print(int(str(K)[-1]))
    # #print(int(str(K)[-1])%2==0 or int(str(K)[-1])==5)
    # if int(str(K)[-1])%2==0 or int(str(K)[-1])==5:
    #     print(-1)
    # #7の倍数チェック
    # elif (int(str(K)[0:-1])-int(str(K)[-1])*2)%7!=0:
    #     print(-1)
    # else:
    #     a=7
    #     i=1
    #     while True:
    #         #print(a)
    #         #print(K)
    #         if a%K==0:
    #             print(i)
    #             break
    #         a=a*10+7
    #         i+=1

if __name__ == '__main__':
    main()