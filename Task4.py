x = input('Введите первый цвет')
y = input('Введите второй цвет')
q = 'Фиолетовый'
w = 'Оранжевый'
e = 'Зелёный'
if (x == 'Красный' and y == 'Синий') or (y == 'Красный' and x == 'Синий'):
    print(q)
elif (x == 'Красный' and y == 'Жёлтый') or (y == 'Красный' and x == 'Жёлтый'):
    print(w)
elif (x == 'Синий' and y == 'Жёлтый') or (y == 'Синий' and x == 'Жёлтый'):
    print(e)
else:
    print('Вы ввели неверные цвета')

