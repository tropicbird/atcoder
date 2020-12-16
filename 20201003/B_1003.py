def main():
N, S = map(str, input().split())
N=int(N)
count=0
for window in range(1,N//2+1):
    window=window*2
    #print(window)
    for i in range(N-window+1):
        #print(f"i:{i}")
        test=S[i:window + i]
        # print(test)
        #print(S[i:window+i])
        a=test.count('A')
        t=test.count('T')
        g=test.count('G')
        c=test.count('C')
        # print(f"a:{a},t:{t},g:{g},c:{c}")
        if a==t and g==c:
            count+=1
print(count)




    # for window in range(2,N+1):
    #     print(window)



    # old=""
    # count=0
    # id=""
    # newid=""
    # for s in S:
    #     if s=="A" and old=="T":
    #         count+=1
    #         newid="TA"
    #
    #         if id=="GC" or id=="CG" :
    #             count+=1
    #
    #     if s == "T" and old=="A":
    #         count += 1
    #         newid = "AT"
    #         if id=="GC" or id=="CG":
    #             count+=1
    #
    #     if s == "C" and old=="G":
    #         count += 1
    #         newid = "GC"
    #         if id=="AT" or id=="TA":
    #             count+=1
    #
    #     if s == "G" and old=="C":
    #         count += 1
    #         newid = "CG"
    #         if id=="AT" or id=="TA":
    #             count+=1
    #
    #
    #     if s=="G" and old=="A":
    #         #count+=1
    #         newid="AG"
    #
    #         if id=="GC" or id=="CG" :
    #             count+=1
    #
    #     id=newid
    #     old=s

    # print(count)




if __name__ == '__main__':
    main()