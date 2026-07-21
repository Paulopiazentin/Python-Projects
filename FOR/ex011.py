#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

for i in range(1, 5):
    nome = input(f"Digite o nome da {i}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    sexo = input(f"Digite o sexo da {i}ª pessoa (M/F): ").upper()

    if i == 1:
        soma_idade = idade
        homem_mais_velho = nome if sexo == 'M' else ''
        idade_homem_mais_velho = idade if sexo == 'M' else 0
        mulheres_menos_20 = 1 if sexo == 'F' and idade < 20 else 0
    else:
        soma_idade += idade
        if sexo == 'M' and idade > idade_homem_mais_velho:
            homem_mais_velho = nome
            idade_homem_mais_velho = idade
        if sexo == 'F' and idade < 20:
            mulheres_menos_20 += 1

media_idade = soma_idade / 4
print(f"A média de idade do grupo é: {media_idade}")
print(f"O nome do homem mais velho é: {homem_mais_velho}")
print(f"O número de mulheres com menos de 20 anos é: {mulheres_menos_20}")