def main():
    import numpy as np
    X=int(input())
    initial=400
    kyu=8
    for add in range(1,9):
        if X<initial+add*200:
            print(int(kyu))
            break
        kyu-=1

if __name__ == '__main__':
    main()