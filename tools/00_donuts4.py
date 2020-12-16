def solution(N):
    def factorial(n):
        fact=1
        for i in range(1, n + 1):
            fact = fact * i
        return fact

    if N==0:
        return 1

    A=list(map(int,str(N)))
    print(A)
    n=len(A)
    zero=A.count(0)
    one=A.count(1)
    two=A.count(2)
    three=A.count(3)
    four=A.count(4)
    five=A.count(5)
    six=A.count(6)
    seven=A.count(7)
    eight=A.count(8)
    nine=A.count(9)


    if zero==0:
        all_nozero=[one, two, three, four, five, six, seven,
             eight, nine]
        ls=[]
        for i in all_nozero:
            if i>1:
                ls.append(i)
        print(n)
        f_above=factorial(n)
        print(f_above)
        f_below=1
        print(ls)

        for i in ls:
            f_below *= factorial(i)

        ans=f_above/f_below
        return int(ans)
    else:
        print('there is zero')
        all_nozero=[one, two, three, four, five, six, seven,
             eight, nine]
        ls=[]
        for i in all_nozero:
            if i>1:
                ls.append(i)
        print(n-zero)
        f_above=factorial(n-zero)
        print(f'f_above:{f_above}')
        f_below=1
        print(ls)
        for i in ls:
            f_below *= factorial(i)
        print(f_below)
        ans=f_above/f_below
        #zeroposi=0
        print(n)
        print(f'ans:{ans}')
        zeroposi=n-zero
        # for i in range(1,n-zero):
        #     zeroposi+=i
        print(zeroposi)
        zeroposi*zero
        ans=ans*zeroposi
        return int(ans)

N=100
print(solution(N))