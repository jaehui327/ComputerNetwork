def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

p = 0
print("----------------------------")
print("|가입자수  |      확률 p        |")
print("----------------------------")
for t in range(21, 80):
    for i in range(21, t + 1):
        # i C 21
        c = factorial(t) / (factorial(i) * factorial(t - i))
        p += c * pow(2 / 10, i) * pow(8 / 10, t - i)
    if p >= 0.01: exit()
    print('|', i, '명   |', '%.15f' %p, '|')