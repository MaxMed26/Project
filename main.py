a = round(float(input('Ввежите страший член ')), 4)
b = round(float(input('Ввежите средний член ')), 4)
c = round(float(input('Ввежите свободный член ')), 4)

x = float()

a * (x * x) + b * x + c == 0

D = b**2 - 4*a*c
if D > 0:
    x1 = (-b-D**(0.5))/(2*a)
    x2 = (-b+D**(0.5))/(2*a)
    print(round(x1, 4), round(x2, 4))
elif D == 0:
    x = (-b)/(2*a)
    print(x)
else:
    print('Корней нет')
