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