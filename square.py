def square(side):
    P = float(side * 4)
    S = float(side ** 2)
    d = float(side * (2 ** 0.5))
    my_list = (P, S, d)
    return my_list

result = square(5)
print('Периметр квадрата, площадь квадрата, диагональ квадрата соответственно равны:', result)