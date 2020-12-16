def main():
    A, B = map(int, input().split())
    X=int((A+B)/2)
    Y = int((A - B) / 2)
    print(f"{str(X)} {str(Y)}")


if __name__ == '__main__':
    main()