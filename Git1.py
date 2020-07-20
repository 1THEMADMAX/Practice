import math

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
z = input('Введите операцию')

if z == '+':
    print(a + b)
elif z=='-':
    print(a - b)
elif z == '*':
    print(a * b)
elif z=='/':
    print( '%2.3f' %(a/b))