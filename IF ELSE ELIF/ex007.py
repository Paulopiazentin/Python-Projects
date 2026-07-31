
idade = 25
valor_compra = 300
cliente_vip = True


if idade < 0 or valor_compra < 0:
    print("Erro: valores inválidos.")

else:
    if idade < 12:
        categoria = "Criança"
    elif idade < 18:
        categoria = "Adolescente"
    elif idade < 60:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    desconto = 0

    if valor_compra >= 100:
        if cliente_vip:
            desconto = 20
        else:
            desconto = 10
    else:
        if cliente_vip:
            desconto = 5    
        else:
            desconto = 0

    if categoria == "Idoso" and valor_compra >= 50:
        desconto += 5  # desconto extra para idosos

    if categoria in ("Criança", "Adolescente") and not cliente_vip:
        desconto += 2  # incentivo para jovens não-VIP

    status = "Cliente Premium" if desconto >= 20 else "Cliente Regular"

    valor_final = valor_compra - (valor_compra * desconto / 100)

    print(f"Categoria: {categoria}")
    print(f"Desconto aplicado: {desconto}%")
    print(f"Status: {status}")
    print(f"Valor final: R$ {round(valor_final, 2)}")