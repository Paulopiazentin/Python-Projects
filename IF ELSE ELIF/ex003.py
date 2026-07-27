item= float(input("1 - caixa   2 - lata\nqual item deseja calcular o volume:"))
if item == 1:
  print("caixa")
  altura=float(input("qual a altura:"))
  largura=float(input("qual a largura:"))
  comprimento=float(input("qual o comprimento:"))
  volume=altura*largura*comprimento
  print("o volume é:",volume)
else:
  if item == 2:
    print("lata")
    raio=float(input("qual o raio:"))
    altura=float(input("qual a altura:"))
    volume=3.14*raio**2*altura
    print("o volume é:",volume)