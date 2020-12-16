correct=[1,2,3]
while True:
    X=input()

    if X == 'q':
        print('終わり')
        break

    try:
        X=int(X)
    except:
        print('整数を入力してください。')
        continue

    if X in correct:
        print('あなたの勝ち')
    else:
        print('あなたの負け')