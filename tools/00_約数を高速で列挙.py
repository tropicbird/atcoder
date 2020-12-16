def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0: #nがiで割り切れる場合
            lower_divisors.append(i)#lower_divisorsにiを追加
            if i != n // i:#i*i=nでは無いとき、
                upper_divisors.append(n//i)#upper_divisorsにn/iを追加
        i += 1
    return lower_divisors + upper_divisors[::-1]

print(make_divisors(951633476))
print(make_divisors(951633476)[-2])