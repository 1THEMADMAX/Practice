import math
def _sqr(x):
    return x*x
def _tri(x):
    return x*x*x
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
z = input('Введите операцию: ')

if z == '+':
    print(a + b)
elif z=='-':
    print(a - b)
elif z == '*':
    print(a * b)
elif z=='/':
    print( '%2.3f' %(a/b))
elif z=='**':
    print(_sqr(a))
elif z=='***':
    print(_tri(a))
