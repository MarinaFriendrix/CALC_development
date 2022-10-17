# Задача: Создать калькулятор для работы с рациональными и комплексными числами,
# организовать меню, добавив в неё систему логирования.


number1 = int (input('Введите число 1: '))
number2 = int (input('Введите число 2: '))

v =  input('Какую операцию вы хотите выполнить? \n + Сложение \n - Вычитание \n / Деление \n * Умножение \n')

if v == '+':
    res = number1 + number2
    ad = 'сложения'
    t = ad
elif v == '-':
    res = number1 - number2
    sub = 'вычитания'
    t = sub
elif v == '/':
    res = float(number1/number2)
    div = 'деления'
    t = div
if v == '*':
    res = number1 * number2
    mul = 'умножения'
    t = mul
print ('Результат ',t,' = ',res)

