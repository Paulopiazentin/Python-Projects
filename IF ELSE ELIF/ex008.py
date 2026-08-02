# --- Dados de login ---
usuario = "admin"
senha = "1234senha"
tentativas = 2
usuario_bloqueado = False

# --- Credenciais corretas (simulando um "banco de dados") ---
usuario_correto = "admin"
senha_correta = "senha1234"

# --- Validação inicial ---
if tentativas < 0:
    print("Erro: número de tentativas inválido.")

else:
    # --- Condição aninhada principal ---
    if usuario_bloqueado:
        acesso = "Negado"
        motivo = "Usuário bloqueado por excesso de tentativas"

    else:
        if usuario == usuario_correto:
            if senha == senha_correta:
                acesso = "Permitido"
                motivo = "Login realizado com sucesso"
            else:
                acesso = "Negado"
                motivo = "Senha incorreta"
        else:
            acesso = "Negado"
            motivo = "Usuário não encontrado"

    # --- Operadores lógicos: regra de bloqueio ---
    if acesso == "Negado" and tentativas >= 3:
        usuario_bloqueado = True
        motivo += " (conta bloqueada após 3 tentativas)"

    # --- Operador ternário ---
    nivel_alerta = "Alto" if usuario_bloqueado else ("Médio" if acesso == "Negado" else "Nenhum")

    # --- Exibição do resultado ---
    print(f"Usuário: {usuario}")
    print(f"Tentativas realizadas: {tentativas}")
    print(f"Acesso: {acesso}")
    print(f"Motivo: {motivo}")
    print(f"Nível de alerta: {nivel_alerta}")