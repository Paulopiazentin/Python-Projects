n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
media = (n1 + n2) / 2
aula = float(input("digite quantas aulas tem ao todo: "))
f =  float(input("digite quantas aulas você nao foi: "))
freq = (aula - f)*100 / aula

if media == 7 and freq >= 75:
  print("aprovado")
else:
  print("reprovado")