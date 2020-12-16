def main():
    N=int(input())
    L=list(map(int, input().split()))
    L.sort(reverse=True)
    unique_vals=sorted(set(L), reverse=True)

    count=0
    #print(unique_vals)
    for i, first in enumerate(unique_vals):
        for j, second in enumerate(unique_vals[i+1:]):
            for third in unique_vals[i+j+2:]:
                if third > first - second:
                    count+=1*L.count(first)*L.count(second)*L.count(third)
                    #print(first, second, third)
                    #print(count)
                else:
                    break
    print(count)


if __name__ == '__main__':
    main()