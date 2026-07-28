item= float(input("1 - retangulo  2 - triangulo\nqual item deseja calcular a area:"))
base= float(input("qual a base:"))
altura= float(input("qual a altura:"))
if item == 1:
  print("retangulo")
  area=base*altura
  print("a area é:",area)
elif item == 2:
      print("triangulo")
      area=base*altura/2
      print("a area é:",area)