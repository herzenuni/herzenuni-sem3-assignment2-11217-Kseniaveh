#Вехова Ксения, ИВТ-2 курс
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))

def function(a, b):
    while a != b:
      if a > b:
        a = a - b
      else:
        b = b - a
    return a
print('Наибольший общий делитель: {}'.format(function(a, b)))
