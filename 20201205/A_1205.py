N = int(input())
T = str(input())
import re

S=10**10

if N==1:
    if T=='1':
        print(2*S)
    elif T=='0':
        print(S)
    exit()

if N==2:
    if T=='11':
        print(S)
    elif T=='01':
        print(S-1)
    elif T=='10':
        print(S)
    else:
        print(0)
    exit()

start=T[:3]

if start=='110':
    if N<=6:
        if (T=='110'):
            print(S)
            exit()
        if (T=='1101') or (T=='11011') or (T=='110110'):
            print(S-1)
            exit()
        print(0)
        exit()

    if N>6:
        amari=N%3

    if amari == 1:
        end = T[-amari:]
        if end=='1':
            center=T[3:-amari]

            #centerを確認
            length = len(center)

            number = int(length / 3)
            tmp='110' * number
            if tmp==center:

            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:

                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 2:
        end = T[-amari:]
        if end=='11':
            center=T[3:-amari]

            #centerを確認
            length = len(center)
            number = int(length / 3)
            tmp='110' * number
            if tmp==center:


            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:
                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 0:
        center = T[3:]

        #centerを確認
        length = len(center)
        number = int(length / 3)
        tmp = '110' * number
        if tmp == center:
        # for i in range(length+1):
        #     center=re.sub("^110", "", center)
        # if len(center)==0:
            number=length/3
            ans=S-number
            print(int(ans))
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()


if start == '101':
    if N<=5:
        if (T=='101')or (T=='1011') or (T=='10110'):
            print(S-1)
            exit()
        print(0)
        exit()

    if N>5:
        amari=(N-2)%3

    if amari == 1:
        end = T[-amari:]
        if end=='1':
            center=T[2:-amari]

            #centerを確認
            length = len(center)
            number = int(length / 3)
            tmp='110' * number
            if tmp==center:
            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:
                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 2:
        end = T[-amari:]
        if end=='11':
            center=T[2:-amari]

            #centerを確認
            length = len(center)
            number = int(length / 3)
            tmp='110' * number
            if tmp==center:
            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:
                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 0:
        center = T[2:]

        #centerを確認
        length = len(center)
        number = int(length / 3)
        tmp = '110' * number
        if tmp == center:
        # for i in range(length+1):
        #     center=re.sub("^110", "", center)
        # if len(center)==0:
            number=length/3
            ans=S-number
            print(int(ans))
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()





if start == '011':
    if N<=4:
        if (T=='011')or (T=='0110'):
            print(S-1)
            exit()
        print(0)
        exit()

    if N>4:
        amari=(N-1)%3

    if amari == 1:
        end = T[-amari:]
        if end=='1':
            center=T[1:-amari]

            #centerを確認
            length = len(center)
            number = int(length / 3)
            tmp='110' * number
            if tmp==center:
            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:
                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 2:
        end = T[-amari:]
        if end=='11':
            center=T[1:-amari]

            #centerを確認
            length = len(center)
            number = int(length / 3)
            tmp='110' * number
            if tmp==center:
            # for i in range(length+1):
            #     center=re.sub("^110", "", center)
            # if len(center)==0:
                number=length/3
                ans=S-number-1
                print(int(ans))
                exit()
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()

    if amari == 0:
        center = T[1:]

        #centerを確認
        length = len(center)
        number = int(length / 3)
        tmp = '110' * number
        if tmp == center:
        # for i in range(length+1):
        #     center=re.sub("^110", "", center)
        # if len(center)==0:
            number=length/3
            ans=S-number
            print(int(ans))
            exit()
        else:
            print(0)
            exit()
    else:
        print(0)
        exit()
print(0)


