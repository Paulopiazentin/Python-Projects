# --- Dados da pessoa ---
peso = 78          # em kg
altura = 1.75       # em metros
idade = 32

# --- Validação inicial ---
if peso <= 0 or altura <= 0:
    print("Erro0: peso e altura devem ser valores positivos.")

else:
    # --- Cálculo do IMC ---
    imc = peso / (altura ** 2)

    # --- if / elif / else para classificação ---
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade Grau 1"
    elif imc < 40:
        classificacao = "Obesidade Grau 2"
    else:
        classificacao = "Obesidade Grau 3"

    # --- Condição aninhada: recomendação varia com idade ---
    if classificacao == "Peso normal":
        if idade >= 60:
            recomendacao = "Manter hábitos saudáveis "
        else:
            recomendacao = "Manter a rotina atual de alimentação e exercícios"
    else:
        if idade >= 60:
            recomendacao = "Procurar orientação médica antes de mudar dieta ou exercícios"
        else:
            recomendacao = "Buscar orientação de nutricionista e educador físico"

    # --- Operadores lógicos ---
    if classificacao in ("Obesidade Grau 2", "Obesidade Grau 3") and idade >= 45:
        alerta_saude = True
    else:
        alerta_saude = False

    # --- Operador ternário ---
    urgencia = "Alta" if alerta_saude else "Baixa"

    # --- Exibição do resultado ---
    print(f"IMC calculado: {round(imc, 2)}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")
    print(f"Urgência de atenção médica: {urgencia}")