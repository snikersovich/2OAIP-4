#Задача 1
def horse2(sell):
    alphavit = 'abcdefgh'
    steps = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    x = alfavit.find(cell[0]) +1
    y = int(cell[1])
    for xy in steps:
        x1, y1 = x + xy[0], y + xy[1]
        if 0 < x1 < 9 and 0 < y1 < 9:
            print(f'{alfavit[x1 - 1]}{y1}')

#Задача 2
def template(a, b, c):
    if a + b > c > b and b + c > a:
        print(f'Периметр: {a + b + c}')
        p = (a + b + c) / 2
        print(f'Площадь: {(p * (p - a) * (p - b) * (p - c)) ** 0.5}')
        if a == b and a != c or a == c and a != b or b ==c:
            print(f'Равнобедренный: да')
        else:
            print(f'Равнобедренный: нет')
        if a == b == c:
            print(f'Равносторонний: да')
        else:
            print(f'Равносторонний: нет')
    else:
        print('None')

#Задача 3
