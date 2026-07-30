v1 = float(input('digite o valor de um lado do triangulo: '))
v2 = float(input('digite o valor de outro lado do triangulo: '))
v3 = float(input('digite o valor de outro lado do triangulo: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('é um triangulo')
    if v1 == v2 == v3:
                print('equilatero')
    elif v1 == v2 or v1 == v3 or v2 == v3:
                print('isosceles')
    elif v1 != v2 != v3:
      print('escaleno')
else:
  print('não é um triangulo')