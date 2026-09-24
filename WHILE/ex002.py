import random

numero_secreto = random.randint(1, 10)
tentativas = 0
max_tentativas = 3
acertou = False

while tentativas < max_tentativas and not acertou:
    palpite = int(input("Tente adivinhar o número (1 a 10): "))
    tentativas += 1

    if palpite == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou em {tentativas} tentativa(s)!")
    elif palpite < numero_secreto:
        print("O número secreto é maior. Tente de novo!")
    else:
        print("O número secreto é menor. Tente de novo!")

if not acertou:
    print(f"Suas tentativas acabaram. O número era {numero_secreto}. ja era!")