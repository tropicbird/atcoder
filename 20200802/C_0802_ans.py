def main():
    import sys
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print('-1')
        sys.exit()
    s = 7
    c = 1
    while True:
        if s % k == 0:
            break
        s = (10 * s + 7) % k
        c += 1
    print(c)

if __name__=='__main__':
    main()