#Desenvolva um programa que leia o primeiro termo e a
# #razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input("Primeiro numero: "))
razao = int(input("razão: "))
decimo = primeiro + (10 -1) *razao

for primeiro in range(primeiro,decimo, razao):
    print(primeiro , end= " > ")
print("FIM")