soma = 0
contador = 0
for c in range(1,7):
     p = int(input("digite o {} numero".format(c)))
     if p % 2 == 0:
          soma += p
          contador += 1
print("você informou {} Números  Pares e a soma foi {}".format(contador, soma))