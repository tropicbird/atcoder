def main():
    X=str(input())
    if X=='RRR':
        print(3)
    elif X=='RRS' or X=='SRR':
        print(2)
    elif X=='SSS':
        print(0)
    else:
        print(1)

if __name__ == '__main__':
    main()