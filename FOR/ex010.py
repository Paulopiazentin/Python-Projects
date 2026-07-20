#Faça um programa que leia o peso de cinco pessoas. 
#No final, mostre qual foi o maior e o menor peso lidos.

soma = 0
for p in range(1, 6):
    input_peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))
    soma += input_peso

    if p == 1:
        maior = input_peso
        menor = input_peso
    else:
        if input_peso > maior:
            maior = input_peso
        if input_peso < menor:
            menor = input_peso

print('O maior peso lido foi: {}'.format(maior))
print('O menor peso lido foi: {}'.format(menor))