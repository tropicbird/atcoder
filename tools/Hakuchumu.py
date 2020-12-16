#---my original solution
S=str(input())
words=['dream','dreamer','erase','eraser']
while 1:
    if S=='':
        print('YES')
        break
    elif S[0]=='d':
        if S[:7]=='dreamdr':
            #print(1)
            S = S[5:]
        elif S[:8]=='dreamerd' or S[:8]=='dreamere':
            #print(2)
            S = S[7:]
        elif S[:8]=='dreamera':
            #print(3)
            S = S[5:]
        elif S=='dreamer':
            #print(4)
            print('YES')
            break
        elif S=='dream':
            #print(5)
            print('YES')
            break
        else:
            print('NO')
            break
    elif S[0]=='e':
        if S[:6]=='erased':
            S = S[5:]
        elif S[:6]=='eraser':
            S = S[6:]
        elif S[:6]=='erasee':
            S = S[5:]
        elif S=='erase':
            print('YES')
            break
        else:
            print('NO')
            break
    else:
        print('NO')

#---other solution
# s = input()
# cdr = s.count("dreamer")
# cd = s.count("dream")
# cer = s.count("eraser")
# ce = s.count("erase")
# double1 = s.count("dreamerase")
# cdr = cdr - double1
# cd = cd - cdr
# ce = ce - cer
# if not cd*5 + cer*6 + cdr*7 + ce*5 == len(s):
#     print("NO")
# else:
#     print("YES")